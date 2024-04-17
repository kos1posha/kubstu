import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Инкремент',
      home: IncrPage(),
    );
  }
}

class IncrPage extends StatefulWidget {
  const IncrPage({super.key});

  @override
  State<IncrPage> createState() => _IncrPageState();
}

class _IncrPageState extends State<IncrPage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() { _counter++; });
  }

  void _decrementCounter() {
    setState(() { _counter--; });
  }

  void _resetCounter() {
    setState(() { _counter = 0; });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.cyan,
        foregroundColor: Colors.white,
        title: const Text('Инкремент'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text('Значение инкремента:', style: TextStyle(fontSize: 20)),
            Text('$_counter', style: const TextStyle(fontSize: 40)),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: _decrementCounter,
                  style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.redAccent)),
                  child: const Text('–', style: TextStyle(color: Colors.black, fontSize: 30)),
                ),
                ElevatedButton(
                  onPressed: _incrementCounter,
                  style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.greenAccent)),
                  child: const Text('+', style: TextStyle(color: Colors.black, fontSize: 30)),
                ),
              ],
            ),
            TextButton(
                onPressed: _resetCounter,
                style: ButtonStyle(foregroundColor: MaterialStateProperty.all<Color>(Colors.black26)),
                child: const Text('Сбросить')
            ),
          ],
        ),
      ),
    );
  }
}
