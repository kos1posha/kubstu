import 'package:flutter/material.dart';
import 'rect_page.dart';

void main() {
  runApp(RectApp());
}

class RectApp extends StatelessWidget {
  const RectApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: RectPage(),
    );
  }
}
