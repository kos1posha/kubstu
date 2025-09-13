import 'package:intl/intl.dart';
import 'package:s8_dmss_cw/utils/functions.dart';

// formatters
DateFormat dFormat = DateFormat('dd.MM.yyyy', 'ru');
DateFormat tFormat = DateFormat('HH:mm', 'ru');
DateFormat dtFormat = DateFormat('d MMMM yyyy г. в H:mm', 'ru');
DateFormat dtFormatWoYear = DateFormat('d MMMM в H:mm', 'ru');

String prettyDateTime(DateTime dateTime, {bool showToday = true}) {
  DateTime now = DateTime.now();
  if (dateTime.year == now.year) {
    if (dateTime.month == now.month && showToday) {
      return switch (dateTime.day - now.day) {
        0 => 'сегодня в ${tFormat.format(dateTime)}',
        -1 => 'вчера в ${tFormat.format(dateTime)}',
        -2 => 'позавчера в ${tFormat.format(dateTime)}',
        _ => dtFormatWoYear.format(dateTime),
      };
    }
    return dtFormatWoYear.format(dateTime);
  } else {
    return dtFormat.format(dateTime);
  }
}

String verboseTimeLeft(Duration timeLeft) {
  if (timeLeft.inDays > 0) {
    return verboseDays(timeLeft.inDays);
  } else if (timeLeft.inHours > 0) {
    return verboseHours(timeLeft.inHours);
  } else if (timeLeft.inMinutes > 0) {
    return verboseMinutes(timeLeft.inMinutes);
  } else {
    return 'менее минуты';
  }
}

String verboseDays(int days) {
  return verboseCount(days, single: 'день', miltiple: 'дней', from2to4: 'дня');
}

String verboseHours(int hours) {
  return verboseCount(hours, single: 'час', miltiple: 'часов', from2to4: 'часа');
}

String verboseMinutes(int minutes) {
  return verboseCount(minutes, single: 'минута', miltiple: 'минут', from2to4: 'минуты');
}
