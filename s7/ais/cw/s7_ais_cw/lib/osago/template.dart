import 'dart:io';

import 'package:docx_template/docx_template.dart';
import 'package:flutter/services.dart';
import 'package:path/path.dart' as path;
import 'package:path_provider/path_provider.dart';
import 'package:s7_ais_cw/extensions.dart';

abstract class OsagoTemplate {
  static Future<String?> fillOsago(Map<String, dynamic> data) async {
    DocxTemplate docxTpl = await getOsagoTemplate();
    try {
      Content content = getContent(data);
      List<int>? docxOsagoBytes = await docxTpl.generate(content, tagPolicy: TagPolicy.removeAll);
      if (docxOsagoBytes == null) return null;
      return createGeneratedAsFile(docxOsagoBytes, 'Osago Calculator/osago');
    } catch (e) {
      return null;
    }
  }

  static Future<DocxTemplate> getOsagoTemplate() async {
    ByteData docxTplBytes = await rootBundle.load('assets/osago_tpl.docx');
    return await DocxTemplate.fromBytes(docxTplBytes.buffer.asUint8List());
  }

  static Content getContent(Map<String, dynamic> data) {
    Content content = Content();
    for (String fsKey in fieldsets.keys) {
      switch (fsKey) {
        case '':
          for (String fKey in fieldsets[fsKey]) {
            String text = data.get(fKey, false) ? ' X' : '  ';
            content.add(TextContent(fKey, text));
          }
        case 'k':
          for (String fKey in fieldsets[fsKey]) {
            String text = data.get(fKey, 1.0).toString();
            content.add(TextContent(fKey, text));
          }
        case _:
          for (String fKey in fieldsets[fsKey].keys) {
            String dKey = '${fsKey}_$fKey';
            String text = (data.get(dKey, '') as String).center(fieldsets[fsKey][fKey], '_');
            content.add(TextContent(dKey, text));
          }
      }
    }
    return content;
  }

  static Future<String> createGeneratedAsFile(List<int> bytes, String fileName) async {
    String appDir = (await getExternalStorageDirectory())!.path;
    File file = File(path.join(appDir, '$fileName.docx'));
    int i = 1;
    while (await file.exists()) {
      file = File(path.join(appDir, '$fileName ($i).docx'));
      i++;
    }
    file
      ..createSync(recursive: true)
      ..writeAsBytesSync(bytes);
    return file.path;
  }
}

const Map<String, dynamic> fieldsets = {
  'ins': {
    'fullname': 59,
    'birthday': 33,
    'doc_type': 53,
    'doc_series': 10,
    'doc_number': 10,
    'addr_index': 10,
    'addr_federal': 48,
    'addr_district': 9,
    'addr_location': 20,
    'addr_street': 21,
    'addr_house': 7,
    'addr_building': 9,
    'addr_apart': 14,
    'phone': 66,
    'shortname': 34,
  },
  'act': {
    'from_day': 2,
    'from_month': 10,
    'from_year': 4,
    'to_day': 2,
    'to_month': 10,
    'to_year': 4,
  },
  'owner': {
    'fullname': 62,
    'birthday': 33,
    'doc_type': 53,
    'doc_series': 10,
    'doc_number': 10,
    'addr_index': 10,
    'addr_federal': 48,
    'addr_district': 9,
    'addr_location': 20,
    'addr_street': 21,
    'addr_house': 7,
    'addr_building': 9,
    'addr_apart': 14,
  },
  'veh': {
    'category': 26,
    'model_mark': 75,
    'id': 27,
    'creation_year': 34,
    'engine_kw': 16,
    'engine_force': 15,
    'weight_limit': 39,
    'passengers': 45,
    'chassis': 24,
    'body': 18,
    'doc_type': 29,
    'doc_series': 9,
    'doc_number': 18,
    'doc_date': 16,
    'reg_number': 40,
  },
  '': ['y', 'n', 'p', 's', 't', 'd', 'r', 'g', 'h', 'c', 'o', 'all', 'only'],
  'k': ['bt', 'kt', 'kbm', 'kvs', 'ks', 'kp', 'km', 'ko', 'itg']
};
