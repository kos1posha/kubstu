import 'dart:convert';
import 'dart:io' as io;
import 'dart:async';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';

class HttpOverrides extends io.HttpOverrides {
  @override
  io.HttpClient createHttpClient(io.SecurityContext? context) {
    return super.createHttpClient(context)
      ..badCertificateCallback =
          (io.X509Certificate cert, String host, int port) => true;
  }
}

void main() {
  io.HttpOverrides.global = HttpOverrides();
  runApp(const NewsApp());
}

class NewsApp extends StatelessWidget {
  const NewsApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(home: NewsListPage());
  }
}

class NewsListPage extends StatelessWidget {
  const NewsListPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar:
      AppBar(title: const Text('Лента новостей КубГАУ'), backgroundColor: Colors.green),
      body: FutureBuilder<List<News>>(
        future: fetchNews(http.Client()),
        builder: (context, snapshot) {
          if (snapshot.hasError) {
            return const Center(child: Text('Ошибка запроса!'));
          } else if (snapshot.hasData)
            return NewsList(news: snapshot.data!);
          else
            return const Center(child: CircularProgressIndicator());
        },
      ),
    );
  }
}

class NewsList extends StatelessWidget {
  const NewsList({Key? key, required this.news}) : super(key: key);

  final List<News> news;

  @override
  Widget build(BuildContext context) {
    return Scrollbar(
      radius: const Radius.circular(10),
      thickness: 8,
      child: ListView.builder(
        itemCount: news.length,
        itemBuilder: (context, index) {
          News n = news[index];
          return Padding(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 4),
            child: Card(
              child: GestureDetector(
                child: Column(
                  children: [
                    ClipRRect(
                        borderRadius: const BorderRadius.only(
                            topLeft: Radius.circular(5),
                            topRight: Radius.circular(5)),
                        child: Image.network(n.previewPictureSrc)),
                    Padding(
                      padding: const EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(n.activeFrom,
                              style: const TextStyle(color: Colors.black54)),
                          Text(n.title,
                              style: const TextStyle(
                                  fontSize: 16, fontWeight: FontWeight.bold)),
                          const Divider(thickness: 1),
                          Text(n.previewText +
                              (n.previewText.endsWith('.') ? '' : '.')),
                        ],
                      ),
                    )
                  ],
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}

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
      previewText:
      Bidi.stripHtmlIfNeeded(json['PREVIEW_TEXT'] as String).trim(),
      previewPictureSrc:
      Bidi.stripHtmlIfNeeded(json['PREVIEW_PICTURE_SRC'] as String).trim(),
      detailPageUrl:
      Bidi.stripHtmlIfNeeded(json['DETAIL_PAGE_URL'] as String).trim(),
      detailText: Bidi.stripHtmlIfNeeded(json['DETAIL_TEXT'] as String).trim(),
      lastModified:
      Bidi.stripHtmlIfNeeded(json['LAST_MODIFIED'] as String).trim(),
    );
  }
}

Future<List<News>> fetchNews(http.Client client) async {
  String newsUrl =
      'https://kubsau.ru/api/getNews.php?key=6df2f5d38d4e16b5a923a6d4873e2ee295d0ac90';
  final response = await client.get(Uri.parse(newsUrl));
  return compute(parseNews, response.body);
}

List<News> parseNews(String responseBody) {
  final parsed = jsonDecode(responseBody).cast<Map<String, dynamic>>();
  return parsed.map<News>((json) => News.fromJson(json)).toList();
}
