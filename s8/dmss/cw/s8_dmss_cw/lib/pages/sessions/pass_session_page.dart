import 'dart:async';
import 'dart:math';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:expandable/expandable.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';
import 'package:s8_dmss_cw/firebase/passes.dart';
import 'package:s8_dmss_cw/firebase/questions.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/firebase/tickets.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/utils/datetime.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';
import 'package:slide_countdown/slide_countdown.dart';

class PassSessionPage extends StatefulWidget {
  const PassSessionPage({super.key, required this.sessionUid, required this.studentKey});

  static const String routeName = 'pass_session';
  static const String routePath = '/session/:uid/pass/:studentKey';

  final String sessionUid;
  final String studentKey;

  @override
  MountedState<PassSessionPage> createState() => _PassSessionPageState();
}

class _PassSessionPageState extends MountedState<PassSessionPage> {
  final ExpandableController _expandableController = ExpandableController();

  StreamDuration? _streamDuration;

  bool _isLoading = false;
  bool _sessionNotExists = false;
  bool _studentNotExists = false;
  bool _passSubmited = false;

  Session? _session;
  Exam? _exam;
  Pass? _pass;
  Ticket? _ticket;

  Map<String, TextEditingController>? _answerControllers;
  Map<String, String> get _answers => {for (var a in _answerControllers!.entries) a.key: a.value.text};

  StreamDuration _streamDurationConfig([int hour = 0, int minutes = 0, int seconds = 0]) {
    return StreamDuration(
      config: StreamDurationConfig(
        autoPlay: false,
        countDownConfig: CountDownConfig(
          duration: Duration(
            hours: hour,
            minutes: minutes,
            seconds: seconds,
          ),
        ),
        onDone: _sendAnswers,
      ),
    );
  }

  @override
  void initState() {
    super.initState();
    Future.microtask(() async {
      _session = await Sessions.one(widget.sessionUid);
      if (_session == null) {
        _sessionNotExists = true;
        return;
      }
      if (!_session!.students.containsKey(widget.studentKey)) {
        _studentNotExists = true;
        return;
      }

      _exam = await Exams.one(_session!.examUid);
      if (_exam == null) {
        _sessionNotExists = true;
        return;
      }

      _pass = await Passes.of(_session!.uid).one(widget.studentKey);
      if (_pass == null) return;
      if (_pass!.submited != null) {
        _passSubmited = true;
      }

      _ticket = await Tickets.of(_exam!.uid).one(_pass!.ticketUid);
      await _loadAnswers();

      Duration? timeLeft = _pass!.timeLeft(_session!.timeForExam);
      _streamDuration = timeLeft == null ? _streamDurationConfig() : _streamDurationConfig(timeLeft.inHours, timeLeft.inMinutes % 60, timeLeft.inSeconds & 60);
      _streamDuration!.play();
      _expandableController.expanded = _ticket != null;
    }).whenComplete(updateState);
  }

  Future<void> _loadAnswers() async {
    _answerControllers = {};
    if (_ticket == null) return;
    _ticket!.putQuestions(await Questions.of(_exam!.uid).all());
    for (String quid in _ticket!.questionUids) {
      _answerControllers![quid] = TextEditingController(text: _pass?.answers[quid] ?? '');
    }
  }

  Future<void> _startPass() async {
    setState(() => _isLoading = true);
    List<Ticket> tickets = await Tickets.of(_exam!.uid).all();
    _ticket = tickets[Random().nextInt(tickets.length)];
    DocumentReference? passRef = await Passes.of(_session!.uid).create(
      Pass.sample(
        uid: widget.studentKey,
        ticketUid: _ticket!.uid,
        answers: {},
        started: DateTime.now(),
        submited: null,
      ),
    );
    if (passRef != null) _pass = Pass.fromDocument(await passRef.get());
    await _loadAnswers();
    _streamDuration = _streamDurationConfig(_session!.timeForExam.hour, _session!.timeForExam.minute % 60, 1);
    _streamDuration!.play();
    _expandableController.expanded = true;
    setState(() => _isLoading = false);
  }

  Future<void> _submitPass() async {
    if (_answerControllers!.values.every((c) => c.text.isEmpty)) {
      pushSnackBarMessage(context, 'Нельзя отправить пустой билет');
      return;
    }
    showConfirmDialog(
      context,
      title: 'Отправить ответы на вопросы?',
      subtitle: 'Убедитель, что ответили на все вопросы. Вы не сможете изменить ответы и повторить отправку позже',
      confirmColor: adaptiveColor(context),
      cancelColor: errorColor(context),
      onConfirm: _sendAnswers,
    );
  }

  Future<void> _sendAnswers() async {
    Passes.of(widget.sessionUid).submit(_pass!.uid, _answers);
    setState(() => _passSubmited = true);
  }

