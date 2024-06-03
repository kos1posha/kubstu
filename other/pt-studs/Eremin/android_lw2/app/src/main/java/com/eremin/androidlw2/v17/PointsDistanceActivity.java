package com.eremin.androidlw2.v17;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.Gravity;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.R;
import com.eremin.androidlw2.databinding.WarningToastBinding;

public class PointsDistanceActivity extends AppCompatActivity {
    EditText x1;
    EditText y1;
    EditText x2;
    EditText y2;
    Button findDistance;

    int decimalsCount;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        PdSettingsActivity.ApplyTheme(sp, this, false);
        decimalsCount = sp.getInt("decimals_count", 3);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_points_distance);

        x1 = findViewById(R.id.x1);
        y1 = findViewById(R.id.y1);
        x2 = findViewById(R.id.x2);
        y2 = findViewById(R.id.y2);
        findDistance = findViewById(R.id.btn_find_distance);

        findDistance.setOnClickListener(v -> {
            float x1f, y1f, x2f, y2f;
            try {
                x1f = Float.parseFloat(x1.getText().toString());
                y1f = Float.parseFloat(y1.getText().toString());
                x2f = Float.parseFloat(x2.getText().toString());
                y2f = Float.parseFloat(y2.getText().toString());
            } catch (NumberFormatException ex) {
                Toast toast = new Toast(getApplicationContext());
                toast.setGravity(Gravity.TOP, 0, 250);
                toast.setDuration(Toast.LENGTH_LONG);
                toast.setView(WarningToastBinding.inflate(getLayoutInflater()).getRoot());
                toast.show();
                return;
            }
            double dist = Math.sqrt(Math.pow(x1f - x2f, 2) + Math.pow(y1f - y2f, 2));
            double decimals = decimalsCount == -1 ? 1 : (int) Math.pow(10, decimalsCount);
            dist = Math.round(dist * decimals) / decimals;
            Toast.makeText(this, "Расстояние: " + dist, Toast.LENGTH_SHORT).show();
        });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_points, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.action_settings) {
            Intent settingsIntent = new Intent(PointsDistanceActivity.this, PdSettingsActivity.class);
            startActivity(settingsIntent);
        } else if (id == R.id.action_about) {
            Toast toast = Toast.makeText(this, "Приложение считает расстояние между двумя точками",
                Toast.LENGTH_SHORT);
            toast.show();
        }
        return super.onOptionsItemSelected(item);
    }
}