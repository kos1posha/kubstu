import 'package:animated_reorderable_list/animated_reorderable_list.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/dialogs/base_dialog.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/main.dart';
import 'package:s8_dmss_cw/pages/sessions/open_session_page.dart';
import 'package:s8_dmss_cw/pages/sessions/results_session_page.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';
import 'package:s8_dmss_cw/utils/functions.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/datetime_fields.dart';
import 'package:s8_dmss_cw/widgets/other/error_text.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';

class CreateSessionDialog extends StatefulWidget {
  const CreateSessionDialog({super.key, required this.examUid});

  final String examUid;

  @override
  MountedState<CreateSessionDialog> createState() => _CreateSessionDialogState();
}

class _CreateSessionDialogState extends MountedState<CreateSessionDialog> {
  DateTime? _startSessionDateTime;
  DateTime? _endSessionDateTime;
  TimeOfDay? _timeForExam;
  final TextEditingController _timeForExamController = TextEditingController();
  final TextEditingController _groupNameController = TextEditingController();

  final TextEditingController _newStudentController = TextEditingController();
  final FocusNode _newStudentFocusNode = FocusNode();
  final List<({String key, TextEditingController controller})> _studentControllers = [];

  final Map<String, String?> _errors = {
    'form': null,
    'startEndDates': null,
    'timeForExam': null,
    'students': null,
  };

  bool _isLoading = false;

  Future<void> _addStudent(String studentName) async {
    _studentControllers.insert(0, (
      key: generateRandomKey(8),
      controller: TextEditingController(text: studentName),
    ));
    _errors['students'] = null;
    _newStudentController.text = '';
    updateState();
  }

  bool get _canSubmit => _errors.values.every((et) => et == null);

  Future<bool> _validateForm() async {
    bool isValid = true;
    if (_startSessionDateTime == null || _endSessionDateTime == null) {
      _errors['startEndDates'] = 'Обязательное поле';
      isValid = false;
    } else {
      if (_startSessionDateTime!.isAfter(_endSessionDateTime!)) {
        _errors['startEndDates'] = 'Начало зачета не может быть позже конца зачета';
        isValid = false;
      }
      if (_endSessionDateTime!.isBefore(DateTime.now())) {
        _errors['startEndDates'] = 'Сроки зачета не могут быть в прошлом';
        isValid = false;
      }
    }
    if (_timeForExam == null) {
      _errors['timeForExam'] = 'Обязательное поле';
      isValid = false;
    } else if (_timeForExam!.hour == 0 && _timeForExam!.minute == 0) {
      _errors['timeForExam'] = 'Время зачета не может быть нулевым';
      isValid = false;
    }
    if (isValid) {
      if (!isTimeWithinDateTimeRange(_startSessionDateTime!, _endSessionDateTime!, _timeForExam!)) {
        _errors['timeForExam'] = 'Время зачета не вмещается в указанные сроки сдачи';
        isValid = false;
      }
    }
    if (_groupNameController.text.isEmpty) {
      _errors['groupName'] = 'Обязательное поле';
      isValid = false;
    }
    if (_studentControllers.isEmpty) {
      _errors['students'] = 'Зачет не может проводиться без студентов';
      isValid = false;
    }
    return isValid;
  }

  Future<void> _createTicket() async {
    if (!await _validateForm()) {
      updateState();
      return;
    }
    setState(() => _isLoading = true);
    try {
      Map<String, String> students = {
        for (var student in _studentControllers) student.key: student.controller.text,
      };
      var ref = await Sessions.of(widget.examUid).create(
        Session.sample(
          examUid: widget.examUid,
          start: _startSessionDateTime!,
          end: _endSessionDateTime!,
          timeForExam: _timeForExam!,
          groupName: _groupNameController.text,
          students: students,
        ),
      );
      if (ref == null) return;
    } on FirebaseException catch (e) {
      _errors['form'] = e.code;
    }
    if (mounted) context.pop();
  }

