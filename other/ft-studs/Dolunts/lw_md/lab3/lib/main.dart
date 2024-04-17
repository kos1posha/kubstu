import 'package:flutter/material.dart';

void main() {
  runApp(const KubgauApp());
}

class KubgauApp extends StatelessWidget {
  const KubgauApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: const Text('Общежития КубГАУ'), backgroundColor: Colors.green,),
        body: Column(
          children: [
            SizedBox(
              height: 603,
              child: SingleChildScrollView(
                scrollDirection: Axis.vertical,
                child: Column(
                  children: [
                    Image.network('https://lh3.googleusercontent.com/p/AF1QipMzjSB9DkNXRwniHjdk21_FnRUWESZbT3vDgOln=s1360-w1360-h1020'),
                    Padding(
                      padding: const EdgeInsets.fromLTRB(30, 30, 30, 5),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Row(
                            children: [
                              const Column(
                                crossAxisAlignment: CrossAxisAlignment.start,
                                children: [
                                  Text('Общежитие №20', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                                  Padding(padding: EdgeInsets.only(top: 10)),
                                  Text('Краснодар, ул. Калинина, 13', style: TextStyle(fontSize: 18, color: Colors.black45)),
                                ],
                              ),
                              const Padding(padding: EdgeInsets.only(left: 35)),
                              IconButton(onPressed: () => {}, icon: const Icon(Icons.favorite, color: Colors.red)),
                              const Text('27'),
                            ],
                          ),
                          const Padding(padding: EdgeInsets.only(top: 15)),
                          Column(
                            children: [
                              Row(
                                mainAxisAlignment: MainAxisAlignment.spaceAround,
                                children: [
                                  SizedBox.fromSize(
                                    size: const Size(100, 100),
                                    child: Column(
                                      crossAxisAlignment: CrossAxisAlignment.center,
                                      children: [
                                        IconButton(
                                            onPressed: () {},
                                            icon: const Icon(
                                                Icons.call,
                                                color: Colors.green,
                                                size: 32)
                                        ),
                                        const Text('ПОЗВОНИТЬ', style: TextStyle(color: Colors.green)),
                                      ],
                                    ),
                                  ),
                                  SizedBox.fromSize(
                                    size: const Size(100, 100),
                                    child: Column(
                                      crossAxisAlignment: CrossAxisAlignment.center,
                                      children: [
                                        IconButton(
                                            onPressed: () {},
                                            icon: const Icon(Icons.navigation,
                                                color: Colors.green,
                                                size: 32)
                                        ),
                                        const Text('МАРШРУТ', style: TextStyle(color: Colors.green)),
                                      ],
                                    ),
                                  ),
                                  SizedBox.fromSize(
                                    size: const Size(100, 100),
                                    child: Column(
                                      crossAxisAlignment: CrossAxisAlignment.center,
                                      children: [
                                        IconButton(
                                            onPressed: () {},
                                            icon: const Icon(Icons.share,
                                                color: Colors.green,
                                                size: 32)
                                        ),
                                        const Text('ПОДЕЛИТЬСЯ', style: TextStyle(color: Colors.green)),
                                      ],
                                    ),
                                  ),
                                ],
                              ),
                              const Text('Студенческий городок или так называемый кампус Кубанского ГАУ состоит из двадцати общежитий, в которых проживает более 8000 студентов, что составляет 96% от всех нуждающихся. Студенты первого курса обеспечены местами в общежитии полностью. В соответствии с Положением о студенческих общежитиях университета, при поселении между администрацией и студентами заключается договор найма жилого помещения. Воспитательная работа в общежитиях направлена на улучшение быта, соблюдение правил внутреннего распорядка, отсутствия асоциальных явлений в молодежной среде. Условия проживания в общежитиях университетского кампуса полностью отвечают санитарным нормам и требованиям: наличие оборудованных кухонь, душевых комнат, прачечных, читальных залов, комнат самоподготовки, помещений для заседаний студенческих советов и наглядной агитации. С целью улучшения условий быта студентов активно работает система студенческого самоуправления - студенческие советы организуют всю работу по самообслуживанию.', style: TextStyle(fontSize: 16)),
                            ],
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
