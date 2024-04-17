import 'package:flutter/material.dart';
import 'package:s5_md_lw_03/like_button.dart';

class DormitoryPage extends StatefulWidget {
  const DormitoryPage({super.key});

  @override
  State<DormitoryPage> createState() => _DormitoryPageState();
}

class _DormitoryPageState extends State<DormitoryPage> {
  final String _mainText =
  '''    Студгородок предназначен для временного размещения и проживания в общежитиях нуждающихся в жилых помещениях студентов, магистрантов, аспирантов, докторантов, обучающихся по очной форме обучения, иностранных граждан, принятых на обучение в университет, сотрудников, и устанавливает единые требования к проживанию в студенческом общежитии.
\n    Студгородок — это одна из составляющих полноценного обучения и отдыха студента. Окружающее пространство играет важную роль в том, как студент чувствует себя во время обучения и насколько остается доволен полученным образованием.
\n    В целях обеспечения безопасности проживания все общежития оборудованы системой видеонаблюдения.
\n    В общежитии №3 имеется медицинский кабинет, в котором организован пункт вакцинации от COVID-19. По предварительной записи его могут посетить все желающие.
\n    Для представления интересов студентов, проживающих в общежитии, из числа самых активных студентов в каждом общежитии избирается Студенческий совет, который совместно с заведующими общежитиями следит за порядком и соблюдением правил проживания в своем корпусе, а также занимается организацией культурных и спортивных мероприятий. Для взаимодействия и координации работы студсоветов общежитий в университете создан Совет студенческих общежитий, в который входят все председатели студсоветов.
\n    Процедура вселения в общежития регламентируется «Положением о Студенческом городке КубГТУ», «Положением о специализированном жилищном фонде (студенческом общежитии) ФГБОУ ВО «КубГТУ».
''';

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Общежития КубГТУ')),
        body: Column(
          children: [
            Image.network('https://avatars.mds.yandex.net/get-altay/5449402/2a0000017f85deee1197013ee6cffb049771/orig'),
            SizedBox(
              height: 477,
              child: SingleChildScrollView(
                scrollDirection: Axis.vertical,
                child: Padding(
                  padding: EdgeInsets.fromLTRB(25, 30, 25, 5),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text('Общежитие №3', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                              Padding(padding: EdgeInsets.only(top: 10)),
                              Text('Краснодар, ул. Московская, 2', style: TextStyle(fontSize: 18, color: Colors.black45)),
                            ],
                          ),
                          Padding(padding: EdgeInsets.only(left: 55)),
                          LikeButton(),
                        ],
                      ),
                      Padding(padding: EdgeInsets.only(top: 15)),
                      Column(
                        children: [
                          Row(
                            mainAxisAlignment: MainAxisAlignment.spaceAround,
                            children: [
                              SizedBox.fromSize(
                                size: Size(100, 100),
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.center,
                                  children: [
                                    IconButton(
                                        onPressed: () {},
                                        icon: Icon(
                                            Icons.call,
                                            color: Colors.blueAccent,
                                            size: 32)
                                    ),
                                    Text('ПОЗВОНИТЬ', style: TextStyle(color: Colors.blue)),
                                  ],
                                ),
                              ),
                              SizedBox.fromSize(
                                size: Size(100, 100),
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.center,
                                  children: [
                                    IconButton(
                                        onPressed: () {},
                                        icon: Icon(Icons.location_on_rounded,
                                            color: Colors.blueAccent,
                                            size: 32)
                                    ),
                                    Text('МАРШРУТ', style: TextStyle(color: Colors.blue)),
                                  ],
                                ),
                              ),
                              SizedBox.fromSize(
                                size: Size(100, 100),
                                child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.center,
                                  children: [
                                    IconButton(
                                      onPressed: () {},
                                      icon: Icon(Icons.share,
                                        color: Colors.blueAccent,
                                        size: 32)
                                    ),
                                    Text('ПОДЕЛИТЬСЯ', style: TextStyle(color: Colors.blue)),
                                  ],
                                ),
                              ),
                            ],
                          ),
                          Text(_mainText, style: TextStyle(fontSize: 16)),
                        ],
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
