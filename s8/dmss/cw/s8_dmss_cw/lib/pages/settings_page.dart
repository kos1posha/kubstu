import 'package:adaptive_theme/adaptive_theme.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/auth/need_auth.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';

class SettingsPage extends StatefulWidget {
  const SettingsPage({super.key});

  static const String routeName = 'settings';
  static const String routePath = '/settings';

  @override
  MountedState<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends MountedState<SettingsPage> {
  List<bool> get _isSelected {
    AdaptiveThemeManager adaptiveTheme = AdaptiveTheme.of(context);
    return [
      adaptiveTheme.mode.isSystem,
      adaptiveTheme.mode.isLight,
      adaptiveTheme.mode.isDark,
    ];
  }

  @override
  Widget build(BuildContext context) {
    AdaptiveThemeManager adaptiveTheme = AdaptiveTheme.of(context);
    Color? fillColor, selectedColor;
    switch (adaptiveTheme.mode) {
      case AdaptiveThemeMode.system:
        fillColor = Colors.transparent;
        selectedColor = null;
      case AdaptiveThemeMode.light:
        fillColor = Colors.blue[100];
        selectedColor = Colors.amber;
      case AdaptiveThemeMode.dark:
        fillColor = Colors.deepPurple[900];
        selectedColor = Colors.white;
    }
    return AdaptiveDrawerScaffold(
      appBar: const MainAppBar(),
      endDrawer: const MainDrawer(),
      body: NeedAuth(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Text('Настройки', style: titleTextStyle),
            const Divider(height: 48),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Text('Тема приложения', style: subtitleTextStyle),
                const Spacer(),
                ToggleButtons(
                  borderRadius: roundedBorderRadius,
                  isSelected: _isSelected,
                  fillColor: fillColor,
                  selectedColor: selectedColor,
                  onPressed: (index) => switch (index) {
                    0 => adaptiveTheme.setSystem(),
                    1 => adaptiveTheme.setLight(),
                    2 => adaptiveTheme.setDark(),
                    _ => null,
                  },
                  children: const [
                    SizedBox(
                      height: 80,
                      width: 200,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.brightness_auto),
                          smallHDivider,
                          Text('Система', style: TextStyle(fontSize: 18)),
                        ],
                      ),
                    ),
                    SizedBox(
                      height: 80,
                      width: 200,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.light_mode),
                          smallHDivider,
                          Text('Светлая', style: TextStyle(fontSize: 18)),
                        ],
                      ),
                    ),
                    SizedBox(
                      height: 80,
                      width: 200,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        children: [
                          Icon(Icons.dark_mode),
                          smallHDivider,
                          Text('Темная', style: TextStyle(fontSize: 18)),
                        ],
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
