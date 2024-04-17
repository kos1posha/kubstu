import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  runApp(const RectApp());
}

class RectApp extends StatelessWidget {
  const RectApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: RectPage(),
    );
  }
}

class RectPage extends StatefulWidget {
  const RectPage({super.key});

  @override
  State<RectPage> createState() => _RectPageState();
}

class _RectPageState extends State<RectPage> {
  final _formKey = GlobalKey<FormState>();
  int _width = 0;
  int _height = 0;
  int _area = 0;
  String _out = '';

  void _calculate() {
    setState(() {
      _area = _width * _height;
      _out = 'S = $_width * $_height = $_area мм²';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Калькулятор прямоугольника')),
      body: Padding(
        padding: const EdgeInsets.all(12.0),
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text('Ширина (мм):'),
              TextFormField(
                inputFormatters: [FilteringTextInputFormatter.allow(RegExp(r'(^\d*)'))],
                onChanged: (String? value) {
                  setState(() => _width = int.parse(value ?? ''));
                },
              ),
              const Padding(padding: EdgeInsets.only(top: 12)),
              const Text('Высота (мм):'),
              TextFormField(
                inputFormatters: [FilteringTextInputFormatter.allow(RegExp(r'(^\d*)'))],
                onChanged: (String? value) {
                  setState(() => _height = int.parse(value ?? ''));
                },
              ),
              const Padding(padding: EdgeInsets.only(top: 12)),
              Center(child: ElevatedButton(onPressed: _calculate, child: const Text('Вычислить'))),
              const Padding(padding: EdgeInsets.only(top: 12)),
              Center(child: Text(_out, style: const TextStyle(fontSize: 24))),
            ],
          ),
        ),
      ),
    );
  }
}
