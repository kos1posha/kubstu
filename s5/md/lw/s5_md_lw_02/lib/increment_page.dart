import 'package:flutter/material.dart';

class IncrementPage extends StatefulWidget {
  const IncrementPage({super.key});

  @override
  State<IncrementPage> createState() => _IncrementPageState();
}

class _IncrementPageState extends State<IncrementPage> {
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
        backgroundColor: Colors.pink,
        foregroundColor: Colors.black,
        title: Text('Инкремент'),
      ),
      body: Dismissible(
        key: Key("IncrementPage"),
        background: Container(
          padding: EdgeInsets.only(bottom: 100),
          color: Colors.black12,
          child: Align(
            alignment: Alignment.bottomCenter,
            child: Icon(
              Icons.rotate_left,
              color: Colors.white,
              size: 120,
            ),
          ),
        ),
        direction: DismissDirection.up,
        confirmDismiss: (DismissDirection direction) {
          _resetCounter();
          return Future(() => false);
        },
        child: Dismissible(
          key: Key("IncrementPage"),
          background: Container(
            padding: EdgeInsets.only(left: 75),
            color: Colors.green,
            child: Align(
              alignment: Alignment.centerLeft,
              child: Icon(
                Icons.add_circle,
                color: Colors.white,
                size: 120,
              ),
            ),
          ),
          secondaryBackground: Container(
            padding: EdgeInsets.only(right: 75),
            color: Colors.red,
            child: Align(
              alignment: Alignment.centerRight,
              child: Icon(
                Icons.remove_circle,
                color: Colors.white,
                size: 120,
              ),
            ),
          ),
          confirmDismiss: (DismissDirection direction) {
            direction == DismissDirection.startToEnd
                ? _incrementCounter()
                : _decrementCounter();
            return Future(() => false);
          },
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Text('Значение инкремента:', style: TextStyle(fontSize: 20)),
                Text('$_counter', style: TextStyle(fontSize: 40)),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    ElevatedButton(
                      onPressed: _incrementCounter,
                      style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.greenAccent)),
                      child: Text('+', style: TextStyle(color: Colors.black, fontSize: 30)),
                    ),
                    Padding(padding: EdgeInsets.only(left: 10)),
                    ElevatedButton(
                      onPressed: _decrementCounter,
                      style: ButtonStyle(backgroundColor: MaterialStateProperty.all<Color>(Colors.redAccent)),
                      child: Text('–', style: TextStyle(color: Colors.black, fontSize: 30)),
                    ),
                  ],
                ),
                TextButton(
                  onPressed: _resetCounter,
                  style: ButtonStyle(foregroundColor: MaterialStateProperty.all<Color>(Colors.black26)),
                  child: Text('Сбросить')
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}