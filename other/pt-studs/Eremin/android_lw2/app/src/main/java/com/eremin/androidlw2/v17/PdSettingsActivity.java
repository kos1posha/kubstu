package com.eremin.androidlw2.v17;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RadioButton;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.R;

import java.util.Arrays;
import java.util.List;
import java.util.Objects;

public class PdSettingsActivity extends AppCompatActivity {
    public static List<Integer> Themes = Arrays.asList(
        com.google.android.material.R.style.Theme_Material3_Light,
        com.google.android.material.R.style.Theme_Material3_Dark
    );

    RadioButton lightTheme;
    RadioButton darkTheme;
    EditText decimalsCount;
    Button btnSave;

    SharedPreferences sp;
    SharedPreferences.Editor editor;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        ApplyTheme(sp, this, false);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pd_settings);

        editor = sp.edit();
        ActionBar actionBar = Objects.requireNonNull(getSupportActionBar());
        actionBar.setDisplayHomeAsUpEnabled(true);
        actionBar.setTitle("Настройки");

        lightTheme = findViewById(R.id.theme_light);
        darkTheme = findViewById(R.id.theme_dark);
        decimalsCount = findViewById(R.id.decimals_count);
        btnSave = findViewById(R.id.btn_save);

        lightTheme.setOnClickListener(v -> changeTheme(Themes.get(0)));
        darkTheme.setOnClickListener(v -> changeTheme(Themes.get(1)));
        btnSave.setOnClickListener(v -> {
            changeDecimalsCount(decimalsCount.getText().toString());
            ApplyTheme(sp, this, true);
            startActivity(getParentActivityIntent());
        });

        lightTheme.setChecked(sp.getInt("theme", com.google.android.material.R.style.Theme_Material3_DayNight) == Themes.get(0));
        darkTheme.setChecked(sp.getInt("theme", com.google.android.material.R.style.Theme_Material3_DayNight) == Themes.get(1));
        int dc = sp.getInt("decimals_count", 3);
        decimalsCount.setText(dc == -1 ? "" : String.valueOf(dc));
    }

    protected void changeTheme(Integer theme) {
        editor.putInt("theme", theme);
        editor.apply();
    }

    protected void changeDecimalsCount(String decimalsCount) {
        editor.putInt("decimals_count", decimalsCount.isEmpty() ? -1 : Integer.parseInt(decimalsCount));
        editor.apply();
    }

    public static void ApplyTheme(SharedPreferences sp, Activity activity, boolean reload) {
        int theme = sp.getInt("theme", com.google.android.material.R.style.Theme_Material3_DayNight);
        activity.setTheme(theme);
        if (reload) {
            activity.finish();
            activity.startActivity(activity.getIntent());
        }
    }
}