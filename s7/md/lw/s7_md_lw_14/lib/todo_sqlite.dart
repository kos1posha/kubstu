import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

class Todo {
  int id;
  String text;
  int order;

  Todo({required this.id, required this.text, required this.order});

  Map<String, Object?> toSqlMap() {
    return {'text': text, 'todo_order': order};
  }

  static final TodoSqliteManager objects = TodoSqliteManager();
}

class TodoSqliteManager {
  static late Database _db;

  static Future<void> initialize() async {
    _db = await openDatabase(
      join(await getDatabasesPath(), 'todo.sqlite3'),
      version: 1,
      onCreate: (db, version) async {
        await db.execute('CREATE TABLE todo(id INTEGER PRIMARY KEY, text TEXT, todo_order INTEGER)');
      },
      onOpen: (db) async {
        await db.execute('CREATE TABLE IF NOT EXISTS todo(id INTEGER PRIMARY KEY, text TEXT, todo_order INTEGER)');
      },
    );
  }

  Future<Todo?> last() async {
    return (await _db.query('todo', orderBy: 'todo_order', limit: 1)).map(
      (todoMap) {
        return Todo(
          id: todoMap['id']! as int,
          text: todoMap['text']! as String,
          order: todoMap['todo_order']! as int,
        );
      },
    ).firstOrNull;
  }

  Future<List<Todo>> all() async {
    return (await _db.query('todo', orderBy: 'todo_order')).map(
      (todoMap) {
        return Todo(
          id: todoMap['id']! as int,
          text: todoMap['text']! as String,
          order: todoMap['todo_order']! as int,
        );
      },
    ).toList();
  }

  Future<void> insert(Todo todo) async {
    await _db.insert(
      'todo',
      todo.toSqlMap(),
      conflictAlgorithm: ConflictAlgorithm.ignore,
    );
  }

  Future<void> update(Todo todo) async {
    await _db.update(
      'todo',
      todo.toSqlMap(),
      where: 'id = ?',
      whereArgs: [todo.id],
    );
  }

  Future<void> updateOrder(List<Todo> todos) async {
    for (int i = 0; i < todos.length; i++) {
      await _db.update(
        'todo',
        {'todo_order': i + 1},
        where: 'id = ?',
        whereArgs: [todos[i].id],
      );
    }
  }

  Future<void> delete(int id) async {
    await _db.delete(
      'todo',
      where: 'id = ?',
      whereArgs: [id],
    );
  }
}
