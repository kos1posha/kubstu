import 'dart:async';

import 'package:animated_reorderable_list/animated_reorderable_list.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:expandable/expandable.dart';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/dialogs/base_dialog.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/firebase/questions.dart';
import 'package:s8_dmss_cw/firebase/tickets.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/other/checkbox_tile.dart';
import 'package:s8_dmss_cw/widgets/other/error_text.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';

class CreateTicketDialog extends StatefulWidget {
  const CreateTicketDialog({super.key, required this.examUid, required this.ticketIndex});

  final String examUid;
  final int ticketIndex;

  @override
  MountedState<CreateTicketDialog> createState() => _CreateTicketDialogState();
}

class _CreateTicketDialogState extends MountedState<CreateTicketDialog> {
  List<Question>? _questions;
  StreamSubscription? _questionsStreamSubscription;
  Map<String, bool>? _questionCheckStates;

  int get _checkedQuestionsCount => _questionCheckStates!.values.where((state) => state == true).length;

  String? _error;
  bool _isLoading = false;
  bool get _canSubmit => _error == null;

  Future<bool> _validateForm() async {
    if (_checkedQuestionsCount == 0) {
      _error = 'Билет не может быть пустым';
      return false;
    }
    return true;
  }

  Future<void> _createTicket() async {
    if (!await _validateForm()) {
      updateState();
      return;
    }
    setState(() => _isLoading = true);
    try {
      Set<String> questionUids = {
        for (Question question in _questions!)
          if (_questionCheckStates![question.uid] ?? false) question.uid
      };
      var ref = await Tickets.of(widget.examUid).create(
        Ticket.sample(
          questionUids: questionUids,
          index: widget.ticketIndex,
        ),
      );
      if (ref == null) return;
    } on FirebaseException catch (e) {
      _error = e.code;
    }
    if (mounted) context.pop();
  }

  Future<void> _onChangedCheckState(bool? state, Question question) async {
    if (_questionCheckStates![question.uid] == state) return;
    _questionCheckStates![question.uid] = state ?? false;
    _error = null;
    updateState();
  }

  @override
  void initState() {
    super.initState();
    _questionCheckStates = {};
    // questions stream
    _questionsStreamSubscription = Questions.of(widget.examUid).streamAll().listen((snapshot) async {
      _questions = snapshot.docs.map((doc) {
        _questionCheckStates![doc.id] = _questionCheckStates!.get(doc.id) ?? false;
        return Question.fromDocument(doc);
      }).toList();
      updateState();
    });
  }

