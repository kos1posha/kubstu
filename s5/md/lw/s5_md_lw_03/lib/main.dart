import 'package:flutter/material.dart';
import 'dormitory_page.dart';

void main() {
  runApp(DormitoryApp());
}

class DormitoryApp extends StatelessWidget {
  const DormitoryApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Общежития КубГАУ',
      home: DormitoryPage(),
    );
  }
}
