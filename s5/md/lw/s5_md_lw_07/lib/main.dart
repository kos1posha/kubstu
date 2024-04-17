import 'dart:io' as io;
import 'package:flutter/material.dart';
import 'news_list_page.dart';

void main() {
  io.HttpOverrides.global = HttpOverrides();
  runApp(const NewsApp());
}

class NewsApp extends StatelessWidget {
  const NewsApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        home: NewsListPage()
    );
  }
}

class HttpOverrides extends io.HttpOverrides {
  @override
  io.HttpClient createHttpClient(io.SecurityContext? context) {
    return super.createHttpClient(context)
      ..badCertificateCallback = (io.X509Certificate cert, String host, int port) => true;
  }
}
