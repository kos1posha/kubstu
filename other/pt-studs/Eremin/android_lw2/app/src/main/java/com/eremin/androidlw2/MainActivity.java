package com.eremin.androidlw2;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;

import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {
    private ActivityMainBinding binding;
    private View view;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityMainBinding.inflate(getLayoutInflater());
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
        binding.btnMolecularCalculator.setOnClickListener(this::goToMolecularCountActivity);
    }

    protected void goToMolecularCountActivity(View view) {
        Intent intent = new Intent(MainActivity.this, MolecularCalculatorActivity.class);
        startActivity(intent);
    }
}