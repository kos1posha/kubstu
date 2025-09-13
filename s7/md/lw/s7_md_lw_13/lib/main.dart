import 'package:flutter/material.dart';
import 'package:s7_md_lw_13/async_buttons_page.dart';

void main() {
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(home: AsyncButtonsPage());
  }
}
