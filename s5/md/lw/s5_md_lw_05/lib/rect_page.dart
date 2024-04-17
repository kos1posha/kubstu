import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class RectPage extends StatefulWidget {
  const RectPage({super.key});

  @override
  State<RectPage> createState() => _RectPageState();
}

class _RectPageState extends State<RectPage> {
  final _formKey = GlobalKey<FormState>();
  double _width = 0;
  double _height = 0;
  double _rectWidth = 0;
  double _rectHeight = 0;
  final _maxWidth = 400.0;
  final _maxHeight = 300.0;

  String _area = '';
  String _perimeter = '';

  void _calculate() {
    setState(() {
      _area = 'S = ${(_width * _height).toDouble()} px²';
      _perimeter = 'P = ${(_width == 0 || _height == 0 ? 0: (_width + _height) * 2).toDouble()} px';
    });
    _resize();
  }

  Size _prResize({double? newWidth, double? newHeight}) {
    Size newSize;
    if (newWidth != null) {
      newSize = Size(newWidth, newWidth * _height / _width);
    } else if (newHeight != null) {
      newSize = Size(newHeight * _width / _height, newHeight);
    } else {
      newSize = Size(0, 0);
    }
    return newSize;
  }

  void _resize() {
    Size newSize = Size(_maxWidth, _maxHeight);
    if (_width == 0 || _height == 0)
      newSize = Size(0, 0);
    else {
      if (_width <= newSize.width && _height <= newSize.height)
        newSize = Size(_width, _height);
      else if (_width > newSize.width && _height > newSize.height) {
        if (_width >= _height) {
          newSize = _prResize(newHeight: _maxHeight);
          if (newSize.width > _maxWidth)
            newSize = _prResize(newWidth: _maxWidth);
        } else {
          newSize = _prResize(newWidth: _maxWidth);
          if (newSize.height > _maxHeight)
            newSize = _prResize(newHeight: _maxHeight);
        }
      }
      else if (_width > newSize.width)
        newSize = _prResize(newWidth: newSize.width);
      else if (_height > newSize.height)
        newSize = _prResize(newHeight: newSize.height);
    }
    setState(() {
      _rectWidth = newSize.width;
      _rectHeight = newSize.height;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Калькулятор прямоугольника')),
      body: Center(
        child: Padding(
          padding: EdgeInsets.all(12.0),
          child: Form(
            key: _formKey,
            child: Column(
              children: [
                TextFormField(
                  decoration: InputDecoration(labelText: 'Ширина (px)'),
                  inputFormatters: [FilteringTextInputFormatter.allow(RegExp(r'(^\d*)'))],
                  style: TextStyle(color: Colors.blue),
                  onChanged: (String? value) {
                    setState(() => _width = double.parse(value ?? ''));
                    _calculate();
                  },
                ),
                TextFormField(
                  decoration: InputDecoration(labelText: 'Высота (px)'),
                  inputFormatters: [FilteringTextInputFormatter.allow(RegExp(r'(^\d*)'))],
                  style: TextStyle(color: Colors.blue),
                  onChanged: (String? value) {
                    setState(() => _height = double.parse(value ?? ''));
                    _calculate();
                  },
                ),
                Padding(padding: EdgeInsets.only(top: 12)),
                Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: [
                    Text(_area, style: TextStyle(fontSize: 18)),
                    Text(_perimeter, style: TextStyle(fontSize: 18)),
                  ],
                ),
                Padding(padding: EdgeInsets.only(top: 12)),
                Align(
                  alignment: Alignment.center,
                  child: Container(
                    decoration: BoxDecoration(border: Border.all(color: Colors.black)),
                    width: _rectWidth,
                    height: _rectHeight,
                  )
                )
              ],
            ),
          ),
        ),
      ),
    );
  }
}
