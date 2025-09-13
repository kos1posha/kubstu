import 'package:auto_size_text/auto_size_text.dart';
import 'package:flutter/material.dart';
import 'package:home_widget/home_widget.dart';

import 'package:s7_md_lw_14/todo_sqlite.dart';

class TodoWidget extends StatelessWidget {
  final List<Todo> todos;
  final Color color;

  static const Size logicalSize = Size(200, 270);

  const TodoWidget({super.key, required this.todos, required this.color});

  static Future<void> initialize() async {
    await HomeWidget.setAppGroupId('com.example.s7_md_lw_14');
  }

  static Future<void> update(TodoWidget widget) async {
    await HomeWidget.renderFlutterWidget(widget, key: 'todoWidget', logicalSize: logicalSize);
    await HomeWidget.updateWidget(androidName: 'TodoWidgetProvider');
  }

  Widget buildExpandedTodoCard(Todo todo) {
    return Expanded(
      child: SizedBox(
        width: double.infinity,
        child: Card(
          shape: const ContinuousRectangleBorder(),
          child: Center(
            child: Padding(
              padding: const EdgeInsets.all(16),
              child: AutoSizeText(
                todo.text,
                softWrap: true,
                maxLines: 3,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(color: Colors.black, fontSize: 100),
                minFontSize: 14,
              ),
            ),
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return ColoredBox(
      color: Colors.white,
      child: SizedBox.fromSize(
        size: logicalSize,
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: todos.isEmpty
              ? const Center(
                  child: Text(
                    'Похоже, вы совершенно свободны от всяческих забот :)',
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      color: Colors.grey,
                      fontSize: 20,
                    ),
                  ),
                )
              : Column(
                  children: [
                    SizedBox(
                      width: double.infinity,
                      child: Text(
                        'Мои TODO\'шки',
                        textAlign: TextAlign.center,
                        style: TextStyle(
                          color: color,
                          fontSize: 22,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                    ),
                    buildExpandedTodoCard(todos[0]),
                    todos.length > 1 ? buildExpandedTodoCard(todos[1]) : const Spacer(),
                  ],
                ),
        ),
      ),
    );
  }
}
