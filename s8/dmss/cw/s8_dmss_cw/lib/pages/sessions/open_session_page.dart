import 'dart:async';

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/pages/sessions/pass_session_page.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';

class OpenSessionPage extends StatefulWidget {
  const OpenSessionPage({super.key, required this.sessionUid});

  static const String routeName = 'open_session';
  static const String routePath = '/session/:uid';

  final String sessionUid;

  @override
  MountedState<OpenSessionPage> createState() => _OpenSessionPageState();
}

class _OpenSessionPageState extends MountedState<OpenSessionPage> {
  final TextEditingController _studentKeyController = TextEditingController();

  String? _error;
  bool _isLoading = false;
  bool _sessionNotExists = false;

  Exam? _exam;
  StreamSubscription? _examStreamSubscription;
  Session? _session;
  StreamSubscription? _sessionStreamSubscription;

  @override
  void initState() {
    super.initState();
    // session stream
    _sessionStreamSubscription = Sessions.streamOne(widget.sessionUid).listen(
      (snapshot) {
        if (!snapshot.exists) {
          setState(() => _sessionNotExists = true);
          return;
        }
        _session = Session.fromDocument(snapshot);
        _examStreamSubscription ??= Exams.streamOne(_session!.examUid).listen(
          (snapshot) {
            _exam = Exam.fromDocument(snapshot);
            updateState();
          },
        );
        updateState();
      },
    );
  }

  Future<void> _submitStudentKey() async {
    if (_studentKeyController.text == '') {
      setState(() => _error = 'Укажите ключ, чтобы продолжить');
      return;
    }
    setState(() => _isLoading = true);
    await Future.delayed(const Duration(milliseconds: 250));
    if (_session!.students.containsKey(_studentKeyController.text) && mounted) {
      context.pushNamed(PassSessionPage.routeName, pathParameters: {
        'uid': _session!.uid,
        'studentKey': _studentKeyController.text,
      });
    } else {
      setState(() => _error = 'Ключ не найден');
    }
    setState(() => _isLoading = false);
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
                    const SizedBox(width: double.infinity),
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
                    if (_session!.isActive)
                      LayoutBuilder(builder: (context, constraints) {
                        var children = [
                          CircularTextField(
                            controller: _studentKeyController,
                            autoTrim: true,
                            decoration: InputDecoration(
                              hintText: 'Введите ключ студента',
                              prefixIcon: const Icon(Icons.person_rounded),
                              errorText: _error,
                            ),
                            onChanged: (_) async => setState(() => _error = null),
                          ),
                          _isLoading
                              ? const Center(child: CircularProgressIndicator())
                              : SizedBox(
                                  width: double.infinity,
                                  child: CircularBorderButton(
                                    onPressed: _submitStudentKey,
                                    child: const Row(
                                      mainAxisSize: MainAxisSize.min,
                                      children: [
                                        Padding(
                                          padding: EdgeInsets.only(right: 4, left: 8),
                                          child: Text('Продолжить', style: TextStyle(fontWeight: FontWeight.bold)),
                                        ),
                                        Icon(Icons.arrow_forward_ios_rounded),
                                      ],
                                    ),
                                  ),
                                ),
                        ];
                        if (constraints.maxWidth >= 600) {
                          return Row(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            spacing: 16,
                            children: [
                              Expanded(flex: 2, child: children[0]),
                              Expanded(flex: 1, child: children[1]),
                            ],
                          );
                        } else {
                          return Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            spacing: 16,
                            children: children,
                          );
                        }
                      }),
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
                  ],
                ),
    );
  }

  @override
  void dispose() {
    _examStreamSubscription?.cancel();
    _sessionStreamSubscription?.cancel();
    _studentKeyController.dispose();
    super.dispose();
  }
}
