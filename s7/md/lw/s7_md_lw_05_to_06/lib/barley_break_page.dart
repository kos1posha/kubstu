import 'package:adaptive_theme/adaptive_theme.dart';
import 'package:collection/collection.dart';
import 'package:flutter/material.dart';
import 'package:s7_md_lw_05_to_06/notification_manager.dart';
import 'package:s7_md_lw_05_to_06/prefs_manager.dart';

class BarleyBreakPage extends StatefulWidget {
  const BarleyBreakPage({super.key});

  @override
  State<StatefulWidget> createState() => _BarleyBreakPageState();
}

class _BarleyBreakPageState extends State<BarleyBreakPage> {
  List<List<int>> winCon = List.generate(4, (i) {
    return List.generate(4, (j) {
      int value = i * 4 + j + 1;
      return value == 16 ? 0 : value;
    });
  });
  List<({int x, int y})> history = [];
  late List<List<int>> bb = winCon.map((e) => e.toList()).toList();

  void _randomize() {
    List<int> random = List.generate(16, (i) => i);
    random.shuffle();
    setState(() {
      for (int i = 0; i < random.length; i++) {
        bb[i ~/ 4][i % 4] = random[i];
      }
      history.clear();
    });
  }

  void _move(({int x, int y}) current, {bool isNext = true}) {
    ({int x, int y}) empty = _getEmptyCell();
    if (_isNearby(current, empty)) {
      setState(() {
        int temp = bb[current.x][current.y];
        bb[current.x][current.y] = bb[empty.x][empty.y];
        bb[empty.x][empty.y] = temp;
        if (isNext) {
          history.add(empty);
        } else {
          history.removeLast();
        }
      });
      if (_isWinning()) {
        NotificationManager.showNotification('Красавчик, выиграл', '');
      }
    }
  }

  void _previous() {
    _move(history.last, isNext: false);
  }

  ({int x, int y}) _getEmptyCell() {
    for (int i = 0; i < 4; i++) {
      int j = bb[i].indexOf(0);
      if (j != -1) {
        return (x: i, y: j);
      }
    }
    throw Exception('This shouldn\'t happen');
  }

  bool _isNearby(({int x, int y}) c1, ({int x, int y}) c2) {
    return (c1.x == c2.x && (c1.y == c2.y + 1 || c1.y == c2.y - 1)) ||
        (c1.y == c2.y && (c1.x == c2.x + 1 || c1.x == c2.x - 1));
  }

  bool _isWinning() {
    return const DeepCollectionEquality().equals(bb, winCon);
  }

  @override
  void initState() {
    super.initState();
    // _randomize();
  }

  @override
  Widget build(BuildContext context) {
    var adaptive = AdaptiveTheme.of(context);
    return Scaffold(
      appBar: AppBar(
        title: const Text('Пятнашки'),
        foregroundColor: adaptive.lightTheme.primaryColor,
        actions: [
          IconButton(onPressed: (history.isEmpty) ? null : _previous, icon: const Icon(Icons.replay)),
          IconButton(
            onPressed: _randomize,
            icon: const Icon(Icons.casino),
          ),
          IconButton(
            onPressed: () async {
              await Navigator.pushNamed(context, '/settings');
              setState(() {});
            },
            icon: const Icon(Icons.settings),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: GridView.count(
          shrinkWrap: true,
          crossAxisCount: 4,
          crossAxisSpacing: 10,
          mainAxisSpacing: 10,
          children: List.generate(16, (index) {
            int x = index ~/ 4, y = index % 4;
            int item = bb[x][y];
            return (item == 0)
                ? const SizedBox.shrink()
                : FilledButton(
                    style: ButtonStyle(
                      shape: WidgetStateProperty.all(RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(PrefsManager.cellBorderRadius),
                      )),
                    ),
                    onPressed: () => _move((x: x, y: y)),
                    child: Text('$item', style: TextStyle(fontSize: PrefsManager.cellFontSize)),
                  );
          }),
        ),
      ),
    );
  }
}
