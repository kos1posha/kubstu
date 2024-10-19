import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

abstract class PrefsManager {
  static late SharedPreferences _prefs;

  static int? _color;
  static double? _cellFontSize;
  static double? _cellBorderRadius;

  static Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
  }

  static Future<bool> _setPref<T>(String key, T value) async {
    switch (T) {
      case const (int):
        return _prefs.setInt(key, value as int);
      case const (double):
        return _prefs.setDouble(key, value as double);
      default:
        throw ArgumentError('Unsupported type: ${T.toString()}');
    }
  }

  static T _getPref<T>(String key, T? cachedValue, T defaultValue) {
    Object? value = cachedValue ?? _prefs.get(key);
    if (value != null) {
      return value as T;
    }
    _setPref(key, defaultValue);
    return defaultValue;
  }

  static Color get color => Color(_getPref('color', _color, Colors.green[900]!.value));
  static set color(Color color) {
    _setPref('color', color.value);
    _color = color.value;
  }

  static double get cellFontSize => _getPref('cellFontSize', _cellFontSize, 24);
  static set cellFontSize(double size) {
    _setPref('cellFontSize', size);
    _cellFontSize = size;
  }

  static double get cellBorderRadius => _getPref('cellBorderRadius', _cellBorderRadius, 5);
  static set cellBorderRadius(double radius) {
    _setPref('cellBorderRadius', radius);
    _cellBorderRadius = radius;
  }
}

Future<({ThemeData light, ThemeData dark})> getSavedColorScheme() async {
  ThemeData light = ThemeData(colorSchemeSeed: PrefsManager.color, brightness: Brightness.light);
  ThemeData dark = ThemeData(colorSchemeSeed: PrefsManager.color, brightness: Brightness.dark);
  return (light: light, dark: dark);
}
