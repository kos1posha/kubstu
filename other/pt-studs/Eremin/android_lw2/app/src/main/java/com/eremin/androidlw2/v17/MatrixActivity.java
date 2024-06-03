package com.eremin.androidlw2.v17;

import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.InputType;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.content.res.AppCompatResources;

import com.eremin.androidlw2.R;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;
import java.util.stream.IntStream;

public class MatrixActivity extends AppCompatActivity {
    private final List<EditText> edits = new ArrayList<>();
    private final int tableWidth = 4;
    private final int tableHeight = 4;

    TableLayout matrixTable;
    TableLayout resultTable;
    Button btnDefine;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        SharedPreferences sp = getSharedPreferences(getPackageName(), MODE_PRIVATE);
        PdSettingsActivity.ApplyTheme(sp, this, false);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_matrix17);
        ActionBar actionBar = Objects.requireNonNull(getSupportActionBar());
        actionBar.setDisplayHomeAsUpEnabled(true);
        actionBar.setTitle("Матрица");

        matrixTable = findViewById(R.id.matrix_table);
        resultTable = findViewById(R.id.result_table);
        btnDefine = findViewById(R.id.btn_define);
        initMatrixTable();

        btnDefine.setOnClickListener(v -> initResultTable());
    }

    protected void initMatrixTable() {
        for (Integer ignored1 : IntStream.range(0, tableHeight).toArray()) {
            TableRow tableRow = new TableRow(this);
            tableRow.setLayoutParams(new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
            for (Integer ignored2 : IntStream.range(0, tableWidth).toArray()) {
                EditText editText = createEditText();
                tableRow.addView(editText);
                edits.add(editText);
            }
            matrixTable.addView(tableRow);
        }
    }

    protected void initResultTable() {
        resultTable.removeAllViews();
        TableRow tableRow = new TableRow(this);
        tableRow.setLayoutParams(new ViewGroup.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        int index = 0;
        for (Integer ignored1 : IntStream.range(0, tableHeight).toArray()) {
            int columnSum = 0;
            boolean negativeMet = false;
            for (Integer ignored2 : IntStream.range(0, tableWidth).toArray()) {
                String text = edits.get(index).getText().toString();
                int value = text.isEmpty() ? 0 : Integer.parseInt(text);
                if (value < 0) {
                    negativeMet = true;
                }
                if (negativeMet) {
                    columnSum += value;
                }
                index++;
            }
            tableRow.addView(createTextView(String.valueOf(columnSum)));
        }
        resultTable.addView(tableRow);
    }

    protected EditText createEditText() {
        EditText editText = new EditText(this);
        editText.setHint("0");
        editText.setInputType(InputType.TYPE_CLASS_NUMBER | InputType.TYPE_NUMBER_FLAG_SIGNED);
        editText.setTextAlignment(View.TEXT_ALIGNMENT_CENTER);
        editText.setLayoutParams(new TableRow.LayoutParams(TableRow.LayoutParams.MATCH_PARENT, TableRow.LayoutParams.WRAP_CONTENT, 1f));
        editText.setId(View.generateViewId());
        editText.setBackground(AppCompatResources.getDrawable(this, R.drawable.et_matrix_shape));
        return editText;
    }

    protected TextView createTextView(String text) {
        TextView textView = new TextView(this);
        textView.setText(text);
        textView.setTextSize(16);
        textView.setPadding(0, 20, 0, 20);
        textView.setTextAlignment(View.TEXT_ALIGNMENT_CENTER);
        textView.setLayoutParams(new TableRow.LayoutParams(TableRow.LayoutParams.MATCH_PARENT, TableRow.LayoutParams.WRAP_CONTENT, 1f));
        textView.setId(View.generateViewId());
        textView.setBackground(AppCompatResources.getDrawable(this, R.drawable.et_matrix_shape));
        return textView;
    }
}