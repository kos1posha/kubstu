// ignore: avoid_web_libraries_in_flutter, deprecated_member_use
import 'dart:html' as html;
import 'dart:math';
import 'dart:ui' as ui;

import 'package:flutter/material.dart';

void iconToPng(int size, IconData icon, Color color) async {
  final recorder = ui.PictureRecorder();
  final canvas = ui.Canvas(recorder);
  TextPainter(textDirection: TextDirection.ltr)
    ..text = TextSpan(
      text: String.fromCharCode(icon.codePoint),
      style: TextStyle(fontSize: size.toDouble(), fontFamily: icon.fontFamily, color: color),
    )
    ..layout()
    ..paint(canvas, Offset.zero);
  final picture = recorder.endRecording();
  final image = await picture.toImage(size, size);
  final data = await image.toByteData(format: ui.ImageByteFormat.png);
  final bytes = data!.buffer.asUint8List();
  final blob = html.Blob([bytes]);
  final url = html.Url.createObjectUrlFromBlob(blob);
  html.AnchorElement(href: url)
    ..setAttribute('download', 'image.png')
    ..click();
  html.Url.revokeObjectUrl(url);
}

void disposeControllers(Iterable<ChangeNotifier> controllers) {
  for (ChangeNotifier controller in controllers) {
    controller.dispose();
  }
}

String generateRandomKey(int length) {
  const String chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
  Random random = Random();
  StringBuffer key = StringBuffer();
  for (int i = 0; i < length; i++) {
    key.write(chars[random.nextInt(chars.length)]);
  }
  return key.toString();
}

bool isTimeWithinDateTimeRange(DateTime start, DateTime end, TimeOfDay time) {
  DateTime timeToCheck = start.add(Duration(hours: time.hour, minutes: time.minute));
  return timeToCheck.isAfter(start) && timeToCheck.isBefore(end);
}

String verboseCount(
  int count, {
  required String single,
  required String miltiple,
  required String from2to4,
}) {
  count = count.abs();
  if (count < 11 || count > 14) {
    int remainder = count % 10;
    if (remainder == 1) return '1 $single';
    if (remainder >= 2 && remainder <= 4) return '$count $from2to4';
  }
  return '$count $miltiple';
}
