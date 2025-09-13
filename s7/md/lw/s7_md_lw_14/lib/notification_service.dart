import 'dart:async';
import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_background_service/flutter_background_service.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';
import 'package:s7_md_lw_14/todo_sqlite.dart';

class BackgroundNotificationService {
  static FlutterLocalNotificationsPlugin fln = FlutterLocalNotificationsPlugin();

  static void start() {
    FlutterBackgroundService().startService();
  }

  static void stop() {
    FlutterBackgroundService().invoke("stop");
  }

  static Future<void> initialize() async {
    var androidInitialize = const AndroidInitializationSettings('mipmap/ic_launcher');
    var initializationSettings = InitializationSettings(android: androidInitialize);
    await fln.initialize(initializationSettings);
    await FlutterBackgroundService().configure(
      iosConfiguration: IosConfiguration(
        autoStart: true,
        onForeground: onStart,
        onBackground: onIosBackground,
      ),
      androidConfiguration: AndroidConfiguration(
        autoStart: true,
        onStart: onStart,
        isForegroundMode: false,
        autoStartOnBoot: true,
      ),
    );
  }
}

@pragma('vm:entry-point')
Future<bool> onIosBackground(ServiceInstance service) async {
  WidgetsFlutterBinding.ensureInitialized();
  DartPluginRegistrant.ensureInitialized();
  return true;
}

@pragma('vm:entry-point')
Future<void> onStart(ServiceInstance service) async {
  Timer.periodic(const Duration(seconds: 20), (timer) async {
    await TodoSqliteManager.initialize();
    Todo? lastTodo = await Todo.objects.last();
    if (lastTodo == null) return;
    Uint8List bytes = (await rootBundle.load('assets/smile-angel.png')).buffer.asUint8List();
    AndroidNotificationDetails details = AndroidNotificationDetails(
      'BackgroundService',
      'Ваша последняя TODO\'шка',
      importance: Importance.max,
      priority: Priority.high,
      playSound: false,
      styleInformation: BigPictureStyleInformation(ByteArrayAndroidBitmap(bytes)),
    );
    await BackgroundNotificationService.fln.show(
      0,
      'Вы же не забыли, что у вас остались дела?',
      'Например, последнее, что вы запланировали: ${lastTodo.text}',
      NotificationDetails(android: details),
    );
  });
}
