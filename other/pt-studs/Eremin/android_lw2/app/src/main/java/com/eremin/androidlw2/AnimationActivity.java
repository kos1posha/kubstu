package com.eremin.androidlw2;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.FrameLayout;
import android.widget.ImageView;

import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.v17.PdSettingsActivity;
import com.eremin.androidlw2.views.SpaceAnimationView;

public class AnimationActivity extends AppCompatActivity {
    FrameLayout main;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SharedPreferences sp = getSharedPreferences(getPackageName(), MODE_PRIVATE);
        PdSettingsActivity.ApplyTheme(sp, this, false);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_animation_view);

        main = findViewById(R.id.frame);
        main.addView(new SpaceAnimationView(this));

        ImageView clockImageView = findViewById(R.id.clock);
        Animation clockTurnAnimation = AnimationUtils.loadAnimation(this, R.anim.clock_turn);
        clockImageView.startAnimation(clockTurnAnimation);

        ImageView hourImageView = findViewById(R.id.hour_hand);
        Animation hourTurnAnimation = AnimationUtils.loadAnimation(this, R.anim.hour_turn);
        hourImageView.startAnimation(hourTurnAnimation);
    }
}