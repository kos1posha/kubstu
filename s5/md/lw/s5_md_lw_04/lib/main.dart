import 'package:flutter/material.dart';
import 'the64powers_page.dart';

void main() {
  runApp(The64PowersApp());
}

class The64PowersApp extends StatelessWidget {
  const The64PowersApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '64 степени',
      home: The64PowersPage(),
    );
  }
}
