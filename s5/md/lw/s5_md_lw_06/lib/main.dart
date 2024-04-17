import 'package:flutter/material.dart';
import 'pages.dart';

void main() {
  runApp(RouteNavigationApp());
}

class RouteNavigationApp extends StatelessWidget {
  RouteNavigationApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/',
      routes: {
        '/': (BuildContext context) => MainPage(),
        '/selection': (BuildContext context) => SelectionPage(),
      },
    );
  }
}
