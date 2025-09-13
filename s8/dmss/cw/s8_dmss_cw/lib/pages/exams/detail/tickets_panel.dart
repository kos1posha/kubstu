import 'dart:async';

import 'package:animated_reorderable_list/animated_reorderable_list.dart';
import 'package:expandable/expandable.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/firebase/questions.dart';
import 'package:s8_dmss_cw/firebase/tickets.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/cards.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';

class ExamTicketsExpandablePanel extends StatefulWidget {
  const ExamTicketsExpandablePanel({
    super.key,
    required this.examUid,
    required this.outerScrollController,
  });

  final String examUid;
  final ScrollController outerScrollController;

  @override
  MountedState<ExamTicketsExpandablePanel> createState() => _ExamTicketsExpandablePanelState();
}

class _ExamTicketsExpandablePanelState extends MountedState<ExamTicketsExpandablePanel> {
  late final ExpandableController _expandableController = ExpandableController();

  List<Ticket>? _tickets;
  StreamSubscription? _ticketsStreamSubscription;
  List<Question>? _questions;
  StreamSubscription? _questionsStreamSubscription;

  Future<void> _putQuestions(List<Ticket>? tickets, List<Question>? questions) async {
    if (tickets == null || questions == null) return;
    for (Ticket ticket in _tickets!) {
      ticket.putQuestions(_questions!);
      if (ticket.questions.isEmpty) {
        Tickets.of(widget.examUid).delete(ticket.uid);
      }
    }
    updateState();
  }

  @override
  void initState() {
    super.initState();
    // tickets stream
    _ticketsStreamSubscription = Tickets.of(widget.examUid).streamAll().listen((snapshot) async {
      _tickets = Ticket.fromDocuments(snapshot.docs);
      _expandableController.expanded = true;
      _putQuestions(_tickets, _questions);
    });
    // questions stream
    _questionsStreamSubscription = Questions.of(widget.examUid).streamAll().listen((snapshot) async {
      _questions = Question.fromDocuments(snapshot.docs);
      _putQuestions(_tickets, _questions);
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
        theme: ExpandableThemeData(
          iconColor: Theme.of(context).brightness == Brightness.light ? Colors.black : Colors.white,
          iconSize: 30,
          iconPadding: const EdgeInsets.only(top: 8),
        ),
        controller: _expandableController,
        header: Row(
          children: [
            Column(
              mainAxisSize: MainAxisSize.min,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Стопка билетов',
                  style: subtitleTextStyle.copyWith(fontWeight: FontWeight.bold),
                ),
                Text(
                  _tickets != null ? (_tickets!.isEmpty ? 'Пусто' : 'Всего ${_tickets!.length}') : 'Загрузка...',
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
                    if (_tickets == null) return;
                    if (_tickets!.isEmpty) {
                      pushSnackBarMessage(context, 'Стопка билетов пуста');
                      return;
                    }
                    showConfirmDialog(
                      context,
                      title: 'Вы уверены, что хотите удалить все билеты данного зачета?',
                      subtitle: 'Данное действие необратимо',
                      onConfirm: () async {
                        await Tickets.of(widget.examUid).clear();
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
            SizedBox(
              width: double.infinity,
              child: CircularBorderButton(
                isRounded: true,
                onPressed: _questions == null
                    ? null
                    : () async {
                        if (_questions!.isEmpty) {
                          pushSnackBarMessage(context, 'Невозможно создать билет с пустым банком вопросов');
                          return;
                        }
                        showCreateTicketDialog(
                          context,
                          examUid: widget.examUid,
                          ticketIndex: _tickets?.length ?? 0,
                        );
                      },
                child: const Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(Icons.add_rounded, size: 28),
                    smallHDivider,
                    Text('Добавить билет'),
                  ],
                ),
              ),
            ),
            smallVDivider,
            LayoutBuilder(
              builder: (context, constraints) {
                return AnimatedReorderableListView(
                  shrinkWrap: true,
                  dragStartDelay: Durations.short2,
                  buildDefaultDragHandles: false,
                  clipBehavior: Clip.hardEdge,
                  isSameItem: (a, b) => a.uid == b.uid,
                  onReorder: (oldIndex, newIndex) {
                    _tickets!.insert(newIndex, _tickets!.removeAt(oldIndex));
                    Tickets.of(widget.examUid).move(oldIndex, newIndex);
                  },
                  insertItemBuilder: (child, animation) {
                    return child;
                  },
                  items: _tickets ?? <Ticket>[],
                  itemBuilder: (context, index) {
                    Ticket ticket = _tickets![index];
                    return KeyedSubtree(
                      key: ValueKey('ticket${ticket.uid}OfExam${widget.examUid}Item'),
                      child: Padding(
                        padding: EdgeInsets.only(bottom: index == _tickets!.length - 1 ? 0 : 8),
                        child: TicketCard(examUid: widget.examUid, ticket: ticket),
                      ),
                    );
                  },
                );
              },
            ),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _ticketsStreamSubscription?.cancel();
    _questionsStreamSubscription?.cancel();
    _expandableController.dispose();
    super.dispose();
  }
}
