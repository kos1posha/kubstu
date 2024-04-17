import 'package:flutter/material.dart';
import 'dart:math';

void main() {
  runApp(const PowApp());
}

class PowApp extends StatelessWidget {
  const PowApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
            title: const Text('Список элементов'),
            backgroundColor: Colors.green),
        body: Padding(
          padding: const EdgeInsets.symmetric(vertical: 8),
          child: ListView.separated(
              itemCount: 63,
              separatorBuilder: (BuildContext context, int index) => const Divider(),
              itemBuilder: (context, index) {
                num p = pow(2, index);
                return Padding(
                  padding:
                  const EdgeInsets.symmetric(horizontal: 8, vertical: 20),
                  child: Text('2 ^ $index = $p',
                      style: const TextStyle(fontSize: 20)),
                );
              }),
        ),
      ),
    );
  }
}
