package com.eremin.androidlw2.views;

import android.content.Context;
import android.content.res.Resources;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.view.View;

import androidx.annotation.NonNull;

import com.eremin.androidlw2.R;

import java.util.Random;

public class SpaceAnimationView extends View {
    private final Resources res = this.getResources();
    private final Bitmap bitmap = BitmapFactory.decodeResource(res, R.drawable.shshs);
    private final Bitmap bitmapScaled = Bitmap.createScaledBitmap(bitmap, bitmap.getWidth() / 6, bitmap.getHeight() / 6, false);

    private final Random random = new Random();
    private final Paint paint = new Paint();

    private int step = 0;

    private final float[] moon = new float[2];
    private final float[] spaceship = new float[2];
    private boolean flag = true;

    public SpaceAnimationView(Context context) {
        super(context);
        spaceship[0] = 50F;
        spaceship[1] = 1500F;

        moon[0] = 680f;
        moon[1] = 400f;
    }

    @Override
    protected void onDraw(@NonNull Canvas canvas) {
        super.onDraw(canvas);
        super.onDraw(canvas);

        paint.setStyle(Paint.Style.FILL);
        paint.setColor(Color.rgb(0, 0, 10));

        canvas.drawPaint(paint);

        if (step <= 1200) {
            for (int i = 0; i <= 30; i++) {
                paint.setColor(Color.rgb(255, 255, 244));
                canvas.drawCircle(random.nextInt(950) + 50, random.nextInt(1950) + 50, 2f, paint);
            }

            paint.setColor(Color.rgb(255, 248, 231));
            canvas.drawCircle(getWidth() - 400F, 400F, 150F, paint);

            paint.setColor(Color.rgb(0, 0, 10));
            canvas.drawCircle(moon[0], moon[1], 150F, paint);

            if (moon[0] >= 600) {
                moon[0] -= 1F;
            }

            if (flag) {
                if (spaceship[0] >= 50) {
                    spaceship[0] -= 5F;
                    spaceship[1] -= 1F;

                } else {
                    flag = false;
                }
            } else {
                if (spaceship[0] <= 800) {
                    spaceship[0] += 5F;
                    spaceship[1] -= 1F;
                } else {
                    flag = true;
                }
            }

            canvas.drawBitmap(bitmapScaled, spaceship[0], spaceship[1], paint);

            step++;
            invalidate();
        } else {
            step = 0;
        }
    }
}