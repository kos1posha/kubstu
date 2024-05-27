package com.eremin.androidlw2;

import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.databinding.ActivityMolecularCalculatorBinding;

import java.util.Locale;

public class MolecularCalculatorActivity extends AppCompatActivity {
    private View view;
    private ActivityMolecularCalculatorBinding binding;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityMolecularCalculatorBinding.inflate(getLayoutInflater());
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
        int quartsCount = Integer.parseInt(binding.etWaterQuartsCount.getText().toString());
        double molecularCount = calculateMolecularCountInQuarts(quartsCount);
        binding.twMolecularCount.setText(String.format(Locale.ROOT, "%.0f", molecularCount));
    }

    protected double calculateMolecularCountInQuarts(int quartsCount) {
        return quartsCount * 950 / 3e-23;
    }
}