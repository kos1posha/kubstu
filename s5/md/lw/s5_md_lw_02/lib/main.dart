import 'package:flutter/material.dart';
import 'increment_page.dart';

void main() {
  runApp(IncrementApp());
}

class IncrementApp extends StatelessWidget {
  const IncrementApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Инкремент',
      home: IncrementPage(),
    );
  }
}
