package com.eremin.androidlw2;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

import com.eremin.androidlw2.views.DrawView;

public class DrawActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(new DrawView(this));
    }
}