  @override
  Widget build(BuildContext context) {
    return BaseTicketDialog(
      title: 'Новый билет',
      subtitle: 'Выберите вопросы из списка',
      error: _error,
      isLoading: _isLoading,
      canSubmit: _canSubmit,
      submitChild: const Text('Добавить'),
      onSubmit: _createTicket,
      body: Column(
        children: [
          Container(
            constraints: const BoxConstraints(maxHeight: 300),
            padding: const EdgeInsets.all(8),
            decoration: BoxDecoration(
              color: adaptiveColor(context, Colors.white54, Colors.black38),
              borderRadius: BorderRadius.circular(8),
            ),
            child: _questions == null
                ? const Center(child: CircularProgressIndicator())
                : AnimatedListView(
                    isSameItem: (a, b) => a.uid == b.uid,
                    items: _questions!,
                    itemBuilder: (context, index) {
                      Question question = _questions![index];
                      return KeyedSubtree(
                        key: ValueKey('question${question.uid}CheckboxTileItem'),
                        child: CheckboxTile(
                          value: _questionCheckStates![question.uid]!,
                          onChanged: (state) async => _onChangedCheckState(state, question),
                          subchild: Text('${question.index + 1}. ', style: const TextStyle(fontSize: 16)),
                          child: Text(question.text, style: const TextStyle(fontSize: 16), maxLines: 2, overflow: TextOverflow.ellipsis),
                        ),
                      );
                    },
                  ),
          ),
          Row(
            children: [
              if (_checkedQuestionsCount != 0) Text('Выбрано $_checkedQuestionsCount', style: dialogSecondaryTextStyle),
              const Spacer(),
              Link(
                'Очистить',
                style: dialogSecondaryTextStyle.copyWith(color: MainTheme.neural),
                onPressed: _isLoading ? null : () async => setState(() => _questionCheckStates?.updateAll((key, value) => false)),
              ),
            ],
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    _questionsStreamSubscription?.cancel();
    super.dispose();
  }
}

class DetailTicketDialog extends StatefulWidget {
  const DetailTicketDialog({super.key, required this.examUid, required this.ticket});

  final String examUid;
  final Ticket ticket;

  @override
  MountedState<DetailTicketDialog> createState() => _DetailTicketDialogState();
}

class _DetailTicketDialogState extends MountedState<DetailTicketDialog> {
  final ExpandableController _expandableController = ExpandableController(initialExpanded: false);

  String? _error;
  bool _isLoading = false;
  bool _isEditMode = false;

  List<Question>? _questions;
  StreamSubscription? _questionsStreamSubscription;
  Map<String, bool>? _questionCheckStates;

  int get _checkedQuestionsCount => _questionCheckStates!.values.where((state) => state == true).length;

  void _toEditMode() {
    _expandableController.expanded = true;
    _isEditMode = true;
    updateState();
  }

  Future<void> _updateTicket() async {
    setState(() => _isLoading = true);
    try {
      Set<String> questionUids = {
        for (Question question in _questions!)
          if (_questionCheckStates![question.uid] ?? false) question.uid
      };
      if (!setEquals(questionUids, widget.ticket.questionUids)) {
        await Tickets.of(widget.examUid).update(
          widget.ticket.uid,
          questionUids: questionUids,
        );
      }
    } on FirebaseException catch (e) {
      _error = e.code;
    }
    if (mounted) context.pop();
  }

  Future<void> _onChangedCheckState(bool? state, Question question) async {
    if (_questionCheckStates![question.uid] == state) return;
    _questionCheckStates![question.uid] = state ?? false;
    if (_checkedQuestionsCount == 0) {
      _error = 'Билет будет удален';
    } else {
      _error = null;
    }
    updateState();
  }

  @override
  void initState() {
    super.initState();
    _questionCheckStates = {};
    // questions stream
    _questionsStreamSubscription = Questions.of(widget.examUid).streamAll().listen((snapshot) async {
      _questions = snapshot.docs.map((doc) {
        _questionCheckStates![doc.id] = _questionCheckStates!.get(doc.id) ?? widget.ticket.questionUids.contains(doc.id);
        return Question.fromDocument(doc);
      }).toList();
      updateState();
    });
  }

  @override
  Widget build(BuildContext context) {
    return BaseTicketDialog(
      title: 'Билет ${widget.ticket.index + 1}',
      subtitle: _isEditMode ? 'Выберите вопросы из списка' : null,
      error: _error,
      isLoading: _isLoading,
      canSubmit: true,
      onSubmit: _isEditMode ? _updateTicket : _toEditMode,
      submitChild: _error != null ? Text('Удалить', style: TextStyle(color: errorColor(context))) : Text(_isEditMode ? 'Сохранить' : 'Изменить'),
      body: ExpandablePanel(
        theme: const ExpandableThemeData(
          tapBodyToCollapse: false,
          tapBodyToExpand: false,
          tapHeaderToExpand: false,
        ),
        controller: _expandableController,
        collapsed: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            AnimatedListView(
              shrinkWrap: true,
              isSameItem: (a, b) => a.uid == b.uid,
              items: widget.ticket.questions,
              itemBuilder: (context, index) {
                Question question = widget.ticket.questions[index];
                return KeyedSubtree(
                  key: ValueKey('question${question.uid}OfTicket${widget.ticket.uid}Item'),
                  child: Text('${question.index + 1}. ${question.text}', style: const TextStyle(fontSize: 16)),
                );
              },
            ),
          ],
        ),
        expanded: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              constraints: const BoxConstraints(maxHeight: 300),
              padding: const EdgeInsets.all(8),
              decoration: BoxDecoration(
                color: adaptiveColor(context, Colors.white54, Colors.black38),
                borderRadius: BorderRadius.circular(8),
              ),
              child: _questions == null
                  ? const Center(child: CircularProgressIndicator())
                  : AnimatedListView(
                      isSameItem: (a, b) => a.uid == b.uid,
                      items: _questions!,
                      itemBuilder: (context, index) {
                        Question question = _questions![index];
                        return KeyedSubtree(
                          key: ValueKey('question${question.uid}CheckboxTileItem'),
                          child: CheckboxTile(
                            value: _questionCheckStates![question.uid]!,
                            onChanged: (state) async => _onChangedCheckState(state, question),
                            subchild: Text('${question.index + 1}. ', style: const TextStyle(fontSize: 16)),
                            child: Text(question.text, style: const TextStyle(fontSize: 16), maxLines: 2, overflow: TextOverflow.ellipsis),
                          ),
                        );
                      },
                    ),
            ),
            if (_checkedQuestionsCount != 0) Text('Выбрано $_checkedQuestionsCount', style: dialogSecondaryTextStyle),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _questionsStreamSubscription?.cancel();
    super.dispose();
  }
}

class BaseTicketDialog extends StatelessWidget {
  const BaseTicketDialog({
    super.key,
    required this.body,
    required this.title,
    this.subtitle,
    this.error,
    required this.isLoading,
    required this.canSubmit,
    required this.submitChild,
    required this.onSubmit,
  });

  final Widget body;
  final String title;
  final String? subtitle;
  final String? error;
  final bool isLoading;
  final bool canSubmit;

  final Widget submitChild;
  final void Function() onSubmit;

  @override
  Widget build(BuildContext context) {
    return BaseDialog(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: dialogTitleTextStyle),
          if (subtitle != null) Text(subtitle!, style: dialogSubtitleTextStyle),
          smallVDivider,
          body,
          ErrorText(error),
          mediumVDivider,
          SizedBox(
            width: double.infinity,
            child: isLoading
                ? const Center(child: CircularProgressIndicator())
                : CircularBorderButton(
                    onPressed: canSubmit ? onSubmit : null,
                    child: submitChild,
                  ),
          ),
        ],
      ),
    );
  }
}
