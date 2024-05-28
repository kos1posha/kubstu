package com.eremin.androidlw2;

import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.databinding.ActivityMainBinding;

public class MainActivity extends AppCompatActivity {
    private View view;
    private ActivityMainBinding binding;

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

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.action_molecular_calculator) {
            goToMolecularCountActivity(view);
        } else if (id == R.id.action_fifteen_puzzle) {
            goToFifteenPuzzleActivity(view);
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

    protected void goToMolecularCountActivity(View view) {
        Intent intent = new Intent(MainActivity.this, MolecularCalculatorActivity.class);
        startActivity(intent);
    }

    protected void goToFifteenPuzzleActivity(View view) {
        Intent intent = new Intent(MainActivity.this, FifteenPuzzleActivity.class);
        startActivity(intent);
    }
}