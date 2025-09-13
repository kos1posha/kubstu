import 'package:flutter/material.dart';
import 'package:s7_md_lw_12/constants.dart';

class Event {
  DateTime? date;
  TimeOfDay? time;
  IconData? icon;
  Color? color;
  String? title;
  String description;

  String get datef => date == null ? '' : dateFormatter.format(date!);
  String get timef => time == null ? '' : '${'${time!.hour}'.padLeft(2, '0')}:${'${time!.minute}'.padLeft(2, '0')}';
  String get titlef => title ?? 'Без названия';

  Event({this.date, this.time, this.icon, this.color, this.title = '', this.description = ''}) {
    if (title == '') {
      title = 'Без названия';
    }
  }
}
