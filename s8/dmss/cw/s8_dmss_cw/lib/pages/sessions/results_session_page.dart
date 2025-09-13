import 'dart:async';

import 'package:animated_reorderable_list/animated_reorderable_list.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';
import 'package:s8_dmss_cw/firebase/passes.dart';
import 'package:s8_dmss_cw/firebase/questions.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/firebase/tickets.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/cards.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';

class ResultsSessionPage extends StatefulWidget {
  const ResultsSessionPage({super.key, required this.sessionUid});

  static const String routeName = 'result_session';
  static const String routePath = '/results/:uid';

  final String sessionUid;

  @override
  MountedState<ResultsSessionPage> createState() => _ResultsSessionPageState();
}

class _ResultsSessionPageState extends MountedState<ResultsSessionPage> {
  final TextEditingController _studentKeyController = TextEditingController();

  bool _sessionNotExists = false;

  Session? _session;
  Exam? _exam;
  Map<String, Ticket>? _tickets;

  Map<String, Pass>? _passes;
  StreamSubscription? _passesStreamSubscription;

  List<MapEntry<String, String>>? get _students => _session?.students.entries.toList();

  @override
  void initState() {
    super.initState();
    // session stream
    Future.microtask(
      () async {
        _session = await Sessions.one(widget.sessionUid);
        if (_session == null) {
          _sessionNotExists = true;
          return;
        }
        _exam = await Exams.one(_session!.examUid);
        if (_exam == null) {
          _sessionNotExists = true;
          return;
        }
        List<Ticket> loadedTickets = await Tickets.of(_exam!.uid).all();
        List<Question> loadedQuestions = await Questions.of(_exam!.uid).all();
        _tickets = {for (Ticket t in loadedTickets) t.uid: t..putQuestions(loadedQuestions)};
        _passesStreamSubscription ??= Passes.of(_session!.uid).streamAll().listen(
          (snapshot) async {
            List<Pass> loadedPasses = await Passes.of(_session!.uid).all();
            _passes = {for (Pass p in loadedPasses) p.uid: p};
            updateState();
          },
        );
      },
    ).whenComplete(updateState);
  }

  @override
  Widget build(BuildContext context) {
    return CenteredBodyScaffold(
      canBack: false,
      maxWidth: 800,
      floatingActionButton: const ToggleThemeFab(),
      body: _sessionNotExists
          ? const Text('Сессия не найдена', style: TextStyle(fontSize: 16))
          : _exam == null || _session == null
              ? const CircularProgressIndicator()
              : Column(
                  mainAxisSize: MainAxisSize.min,
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    groupVDivider,
                    const SizedBox(width: double.infinity),
                    const Text('Результаты', style: titleTextStyle),
                    // title
                    Padding(
                      padding: const EdgeInsets.symmetric(vertical: 8),
                      child: Text(
                        _exam!.title,
                        style: logoTextStyle,
                      ),
                    ),
                    // description
                    if (_exam!.description != '')
                      Padding(
                        padding: const EdgeInsets.only(bottom: 20),
                        child: Text(_exam!.description, style: subtitleTextStyle),
                      ),
                    // teacher
                    if (_exam!.teacher != '')
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Text('Преподаватель: ', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                          Text(_exam!.teacher, style: const TextStyle(fontSize: 18)),
                        ],
                      ),
                    // discipline
                    if (_exam!.discipline != '')
                      Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          const Text('Дисциплина: ', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                          Text(_exam!.discipline, style: const TextStyle(fontSize: 18)),
                        ],
                      ),
                    // group name
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('Группа: ', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                        Text(_session!.groupName, style: const TextStyle(fontSize: 18)),
                      ],
                    ),
                    groupVDivider,
                    _passes == null
                        ? const Center(child: CircularProgressIndicator())
                        : AnimatedListView(
                            shrinkWrap: true,
                            isSameItem: (a, b) => a.key == b.key,
                            items: _students!,
                            itemBuilder: (context, index) {
                              MapEntry<String, String> student = _students![index];
                              Pass? pass = _passes![student.key];
                              return KeyedSubtree(
                                key: ValueKey('student${student.key}OfSession${_session!.uid}'),
                                child: Padding(
                                  padding: EdgeInsets.only(top: index == 0 ? 0 : 4),
                                  child: PassResultCard(
                                    studentKey: student.key,
                                    studentName: student.value,
                                    pass: pass,
                                    ticket: _tickets![pass?.ticketUid],
                                  ),
                                ),
                              );
                            },
                          ),
                    groupVDivider,
                    // time until
                    Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: [
                        if (_session!.isBefore)
                          Text(
                            _session!.untilStartF,
                            style: const TextStyle(color: MainTheme.neural, fontSize: 22),
                          ),
                        if (_session!.isActive)
                          Text(
                            _session!.untilEndF,
                            style: const TextStyle(color: MainTheme.neural, fontSize: 22),
                          ),
                      ],
                    ),
                    groupVDivider,
                  ],
                ),
    );
  }

  @override
  void dispose() {
    _passesStreamSubscription?.cancel();
    _studentKeyController.dispose();
    super.dispose();
  }
}
