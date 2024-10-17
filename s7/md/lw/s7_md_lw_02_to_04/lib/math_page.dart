import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_math_fork/flutter_math.dart';

class MathPage extends StatefulWidget {
  const MathPage({super.key});

  @override
  State<StatefulWidget> createState() => _MathPageState();
}

class _MathPageState extends State<MathPage> {
  double? x = 1.236;
  double? z = 4.5;
  String? a;
  String? y;

  void _solve() {
    bool xIsNull = x == null, zIsNull = z == null;
    if (xIsNull || zIsNull) {
      _showEmptyInputDialog(xIsNull, zIsNull);
      return;
    }
    double yVal = (pow(z!, 2).toDouble()) / (5 + pow(z!, 2).toDouble() / 7);
    double cosArg = (x! - 30) * (pi / 180), sinArg = (yVal + 2) * (pi / 180);
    double aVal = (2 * cos(cosArg)) / (1 / 3 + pow(sin(sinArg), 2));
    setState(() {
      y = yVal.toStringAsFixed(5);
      a = aVal.toStringAsFixed(5);
    });
  }

  void _clear() {
    setState(() {
      y = null;
      a = null;
    });
  }

  Future _showEmptyInputDialog(bool xIsNull, bool zIsNull) {
    String message = '';
    if (xIsNull && zIsNull) {
      message = 'Введите значения для "x" и "z"';
    } else if (xIsNull) {
      message = 'Введите значение для "x"';
    } else if (zIsNull) {
      message = 'Введите значение для "z"';
    }
    return showDialog(
      context: context,
      builder: (BuildContext context) => Dialog(
        child: Padding(
          padding: EdgeInsets.all(32),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Image.asset('assets/images/smile-unknown.png'),
              SizedBox(height: 16),
              Text(
                message,
                style: TextStyle(fontSize: 18),
                textAlign: TextAlign.center,
              ),
              SizedBox(height: 8),
              TextButton(
                onPressed: () {
                  Navigator.pop(context);
                },
                child: Text(
                  'Закрыть',
                  style: TextStyle(fontSize: 18),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Расчет по формуле'),
        foregroundColor: ThemeData.light().primaryColor,
      ),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              decoration: BoxDecoration(
                border: Border.all(color: Colors.white),
                borderRadius: BorderRadius.circular(5),
              ),
              constraints: BoxConstraints.tightFor(height: 120),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Math.tex(
                    a == null
                        ? r'a = \frac{2\cos(x-30^\circ)}{\frac{1}{3} + \sin^2(y+2)}'
                        : 'a = $a',
                    textStyle: TextStyle(fontSize: 24),
                  ),
                  Math.tex(
                    y == null ? r'y = \frac{z^2}{5 + \frac{z^2}{7}}' : 'y = $y',
                    textStyle: TextStyle(fontSize: 24),
                  ),
                ],
              ),
            ),
            SizedBox(height: 16),
            TextFormField(
              initialValue: x.toString(),
              decoration: InputDecoration(label: Text('Введите x')),
              keyboardType: TextInputType.number,
              inputFormatters: [
                FilteringTextInputFormatter.allow(RegExp(r'(^-?\d*\.?\d*)'))
              ],
              onChanged: (value) => setState(() => x = double.tryParse(value)),
            ),
            TextFormField(
              initialValue: z.toString(),
              decoration: InputDecoration(label: Text('Введите z')),
              keyboardType: TextInputType.number,
              inputFormatters: [
                FilteringTextInputFormatter.allow(RegExp(r'(^-?\d*\.?\d*)'))
              ],
              onChanged: (value) => setState(() => z = double.tryParse(value)),
            ),
            SizedBox(height: 16),
            Row(
              children: [
                Expanded(
                  child: ElevatedButton(
                    onPressed: _solve,
                    child: Text('Решить'),
                  ),
                ),
                SizedBox(width: 16),
                Expanded(
                  child: ElevatedButton(
                    onPressed: _clear,
                    child: Text('Очистить'),
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
