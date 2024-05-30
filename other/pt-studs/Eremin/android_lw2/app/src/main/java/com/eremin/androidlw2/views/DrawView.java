package com.eremin.androidlw2.views;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.drawable.BitmapDrawable;
import android.graphics.drawable.Drawable;
import android.view.View;

import androidx.annotation.NonNull;
import androidx.core.content.res.ResourcesCompat;

import com.eremin.androidlw2.R;

import java.util.Random;
import java.util.stream.IntStream;

public class DrawView extends View {
    private final Paint paint = new Paint(Paint.ANTI_ALIAS_FLAG);
    private final Random random = new Random();
    private final Bitmap spaceShip;

    public DrawView(Context context) {
        super(context);
        Drawable drawable = ResourcesCompat.getDrawable(getResources(), R.drawable.space_ship_item, context.getTheme());
        spaceShip = drawableToBitmap(drawable);
    }

    @Override
    protected void onDraw(@NonNull Canvas canvas) {
        super.onDraw(canvas);
        int night = Color.parseColor("#191551");
        paint.setStyle(Paint.Style.FILL);

        // Небо
        paint.setColor(night);
        canvas.drawPaint(paint);

        // Луна
        paint.setColor(Color.YELLOW);
        canvas.drawCircle(275, 300, 180, paint);
        paint.setColor(night);
        canvas.drawCircle(300, 290, 160, paint);

        // Звезды
        paint.setColor(Color.YELLOW);
        for (int ignored : IntStream.range(0, 120).toArray()) {
            int x = random.nextInt(getWidth());
            int y = random.nextInt(getHeight());
            int size = random.nextInt(6);
            canvas.drawCircle(x, y, size, paint);
        }

        // Корабль
        canvas.save();
        float spaceShipX = 350 + random.nextInt(getWidth() - 350);
        float spaceShipY = 200 + random.nextInt(getHeight() - 100);
        canvas.rotate(random.nextInt(360), spaceShipX + spaceShip.getWidth() / 2.0f, spaceShipY + spaceShip.getHeight() / 2.0f);
        canvas.drawBitmap(spaceShip, spaceShipX, spaceShipY, paint);
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
}