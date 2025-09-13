import 'dart:math';
import 'package:dynamic_height_grid_view/dynamic_height_grid_view.dart';
import 'package:flutter/material.dart';

class MatrixPage extends StatefulWidget {
  const MatrixPage({super.key});

  @override
  State<StatefulWidget> createState() => _MatrixPageState();
}

class _MatrixPageState extends State<MatrixPage> {
  int _rowCount = 4;
  int _columnCount = 4;

  final List<int> _firstEvens = List.filled(9, -1);
  final List<List<TextEditingController>> _cells = List.generate(
    9,
    (_) => List.generate(9, (_) => TextEditingController()),
  );

  Future<void> _findFirstEvens() async {
    for (int i = 0; i < 9; i++) {
      _findFirstEvenForColumn(i);
    }
  }

  Future<void> _findFirstEvenForColumn(int i) async {
    for (int j = 0; j < 9; j++) {
      int cell = int.tryParse(_cells[i][j].text) ?? -1;
      if (cell.isEven) {
        setState(() => _firstEvens[i] = j);
        return;
      }
    }
  }

  Future<void> _randomize() async {
    setState(() {
      Random r = Random();
      for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
          _cells[i][j].value = TextEditingValue(text: '${r.nextInt(15)}');
        }
      }
    });
    _findFirstEvens();
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
        title: const Text('s7_md_lw_07'),
        foregroundColor: Theme.of(context).primaryColor,
        actions: [
          IconButton(
            onPressed: _randomize,
            icon: const Icon(Icons.casino),
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 16),
        child: OrientationBuilder(
          builder: (context, orientation) {
            if (orientation == Orientation.portrait) {
              return Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      const Expanded(flex: 1, child: Text('Строк', style: TextStyle(fontSize: 18))),
                      Expanded(
                        flex: 3,
                        child: Slider(
                          min: 2.0,
                          max: 9.0,
                          divisions: 7,
                          label: _rowCount.toString(),
                          value: _rowCount.toDouble(),
                          onChanged: (value) async => setState(() => _rowCount = value.toInt()),
                        ),
                      ),
                    ],
                  ),
                  Row(
                    children: [
                      const Expanded(flex: 1, child: Text('Столбцов', style: TextStyle(fontSize: 18))),
                      Expanded(
                        flex: 3,
                        child: Slider(
                          min: 2.0,
                          max: 9.0,
                          divisions: 7,
                          label: _columnCount.toString(),
                          value: _columnCount.toDouble(),
                          onChanged: (value) async => setState(() => _columnCount = value.toInt()),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 16),
                  Expanded(
                    child: SingleChildScrollView(
                      primary: true,
                      child: Padding(
                        padding: const EdgeInsets.only(bottom: 16),
                        child: DynamicHeightGridView(
                          physics: const NeverScrollableScrollPhysics(),
                          shrinkWrap: true,
                          mainAxisSpacing: 0,
                          crossAxisSpacing: 0,
                          crossAxisCount: _columnCount,
                          itemCount: _rowCount * _columnCount,
                          builder: (context, index) {
                            int row = index ~/ _columnCount;
                            int column = index % _columnCount;
                            return TextField(
                              controller: _cells[column][row],
                              keyboardType: TextInputType.number,
                              textAlign: TextAlign.center,
                              decoration: InputDecoration(
                                border: const OutlineInputBorder(borderRadius: BorderRadius.zero),
                                filled: _firstEvens[column] == row,
                                fillColor: (Theme.of(context).primaryColor.withAlpha(160)),
                              ),
                              onChanged: (_) => _findFirstEvenForColumn(column),
                            );
                          },
                        ),
                      ),
                    ),
                  ),
                ],
              );
            } else {
              return Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Expanded(
                    flex: 5,
                    child: SingleChildScrollView(
                      primary: true,
                      child: Padding(
                        padding: const EdgeInsets.only(bottom: 16),
                        child: DynamicHeightGridView(
                          physics: const NeverScrollableScrollPhysics(),
                          shrinkWrap: true,
                          mainAxisSpacing: 0,
                          crossAxisSpacing: 0,
                          crossAxisCount: _columnCount,
                          itemCount: _rowCount * _columnCount,
                          builder: (context, index) {
                            int row = index ~/ _columnCount;
                            int column = index % _columnCount;
                            return TextField(
                              controller: _cells[column][row],
                              keyboardType: TextInputType.number,
                              textAlign: TextAlign.center,
                              decoration: InputDecoration(
                                border: const OutlineInputBorder(borderRadius: BorderRadius.zero),
                                filled: _firstEvens[column] == row,
                                fillColor: (Theme.of(context).primaryColor.withAlpha(160)),
                              ),
                              onChanged: (_) => _findFirstEvenForColumn(column),
                            );
                          },
                        ),
                      ),
                    ),
                  ),
                  Expanded(
                    flex: 1,
                    child: Column(
                      children: [
                        const Text('Строк', style: TextStyle(fontSize: 18)),
                        Expanded(
                          child: RotatedBox(
                            quarterTurns: -1,
                            child: Slider(
                              min: 2.0,
                              max: 9.0,
                              divisions: 7,
                              value: _rowCount.toDouble(),
                              onChanged: (value) async => setState(() => _rowCount = value.toInt()),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  Expanded(
                    flex: 1,
                    child: Column(
                      children: [
                        const Text('Столбцов', style: TextStyle(fontSize: 18)),
                        Expanded(
                          flex: 10,
                          child: RotatedBox(
                            quarterTurns: -1,
                            child: Slider(
                              min: 2.0,
                              max: 9.0,
                              divisions: 7,
                              value: _columnCount.toDouble(),
                              onChanged: (value) async => setState(() => _columnCount = value.toInt()),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              );
            }
          },
        ),
      ),
    );
  }
}
