package com.eremin.androidlw2;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NavUtils;

import com.eremin.androidlw2.databinding.ActivityMolecularCalculatorBinding;
import com.eremin.androidlw2.databinding.EmptyInputToastBinding;

import java.util.Collections;
import java.util.Locale;
import java.util.Objects;

public class MolecularCalculatorActivity extends AppCompatActivity {
    private ActivityMolecularCalculatorBinding binding;
    private View view;
    private ActionBar actionBar;
    private LayoutInflater layoutInflater;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        layoutInflater = getLayoutInflater();
        binding = ActivityMolecularCalculatorBinding.inflate(layoutInflater);
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
        binding.btnCalculate.setOnClickListener(this::calculate);
    }

    protected void setupTheme() {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        int pColor = sp.getInt("primaryColor", getColor(android.R.color.background_light));
        int sColor = sp.getInt("secondaryColor", getColor(android.R.color.holo_green_dark));
        int sSupColor = sp.getInt("secondarySupColor", getColor(android.R.color.background_light));
        view.setBackgroundColor(pColor);
        actionBar.setBackgroundDrawable(new ColorDrawable(sColor));
        for (Button button : Collections.singletonList(binding.btnCalculate)) {
            button.setBackgroundColor(sColor);
            button.setTextColor(sSupColor);
        }
    }

    protected void calculate(View view) {
        String quartsString = binding.etWaterQuartsCount.getText().toString();
        if (quartsString.isEmpty()) {
            showEmptyInputToast();
            return;
        }
        int quartsCount = Integer.parseInt(quartsString);
        double molecularCount = calculateMolecularCountInQuarts(quartsCount);
        binding.twMolecularCount.setText(String.format(Locale.ROOT, "%.0f", molecularCount));
    }

    protected double calculateMolecularCountInQuarts(int quartsCount) {
        return quartsCount * 950 / 3e-23;
    }

    protected void showEmptyInputToast() {
        Toast toast = new Toast(getApplicationContext());
        toast.setGravity(Gravity.TOP, 0, 40);
        toast.setDuration(Toast.LENGTH_LONG);
        toast.setView(EmptyInputToastBinding.inflate(layoutInflater).getRoot());
        toast.show();
    }
}