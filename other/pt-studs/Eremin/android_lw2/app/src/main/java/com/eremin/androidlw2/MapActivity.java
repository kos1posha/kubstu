package com.eremin.androidlw2;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.drawable.ColorDrawable;
import android.location.Address;
import android.location.Geocoder;
import android.net.Uri;
import android.os.Bundle;
import android.view.Gravity;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.ActionBar;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.NavUtils;

import com.eremin.androidlw2.databinding.ActivityMapBinding;
import com.eremin.androidlw2.databinding.EmptyInputToastBinding;
import com.google.type.LatLng;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.Locale;
import java.util.Objects;

public class MapActivity extends AppCompatActivity {
    private ActivityMapBinding binding;
    private View view;
    private ActionBar actionBar;
    private LayoutInflater layoutInflater;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        layoutInflater = getLayoutInflater();
        binding = ActivityMapBinding.inflate(layoutInflater);
        view = binding.getRoot();
        actionBar = Objects.requireNonNull(getSupportActionBar());
        actionBar.setDisplayHomeAsUpEnabled(true);
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
    public boolean onOptionsItemSelected(MenuItem item) {
        switch (item.getItemId()) {
            case android.R.id.home:
                NavUtils.navigateUpFromSameTask(this);
                return true;
        }
        return super.onOptionsItemSelected(item);
    }

    protected void setupListeners() {
        binding.btnSearch.setOnClickListener(this::searchMap);
        binding.btnStreetview.setOnClickListener(this::searchStreet);
    }

    protected void setupTheme() {
        SharedPreferences sp = getSharedPreferences(getPackageName(), Context.MODE_PRIVATE);
        int pColor = sp.getInt("primaryColor", getColor(android.R.color.background_light));
        int sColor = sp.getInt("secondaryColor", getColor(android.R.color.holo_green_dark));
        int sSupColor = sp.getInt("secondarySupColor", getColor(android.R.color.background_light));
        view.setBackgroundColor(pColor);
        actionBar.setBackgroundDrawable(new ColorDrawable(sColor));
        for (Button button : Arrays.asList(binding.btnSearch, binding.btnStreetview)) {
            button.setBackgroundColor(sColor);
            button.setTextColor(sSupColor);
        }
    }

    protected void searchMap(View view) {
        String address = binding.etAddress.getText().toString();
        if (address.isEmpty()) {
            showEmptyInputToast();
        }
        Uri gmmIntentUri = Uri.parse("geo:0,0?q=" + address);
        Intent map = new Intent(Intent.ACTION_VIEW, gmmIntentUri);
        map.setPackage("com.google.android.apps.maps");
        if (map.resolveActivity(getPackageManager()) != null) {
            startActivity(map);
        }
    }

    protected void searchStreet(View view) {
        String address = binding.etAddress.getText().toString();
        if (address.isEmpty()) {
            showEmptyInputToast();
        }
        LatLng point = getLocationFromAddress(this, address);
        String geoUriString = "google.streetview:cbll=LONG,LAT&cbp=1,99.56,,1,2.0&mz=19";
        String geoUri = geoUriString
            .replace("LONG", String.format(Locale.ROOT, "%f", point.getLongitude()).replace(',', '.'))
            .replace("LAT", String.format(Locale.ROOT, "%f", point.getLatitude()).replace(',', '.'));
        Intent map = new Intent(Intent.ACTION_VIEW, Uri.parse(geoUri));
        startActivity(map);
    }

    public LatLng getLocationFromAddress(Context context, String strAddress) {
        Geocoder coder = new Geocoder(context);
        List<Address> address;
        LatLng p1 = null;

        try {
            address = coder.getFromLocationName(strAddress, 5);
            if (address == null) {
                return null;
            }
            Address location = address.get(0);
            p1 = LatLng.newBuilder()
                .setLatitude(location.getLatitude())
                .setLongitude(location.getLongitude()).build();
        } catch (IOException ex) {
            Toast.makeText(this, "Такое место не найдено", Toast.LENGTH_LONG).show();
        }
        return p1;
    }

    protected void showEmptyInputToast() {
        Toast toast = new Toast(getApplicationContext());
        toast.setGravity(Gravity.TOP, 0, 40);
        toast.setDuration(Toast.LENGTH_LONG);
        toast.setView(EmptyInputToastBinding.inflate(layoutInflater).getRoot());
        toast.show();
    }
}