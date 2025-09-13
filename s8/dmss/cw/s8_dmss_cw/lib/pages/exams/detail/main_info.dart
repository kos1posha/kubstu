import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/datetime.dart';
import 'package:s8_dmss_cw/utils/functions.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';

class ExamMainInfo extends StatefulWidget {
  const ExamMainInfo({super.key, required this.examUid});

  final String examUid;

  @override
  MountedState<ExamMainInfo> createState() => _ExamMainInfoState();
}

class _ExamMainInfoState extends MountedState<ExamMainInfo> {
  User get user => FirebaseAuth.instance.currentUser!;

  Exam? _exam;
  StreamSubscription? _examStreamSubscription;

  // controllers
  final Map<String, TextEditingController> _controllers = {
    'title': TextEditingController(),
    'teacher': TextEditingController(),
    'discipline': TextEditingController(),
    'description': TextEditingController(),
  };

  Future<void> _setupControllers(Exam exam) async {
    _controllers['title']!.text = exam.title;
    _controllers['teacher']!.text = exam.teacher;
    _controllers['discipline']!.text = exam.discipline;
    _controllers['description']!.text = exam.description;
    updateState();
  }

  // changed fields
  final Map<String, bool> _changedFields = {'title': false, 'teacher': false, 'discipline': false, 'description': false};
  bool get _isChanged => _changedFields.values.any((isChanged) => isChanged == true);
  bool _isSaving = false;
  Timer? _saveTimer;

  Future<void> _runSaveTimer() async {
    _saveTimer?.cancel();
    _saveTimer = Timer(const Duration(seconds: 3), _saveExamChanges);
  }

  Future<void> _saveExamChanges() async {
    if (!_isChanged) return;
    setState(() => _isSaving = true);
    await Exams.save(
      widget.examUid,
      title: _changedFields['title']! ? _controllers['title']!.text : null,
      teacher: _changedFields['teacher']! ? _controllers['teacher']!.text : null,
      discipline: _changedFields['discipline']! ? _controllers['discipline']!.text : null,
      description: _changedFields['description']! ? _controllers['description']!.text : null,
    );
    _changedFields.updateAll((_, __) => false);
    setState(() => _isSaving = false);
  }

  @override
  void initState() {
    super.initState();
    // exam stream
    _examStreamSubscription = Exams.of(user.uid).streamOne(widget.examUid).listen((snapshot) async {
      _exam = Exam.fromDocument(snapshot);
      _setupControllers(_exam!);
    });
  }

  @override
  Widget build(BuildContext context) {
    if (_exam == null) return const Text('Загрузка...', style: secondaryTextStyle);
    return Column(
      mainAxisSize: MainAxisSize.min,
      mainAxisAlignment: MainAxisAlignment.start,
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // title field
        IntrinsicWidth(
          child: TransparentTextField(
            controller: _controllers['title']!,
            maxLines: 3,
            textStyle: titleTextStyle,
            decoration: const InputDecoration(hintText: 'Введите название (обязательно)'),
            underlineFocused: true,
            onChanged: (_) async {
              if (_isChanged) _runSaveTimer();
            },
            onEditingComplete: () async {
              if (_controllers['title']!.text.isEmpty) {
                _controllers['title']!.text = _exam!.title;
              } else {
                setState(() {
                  _changedFields['title'] = _controllers['title']!.text != _exam!.title;
                });
                if (!(_saveTimer?.isActive ?? false)) _runSaveTimer();
              }
            },
          ),
        ),
        // important dates
        ImportantDates(
          examCreated: _exam!.created,
          examModified: _exam!.modified,
          isChanged: _isChanged,
          isSaving: _isSaving,
        ),
        // uid
        mediumVDivider,
        Row(
          children: [
            const Icon(Icons.vpn_key_rounded, color: MainTheme.secondary),
            smallHDivider,
            SelectableText(
              _exam!.uid,
              style: const TextStyle(
                color: MainTheme.secondary,
                fontSize: 17,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
        // teacher field
        smallVDivider,
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Icon(Icons.person),
            smallHDivider,
            Flexible(
              child: IntrinsicWidth(
                child: TransparentTextField(
                  controller: _controllers['teacher']!,
                  textStyle: const TextStyle(fontSize: 18),
                  decoration: const InputDecoration(
                    constraints: BoxConstraints(minWidth: 300),
                    hintText: 'Указать преподавателя',
                  ),
                  underlineFocused: true,
                  onChanged: (_) async {
                    if (_isChanged) _runSaveTimer();
                  },
                  onEditingComplete: () async {
                    setState(() {
                      _changedFields['teacher'] = _controllers['teacher']!.text != _exam!.teacher;
                    });
                    if (!(_saveTimer?.isActive ?? false)) _runSaveTimer();
                  },
                ),
              ),
            ),
          ],
        ),
        // discipline field
        smallVDivider,
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Icon(Icons.school_rounded),
            smallHDivider,
            Flexible(
              child: IntrinsicWidth(
                child: TransparentTextField(
                  controller: _controllers['discipline']!,
                  textStyle: const TextStyle(fontSize: 18),
                  decoration: const InputDecoration(
                    constraints: BoxConstraints(minWidth: 300),
                    hintText: 'Указать дисциплину',
                  ),
                  underlineFocused: true,
                  onChanged: (_) async {
                    if (_isChanged) _runSaveTimer();
                  },
                  onEditingComplete: () async {
                    setState(() {
                      _changedFields['discipline'] = _controllers['discipline']!.text != _exam!.discipline;
                    });
                    if (!(_saveTimer?.isActive ?? false)) _runSaveTimer();
                  },
                ),
              ),
            ),
          ],
        ),
        // description field
        smallVDivider,
        Row(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const Icon(Icons.comment_rounded),
            smallHDivider,
            Flexible(
              child: IntrinsicWidth(
                child: TransparentTextField(
                  controller: _controllers['description']!,
                  maxLines: 3,
                  textStyle: const TextStyle(fontSize: 18),
                  decoration: const InputDecoration(
                    constraints: BoxConstraints(minWidth: 300),
                    hintText: 'Указать описание',
                  ),
                  underlineFocused: true,
                  onChanged: (_) async {
                    if (_isChanged) _runSaveTimer();
                  },
                  onEditingComplete: () async {
                    setState(() {
                      _changedFields['description'] = _controllers['description']!.text != _exam!.description;
                    });
                    if (!(_saveTimer?.isActive ?? false)) _runSaveTimer();
                  },
                ),
              ),
            ),
          ],
        ),
      ],
    );
  }

  @override
  void dispose() {
    _examStreamSubscription?.cancel();
    _saveTimer?.cancel();
    if (_isChanged) {
      Exams.save(
        _exam!.uid,
        title: _changedFields['title']! ? _controllers['title']!.text : null,
        teacher: _changedFields['teacher']! ? _controllers['teacher']!.text : null,
        discipline: _changedFields['discipline']! ? _controllers['discipline']!.text : null,
        description: _changedFields['description']! ? _controllers['description']!.text : null,
      ).whenComplete(() => disposeControllers(_controllers.values));
    } else {
      disposeControllers(_controllers.values);
    }
    super.dispose();
  }
}

