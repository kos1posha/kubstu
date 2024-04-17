import 'package:flutter/material.dart';

class MainPage extends StatelessWidget {
  const MainPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Возвращение значения')),
      body: Center(
        child: ElevatedButton(
          child: Text('Приступить к выбору...'),
          onPressed: () {
            Navigator.of(context).pushNamed('/selection');
          },
        ),
      ),
    );
  }
}

class SelectionPage extends StatelessWidget {
  const SelectionPage({super.key});

  final List<String> _choises = const [
    'Да!',
    'Нет.',
    'Возможно'
  ];

  void _sendToScaffoldMessager(String message, context) {
    Navigator.of(context).pop();
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content: Text(message), duration: Duration(milliseconds: 750)));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Выберите любой вариант')),
      body: Center(
        child: ListView.builder(
          shrinkWrap: true,
          padding: EdgeInsets.symmetric(vertical: 0.0, horizontal: 120.0),
          itemCount: _choises.length,
          itemBuilder: (BuildContext context, int index) {
            return ElevatedButton(
              onPressed: () {
                _sendToScaffoldMessager(_choises[index], context);
              },
              child: Text(_choises[index]));
          }
        ),
      ),
    );
  }
}
