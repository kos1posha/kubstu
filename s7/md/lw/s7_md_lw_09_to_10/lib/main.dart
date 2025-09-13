import 'package:flutter/material.dart';
import 'package:s7_md_lw_09_to_10/space_page.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const SpacePage(),
    );
  }
}