class ImportantDates extends StatefulWidget {
  const ImportantDates({
    super.key,
    required this.examCreated,
    required this.examModified,
    required this.isChanged,
    required this.isSaving,
  });

  final DateTime examCreated;
  final DateTime? examModified;
  final bool isChanged;
  final bool isSaving;

  @override
  MountedState<ImportantDates> createState() => _ImportantDatesState();
}

class _ImportantDatesState extends MountedState<ImportantDates> {
  bool _isHovered = false;

  Future<void> _toggleHover(bool state) async {
    if (_isHovered == state) return;
    _isHovered = state;
    if (_dateStateChanged) {
      _dateState = !_dateState;
      _dateStateChanged = false;
    }
    updateState();
  }

  bool _dateState = false;
  bool _dateStateChanged = false;

  Future<void> _toggleShowCreated(bool state) async {
    if (_dateState == state) return;
    _dateStateChanged = true;
    updateState();
  }

  double _getCreatedOpacity() {
    if (widget.examModified == null) {
      return 1.0;
    } else if (_isHovered) {
      return _dateState ? 0.0 : 1.0;
    } else {
      return _dateState ? 1.0 : 0.0;
    }
  }

  double _getModifiedOpacity() {
    if (widget.examModified == null) {
      return 0.0;
    } else if (_isHovered) {
      return _dateState ? 1.0 : 0.0;
    } else {
      return _dateState ? 0.0 : 1.0;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Row(
      children: [
        AnimatedSize(
          duration: Durations.short3,
          child: Padding(
            padding: EdgeInsets.only(right: widget.isChanged ? 4 : 0),
            child: widget.isSaving
                ? SizedBox.square(
                    dimension: widget.isChanged ? 10 : 0,
                    child: const CircularProgressIndicator(
                      color: MainTheme.primary,
                      strokeWidth: 2,
                    ),
                  )
                : Icon(
                    Icons.circle,
                    size: widget.isChanged ? 10 : 0,
                    color: MainTheme.primary,
                  ),
          ),
        ),
        Padding(
          padding: const EdgeInsets.only(bottom: 3),
          child: InkWell(
            onTap: widget.examModified == null ? null : () async => _toggleShowCreated(!_dateState),
            onHover: widget.examModified == null ? null : (state) async => _toggleHover(state),
            hoverColor: Colors.transparent,
            splashColor: Colors.transparent,
            highlightColor: Colors.transparent,
            focusColor: Colors.transparent,
            child: Stack(
              children: [
                AnimatedOpacity(
                  opacity: _getCreatedOpacity(),
                  duration: Durations.short3,
                  child: Text(
                    'создан ${prettyDateTime(widget.examCreated)}',
                    style: secondaryTextStyle,
                  ),
                ),
                if (widget.examModified != null)
                  AnimatedOpacity(
                    opacity: _getModifiedOpacity(),
                    duration: Durations.short3,
                    child: Text(
                      'изменен ${prettyDateTime(widget.examModified!)}',
                      style: secondaryTextStyle,
                    ),
                  ),
              ],
            ),
          ),
        ),
      ],
    );
  }
}
