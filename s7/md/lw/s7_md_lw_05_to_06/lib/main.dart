import 'package:adaptive_theme/adaptive_theme.dart';
import 'package:flutter/material.dart';
import 'package:s7_md_lw_05_to_06/prefs_manager.dart';
import 'barley_break_page.dart';
import 'settings_page.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await PrefsManager.init();
  runApp(MainApp(
    savedThemeMode: await AdaptiveTheme.getThemeMode(),
    savedColorScheme: await getSavedColorScheme(),
  ));
}

class MainApp extends StatelessWidget {
  final AdaptiveThemeMode? savedThemeMode;
  final ({ThemeData light, ThemeData dark})? savedColorScheme;

  const MainApp({super.key, this.savedThemeMode, this.savedColorScheme});

  @override
  Widget build(BuildContext context) {
    return AdaptiveTheme(
      light: savedColorScheme!.light,
      dark: savedColorScheme!.dark,
      initial: savedThemeMode ?? AdaptiveThemeMode.system,
      builder: (theme, darkTheme) => MaterialApp(
        theme: theme,
        darkTheme: darkTheme,
        initialRoute: '/',
        routes: {
          '/': (context) => const BarleyBreakPage(),
          '/settings': (context) => const SettingsPage(),
        },
      ),
    );
  }
}
