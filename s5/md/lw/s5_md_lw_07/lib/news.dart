import 'dart:async';
import 'dart:convert';

import 'package:intl/intl.dart';
import 'package:flutter/foundation.dart';
import 'package:http/http.dart' as http;

class News {
  final String id;
  final String activeFrom;
  final String title;
  final String previewText;
  final String previewPictureSrc;
  final String detailPageUrl;
  final String detailText;
  final String lastModified;

  const News({
    required this.id,
    required this.activeFrom,
    required this.title,
    required this.previewText,
    required this.previewPictureSrc,
    required this.detailPageUrl,
    required this.detailText,
    required this.lastModified,
  });

  factory News.fromJson(Map<String, dynamic> json) {
    return News(
      id: Bidi.stripHtmlIfNeeded(json['ID'] as String).trim(),
      activeFrom: Bidi.stripHtmlIfNeeded(json['ACTIVE_FROM'] as String).trim(),
      title: Bidi.stripHtmlIfNeeded(json['TITLE'] as String).trim(),
      previewText: Bidi.stripHtmlIfNeeded(json['PREVIEW_TEXT'] as String).trim(),
      previewPictureSrc: Bidi.stripHtmlIfNeeded(json['PREVIEW_PICTURE_SRC'] as String).trim(),
      detailPageUrl: Bidi.stripHtmlIfNeeded(json['DETAIL_PAGE_URL'] as String).trim(),
      detailText: Bidi.stripHtmlIfNeeded(json['DETAIL_TEXT'] as String).trim(),
      lastModified: Bidi.stripHtmlIfNeeded(json['LAST_MODIFIED'] as String).trim(),
    );
  }
}

Future<List<News>> fetchNews(http.Client client) async {
  String newsUrl = 'https://kubsau.ru/api/getNews.php?key=6df2f5d38d4e16b5a923a6d4873e2ee295d0ac90';
  final response = await client.get(Uri.parse(newsUrl));
  return compute(parseNews, response.body);
}

List<News> parseNews(String responseBody) {
  final parsed = jsonDecode(responseBody).cast<Map<String, dynamic>>();
  return parsed.map<News>((json) => News.fromJson(json)).toList();
}
