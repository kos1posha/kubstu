package com.eremin.androidlw2;

import android.app.Notification;
import android.app.NotificationChannel;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.BitmapFactory;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.databinding.ActivityMainBinding;

import java.util.Arrays;
import java.util.Objects;

public class MainActivity extends AppCompatActivity {
    private ActivityMainBinding binding;
    private View view;
    private ActionBar actionBar;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityMainBinding.inflate(getLayoutInflater());
        view = binding.getRoot();
        actionBar = Objects.requireNonNull(getSupportActionBar());
        setContentView(view);
        setupListeners();
        setupTheme();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        binding = null;
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            goToSettingsActivity();
        } else if (id == R.id.action_about) {
            Toast toast = Toast.makeText(this, "Да нечего рассказывать...", Toast.LENGTH_SHORT);
            toast.show();
        }
        return super.onOptionsItemSelected(item);
    }

    protected void setupListeners() {
        binding.btnMolecularCalculator.setOnClickListener(this::goToMolecularCountActivity);
        binding.btnFifteenPuzzle.setOnClickListener(this::goToFifteenPuzzleActivity);
        binding.btnMatrix.setOnClickListener(this::goToMatrixActivity);
        binding.btnNotification.setOnClickListener(this::showFifteenPuzzleNotification);
        binding.btnDraw.setOnClickListener(this::goToDrawActivity);
    }

    protected void setupTheme() {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        int pColor = sp.getInt("primaryColor", getColor(android.R.color.background_light));
        int sColor = sp.getInt("secondaryColor", getColor(android.R.color.holo_green_dark));
        int sSupColor = sp.getInt("secondarySupColor", getColor(android.R.color.background_light));
        view.setBackgroundColor(pColor);
        actionBar.setBackgroundDrawable(new ColorDrawable(sColor));
        for (Button button : Arrays.asList(binding.btnMolecularCalculator, binding.btnFifteenPuzzle,
            binding.btnMatrix, binding.btnNotification, binding.btnDraw)) {
            button.setBackgroundColor(sColor);
            button.setTextColor(sSupColor);
        }
    }

    protected void goToMolecularCountActivity(View view) {
        Intent intent = new Intent(MainActivity.this, MolecularCalculatorActivity.class);
        startActivity(intent);
    }

    protected void goToFifteenPuzzleActivity(View view) {
        Intent intent = new Intent(MainActivity.this, FifteenPuzzleActivity.class);
        startActivity(intent);
    }

    protected void goToMatrixActivity(View view) {
        Intent intent = new Intent(MainActivity.this, MatrixActivity.class);
        startActivity(intent);
    }

    protected void goToDrawActivity(View view) {
        Intent intent = new Intent(MainActivity.this, DrawActivity.class);
        startActivity(intent);
    }

    protected void goToSettingsActivity() {
        Intent intent = new Intent(MainActivity.this, SettingsActivity.class);
        startActivity(intent);
    }

    protected void showFifteenPuzzleNotification(View view) {
        NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        Intent intent = new Intent(this, FifteenPuzzleActivity.class);
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_CANCEL_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        Notification.Builder builder = new Notification.Builder(this)
            .setContentIntent(pendingIntent)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setLargeIcon(BitmapFactory.decodeResource(getResources(), R.drawable.well_i_do_not_know_item))
            .setTicker("Новое уведомление")
            .setWhen(System.currentTimeMillis())
            .setAutoCancel(true)
            .setContentTitle("Тебя давно не было в пятнашках")
            .setContentText("Скорее заходи, если хочешь жить!");
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
            String channelId = "main_channel";
            NotificationChannel channel = new NotificationChannel(channelId, "Main channel", NotificationManager.IMPORTANCE_HIGH);
            nm.createNotificationChannel(channel);
            builder.setChannelId(channelId);
        }
        Notification notification = builder.build();
        notification.defaults = Notification.DEFAULT_SOUND | Notification.DEFAULT_VIBRATE;
        nm.notify(1337, notification);
    }
}