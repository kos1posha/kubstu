package com.eremin.androidlw2.v6;

import android.content.Context;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.R;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Locale;
import java.util.Objects;
import java.util.stream.IntStream;

public class NMMatrixActivity extends AppCompatActivity {
    SharedPreferences sp;

    List<View> bv;
    List<View> mv;
    List<View> sv;
    List<View> vs = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        TcSettingsActivity.ApplySPTheme(sp, this, false);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_nmmatrix);

        Objects.requireNonNull(getSupportActionBar()).setTitle(R.string.matrix);
        Objects.requireNonNull(getSupportActionBar()).setDisplayHomeAsUpEnabled(true);

        bv = Collections.singletonList(
            findViewById(R.id.et_nmmatrix)
        );
        mv = Collections.singletonList(
            findViewById(R.id.nmmatrix_descr)
        );
        sv = Arrays.asList(
            findViewById(R.id.btn_find),
            findViewById(R.id.nmmatrix_help_text)
        );
        vs.addAll(bv);
        vs.addAll(mv);
        vs.addAll(sv);

        TcSettingsActivity.ApplySPFontFamily(sp, vs);
        TcSettingsActivity.ApplySPFontSize(sp, sv, mv, bv);

        findViewById(R.id.btn_find).setOnClickListener(v -> solve());
    }

    private static int[][] stringToMatrix(String input) {
        String[] rows = input.split("\n");
        int[][] matrix = new int[rows.length][];
        for (int i = 0; i < rows.length; i++) {
            String[] cells = rows[i].split(" ");
            matrix[i] = new int[cells.length];
            for (int j = 0; j < cells.length; j++) {
                matrix[i][j] = Integer.parseInt(cells[j]);
            }
        }
        return matrix;
    }

    protected void solve() {
        String input = ((EditText) findViewById(R.id.et_nmmatrix)).getText().toString();
        if (input.isEmpty()) {
            return;
        }
        List<Integer> result = new ArrayList<>();
        int[][] matrix = stringToMatrix(input);
        for (int i : IntStream.range(0, matrix[0].length).toArray()) {
            int pCount = 0;
            int nCount = 0;
            for (int j : IntStream.range(0, matrix.length).toArray()) {
                if (matrix[j][i] > 0) {
                    pCount++;
                } else if (matrix[j][i] < 0) {
                    nCount++;
                }
            }
            if (pCount == nCount) {
                result.add(i + 1);
            }
        }
        String message;
        if (result.isEmpty()) {
            message = "Подходящих столбцов нет";
        } else {
            message = String.format(Locale.ROOT, "Подходящие столбцы: %s", Arrays.toString(result.toArray()));
        }
        Toast.makeText(this, message, Toast.LENGTH_SHORT).show();
    }
}