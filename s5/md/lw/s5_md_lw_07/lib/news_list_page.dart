import 'news.dart';
import 'news_detail_page.dart';

import 'package:http/http.dart' as http;
import 'package:flutter/material.dart';

class NewsListPage extends StatelessWidget {
  const NewsListPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Новости'), backgroundColor: Colors.green),
      body: FutureBuilder<List<News>>(
        future: fetchNews(http.Client()),
        builder: (context, snapshot) {
          if (snapshot.hasError)
            return Center(child: Text('Ошибка запроса!'));
          else if (snapshot.hasData)
            return NewsList(news: snapshot.data!);
          else
            return Center(child: CircularProgressIndicator());
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
      radius: Radius.circular(10),
      thickness: 8,
      child: ListView.builder(
        itemCount: news.length,
        itemBuilder: (context, index) {
          News n = news[index];
          return Padding(
            padding: EdgeInsets.symmetric(horizontal: 16, vertical: 4),
            child: Card(
              child: GestureDetector(
                child: Column(
                  children: [
                    ClipRRect(
                        borderRadius: BorderRadius.only(topLeft: Radius.circular(5), topRight: Radius.circular(5)),
                        child: Image.network(n.previewPictureSrc)
                    ),
                    Padding(
                      padding: EdgeInsets.all(16),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(n.title, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                          Text(n.activeFrom, style: TextStyle(color: Colors.black54)),
                          Divider(thickness: 1),
                          Text(n.previewText + (n.previewText.endsWith('.') ? '' : '.')),
                        ],
                      ),
                    )
                  ],
                ),
                onTap: () {
                  Navigator.of(context).push(MaterialPageRoute(builder: (BuildContext context) {
                    return NewsDetailPage(news: n);
                  }));
                },
              ),
            ),
          );
        },
      ),
    );
  }
}
