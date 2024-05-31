package com.eremin.androidlw2.views;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.os.Handler;
import android.view.View;

import androidx.annotation.NonNull;
import androidx.core.content.res.ResourcesCompat;

import com.eremin.androidlw2.R;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Random;
import java.util.stream.IntStream;

public class DrawView extends View {
    private final Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Random random = new Random();
    private final Bitmap spaceShip;
    private boolean spaceShipDir;
    private int spaceShipSpeed = 12;
    private int spaceShipAngle = 25;
    private double spaceShipRad;
    private double spaceShipX;
    private double spaceShipY;
    private final Handler handler;
    private final Runnable runnable;
    private final List<List<Integer>> stars;
    private boolean sceneInitialized;
    private boolean timeDir;
    private int timeState;

    public DrawView(Context context) {
        super(context);
        Drawable drawable = ResourcesCompat.getDrawable(getResources(), R.drawable.space_ship_item, context.getTheme());
        spaceShip = drawableToBitmap(drawable);
        timeDir = true;
        stars = new ArrayList<>();
        sceneInitialized = false;
        spaceShipRad = Math.toRadians(-spaceShipAngle);
        spaceShipDir = true;

        handler = new Handler();
        runnable = new Runnable() {
            @Override
            public void run() {
                if (timeDir) {
                    timeState++;
                    timeDir = timeState != 250;
                } else {
                    timeState--;
                    timeDir = timeState == 0;
                }
                if (sceneInitialized) {
                    if (spaceShipDir) {
                        spaceShipX += spaceShipSpeed * Math.cos(spaceShipRad);
                        spaceShipY += spaceShipSpeed * Math.sin(spaceShipRad);
                    } else {
                        spaceShipX -= spaceShipSpeed * Math.cos(spaceShipRad);
                        spaceShipY -= spaceShipSpeed * Math.sin(spaceShipRad);
                    }
                    if (spaceShipX > 2 * getWidth() || spaceShipX < -1.5 * getWidth() ||
                        spaceShipY > 2 * getHeight() || spaceShipY < -0.5 * getHeight()) {
                        spaceShipDir = !spaceShipDir;
                        reinitSpaceShip();
                    }
                }
                invalidate();
                handler.postDelayed(this, 10);
            }
        };
    }


    @Override
    protected void onAttachedToWindow() {
        super.onAttachedToWindow();
        handler.postDelayed(runnable, 10);
    }

    @Override
    protected void onDetachedFromWindow() {
        super.onDetachedFromWindow();
        handler.removeCallbacks(runnable);
    }

    @Override
    protected void onDraw(@NonNull Canvas canvas) {
        super.onDraw(canvas);
        int night = Color.parseColor("#191551");
        paint.setStyle(Paint.Style.FILL);

        if (!sceneInitialized) {
            initStarsAndSpaceShip();
        }

        // Небо
        paint.setColor(night);
        canvas.drawPaint(paint);

        // Луна
        paint.setColor(Color.YELLOW);
        canvas.drawCircle(275, 300, 180, paint);
        paint.setColor(night);
        canvas.drawCircle(300, 290, 160, paint);

        // Звезды
        for (List<Integer> star : stars) {
            paint.setColor(Color.argb((int) (star.get(3) + timeState * 0.7), 255, 255, 0));
            canvas.drawCircle(star.get(0), star.get(1), star.get(2) + ((float) (timeState) / 125), paint);
        }

        // Корабль
        canvas.save();
        paint.setAlpha(255);
        int rotateAngle;
        if (spaceShipDir) {
            rotateAngle = 45 - spaceShipAngle;
        } else {
            rotateAngle = -135 - spaceShipAngle;
        }
        canvas.rotate(rotateAngle, (int) spaceShipX, (int) spaceShipY);
        canvas.drawBitmap(spaceShip, (int) spaceShipX, (int) spaceShipY, paint);
    }

    protected static Bitmap drawableToBitmap(Drawable drawable) {
        if (drawable instanceof BitmapDrawable) {
            return ((BitmapDrawable) drawable).getBitmap();
        }
        Bitmap bitmap = Bitmap.createBitmap(drawable.getIntrinsicWidth(), drawable.getIntrinsicHeight(), Bitmap.Config.ARGB_8888);
        Canvas canvas = new Canvas(bitmap);
        drawable.setBounds(0, 0, canvas.getWidth(), canvas.getHeight());
        drawable.draw(canvas);
        return bitmap;
    }

    protected void initStarsAndSpaceShip() {
        spaceShipX = -spaceShip.getWidth();
        spaceShipY = 300 + random.nextInt(getHeight() - spaceShip.getHeight() - 500);
        for (int ignored : IntStream.range(0, 120).toArray()) {
            int x = random.nextInt(getWidth());
            int y = random.nextInt(getHeight());
            int size = random.nextInt(6);
            int timeShift = random.nextInt(80);
            stars.add(Arrays.asList(x, y, size, timeShift));
        }
        sceneInitialized = true;
    }

    protected void reinitSpaceShip() {
        spaceShipY = 300 + random.nextInt(getHeight() - spaceShip.getHeight() - 500);
        if (spaceShipDir) {
            spaceShipX = -0.3 * getWidth();
            spaceShipAngle = 45 - random.nextInt(135);
        } else {
            spaceShipX = 1.3 * getWidth();
            spaceShipAngle = random.nextInt(135) - 45;
        }
        spaceShipRad = Math.toRadians(-spaceShipAngle);
        spaceShipSpeed = 9 + random.nextInt(9);
    }
}