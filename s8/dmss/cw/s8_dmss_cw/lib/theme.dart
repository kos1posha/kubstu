import 'package:adaptive_theme/adaptive_theme.dart';
import 'package:flutter/material.dart';

abstract class MainTheme {
  static const Color primary = Color(0xff518005);
  static const Color secondary = Color(0xff85976E);
  static const Color tertiary = Color(0xff4D9D98);
  static const Color neural = Color(0xFF878B8B);

  static ThemeData light = theme(lightScheme);

  static const ColorScheme lightScheme = ColorScheme(
    brightness: Brightness.light,
    primary: Color(0xff253d05),
    surfaceTint: Color(0xff4c662b),
    onPrimary: Color(0xffffffff),
    primaryContainer: Color(0xff5a7539),
    onPrimaryContainer: Color(0xffffffff),
    secondary: Color(0xff303924),
    onSecondary: Color(0xffffffff),
    secondaryContainer: Color(0xff667157),
    onSecondaryContainer: Color(0xffffffff),
    tertiary: Color(0xff083d3a),
    onTertiary: Color(0xffffffff),
    tertiaryContainer: Color(0xff477572),
    onTertiaryContainer: Color(0xffffffff),
    error: Color(0xffaf282f),
    onError: Color(0xffffffff),
    errorContainer: Color(0xffcf2c27),
    onErrorContainer: Color(0xffffffff),
    surface: Color(0xffffffff),
    onSurface: Color(0xff0f120c),
    onSurfaceVariant: Color(0xff34382d),
    outline: Color(0xff505449),
    outlineVariant: Color(0xff6b6f62),
    shadow: Color(0xff000000),
    scrim: Color(0xff000000),
    inverseSurface: Color(0xff2f312a),
    inversePrimary: Color(0xffb1d18a),
    primaryFixed: Color(0xff5a7539),
    onPrimaryFixed: Color(0xffffffff),
    primaryFixedDim: Color(0xff425c23),
    onPrimaryFixedVariant: Color(0xffffffff),
    secondaryFixed: Color(0xff667157),
    onSecondaryFixed: Color(0xffffffff),
    secondaryFixedDim: Color(0xff4e5840),
    onSecondaryFixedVariant: Color(0xffffffff),
    tertiaryFixed: Color(0xff477572),
    onTertiaryFixed: Color(0xffffffff),
    tertiaryFixedDim: Color(0xff2e5c59),
    onTertiaryFixedVariant: Color(0xffffffff),
    surfaceDim: Color(0xffc6c7bd),
    surfaceBright: Color(0xfff9faef),
    surfaceContainerLowest: Color(0xffffffff),
    surfaceContainerLow: Color(0xfff3f4e9),
    surfaceContainer: Color(0xffe8e9de),
    surfaceContainerHigh: Color(0xffe8e9de),
    surfaceContainerHighest: Color(0xffd1d3c8),
  );

  static ThemeData dark = theme(darkScheme);

  static const ColorScheme darkScheme = ColorScheme(
    brightness: Brightness.dark,
    primary: Color(0xffc7e79e),
    surfaceTint: Color(0xffb1d18a),
    onPrimary: Color(0xffffffff),
    primaryContainer: Color(0xff7d9a59),
    onPrimaryContainer: Color(0xffffffff),
    secondary: Color(0xffd5e1c2),
    onSecondary: Color(0xffffffff),
    secondaryContainer: Color(0xff8a9579),
    onSecondaryContainer: Color(0xffffffff),
    tertiary: Color(0xffb5e6e1),
    onTertiary: Color(0xffffffff),
    tertiaryContainer: Color(0xff6b9995),
    onTertiaryContainer: Color(0xffffffff),
    error: Color(0xffffd2cc),
    onError: Color(0xff540003),
    errorContainer: Color(0xffff5449),
    onErrorContainer: Color(0xff000000),
    surface: Color(0xff12140e),
    onSurface: Color(0xffffffff),
    onSurfaceVariant: Color(0xffdbdecf),
    outline: Color(0xffb0b3a6),
    outlineVariant: Color(0xff8e9285),
    shadow: Color(0xff000000),
    scrim: Color(0xff000000),
    inverseSurface: Color(0xffe2e3d8),
    inversePrimary: Color(0xff364f17),
    primaryFixed: Color(0xffcdeda3),
    onPrimaryFixed: Color(0xff081400),
    primaryFixedDim: Color(0xffb1d18a),
    onPrimaryFixedVariant: Color(0xff253d05),
    secondaryFixed: Color(0xffdce7c8),
    onSecondaryFixed: Color(0xff0b1403),
    secondaryFixedDim: Color(0xffbfcbad),
    onSecondaryFixedVariant: Color(0xff303924),
    tertiaryFixed: Color(0xffbcece7),
    onTertiaryFixed: Color(0xff001413),
    tertiaryFixedDim: Color(0xffa0d0cb),
    onTertiaryFixedVariant: Color(0xff083d3a),
    surfaceDim: Color(0xff12140e),
    surfaceBright: Color(0xff43453d),
    surfaceContainerLowest: Color(0xff060804),
    surfaceContainerLow: Color(0xff1c1e18),
    surfaceContainer: Color(0xff262922),
    surfaceContainerHigh: Color(0xff31342c),
    surfaceContainerHighest: Color(0xff3c3f37),
  );
}

double toolbarHeight = 80;

ThemeData theme(ColorScheme colorScheme) {
  return ThemeData(
    useMaterial3: true,
    brightness: colorScheme.brightness,
    colorScheme: colorScheme,
    canvasColor: colorScheme.surface,
    scaffoldBackgroundColor: colorScheme.surface,
    appBarTheme: AppBarTheme(
      titleSpacing: 0,
      titleTextStyle: TextStyle(
        color: colorScheme.onSurface,
        fontSize: 22,
        fontWeight: FontWeight.bold,
      ),
      iconTheme: const IconThemeData(
        color: MainTheme.primary,
        size: 28,
      ),
      toolbarHeight: toolbarHeight,
    ),
    textTheme: const TextTheme().apply(
      bodyColor: colorScheme.onSurface,
      displayColor: colorScheme.onSurface,
    ),
    pageTransitionsTheme: PageTransitionsTheme(builders: {
      for (var tp in TargetPlatform.values) tp: const CupertinoPageTransitionsBuilder(),
    }),
  );
}

Color adaptiveColor(BuildContext context, [Color? colorLight, Color? colorDark]) {
  if (AdaptiveTheme.of(context).brightness == Brightness.light) {
    return colorLight ?? Colors.black;
  } else {
    return colorDark ?? Colors.white;
  }
}

Color errorColor(BuildContext context) => Theme.of(context).colorScheme.error;
