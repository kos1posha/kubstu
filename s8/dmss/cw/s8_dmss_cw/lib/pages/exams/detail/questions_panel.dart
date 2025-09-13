import 'dart:async';

import 'package:animated_reorderable_list/animated_reorderable_list.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:expandable/expandable.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/firebase/questions.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';
import 'package:s8_dmss_cw/utils/functions.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';

class ExamQuestionsExpandablePanel extends StatefulWidget {
  const ExamQuestionsExpandablePanel({
    super.key,
    required this.examUid,
    required this.outerScrollController,
  });

  final String examUid;
  final ScrollController outerScrollController;

  @override
  MountedState<ExamQuestionsExpandablePanel> createState() => _ExamQuestionsExpandablePanelState();
}

class _ExamQuestionsExpandablePanelState extends MountedState<ExamQuestionsExpandablePanel> {
  late final ExpandableController _expandableController = ExpandableController();

  List<Question>? _questions;
  StreamSubscription? _questionsStreamSubscription;
  List<TextEditingController>? _questionControllers;

  bool _newQuestionIsSaving = false;
  final FocusNode _newQuestionFocusNode = FocusNode();
  final TextEditingController _newQuestionController = TextEditingController();

  Future<void> _createQuestion() async {
    if (_newQuestionController.text == '') return;
    setState(() => _newQuestionIsSaving = true);
    try {
      var ref = await Questions.of(widget.examUid).create(
        Question.sample(
          text: _newQuestionController.text,
          index: _questions?.length ?? 0,
        ),
      );
      if (ref == null) return;
    } on FirebaseException catch (e) {
      if (mounted) {
        pushSnackBarErrorCodeMessage(context, e.code);
      }
    }
    _newQuestionController.text = '';
    _newQuestionFocusNode.requestFocus();
    setState(() => _newQuestionIsSaving = false);
  }

  @override
  void initState() {
    super.initState();
    // questions stream
    _questionsStreamSubscription = Questions.of(widget.examUid).streamAll().listen((snapshot) async {
      _questions = Question.fromDocuments(snapshot.docs);
      _questionControllers = [for (Question q in _questions!) TextEditingController(text: q.text)];
      _expandableController.expanded = true;
      updateState();
    });
  }

  @override
  Widget build(BuildContext context) {
    return Theme(
      data: Theme.of(context).copyWith(
        splashColor: Colors.transparent,
        hoverColor: Colors.transparent,
        highlightColor: Colors.transparent,
        dividerColor: Colors.transparent,
      ),
      child: ExpandablePanel(
        controller: _expandableController,
        theme: ExpandableThemeData(
          iconColor: Theme.of(context).brightness == Brightness.light ? Colors.black : Colors.white,
          iconSize: 30,
          iconPadding: const EdgeInsets.only(top: 8),
        ),
        header: Row(
          children: [
            Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Банк вопросов',
                  style: subtitleTextStyle.copyWith(fontWeight: FontWeight.bold),
                ),
                Text(
                  _questions != null ? (_questions!.isEmpty ? 'Пусто' : 'Всего ${_questions!.length}') : 'Загрузка...',
                  style: secondaryTextStyle,
                ),
              ],
            ),
            const Spacer(),
            PopupMenuButton(
              tooltip: '',
              constraints: const BoxConstraints(minWidth: 150),
              itemBuilder: (BuildContext context) => <PopupMenuEntry>[
                PopupMenuItem(
                  value: 'clearQuestions',
                  child: Text('Очистить', style: TextStyle(color: errorColor(context))),
                  onTap: () async {
                    if (_questions == null) return;
                    if (_questions!.isEmpty) {
                      pushSnackBarMessage(context, 'Банк вопросов пуст');
                      return;
                    }
                    showConfirmDialog(
                      context,
                      title: 'Вы уверены, что хотите удалить все вопросы данного зачета?',
                      subtitle: 'Данное действие необратимо',
                      onConfirm: () async {
                        await Questions.of(widget.examUid).clear();
                        if (context.mounted) pushSnackBarMessage(context, 'Банк вопросов успешно очищен');
                      },
                      confirmText: widget.examUid.s_(0, 6),
                      confirmHelpText: 'Введите первые 6 символов ключа зачета',
                    );
                  },
                ),
              ],
              child: const Icon(Icons.settings_rounded, size: 20),
            ),
            smallHDivider,
          ],
        ),
        collapsed: const SizedBox.shrink(),
        expanded: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(height: 4),
            AnimatedReorderableListView(
              shrinkWrap: true,
              dragStartDelay: Durations.short2,
              clipBehavior: Clip.hardEdge,
              isSameItem: (a, b) => a.uid == b.uid,
              onReorder: (oldIndex, newIndex) {
                _questions!.insert(newIndex, _questions!.removeAt(oldIndex));
                Questions.of(widget.examUid).move(oldIndex, newIndex);
              },
              items: _questions ?? <Question>[],
              itemBuilder: (context, index) {
                Question question = _questions![index];
                TextEditingController controller = _questionControllers![question.index];
                return KeyedSubtree(
                  key: ValueKey('question${question.uid}OfExam${widget.examUid}Item'),
                  child: Padding(
                    padding: EdgeInsets.only(bottom: index != _questions!.length - 1 ? 2 : 1),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text('${question.index + 1}. ', style: const TextStyle(fontSize: 16)),
                        Expanded(
                          child: Padding(
                            padding: const EdgeInsets.only(right: 36),
                            child: Material(
                              child: TransparentTextField(
                                controller: controller,
                                minLines: 1,
                                maxLines: 4,
                                decoration: InputDecoration(hintText: 'Удалить вопрос', hintStyle: TextStyle(color: errorColor(context))),
                                onEditingComplete: () {
                                  if (controller.text == '') {
                                    Questions.of(widget.examUid).delete(question.uid);
                                  } else if (controller.text != question.text) {
                                    Questions.of(widget.examUid).update(question.uid, text: controller.text);
                                  }
                                },
                              ),
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
            ),
            if (!_newQuestionIsSaving && _questions != null)
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text('${_questions!.length + 1}. ', style: const TextStyle(color: MainTheme.secondary, fontSize: 16)),
                  Expanded(
                    child: TransparentTextField(
                      controller: _newQuestionController,
                      focusNode: _newQuestionFocusNode,
                      minLines: 1,
                      maxLines: 4,
                      decoration: const InputDecoration(
                        hintText: 'Добавить вопрос',
                        hintStyle: TextStyle(color: MainTheme.secondary),
                      ),
                      textStyle: const TextStyle(color: MainTheme.secondary),
                      onEditingComplete: _createQuestion,
                    ),
                  ),
                ],
              )
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _questionsStreamSubscription?.cancel();
    _expandableController.dispose();
    _newQuestionController.dispose();
    if (_questionControllers != null) disposeControllers(_questionControllers!);
    super.dispose();
  }
}
