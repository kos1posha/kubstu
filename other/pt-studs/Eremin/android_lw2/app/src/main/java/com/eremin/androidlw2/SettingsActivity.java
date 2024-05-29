package com.eremin.androidlw2;

import android.content.Context;
import android.content.SharedPreferences;
import android.content.res.ColorStateList;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.RadioButton;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NavUtils;

import com.eremin.androidlw2.databinding.ActivitySettingsBinding;

import java.util.Arrays;
import java.util.Collections;
import java.util.Objects;

public class SettingsActivity extends AppCompatActivity {
    private ActivitySettingsBinding binding;
    private View view;
    private ActionBar actionBar;
    private LayoutInflater layoutInflater;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        layoutInflater = getLayoutInflater();
        binding = ActivitySettingsBinding.inflate(layoutInflater);
        view = binding.getRoot();
        actionBar = Objects.requireNonNull(getSupportActionBar());
        actionBar.setDisplayHomeAsUpEnabled(true);
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
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case android.R.id.home:
                NavUtils.navigateUpFromSameTask(this);
                return true;
        }
        return super.onOptionsItemSelected(item);
    }

    protected void setupListeners() {
        binding.btnApply.setOnClickListener(this::applyNewTheme);
    }

    protected void setupTheme() {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        int pColor = sp.getInt("primaryColor", getColor(android.R.color.background_light));
        int pOnColor = sp.getInt("primaryOnColor", getColor(android.R.color.background_dark));
        int sColor = sp.getInt("secondaryColor", getColor(android.R.color.holo_green_dark));
        int sSupColor = sp.getInt("secondarySupColor", getColor(android.R.color.background_light));
        view.setBackgroundColor(pColor);
        actionBar.setBackgroundDrawable(new ColorDrawable(sColor));
        for (Button button : Collections.singletonList(binding.btnApply)) {
            button.setBackgroundColor(sColor);
            button.setTextColor(sSupColor);
        }
        ColorStateList colorStateList = new ColorStateList(
            new int[][]{
                new int[]{-android.R.attr.state_checked},
                new int[]{android.R.attr.state_checked}
            },
            new int[]{
                sColor,
                sColor
            }
        );
        for (RadioButton rButton : Arrays.asList(
            binding.rbPcLight, binding.rbPcDark, binding.rbPcGreen,
            binding.rbScLight, binding.rbScDark, binding.rbScGreen,
            binding.rbTcLight, binding.rbTcDark, binding.rbTcGreen
        )) {
            rButton.setButtonTintList(colorStateList);
            rButton.setTextColor(pOnColor);
        }
    }

    protected void applyNewTheme(View view) {
        if (binding.rbPcLight.isChecked() && binding.rbScLight.isChecked() ||
            binding.rbPcDark.isChecked() && binding.rbScDark.isChecked() ||
            binding.rbPcGreen.isChecked() && binding.rbScGreen.isChecked()) {
            Toast.makeText(this, "Основной и дополнительный цвета должны отличаться", Toast.LENGTH_SHORT).show();
            return;
        }
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        SharedPreferences.Editor editor = sp.edit();
        if (binding.rbPcLight.isChecked()) {
            editor.putInt("primaryColor", getColor(android.R.color.background_light));
            editor.putInt("primaryOnColor", getColor(android.R.color.background_dark));
        } else if (binding.rbPcDark.isChecked()) {
            editor.putInt("primaryColor", getColor(android.R.color.background_dark));
            editor.putInt("primaryOnColor", getColor(android.R.color.background_light));
        } else if (binding.rbPcGreen.isChecked()) {
            editor.putInt("primaryColor", getColor(android.R.color.holo_green_dark));
            editor.putInt("primaryOnColor", getColor(android.R.color.background_light));
        }
        if (binding.rbScLight.isChecked()) {
            editor.putInt("secondaryColor", getColor(android.R.color.background_light));
            editor.putInt("secondarySupColor", getColor(android.R.color.background_dark));
        } else if (binding.rbScDark.isChecked()) {
            editor.putInt("secondaryColor", getColor(android.R.color.background_dark));
            editor.putInt("secondarySupColor", getColor(android.R.color.background_light));
        } else if (binding.rbScGreen.isChecked()) {
            editor.putInt("secondaryColor", getColor(android.R.color.holo_green_dark));
            editor.putInt("secondarySupColor", getColor(android.R.color.background_light));
        }
        editor.apply();
        setupTheme();
    }
}