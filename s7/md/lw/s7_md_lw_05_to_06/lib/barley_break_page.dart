import 'package:flutter/material.dart';

class BarleyBreakPage extends StatefulWidget {
  const BarleyBreakPage({super.key});

  @override
  State<StatefulWidget> createState() => _BarleyBreakPageState();
}

class _BarleyBreakPageState extends State<BarleyBreakPage> {
  List<List<int>> bb = List.generate(4, (i) => List.generate(4, (j) => 0));
  List<({int x, int y})> history = [];

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

  @override
  void initState() {
    super.initState();
    _randomize();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Пятнашки'),
        foregroundColor: ThemeData.light().primaryColor,
        actions: [
          IconButton(
              onPressed: (history.isEmpty) ? null : _previous,
              icon: Icon(Icons.replay)),
          IconButton(
            onPressed: _randomize,
            icon: Icon(Icons.casino),
          ),
        ],
      ),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: GridView.builder(
          itemCount: 16,
          gridDelegate: SliverGridDelegateWithMaxCrossAxisExtent(
            maxCrossAxisExtent: 100,
            mainAxisSpacing: 10,
            crossAxisSpacing: 10,
          ),
          itemBuilder: (context, index) {
            int x = index ~/ 4, y = index % 4;
            int item = bb[x][y];
            if (item == 0) {
              return SizedBox.shrink();
            }
            return FilledButton(
              onPressed: () => _move((x: x, y: y)),
              style: ButtonStyle(
                shape: WidgetStateProperty.all<RoundedRectangleBorder>(
                  RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(0),
                  ),
                ),
              ),
              child: Text('$item'),
            );
          },
        ),
      ),
    );
  }
}
