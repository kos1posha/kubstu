import 'package:flutter/material.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: Scaffold(
        body: Center(
          child: Text(
            'Hello World!',
            style: TextStyle(
                fontSize: 48,
                fontWeight: FontWeight.bold,
                fontStyle: FontStyle.italic,
                fontFamily: 'serif',
                color: Colors.pinkAccent,
                shadows: [
                  Shadow(
                    color: Colors.cyan,
                    blurRadius: 10,
                    offset: Offset(5, 5),
                  ),
                  Shadow(
                    color: Colors.deepPurple,
                    blurRadius: 5,
                    offset: Offset(-5, -5),
                  ),
                ],
                decoration: TextDecoration.underline,
                decorationColor: Colors.green,
                decorationStyle: TextDecorationStyle.wavy,
                decorationThickness: 2),
          ),
        ),
      ),
    );
  }
}
