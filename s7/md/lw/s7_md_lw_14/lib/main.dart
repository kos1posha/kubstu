import 'package:flutter/material.dart';
import 'package:s7_md_lw_14/notification_service.dart';
import 'package:s7_md_lw_14/todo_page.dart';
import 'package:s7_md_lw_14/todo_sqlite.dart';
import 'package:s7_md_lw_14/todo_widget.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await TodoSqliteManager.initialize();
  await TodoWidget.initialize();
  await BackgroundNotificationService.initialize();
  BackgroundNotificationService.start();
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(home: TodoPage());
  }
}
