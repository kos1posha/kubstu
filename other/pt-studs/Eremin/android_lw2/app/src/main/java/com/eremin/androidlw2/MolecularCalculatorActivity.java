package com.eremin.androidlw2;

import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.databinding.ActivityMolecularCalculatorBinding;
import com.eremin.androidlw2.databinding.EmptyInputToastBinding;

import java.util.Locale;

public class MolecularCalculatorActivity extends AppCompatActivity {
    private View view;
    private LayoutInflater layoutInflater;
    private ActivityMolecularCalculatorBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        layoutInflater = getLayoutInflater();
        binding = ActivityMolecularCalculatorBinding.inflate(layoutInflater);
        view = binding.getRoot();
        setContentView(view);
        setupListeners();
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        binding = null;
    }

    protected void setupListeners() {
        binding.btnCalculate.setOnClickListener(this::calculate);
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