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

import com.eremin.androidlw2.databinding.ActivityFifteenPuzzleBinding;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.Random;
import java.util.stream.IntStream;

public class FifteenPuzzleActivity extends AppCompatActivity {
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
        int n = 4;
        int[][] matrix = IntStream.range(0, n).mapToObj(i -> IntStream.range(1, n + 1).map(j -> i * n + j).toArray()).toArray(int[][]::new);
        shuffleMatrix(matrix);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Button button = createButton(j, i, matrix[i][j]);
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
                int correctX = (int) (column * buttonSize + tableOffsetX + 10 * scale * column);
                int correctY = row * buttonSize + tableOffsetY;
                if ((int) button.getX() != correctX || (int) button.getY() != correctY) {
                    return false;
                }
                index++;
            }
        }
        return true;
    }

    protected Button createButton(int x, int y, int buttonId) {
        Button button = new Button(this);
        button.setX(x * buttonSize + tableOffsetX + 10 * scale * x);
        button.setY(y * buttonSize + tableOffsetY);
        button.setWidth(buttonSize);
        button.setHeight(buttonSize);
        button.setId(buttonId);
        button.setOnClickListener(v -> moveButton(button));
        button.setText(String.valueOf(buttonId));
        button.getBackground().setTint(buttonsColor);
        button.setTextColor(buttonsTextColor);
        if (buttonId == 16) {
            button.setTag("target");
            button.getBackground().setTint(Color.WHITE);
        }
        return button;
    }

    public static void shuffleMatrix(int[][] matrix) {
        Random random = new Random();
        for (int i = matrix.length - 1; i > 0; i--) {
            for (int j = matrix[i].length - 1; j > 0; j--) {
                int m = random.nextInt(i + 1);
                int n = random.nextInt(j + 1);

                int temp = matrix[i][j];
                matrix[i][j] = matrix[m][n];
                matrix[m][n] = temp;
            }
        }
    }
}