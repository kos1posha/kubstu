import 'package:adaptive_theme/adaptive_theme.dart';
import 'package:flutter/material.dart';
import 'package:s7_md_lw_05_to_06/prefs_manager.dart';

class SettingsPage extends StatefulWidget {
  const SettingsPage({super.key});

  @override
  State<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  List<int> cells = [4, 2, 0, 7];

  List<IconData> themeIcons = [Icons.brightness_5, Icons.brightness_4, Icons.brightness_6];
  List<({String title, Color color, ThemeData light, ThemeData dark})> colorSchemes = [
    _getColorScheme('Бескрайний космос', Colors.deepPurpleAccent[700]!),
    _getColorScheme('Весенний лес', Colors.green[900]!),
    _getColorScheme('Подводные глубины', Colors.blue[900]!),
  ];

  late double cellFontSize;
  late double cellBorderRadius;

  @override
  void initState() {
    super.initState();
    setState(() {
      cellFontSize = PrefsManager.cellFontSize;
      cellBorderRadius = PrefsManager.cellBorderRadius;
    });
  }

  @override
  Widget build(BuildContext context) {
    AdaptiveThemeManager<ThemeData> adaptive = AdaptiveTheme.of(context);
    return Scaffold(
      appBar: AppBar(
        title: Text('Настройки'),
        foregroundColor: adaptive.lightTheme.primaryColor,
        actions: [
          IconButton(
            onPressed: adaptive.toggleThemeMode,
            icon: Icon(themeIcons[adaptive.mode.index]),
          )
        ],
      ),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text('Превью', style: TextStyle(fontSize: 24)),
            SizedBox(height: 10),
            GridView.count(
              shrinkWrap: true,
              crossAxisCount: 4,
              crossAxisSpacing: 10,
              mainAxisSpacing: 10,
              children: List.generate(4, (index) {
                int item = cells[index];
                return (item == 0)
                    ? SizedBox.shrink()
                    : FilledButton(
                        style: ButtonStyle(
                          shape: WidgetStateProperty.all(RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(cellBorderRadius),
                          )),
                        ),
                        onPressed: () {
                          int empty = cells.indexOf(0);
                          if ((empty - index).abs() == 1) {
                            setState(() {
                              cells[index] = cells[empty];
                              cells[empty] = item;
                            });
                          }
                        },
                        child: Text('$item', style: TextStyle(fontSize: cellFontSize)),
                      );
              }),
            ),
            SizedBox(height: 10),
            Text('Цветовая схема', style: TextStyle(fontSize: 24)),
            SizedBox(height: 10),
            ListView.builder(
              shrinkWrap: true,
              itemCount: colorSchemes.length,
              itemBuilder: (context, index) {
                var scheme = colorSchemes[index];
                return Theme(
                  data: (adaptive.theme.brightness == Brightness.light) ? scheme.light : scheme.dark,
                  child: ElevatedButton(
                    child: Text(scheme.title),
                    onPressed: () {
                      adaptive.setTheme(light: scheme.light, dark: scheme.dark, notify: true);
                      PrefsManager.color = scheme.color;
                    },
                  ),
                );
              },
            ),
            SizedBox(height: 10),
            Text('Шрифт в ячейках', style: TextStyle(fontSize: 24)),
            Slider(
              min: 16,
              max: 32,
              divisions: 4,
              value: cellFontSize,
              onChanged: (value) => setState(() => cellFontSize = value),
              onChangeEnd: (value) => setState(() => PrefsManager.cellFontSize = cellFontSize),
            ),
            Text('Округлость краев', style: TextStyle(fontSize: 24)),
            Slider(
              min: 0,
              max: 45,
              divisions: 22,
              value: cellBorderRadius,
              onChanged: (value) => setState(() => cellBorderRadius = value),
              onChangeEnd: (value) => setState(() => PrefsManager.cellBorderRadius = cellBorderRadius),
            ),
          ],
        ),
      ),
    );
  }
}

_getColorScheme(String title, Color color) {
  return (
    title: title,
    color: color,
    light: ThemeData(brightness: Brightness.light, colorSchemeSeed: color),
    dark: ThemeData(brightness: Brightness.dark, colorSchemeSeed: color),
  );
}