  @override
  Widget build(BuildContext context) {
    return CenteredBodyScaffold(
      canBack: false,
      maxWidth: 800,
      floatingActionButton: const ToggleThemeFab(),
      body: _sessionNotExists
          ? const Text('Сессия не найдена')
          : _studentNotExists
              ? const Text('Студент не найден')
              : _exam == null || _session == null
                  ? const CircularProgressIndicator()
                  : Column(
                      mainAxisSize: MainAxisSize.min,
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const SizedBox(width: double.infinity),
                        groupVDivider,
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
                        // student
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text('Студент: ', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                            Text(_session!.students[widget.studentKey]!, style: const TextStyle(fontSize: 18)),
                          ],
                        ),
                        // time for exam
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            const Text('Время на зачет: ', style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
                            if (_session!.timeForExam.hour != 0)
                              Text(
                                '${verboseHours(_session!.timeForExam.hour)} ',
                                style: const TextStyle(fontSize: 18),
                              ),
                            if (_session!.timeForExam.minute != 0)
                              Text(
                                verboseMinutes(_session!.timeForExam.minute),
                                style: const TextStyle(fontSize: 18),
                              ),
                          ],
                        ),
                        ExpandablePanel(
                          controller: _expandableController,
                          theme: const ExpandableThemeData(
                            tapBodyToCollapse: false,
                            tapBodyToExpand: false,
                            tapHeaderToExpand: false,
                          ),
                          collapsed: const SizedBox(height: 4),
                          expanded: _ticket == null
                              ? const CircularProgressIndicator()
                              : Card(
                                  margin: const EdgeInsets.only(top: 24),
                                  child: Padding(
                                    padding: const EdgeInsets.fromLTRB(36, 30, 36, 36),
                                    child: Column(
                                      children: [
                                        Row(
                                          children: [
                                            const Icon(Icons.list_alt_rounded, size: 36),
                                            smallHDivider,
                                            Text(_ticket!.title, style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
                                            const Spacer(),
                                            if (!_passSubmited)
                                              SlideCountdown(
                                                streamDuration: _streamDuration,
                                                padding: const EdgeInsets.all(8),
                                                style: const TextStyle(fontSize: 22),
                                                decoration: BoxDecoration(
                                                  color: adaptiveColor(context, Colors.black12, Colors.black26),
                                                  borderRadius: BorderRadius.circular(8),
                                                ),
                                              ),
                                          ],
                                        ),
                                        smallVDivider,
                                        ListView.builder(
                                          shrinkWrap: true,
                                          itemCount: _ticket!.questions.length,
                                          itemBuilder: (context, index) {
                                            Question question = _ticket!.questions[index];
                                            return Column(
                                              crossAxisAlignment: CrossAxisAlignment.start,
                                              children: [
                                                Text(
                                                  '${index + 1}. ${question.text}',
                                                  style: const TextStyle(fontSize: 20),
                                                ),
                                                RoundedTextField(
                                                  controller: _answerControllers![question.uid],
                                                  minLines: 3,
                                                  maxLines: 5,
                                                  readOnly: _passSubmited,
                                                  decoration: InputDecoration(
                                                    filled: true,
                                                    fillColor: adaptiveColor(context, Colors.white30, Colors.black12),
                                                    hintText: _passSubmited ? 'Ответ не предоставлен' : 'Введите ответ на вопрос',
                                                  ),
                                                  onEditingComplete: () async {
                                                    Passes.of(widget.sessionUid).send(_pass!.uid, _answers);
                                                  },
                                                ),
                                                mediumVDivider,
                                              ],
                                            );
                                          },
                                        ),
                                      ],
                                    ),
                                  ),
                                ),
                        ),
                        groupVDivider,
                        SizedBox(
                          width: double.infinity,
                          child: _isLoading
                              ? const Center(child: CircularProgressIndicator())
                              : CircularBorderButton(
                                  onPressed: _pass == null
                                      ? _startPass
                                      : _passSubmited
                                          ? null
                                          : _submitPass,
                                  child: Row(
                                    mainAxisSize: MainAxisSize.min,
                                    children: [
                                      Padding(
                                        padding: const EdgeInsets.only(right: 4, left: 8),
                                        child: Text(
                                          _pass == null
                                              ? 'Начать'
                                              : _passSubmited
                                                  ? 'Ответы отправлены'
                                                  : 'Отправить ответы',
                                        ),
                                      ),
                                      _pass == null
                                          ? const Icon(Icons.arrow_forward_ios_rounded)
                                          : _passSubmited
                                              ? const Icon(Icons.done_rounded)
                                              : const Icon(Icons.upload_rounded),
                                    ],
                                  ),
                                ),
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
    _streamDuration?.pause();
    _streamDuration?.dispose();
    super.dispose();
  }
}
