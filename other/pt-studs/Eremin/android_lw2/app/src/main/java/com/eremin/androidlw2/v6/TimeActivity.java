package com.eremin.androidlw2.v6;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.Gravity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.eremin.androidlw2.R;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Calendar;
import java.util.Collections;
import java.util.Date;
import java.util.List;
import java.util.Locale;
import java.util.Objects;

public class TimeActivity extends AppCompatActivity {
    boolean outputMinutes;
    boolean outputSeconds;
    TextView timeResultMin;
    TextView timeResultSec;
    EditText timeInput;

    SharedPreferences sp;

    List<View> bv;
    List<View> mv;
    List<View> sv;

    @SuppressLint("CutPasteId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        TcSettingsActivity.ApplySPTheme(sp, this, false);

        super.onCreate(savedInstanceState);
        Objects.requireNonNull(getSupportActionBar()).setTitle(R.string.time_converter);
        Objects.requireNonNull(getSupportActionBar()).setDisplayHomeAsUpEnabled(false);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_time);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        bv = Arrays.asList(findViewById(R.id.time_result_min), findViewById(R.id.time_result_sec));
        mv = Collections.singletonList(findViewById(R.id.time_input));
        sv = Collections.singletonList(findViewById(R.id.time_hint));
        TcSettingsActivity.ApplySPFontSize(sp, sv, mv, bv);
        List<View> vs = new ArrayList<>();
        if (sv != null) vs.addAll(sv);
        if (mv != null) vs.addAll(mv);
        if (bv != null) vs.addAll(bv);
        TcSettingsActivity.ApplySPFontFamily(sp, vs);

        outputMinutes = true;
        outputSeconds = true;
        timeResultMin = findViewById(R.id.time_result_min);
        timeResultSec = findViewById(R.id.time_result_sec);
        timeInput = findViewById(R.id.time_input);
        timeInput.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
            }

            @Override
            public void afterTextChanged(Editable s) {
                convertAll(s);
            }
        });
    }

    protected void convertAll(Editable s) {
        String input = s.toString();
        SimpleDateFormat sdf = new SimpleDateFormat("HH:mm:ss", Locale.ROOT);

        try {
            Date date = sdf.parse(input);
            Calendar calendar = Calendar.getInstance();
            calendar.setTime(date);
            int hours = calendar.get(Calendar.HOUR_OF_DAY);
            int minutes = calendar.get(Calendar.MINUTE);
            int seconds = calendar.get(Calendar.SECOND);
            if (outputMinutes) {
                timeResultMin.setText(String.format(Locale.ROOT, "%d мин.", hours * 60 + minutes));
            } else {
                timeResultMin.setText("");
            }
            if (outputSeconds) {
                timeResultSec.setText(String.format(Locale.ROOT, "%d сек.", hours * 3600 + minutes * 60 + seconds));
            } else {
                timeResultSec.setText("");
            }
        } catch (Exception e) {
            int divCount = 0;
            for (int i = 0; i < input.length(); i++) {
                if (input.charAt(i) == ':') {
                    divCount++;
                }
            }
            if (divCount >= 2) {
                Toast invalid = new Toast(getApplicationContext());
                invalid.setGravity(Gravity.CENTER, 0, -50);
                invalid.setDuration(Toast.LENGTH_SHORT);
                View toastView = getLayoutInflater().inflate(R.layout.invalid_time_format_toast, findViewById(R.id.invalid_time_format_main));
                invalid.setView(toastView);
                invalid.show();
                e.printStackTrace();
            }
        }
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.menu_time, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        int id = item.getItemId();
        if (id == R.id.output_minutes) {
            outputMinutes = !outputMinutes;
            item.setChecked(!item.isChecked());
            convertAll(timeInput.getText());
        } else if (id == R.id.output_seconds) {
            outputSeconds = !outputSeconds;
            item.setChecked(!item.isChecked());
            convertAll(timeInput.getText());
        } else if (id == R.id.action_clear_output) {
            timeResultSec.setText("");
            timeResultMin.setText("");
        } else if (id == R.id.to_nmmatrix) {
            startActivity(new Intent(
                TimeActivity.this,
                NMMatrixActivity.class
            ));
        } else if (id == R.id.settings) {
            startActivity(new Intent(
                TimeActivity.this,
                TcSettingsActivity.class
            ));
        }
        return super.onOptionsItemSelected(item);
    }
}