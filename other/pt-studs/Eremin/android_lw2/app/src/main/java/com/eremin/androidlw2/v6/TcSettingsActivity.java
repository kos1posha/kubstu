package com.eremin.androidlw2.v6;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Typeface;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.eremin.androidlw2.R;
import com.eremin.androidlw2.databinding.ActivityTcSettingsBinding;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Objects;

import kotlin.Triple;

public class TcSettingsActivity extends AppCompatActivity {
    public static List<Integer> Themes = Arrays.asList(
        com.google.android.material.R.style.Theme_Material3_Light,
        com.google.android.material.R.style.Theme_Material3_Dark,
        com.google.android.material.R.style.Theme_Material3_DayNight
    );
    public static List<String> FontFamilies = Arrays.asList(
        "sans-serif",
        "serif-monospace",
        "sans-serif-condensed"
    );
    public static List<Triple<Integer, Integer, Integer>> FontSizes = Arrays.asList(
        new Triple<>(14, 18, 24),
        new Triple<>(24, 28, 34),
        new Triple<>(34, 38, 44)
    );

    SharedPreferences sp;
    SharedPreferences.Editor editor;

    List<View> bv;
    List<View> mv;
    List<View> sv;
    List<View> vs = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        editor = sp.edit();
        ApplySPTheme(sp, this, false);

        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        ActivityTcSettingsBinding binding = ActivityTcSettingsBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        ActionBar actionBar = Objects.requireNonNull(getSupportActionBar());
        actionBar.setDisplayHomeAsUpEnabled(true);
        actionBar.setTitle("Настройки");

        bv = Arrays.asList(
            findViewById(R.id.theme_title),
            findViewById(R.id.ff_title),
            findViewById(R.id.fs_title)
        );
        mv = Arrays.asList(
            findViewById(R.id.theme_light),
            findViewById(R.id.theme_dark),
            findViewById(R.id.theme_system),
            findViewById(R.id.ff_sans_serif),
            findViewById(R.id.ff_monospace),
            findViewById(R.id.ff_roboto),
            findViewById(R.id.fs_big),
            findViewById(R.id.fs_medium),
            findViewById(R.id.fs_small)
        );
        sv = null;
        vs.addAll(mv);
        vs.addAll(bv);

        ApplySPFontFamily(sp, vs);
        ApplySPFontSize(sp, sv, mv, bv);

        binding.themeLight.setOnClickListener(v -> {
            SetSPTheme(Themes.get(0));
            ApplySPTheme(sp, this, true);
        });
        binding.themeDark.setOnClickListener(v -> {
            SetSPTheme(Themes.get(1));
            ApplySPTheme(sp, this, true);
        });
        binding.themeSystem.setOnClickListener(v -> {
            SetSPTheme(Themes.get(2));
            ApplySPTheme(sp, this, true);
        });
        binding.fsSmall.setOnClickListener(v -> {
            SetSPFontSize(FontSizes.get(0));
            ApplySPFontSize(sp, sv, mv, bv);
        });
        binding.fsMedium.setOnClickListener(v -> {
            SetSPFontSize(FontSizes.get(1));
            ApplySPFontSize(sp, sv, mv, bv);
        });
        binding.fsBig.setOnClickListener(v -> {
            SetSPFontSize(FontSizes.get(2));
            ApplySPFontSize(sp, sv, mv, bv);
        });
        binding.ffSansSerif.setOnClickListener(v -> {
            SetSPFontFamily(FontFamilies.get(0));
            ApplySPFontFamily(sp, vs);
        });
        binding.ffMonospace.setOnClickListener(v -> {
            SetSPFontFamily(FontFamilies.get(1));
            ApplySPFontFamily(sp, vs);
        });
        binding.ffRoboto.setOnClickListener(v -> {
            SetSPFontFamily(FontFamilies.get(2));
            ApplySPFontFamily(sp, vs);
        });
        putSettings(binding);

    }

    protected void putSettings(ActivityTcSettingsBinding binding) {
        binding.themeLight.setChecked(sp.getInt("theme", com.google.android.material.R.style.Theme_Material3_DayNight) == Themes.get(0));
        binding.themeDark.setChecked(sp.getInt("theme", com.google.android.material.R.style.Theme_Material3_DayNight) == Themes.get(1));
        binding.themeSystem.setChecked(sp.getInt("theme", com.google.android.material.R.style.Theme_Material3_DayNight) == Themes.get(2));
        binding.fsSmall.setChecked(sp.getInt("fontSizeS", 14) == FontSizes.get(0).component1());
        binding.fsMedium.setChecked(sp.getInt("fontSizeS", 14) == FontSizes.get(1).component1());
        binding.fsBig.setChecked(sp.getInt("fontSizeS", 14) == FontSizes.get(2).component1());
        binding.ffSansSerif.setChecked(sp.getString("fontFamily", "sans-serif").equals(FontFamilies.get(0)));
        binding.ffMonospace.setChecked(sp.getString("fontFamily", "sans-serif").equals(FontFamilies.get(1)));
        binding.ffRoboto.setChecked(sp.getString("fontFamily", "sans-serif").equals(FontFamilies.get(2)));
    }

    protected void SetSPTheme(Integer theme) {
        editor.putInt("theme", theme);
        editor.apply();
    }

    protected void SetSPFontSize(Triple<Integer, Integer, Integer> fontSize) {
        editor.putInt("fontSizeS", fontSize.component1());
        editor.putInt("fontSizeM", fontSize.component2());
        editor.putInt("fontSizeB", fontSize.component3());
        editor.apply();
    }

    protected void SetSPFontFamily(String fontFamily) {
        editor.putString("fontFamily", fontFamily);
        editor.apply();
    }

    protected static void ApplySPTheme(SharedPreferences sp, Activity activity, boolean reload) {
        int theme = sp.getInt("theme", com.google.android.material.R.style.Theme_Material3_DayNight);
        activity.setTheme(theme);
        if (reload) {
            activity.finish();
            activity.startActivity(activity.getIntent());
        }
    }

    protected static void ApplySPFontSize(SharedPreferences sp, List<View> sv, List<View> mv, List<View> bv) {
        int fontSizeS = sp.getInt("fontSizeS", 14);
        int fontSizeM = sp.getInt("fontSizeM", 18);
        int fontSizeB = sp.getInt("fontSizeB", 24);
        if (sv != null) apply_spfs(sv, fontSizeS);
        if (mv != null) apply_spfs(mv, fontSizeM);
        if (bv != null) apply_spfs(bv, fontSizeB);
    }

    protected static void apply_spfs(List<View> vs, int fs) {
        for (View view : vs) {
            if (view instanceof Button) {
                ((Button) view).setTextSize(fs);
            } else if (view instanceof TextView) {
                ((TextView) view).setTextSize(fs);
            }
        }
    }

    protected static void ApplySPFontFamily(SharedPreferences sp, List<View> vs) {
        String fontFamily = sp.getString("fontFamily", "sans-serif");
        Typeface tf = Typeface.create(fontFamily, Typeface.NORMAL);
        for (View view : vs) {
            if (view instanceof Button) {
                ((Button) view).setTypeface(tf);
            } else if (view instanceof TextView) {
                ((TextView) view).setTypeface(tf);
            }
        }
    }
}