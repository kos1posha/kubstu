package com.eremin.androidlw2;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.drawable.ColorDrawable;
import android.os.Bundle;
import android.text.InputType;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup.LayoutParams;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TableRow;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.content.res.AppCompatResources;
import androidx.core.app.NavUtils;

import com.eremin.androidlw2.databinding.ActivityMatrixBinding;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Objects;
import java.util.stream.IntStream;

public class MatrixActivity extends AppCompatActivity {
    private ActivityMatrixBinding binding;
    private View view;
    private ActionBar actionBar;
    private LayoutInflater layoutInflater;
    private final List<EditText> edits = new ArrayList<>();
    private final int tableWidth = 4;
    private final int tableHeight = 4;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        layoutInflater = getLayoutInflater();
        binding = ActivityMatrixBinding.inflate(layoutInflater);
        view = binding.getRoot();
        actionBar = Objects.requireNonNull(getSupportActionBar());
        actionBar.setDisplayHomeAsUpEnabled(true);
        setContentView(view);
        setupListeners();
        setupTheme();
        initTable();
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
        binding.btnDefine.setOnClickListener(this::solveTask);
    }

    protected void setupTheme() {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        int pColor = sp.getInt("primaryColor", getColor(android.R.color.background_light));
        int sColor = sp.getInt("secondaryColor", getColor(android.R.color.holo_green_dark));
        int sSupColor = sp.getInt("secondarySupColor", getColor(android.R.color.background_light));
        view.setBackgroundColor(pColor);
        actionBar.setBackgroundDrawable(new ColorDrawable(sColor));
        for (Button button : Collections.singletonList(binding.btnDefine)) {
            button.setBackgroundColor(sColor);
            button.setTextColor(sSupColor);
        }
    }

    protected void initTable() {
        for (Integer ignored1 : IntStream.range(0, tableHeight).toArray()) {
            TableRow tableRow = new TableRow(this);
            tableRow.setLayoutParams(new LayoutParams(LayoutParams.MATCH_PARENT, LayoutParams.MATCH_PARENT));
            for (Integer ignored2 : IntStream.range(0, tableWidth).toArray()) {
                EditText editText = createEditText();
                tableRow.addView(editText);
                edits.add(editText);
            }
            binding.tlMatrixTable.addView(tableRow);
        }
    }

    protected EditText createEditText() {
        EditText editText = new EditText(this);
        editText.setHint("0");
        editText.setInputType(InputType.TYPE_CLASS_NUMBER);
        editText.setTextAlignment(View.TEXT_ALIGNMENT_CENTER);
        editText.setLayoutParams(new TableRow.LayoutParams(TableRow.LayoutParams.MATCH_PARENT, TableRow.LayoutParams.WRAP_CONTENT, 1f));
        editText.setId(View.generateViewId());
        editText.setBackground(AppCompatResources.getDrawable(this, R.drawable.et_matrix_shape));
        return editText;
    }

    protected void solveTask(View view) {
        String a = binding.etA.getText().toString(), b = binding.etB.getText().toString();
        if (a.isEmpty() || b.isEmpty()) {
            Toast.makeText(this, "Введите оба значения A и B", Toast.LENGTH_SHORT).show();
            return;
        }
        int A = Integer.parseInt(a), B = Integer.parseInt(b);
        if (A > B) {
            Toast.makeText(this, "A должно быть меньше B", Toast.LENGTH_SHORT).show();
            return;
        }
        for (int i = 0; i < edits.size(); i += tableWidth) {
            List<EditText> row = edits.subList(i, i + tableWidth);
            boolean rowPassed = true;
            for (EditText editText : row) {
                String text = editText.getText().toString();
                int num = text.isEmpty() ? 0 : Integer.parseInt(text);
                if (num < A || B < num) {
                    rowPassed = false;
                    break;
                }
            }
            if (rowPassed) {
                Toast.makeText(this, "Утверждение верно для данной матрицы", Toast.LENGTH_LONG).show();
                return;
            }
        }
        Toast.makeText(this, "Утверждение ложно для данной матрицы", Toast.LENGTH_LONG).show();
    }
}