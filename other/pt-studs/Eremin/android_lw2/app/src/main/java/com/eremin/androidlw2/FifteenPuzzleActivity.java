package com.eremin.androidlw2;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NavUtils;
import androidx.lifecycle.LifecycleOwner;

import com.eremin.androidlw2.databinding.ActivityFifteenPuzzleBinding;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class FifteenPuzzleActivity extends AppCompatActivity implements LifecycleOwner {
    private ActivityFifteenPuzzleBinding binding;
    private View view;
    private ActionBar actionBar;

    int buttonsColor;
    int buttonsTextColor;

    int matrixSize = 4;
    int buttonSize = 80;
    int tableOffsetX = 20;
    int tableOffsetY = 20;
    float scale = 1.0f;
    List<Button> buttons = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityFifteenPuzzleBinding.inflate(getLayoutInflater());
        view = binding.getRoot();
        actionBar = Objects.requireNonNull(getSupportActionBar());
        actionBar.setDisplayHomeAsUpEnabled(true);
        setContentView(binding.getRoot());
        setupTheme();
        scale = getApplicationContext().getResources().getDisplayMetrics().density;
        buttonSize = (int) (buttonSize * scale);
        tableOffsetX = (int) (tableOffsetX * scale);
        tableOffsetY = (int) (tableOffsetY * scale);
        initGame();
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

    protected void setupTheme() {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        int pColor = sp.getInt("primaryColor", getColor(android.R.color.background_light));
        int sColor = sp.getInt("secondaryColor", getColor(android.R.color.holo_green_dark));
        int sSupColor = sp.getInt("secondarySupColor", getColor(android.R.color.background_light));
        view.setBackgroundColor(pColor);
        actionBar.setBackgroundDrawable(new ColorDrawable(sColor));
        buttonsColor = sColor;
        buttonsTextColor = sSupColor;
    }

    protected void initGame() {
        binding.main.removeAllViews();
        List<Integer> rows = IntStream.range(0, matrixSize).boxed().collect(Collectors.toList());
        List<Integer> columns = IntStream.range(0, matrixSize).boxed().collect(Collectors.toList());
        Collections.shuffle(rows);
        Collections.shuffle(columns);
        for (Integer row : rows) {
            for (Integer column : columns) {
                Button button = createButton((float) column, (float) row);
                buttons.add(button);
                binding.main.addView(button);
            }
        }
    }

    protected void moveButton(Button currentButton) {
        Button targetButton = binding.main.findViewWithTag("target");
        int tbX = (int) targetButton.getX(), tbY = (int) targetButton.getY();
        int cbX = (int) currentButton.getX(), cbY = (int) currentButton.getY();
        boolean isNeighbour = isNeighbours(
            (tbX - tableOffsetX) / buttonSize, (tbY - tableOffsetY) / buttonSize,
            (cbX - tableOffsetX) / buttonSize, (cbY - tableOffsetY) / buttonSize
        );
        if (isNeighbour) {
            currentButton.setX(tbX);
            currentButton.setY(tbY);
            targetButton.setX(cbX);
            targetButton.setY(cbY);
        }
        if (gameCompleted()) {
            Toast.makeText(this, "Ура! Победа!", Toast.LENGTH_SHORT).show();
        }
    }

    protected Boolean isNeighbours(int x1, int y1, int x2, int y2) {
        return Math.abs(x1 - x2) + Math.abs(y1 - y2) == 1;
    }

    protected Boolean gameCompleted() {
        int index = 1;
        for (int row : IntStream.range(0, matrixSize).toArray()) {
            for (int column : IntStream.range(0, matrixSize).toArray()) {
                Button button = binding.main.findViewById(index);
                if (button.getX() != column * buttonSize + tableOffsetX || button.getY() != row * buttonSize + tableOffsetY) {
                    return false;
                }
                index++;
            }
        }
        return true;
    }

    protected Button createButton(Float x, Float y) {
        Button button = new Button(this);
        int buttonId = View.generateViewId();
        button.setX(x * buttonSize + tableOffsetX + 10 * scale * x);
        button.setY(y * buttonSize + tableOffsetY);
        button.setWidth(buttonSize);
        button.setHeight(buttonSize);
        button.setId(buttonId);
        button.setOnClickListener(v -> moveButton(button));
        button.setText(String.valueOf(buttonId));
        button.getBackground().setTint(buttonsColor);
        button.setTextColor(buttonsTextColor);
        if (buttonId == matrixSize * matrixSize) {
            button.setText(" ");
            button.setTag("target");
            button.getBackground().setTint(Color.WHITE);
        }
        return button;
    }
}