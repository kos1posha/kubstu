import 'package:flutter/material.dart';

class The64PowersPage extends StatefulWidget {
  const The64PowersPage({super.key});

  @override
  State<The64PowersPage> createState() => _The64PowersPageState();
}

class _The64PowersPageState extends State<The64PowersPage> {
  final List<int> _intList = List<int>.filled(64, 2);

  Future<bool?> _dismissRow(DismissDirection direction, int index) {
    setState(() {
      direction == DismissDirection.startToEnd
          ? _intList[index]++
          : _intList[index] != 1
          ? _intList[index]--
          : _intList[index];
    });
    return Future(() => false);
  }

  int? power(int x, int n) {
    int result = 1;
    int old;
    while (0 < n--) {
      old = result;
      result *= x;
      if (old > result) {
        return null;
      }
    }
    return result;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
          title: Text('64 cтепени'), backgroundColor: Colors.red[900]),
      body: Padding(
        padding: const EdgeInsets.symmetric(vertical: 8),
        child: ListView.builder(
          itemCount: 64,
          itemBuilder: (context, index) {
            int p = power(_intList[index], index) ?? 0;
            if (p > 0) {
              return Dismissible(
                key: Key(''),
                confirmDismiss: (DismissDirection direction) {
                  return _dismissRow(direction, index);
                },
                background: Align(
                  alignment: Alignment.centerLeft,
                  child: Icon(Icons.add, color: Colors.green),
                ),
                secondaryBackground: Align(
                  alignment: Alignment.centerRight,
                  child: Icon(Icons.remove, color: Colors.red),
                ),
                child: Padding(
                  padding: EdgeInsets.symmetric(horizontal: 0, vertical: 8),
                  child: ListTile(
                    title: Align(
                        alignment: Alignment.center,
                        child: Text('${_intList[index]} ^ $index',
                            style: TextStyle(fontSize: 16, color: Colors.grey))
                    ),
                    subtitle: Align(
                        alignment: Alignment.center,
                        child: Text('$p', style: TextStyle(fontSize: 20, color: Colors.black))
                    ),
                    tileColor: Colors.black12,
                    dense: true,
                  ),
                ),
              );
            } else {
              return Dismissible(
                key: Key(''),
                confirmDismiss: (DismissDirection direction) {
                  return _dismissRow(direction, index);
                },
                child: Card(
                    margin:
                    EdgeInsets.symmetric(vertical: 1, horizontal: 0),
                    color: Colors.red,
                    child: Padding(
                      padding: EdgeInsets.symmetric(horizontal: 16.0),
                      child: Row(
                        children: [
                          Text('Переполнение...', style: TextStyle(fontSize: 16, color: Colors.white)),
                          Spacer(),
                          Text('${_intList[index]} ^ $index', style: TextStyle(color: Colors.black38)),
                        ],
                      ),
                    )
                ),
              );
            }
          }
        ),
      ),
    );
  }
}
