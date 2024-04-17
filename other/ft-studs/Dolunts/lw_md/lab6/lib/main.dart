import 'package:flutter/material.dart';

void main() {
  runApp(const SelectApp());
}

class SelectApp extends StatelessWidget {
  const SelectApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/main',
      routes: {
        '/main': (BuildContext context) => const Page1(),
        '/select': (BuildContext context) => const Page2(),
      },
    );
  }
}

class Page1 extends StatelessWidget {
  const Page1({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Возвращение значения')),
      body: Center(
        child: ElevatedButton(
          child: const Text('Приступить к выбору...'),
          onPressed: () {
            Navigator.of(context).pushNamed('/select');
          },
        ),
      ),
    );
  }
}

class Page2 extends StatelessWidget {
  const Page2({super.key});

  void _showMes(String message, context) {
    Navigator.of(context).pop();
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: Text(message), duration: const Duration(milliseconds: 750)));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Выберите любой вариант')),
      body: Center(
        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          ElevatedButton(
              onPressed: () {
                _showMes('Да!', context);
              },
              child: const Text('Да!')),
          ElevatedButton(
              onPressed: () {
                _showMes('Нет.', context);
              },
              child: const Text('Нет.')),
        ]),
      ),
    );
  }
}
