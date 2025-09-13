import 'package:expandable/expandable.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:s7_md_lw_12/constants.dart';
import 'package:s7_md_lw_12/event.dart';
import 'package:s7_md_lw_12/pages/create_or_edit_event_page.dart';

class EventsPage extends StatefulWidget {
  const EventsPage({super.key});

  @override
  State<EventsPage> createState() => EventsPageState();
}

class EventsPageState extends State<EventsPage> {
  late Color primaryColor = Theme.of(context).primaryColor;

  List<Event> events = [
    Event(
      date: DateTime(2025, 1, 1),
      icon: Icons.celebration_rounded,
      color: Colors.red,
      title: 'Новый год',
      description: 'Праздник к нам приходит',
    ),
    Event(),
    Event(
      date: DateTime(2024, 12, 20),
      time: const TimeOfDay(hour: 8, minute: 30),
      color: Colors.orange,
      title: 'Сходить за продуктами',
      description: 'Много сыра и много колы',
    ),
    Event(
      date: DateTime(2024, 12, 22),
      time: const TimeOfDay(hour: 0, minute: 0),
      icon: Icons.cake_rounded,
      title: 'День рождения мамы',
    ),
    Event(
      date: DateTime(2024, 12, 25),
      time: const TimeOfDay(hour: 0, minute: 0),
      icon: Icons.timelapse,
      color: Colors.purple,
      title: 'Занятие',
      description: 'Подготовить хлеб, колбасу и гвозди',
    ),
    Event(
      date: DateTime(2024, 12, 25),
      description: 'Представьте себе, что группа студентов решила подготовить проект о космосе. Один из них, с огромными очками и '
          'растрепанными волосами, стоит у доски и рисует планету, которая выглядит как огромный апельсин с космическими '
          'ушами. Другой студент, с книгой в руках, пытается объяснить, почему планеты не могут быть фруктами, но его '
          'собеседник уже рисует ракеты, которые выглядят как бананы. В углу комнаты, робот-помощник с улыбающимся экраном '
          'пытается подать им бумагу, но вместо этого раздает им конфеты, потому что перепутал задание с праздником!',
    ),
  ];
  Event? get currentEvent => currentEventIndex == 1 ? null : events[currentEventIndex];
  int currentEventIndex = -1;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: primaryColor,
        leading: const Icon(Icons.event, color: Colors.white),
        title: const Text(
          'Мои события',
          style: TextStyle(color: Colors.white),
        ),
        actions: [
          Padding(
            padding: const EdgeInsets.only(top: 4, right: 20),
            child: Text(
              '${events.length}',
              style: const TextStyle(
                color: Colors.white,
                fontSize: 20,
              ),
            ),
          ),
        ],
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () {
          Navigator.of(context).push(
            CupertinoPageRoute(
              builder: (context) => CreateOrEditEventPage(
                parent: this,
                event: null,
              ),
            ),
          );
        }, // TODO create event page
        child: const Icon(Icons.add),
      ),
      body: events.isEmpty
          ? Center(
              child: Text(
                'События отсутствуют',
                style: TextStyle(color: Colors.grey[600]),
              ),
            )
          : SingleChildScrollView(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: ListView(
                  physics: const NeverScrollableScrollPhysics(),
                  shrinkWrap: true,
                  children: [
                    ...List.generate(
                      events.length,
                      (index) {
                        Event event = events[index];
                        return Card.filled(
                          color: event.color,
                          shape: RoundedRectangleBorder(borderRadius: borderRadius),
                          child: InkWell(
                            onLongPress: () {
                              Navigator.of(context).push(
                                CupertinoPageRoute(
                                  builder: (context) => CreateOrEditEventPage(
                                    parent: this,
                                    event: event,
                                  ),
                                ),
                              );
                            },
                            child: ExpandablePanel(
                              theme: ExpandableThemeData(
                                hasIcon: false,
                                tapHeaderToExpand: event.description != '',
                                inkWellBorderRadius: borderRadius,
                              ),
                              header: Padding(
                                padding: const EdgeInsets.all(16),
                                child: Row(
                                  children: [
                                    if (event.icon != null)
                                      Padding(
                                        padding: const EdgeInsets.only(left: 4, right: 16),
                                        child: Icon(event.icon, size: 35, color: Colors.black),
                                      ),
                                    Expanded(
                                      child: Column(
                                        crossAxisAlignment: CrossAxisAlignment.start,
                                        children: [
                                          if (event.title != '')
                                            Text(
                                              event.titlef,
                                              style: const TextStyle(fontSize: 17),
                                            ),
                                          if (event.time != null || event.date != null)
                                            Text(
                                              [
                                                if (event.time != null) event.timef,
                                                if (event.date != null) event.datef,
                                              ].join(' '),
                                              style: const TextStyle(fontSize: 14),
                                            ),
                                        ],
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                              collapsed: const SizedBox(width: double.infinity),
                              expanded: Padding(
                                padding: const EdgeInsets.fromLTRB(16, 8, 16, 16),
                                child: SelectableText(event.description),
                              ),
                            ),
                          ),
                        );
                      },
                    ),
                    const SizedBox(height: 60),
                  ],
                ),
              ),
            ),
    );
  }
}
