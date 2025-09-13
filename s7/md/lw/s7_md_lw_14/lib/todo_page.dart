import 'package:flutter/material.dart';
import 'package:s7_md_lw_14/todo_sqlite.dart';
import 'package:s7_md_lw_14/todo_widget.dart';

class TodoPage extends StatefulWidget {
  const TodoPage({super.key});

  @override
  State<TodoPage> createState() => _TodoPageState();
}

class _TodoPageState extends State<TodoPage> {
  late Color primaryColor = Theme.of(context).primaryColor;
  bool loading = true;

  List<Todo> todos = [];

  @override
  void initState() {
    super.initState();
    loadTodos();
  }

  Future<void> loadTodos() async {
    List<Todo> loadedTodos = await Todo.objects.all();
    setState(() {
      todos = loadedTodos;
      loading = false;
    });
    if (mounted) {
      TodoWidget.update(TodoWidget(todos: todos, color: primaryColor));
    }
  }

  Future<void> addTodo() async {
    final TextEditingController taskNameController = TextEditingController();
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Добавить TODO\'шку', style: TextStyle(fontSize: 22)),
          content: TextFormField(
            controller: taskNameController,
            style: const TextStyle(fontSize: 14),
            decoration: const InputDecoration(
              contentPadding: EdgeInsets.all(8),
              hintText: 'TODO\'шка',
              border: OutlineInputBorder(),
            ),
          ),
          actions: [
            SizedBox(
              width: double.infinity,
              child: TextButton(
                onPressed: () async {
                  if (taskNameController.value.text.isNotEmpty) {
                    await Todo.objects.insert(Todo(
                      id: 0,
                      text: taskNameController.value.text,
                      order: todos.length + 1,
                    ));
                    loadTodos();
                  }
                  if (context.mounted) {
                    Navigator.of(context).pop();
                  }
                },
                child: const Text('Добавить'),
              ),
            ),
          ],
        );
      },
    );
  }

  Future<void> deleteTodo(int id) async {
    await Todo.objects.delete(id);
    loadTodos();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Мои TODO\'шки'),
        foregroundColor: Colors.white,
        backgroundColor: primaryColor,
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: addTodo,
        child: const Icon(Icons.add),
      ),
      body: loading
          ? Center(
              child: CircularProgressIndicator(
                color: primaryColor,
                strokeWidth: 3,
              ),
            )
          : todos.isEmpty
              ? const Center(
                  child: Padding(
                    padding: EdgeInsets.fromLTRB(60, 0, 60, 60),
                    child: Text(
                      'Похоже, вы совершенно свободны от всяческих забот :)',
                      textAlign: TextAlign.center,
                      style: TextStyle(
                        color: Colors.grey,
                        fontSize: 16,
                      ),
                    ),
                  ),
                )
              : Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                  child: ReorderableListView(
                    children: [
                      for (int index = 0; index < todos.length; index += 1)
                        Dismissible(
                          key: UniqueKey(),
                          onDismissed: (direction) => deleteTodo(todos[index].id),
                          child: Card(
                            shape: const ContinuousRectangleBorder(),
                            child: Padding(
                              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 8),
                              child: Row(
                                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                                children: [
                                  Text(todos[index].text),
                                  const Icon(Icons.drag_handle),
                                ],
                              ),
                            ),
                          ),
                        ),
                    ],
                    onReorder: (int oldIndex, int newIndex) {
                      setState(() {
                        if (oldIndex < newIndex) newIndex -= 1;
                        Todo item = todos.removeAt(oldIndex);
                        todos.insert(newIndex, item);
                      });
                      Todo.objects.updateOrder(todos);
                      TodoWidget.update(TodoWidget(todos: todos, color: primaryColor));
                    },
                  ),
                ),
    );
  }
}
