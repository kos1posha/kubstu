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

public class SimpleDrawView extends View {
    private final Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Random random = new Random();

    private final List<Bitmap> spaceShipsBms;
    private int spaceShip1Y;
    private int spaceShip2Y;
    private int spaceShip3Y;

    private final List<List<Integer>> stars = new ArrayList<>();
    String[] starColors = {"#FFD700", "#0000FF", "#800080", "#008000", "#FF0000"};

    private final Handler handler;
    private final Runnable runnable;

    private int timeState;
    private boolean timeDir;
    private boolean initialized = false;

    public SimpleDrawView(Context context) {
        super(context);
        Drawable spaceShip1 = ResourcesCompat.getDrawable(getResources(), R.drawable.space_ship_s1_item, context.getTheme());
        Drawable spaceShip2 = ResourcesCompat.getDrawable(getResources(), R.drawable.space_ship_s2_item, context.getTheme());
        Drawable spaceShip3 = ResourcesCompat.getDrawable(getResources(), R.drawable.space_ship_s3_item, context.getTheme());

        spaceShipsBms = Arrays.asList(
            drawableToBitmap(spaceShip1),
            drawableToBitmap(spaceShip2),
            drawableToBitmap(spaceShip3)
        );

        handler = new Handler();
        runnable = new Runnable() {
            @Override
            public void run() {
                if (timeDir) {
                    timeState += 8;
                    timeDir = timeState != 250;
                } else {
                    timeState -= 8;
                    timeDir = timeState == 0;
                }
                if (initialized) {
                    spaceShip1Y -= 8;
                    spaceShip2Y -= 8;
                    spaceShip3Y -= 8;
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
        paint.setStyle(Paint.Style.FILL);
        if (!initialized) {
            randomStars();
        }
        int sky = Color.rgb(17, 24, 187);
        paint.setColor(sky);
        canvas.drawPaint(paint);
        for (List<Integer> star : stars) {
            int s0 = star.get(0), s1 = star.get(1), s2 = star.get(2);
            paint.setColor(Color.parseColor(starColors[star.get(3)]));
            paint.setAlpha((timeState + star.get(0) + star.get(1)) / 255);
            canvas.drawRect(s0, s1, s0 + s2, s1 + s2, paint);
            paint.setColor(sky);
            canvas.drawCircle(s0, s1, (float) s2 / 2, paint);
            canvas.drawCircle(s0, s1 + s2, (float) s2 / 2, paint);
            canvas.drawCircle(s0 + s2, s1, (float) s2 / 2, paint);
            canvas.drawCircle(s0 + s2, s1 + s2, (float) s2 / 2, paint);
        }
        paint.setColor(Color.YELLOW);
        canvas.drawCircle(570, 365, 180, paint);
        paint.setColor(sky);
        canvas.drawCircle(640, 350, 160, paint);
        canvas.save();
        int X = getWidth() / 10;
        int stepX = (int) (getWidth() / 3.5);
        int[] Ys = {spaceShip1Y, spaceShip2Y, spaceShip3Y};
        for (int i = 0; i < 3; i++) {
            canvas.drawBitmap(spaceShipsBms.get(i), X, Ys[i], paint);
            X += stepX;
        }
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

    protected void randomStars() {
        spaceShip1Y = getHeight() + 200;
        spaceShip2Y = getHeight() + 50;
        spaceShip3Y = getHeight() + 200;
        for (int ignored : IntStream.range(0, 50).toArray()) {
            stars.add(Arrays.asList(random.nextInt(getWidth()), random.nextInt(getHeight()),
                10 + random.nextInt(30), random.nextInt(starColors.length)));
        }
        initialized = true;
    }
}
