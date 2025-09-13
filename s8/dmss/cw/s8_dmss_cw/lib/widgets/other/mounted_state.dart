import 'package:flutter/material.dart';

void _doNothing() {}

abstract class MountedState<T extends StatefulWidget> extends State<T> {
  @override
  void setState(VoidCallback fn) {
    if (mounted) {
      super.setState(fn);
    }
  }

  void updateState() => setState(_doNothing);
}
