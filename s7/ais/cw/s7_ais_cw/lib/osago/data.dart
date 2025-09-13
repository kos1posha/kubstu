import 'dart:convert';

import 'package:flutter/services.dart';

class Condition {
  final double low;
  final double high;

  Condition({required this.low, required this.high});

  bool check(double value) {
    return low <= value && value <= high;
  }
}

abstract class OsagoData {
  static late Map<String, dynamic> coefficients;
  static Map<String, dynamic> get tb => coefficients['ТБ'];
  static Map<String, dynamic> get kt => coefficients['КТ'];
  static Map<String, dynamic> get km => coefficients['КМ'];

  static late List<String> categories;
  static late Map<String, dynamic> territories; // Map<String, null | List<String>>

  //

  static void initialize() async {
    String coefficientsRaw = await rootBundle.loadString('assets/coefficients.json');
    coefficients = jsonDecode(coefficientsRaw);
    categories = tb.keys.toList();
    territories = kt.map((key, value) => value is num ? MapEntry(key, null) : MapEntry(key, value.keys.toList()));
  }

  static ({int min, int max}) getTB(String category, [String? extra]) {
    dynamic tbValue = tb[category];
    if (extra != null) {
      tbValue = tbValue[extra];
    }
    return (min: tbValue['min'] as int, max: tbValue['max'] as int);
  }

  static double getKM(double horsePower) {
    for (String kmKey in km.keys) {
      if (horsePower <= double.parse(kmKey)) {
        return km[kmKey] as double;
      }
    }
    return 1.0;
  }
}
