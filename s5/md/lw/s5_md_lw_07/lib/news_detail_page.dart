import 'news.dart';

import 'package:flutter/material.dart';

class NewsDetailPage extends StatelessWidget {
  const NewsDetailPage({Key? key, required this.news}) : super(key: key);

  final News news;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(news.title), backgroundColor: Colors.green),
      body: Column(
        children: [
          Image.network(news.previewPictureSrc),
          SizedBox(
            height: 580,
            child: SingleChildScrollView(
              child: Padding(
                padding: EdgeInsets.fromLTRB(25, 30, 25, 5),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(news.title, style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                    Padding(padding: EdgeInsets.only(top: 10)),
                    Text(news.activeFrom, style: TextStyle(fontSize: 16, color: Colors.black54)),
                    Divider(thickness: 1),
                    Text(news.detailText, style: TextStyle(fontSize: 16)),
                    Align(
                      alignment: Alignment.centerRight,
                      child: Text(
                        'изменено: ${news.lastModified}',
                        style: TextStyle(
                          fontSize: 12,
                          fontStyle: FontStyle.italic,
                          color: Colors.grey
                        )
                      ),
                    )
                  ]
                ),
              ),
            ),
          ),
        ],
      )
    );
  }
}
