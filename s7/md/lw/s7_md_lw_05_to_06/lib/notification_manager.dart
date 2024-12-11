import 'package:flutter/services.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

class NotificationManager {
  static late FlutterLocalNotificationsPlugin fln;

  static Future init() async {
    fln = FlutterLocalNotificationsPlugin();
    var androidInitialize = const AndroidInitializationSettings('mipmap/ic_launcher');
    var initializationSettings = InitializationSettings(android: androidInitialize);
    await fln.initialize(initializationSettings);
  }

  static Future showNotification(String title, String body) async {
    Uint8List bytes = (await rootBundle.load('assets/smile-nice.png')).buffer.asUint8List();
    AndroidNotificationDetails details = AndroidNotificationDetails(
      'bb_id',
      'bb_chanel',
      importance: Importance.max,
      priority: Priority.high,
      playSound: false,
      styleInformation: BigPictureStyleInformation(ByteArrayAndroidBitmap(bytes)),
    );
    await fln.show(0, title, body, NotificationDetails(android: details));
  }
}
