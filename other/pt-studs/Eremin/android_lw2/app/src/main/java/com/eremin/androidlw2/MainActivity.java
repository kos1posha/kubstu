package com.eremin.androidlw2;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
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
    }

    protected void setupTheme() {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        int pColor = sp.getInt("primaryColor", getColor(android.R.color.background_light));
        int sColor = sp.getInt("secondaryColor", getColor(android.R.color.holo_green_dark));
        int sSupColor = sp.getInt("secondarySupColor", getColor(android.R.color.background_light));
        view.setBackgroundColor(pColor);
        actionBar.setBackgroundDrawable(new ColorDrawable(sColor));
        for (Button button : Arrays.asList(binding.btnMolecularCalculator, binding.btnFifteenPuzzle)) {
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

    protected void goToSettingsActivity() {
        Intent intent = new Intent(MainActivity.this, SettingsActivity.class);
        startActivity(intent);
    }
}