  @override
  Widget build(BuildContext context) {
    DateTime now = DateTime.now().clean();
    DateTime weekAfter = now.add(const Duration(days: 7));
    DateTime yearAfter = now.add(const Duration(days: 365));
    return BaseDialog(
      maxWidth: 500,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const Text('Начать зачетную сессию', style: dialogTitleTextStyle),
          const Text('Сроки сдачи', style: subtitleTextStyle),
          smallVDivider,
          DateTimeRangeFields(
            startDate: _startSessionDateTime,
            startPickerHelpText: 'Начало зачета',
            startInitialDate: now.copyWith(hour: 8, minute: 0),
            startFirstDate: now.copyWith(hour: 0, minute: 0),
            startLastDate: yearAfter,
            startOnChanged: (date) async {
              if (_startSessionDateTime == date) return;
              _startSessionDateTime = date.clean();
              if (_endSessionDateTime != null) _errors['startEndDates'] = null;
              updateState();
            },
            endDate: _endSessionDateTime,
            endPickerHelpText: 'Конец зачета',
            endInitialDate: weekAfter.copyWith(hour: 23, minute: 59),
            endFirstDate: now.copyWith(hour: 0, minute: 0),
            endLastDate: yearAfter,
            endOnChanged: (date) async {
              if (_endSessionDateTime == date) return;
              _endSessionDateTime = date.clean();
              if (_endSessionDateTime != null) _errors['startEndDates'] = null;
              updateState();
            },
          ),
          Padding(
            padding: const EdgeInsets.only(left: 12),
            child: ErrorText(_errors['startEndDates']),
          ),
          smallVDivider,
          Row(
            children: [
              Expanded(
                child: TimeField(
                  controller: _timeForExamController,
                  pickerHelpText: 'Время зачета',
                  decoration: const InputDecoration(hintText: 'Время зачета '),
                  initialTime: _timeForExam ?? const TimeOfDay(hour: 1, minute: 30),
                  onChanged: (time) async {
                    if (_timeForExam == time) return;
                    _timeForExam = time;
                    _errors['timeForExam'] = null;
                    updateState();
                  },
                ),
              ),
              mediumHDivider,
              const Expanded(child: Text('Время, отведенное студенту на отправку ответов', style: dialogSecondaryTextStyle)),
            ],
          ),
          Padding(
            padding: const EdgeInsets.only(left: 12),
            child: ErrorText(_errors['timeForExam']),
          ),
          smallVDivider,
          const Text('Группа', style: subtitleTextStyle),
          smallVDivider,
          RoundedTextField(
            controller: _groupNameController,
            decoration: const InputDecoration(hintText: 'Название группы'),
            onChanged: (_) async => setState(() => _errors['groupName'] = null),
          ),
          Padding(
            padding: const EdgeInsets.only(left: 12),
            child: ErrorText(_errors['groupName']),
          ),
          smallVDivider,
          Container(
            clipBehavior: Clip.hardEdge,
            constraints: const BoxConstraints(maxHeight: 200),
            decoration: BoxDecoration(
              border: Border.all(color: MainTheme.neural, width: 2),
              borderRadius: roundedBorderRadius,
            ),
            child: Column(
              children: [
                Container(
                  padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
                  color: adaptiveColor(context, Colors.white10, Colors.black12),
                  child: Row(
                    children: [
                      Flexible(
                        flex: 10,
                        child: TransparentTextField(
                          controller: _newStudentController,
                          focusNode: _newStudentFocusNode,
                          decoration: const InputDecoration(
                            hintText: 'ФИО студента',
                            hintStyle: TextStyle(),
                          ),
                          underlineFocused: true,
                        ),
                      ),
                      Flexible(
                        flex: 4,
                        child: Align(
                          alignment: Alignment.centerRight,
                          child: Link(
                            'Добавить',
                            style: const TextStyle(fontSize: 16),
                            onPressed: () async {
                              if (_newStudentController.text == '') {
                                _newStudentFocusNode.requestFocus();
                              } else {
                                _addStudent(_newStudentController.text);
                              }
                            },
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                const Divider(thickness: 2, height: 0, color: MainTheme.neural),
                Expanded(
                  child: AnimatedListView(
                    padding: const EdgeInsets.symmetric(vertical: 4),
                    shrinkWrap: true,
                    isSameItem: (a, b) => a.key == b.key,
                    items: _studentControllers,
                    itemBuilder: (context, index) {
                      var studentItem = _studentControllers[index];
                      return KeyedSubtree(
                        key: ValueKey('student${studentItem.key}'),
                        child: Padding(
                          padding: const EdgeInsets.fromLTRB(16, 4, 16, 4),
                          child: Row(
                            children: [
                              Expanded(
                                flex: 10,
                                child: TransparentTextField(
                                  controller: studentItem.controller,
                                  decoration: InputDecoration(hintText: 'Удалить студента', hintStyle: TextStyle(color: errorColor(context))),
                                  underlineFocused: true,
                                  onEditingComplete: () {
                                    if (studentItem.controller.text == '') {
                                      _studentControllers.removeAt(index);
                                      updateState();
                                    }
                                  },
                                ),
                              ),
                              Expanded(
                                flex: 4,
                                child: Align(
                                  alignment: Alignment.centerRight,
                                  child: SelectableText(
                                    studentItem.key,
                                    style: const TextStyle(fontSize: 16),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 12),
            child: Row(
              children: [
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      if (_studentControllers.isNotEmpty) Text('Всего ${_studentControllers.length}', style: dialogSecondaryTextStyle),
                      ErrorText(_errors['students']),
                    ],
                  ),
                ),
                Link(
                  'Очистить',
                  style: dialogSecondaryTextStyle.copyWith(color: MainTheme.neural),
                  onPressed: _isLoading ? null : () async => setState(() => _studentControllers.clear()),
                ),
              ],
            ),
          ),
          mediumVDivider,
          SizedBox(
            width: double.infinity,
            child: _isLoading
                ? const Center(child: CircularProgressIndicator())
                : CircularBorderButton(
                    onPressed: _canSubmit ? _createTicket : null,
                    child: const Text('Начать'),
                  ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    super.dispose();
    _newStudentController.dispose();
    _groupNameController.dispose();
    _timeForExamController.dispose();
    for (var sc in _studentControllers) {
      sc.controller.dispose();
    }
  }
}

class DetailSessionDialog extends StatefulWidget {
  const DetailSessionDialog({super.key, required this.examUid, required this.session});

  final String examUid;
  final Session session;

  @override
  MountedState<DetailSessionDialog> createState() => _DetailSessionDialogState();
}

class _DetailSessionDialogState extends MountedState<DetailSessionDialog> {
  final bool _isLoading = false;

  final TextEditingController _timeForExamController = TextEditingController();

  @override
  void initState() {
    super.initState();
    _timeForExamController.text = TimeField.formatter.format(widget.session.timeForExam.toDate());
  }

  @override
  Widget build(BuildContext context) {
    return BaseDialog(
      maxWidth: 500,
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Text(widget.session.groupName, style: titleTextStyle),
              const Spacer(),
              CopyLinkButton(
                link: getLink(context, name: OpenSessionPage.routeName, pathParameters: {'uid': widget.session.uid}),
              ),
              smallHDivider,
              IconButton(
                onPressed: () {
                  context.goNamed(OpenSessionPage.routeName, pathParameters: {'uid': widget.session.uid});
                },
                icon: const Icon(Icons.open_in_new_rounded),
              ),
            ],
          ),
          const Text('Сроки сдачи', style: subtitleTextStyle),
          smallVDivider,
          DateTimeRangeFields(startDate: widget.session.start, endDate: widget.session.end, readOnly: true),
          smallVDivider,
          Row(
            children: [
              Expanded(
                child: TimeField(
                  controller: _timeForExamController,
                  readOnly: true,
                  decoration: const InputDecoration(hintText: 'Время зачета '),
                  pickerHelpText: 'Время зачета',
                ),
              ),
              mediumHDivider,
              const Expanded(child: Text('Время, отведенное студенту на отправку ответов', style: dialogSecondaryTextStyle)),
            ],
          ),
          smallVDivider,
          const Text('Студенты', style: subtitleTextStyle),
          smallVDivider,
          Container(
            clipBehavior: Clip.hardEdge,
            constraints: const BoxConstraints(maxHeight: 200),
            decoration: BoxDecoration(
              border: Border.all(color: MainTheme.neural, width: 2),
              borderRadius: roundedBorderRadius,
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Container(
                  padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
                  color: adaptiveColor(context, Colors.white10, Colors.black12),
                  child: const Row(
                    children: [
                      Text('ФИО студента', style: TextStyle(fontSize: 16)),
                      Spacer(),
                      Text('Ключ', style: TextStyle(fontSize: 16)),
                    ],
                  ),
                ),
                const Divider(thickness: 2, height: 0, color: MainTheme.neural),
                Expanded(
                  child: AnimatedListView(
                    padding: const EdgeInsets.symmetric(vertical: 4),
                    shrinkWrap: true,
                    isSameItem: (a, b) => a.key == b.key,
                    items: widget.session.students.entries.toList(),
                    itemBuilder: (context, index) {
                      var studentEntry = widget.session.students.entries.elementAt(index);
                      return KeyedSubtree(
                        key: ValueKey('student${studentEntry.key}OfSession${widget.session.uid}'),
                        child: Padding(
                          padding: const EdgeInsets.fromLTRB(16, 4, 16, 4),
                          child: Row(
                            children: [
                              Expanded(
                                flex: 10,
                                child: SelectableText(
                                  studentEntry.value,
                                  style: const TextStyle(fontSize: 16),
                                ),
                              ),
                              Expanded(
                                flex: 4,
                                child: Align(
                                  alignment: Alignment.centerRight,
                                  child: SelectableText(
                                    studentEntry.key,
                                    style: const TextStyle(fontSize: 16),
                                  ),
                                ),
                              ),
                            ],
                          ),
                        ),
                      );
                    },
                  ),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 12),
            child: Text('Всего ${widget.session.students.length}', style: dialogSecondaryTextStyle),
          ),
          mediumVDivider,
          SizedBox(
            width: double.infinity,
            child: !widget.session.isActive || !widget.session.isPassed
                ? _isLoading
                    ? const Center(child: CircularProgressIndicator())
                    : CircularBorderButton(
                        onPressed: () async {
                          showConfirmDialog(
                            context,
                            title: 'Вы уверены, что хотите отменить проведение зачета?',
                            subtitle: 'Данное действие необратимо',
                            onConfirm: () async {
                              await Sessions.of(widget.examUid).delete(widget.session.uid);
                              if (context.mounted) {
                                pushSnackBarMessage(context, 'Зачет успешно отменен');
                                context.pop();
                              }
                            },
                          );
                        },
                        child: Text(
                          'Отменить',
                          style: TextStyle(color: errorColor(context)),
                        ),
                      )
                : CircularBorderButton(
                    onPressed: () {
                      context.goNamed(ResultsSessionPage.routeName, pathParameters: {'uid': widget.session.uid});
                    },
                    child: const Text('Результаты'),
                  ),
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    super.dispose();
    _timeForExamController.dispose();
  }
}
