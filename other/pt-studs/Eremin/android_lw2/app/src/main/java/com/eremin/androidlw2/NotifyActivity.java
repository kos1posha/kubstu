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
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Button;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.databinding.ActivityNotifiyBinding;

import java.util.Arrays;
import java.util.Objects;

public class NotifyActivity extends AppCompatActivity {
    private ActivityNotifiyBinding binding;
    private View view;
    private ActionBar actionBar;
    private LayoutInflater layoutInflater;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        layoutInflater = getLayoutInflater();
        binding = ActivityNotifiyBinding.inflate(layoutInflater);
        view = binding.getRoot();
        actionBar = Objects.requireNonNull(getSupportActionBar());
        actionBar.setDisplayHomeAsUpEnabled(true);
        setContentView(view);
        setupListeners();
        setupTheme();
    }

    protected void setupListeners() {
        binding.btnCommon.setOnClickListener(v -> execNotification(notifyCommon()));
        binding.btnWithButtons.setOnClickListener(v -> execNotification(notifyWithButtons()));
        binding.btnWithLongText.setOnClickListener(v -> execNotification(notifyWithLongText()));
        binding.btnWithBigPicture.setOnClickListener(v -> execNotification(notifyWithBigPicture()));
        binding.btnInbox.setOnClickListener(v -> execNotification(notifyInbox()));
    }

    protected void setupTheme() {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        int pColor = sp.getInt("primaryColor", getColor(android.R.color.background_light));
        int sColor = sp.getInt("secondaryColor", getColor(android.R.color.holo_green_dark));
        int sSupColor = sp.getInt("secondarySupColor", getColor(android.R.color.background_light));
        view.setBackgroundColor(pColor);
        actionBar.setBackgroundDrawable(new ColorDrawable(sColor));
        for (Button button : Arrays.asList(binding.btnCommon, binding.btnWithButtons,
            binding.btnWithLongText, binding.btnWithBigPicture, binding.btnInbox)) {
            button.setBackgroundColor(sColor);
            button.setTextColor(sSupColor);
        }
    }

    private void execNotification(Notification.Builder builder) {
        NotificationManager nm = (NotificationManager) getSystemService(NOTIFICATION_SERVICE);
        Notification notification = builder.build();
        notification.defaults = Notification.DEFAULT_SOUND | Notification.DEFAULT_VIBRATE;
        if (android.os.Build.VERSION.SDK_INT >= android.os.Build.VERSION_CODES.O) {
            String channelId = "main_channel";
            NotificationChannel channel = new NotificationChannel(channelId, "Main channel", NotificationManager.IMPORTANCE_HIGH);
            nm.createNotificationChannel(channel);
            builder.setChannelId(channelId);
        }
        nm.notify(1337, notification);
    }

    private Notification.Builder notifyCommon() {
        Intent intent = new Intent(this, FifteenPuzzleActivity.class);
        PendingIntent pendingIntent = PendingIntent.getActivity(this, 0, intent, PendingIntent.FLAG_CANCEL_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        return new Notification.Builder(this)
            .setContentIntent(pendingIntent)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setLargeIcon(BitmapFactory.decodeResource(getResources(), R.drawable.well_i_do_not_know_item))
            .setTicker("Новое уведомление")
            .setWhen(System.currentTimeMillis())
            .setAutoCancel(true)
            .setContentTitle("Тебя давно не было в пятнашках")
            .setContentText("Скорее заходи, если хочешь жить!");
    }

    private Notification.Builder notifyWithButtons() {
        Intent molecularIntent = new Intent(this, FifteenPuzzleActivity.class);
        PendingIntent molecularPendingIntent = PendingIntent.getActivity(this, 0, molecularIntent, PendingIntent.FLAG_CANCEL_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        Intent matrixIntent = new Intent(this, FifteenPuzzleActivity.class);
        PendingIntent matrixPendingIntent = PendingIntent.getActivity(this, 0, matrixIntent, PendingIntent.FLAG_CANCEL_CURRENT | PendingIntent.FLAG_IMMUTABLE);
        return new Notification.Builder(this)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentTitle("Напоминание")
            .setContentText("Молекулы или матрица?")
            .setAutoCancel(true)
            .addAction(R.drawable.ic_launcher_foreground, "Молекулы", molecularPendingIntent)
            .addAction(R.drawable.ic_launcher_foreground, "Матрица", matrixPendingIntent);
    }

    private Notification.Builder notifyWithLongText() {
        return new Notification.Builder(this)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setColor(getColor(android.R.color.holo_green_dark))
            .setContentTitle("Пушкин")
            .setStyle(new Notification.BigTextStyle().bigText(getString(R.string.pushkin)));
    }

    private Notification.Builder notifyWithBigPicture() {
        return new Notification.Builder(this)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentTitle("Долго будешь всюду одну картинку пихать?")
            .setStyle(
                new Notification.BigPictureStyle()
                    .bigPicture(BitmapFactory.decodeResource(getResources(), R.drawable.well_i_do_not_know))
                    .bigLargeIcon(BitmapFactory.decodeResource(getResources(), R.drawable.well_i_do_not_know))
                    .setBigContentTitle("Да")
            );
    }

    private Notification.Builder notifyInbox() {
        return new Notification.Builder(this)
            .setSmallIcon(R.drawable.ic_launcher_foreground)
            .setContentTitle("Inbox")
            .setContentText("Inbox?")
            .setStyle(
                new Notification.InboxStyle()
                    .addLine("Inbox...")
                    .addLine("In.. box..?")
                    .addLine("Inbox!")
                    .addLine("Inbox!!!!")
                    .setBigContentTitle("Inbox")
            );
    }
}