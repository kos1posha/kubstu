import 'dart:async';

import 'package:animated_reorderable_list/animated_reorderable_list.dart';
import 'package:expandable/expandable.dart';
import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/firebase/tickets.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/widgets/cards.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';

class SessionsExpandablePanel extends StatefulWidget {
  const SessionsExpandablePanel({
    super.key,
    required this.examUid,
    required this.outerScrollController,
    required this.innerScrollController,
  });

  final String examUid;

  final ScrollController outerScrollController;
  final ScrollController innerScrollController;

  @override
  MountedState<SessionsExpandablePanel> createState() => _SessionsExpandablePanelState();
}

class _SessionsExpandablePanelState extends MountedState<SessionsExpandablePanel> {
  late final ExpandableController _expandableController = ExpandableController();

  List<Session>? _sessions;
  StreamSubscription? _sessionsStreamSubscription;
  List<Ticket>? _tickets;
  StreamSubscription? _ticketsStreamSubscription;

  @override
  void initState() {
    super.initState();
    // _sessions stream
    _sessionsStreamSubscription = Sessions.of(widget.examUid).streamAll().listen((snapshot) async {
      _sessions = Session.fromDocuments(snapshot.docs);
      _expandableController.expanded = true;
      updateState();
    });
    // tickets stream
    _ticketsStreamSubscription = Tickets.of(widget.examUid).streamAll().listen((snapshot) async {
      _tickets = Ticket.fromDocuments(snapshot.docs);
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
                  'Зачетные сессии',
                  style: subtitleTextStyle.copyWith(fontWeight: FontWeight.bold),
                ),
                Text(
                  _sessions != null ? (_sessions!.isEmpty ? 'Пусто' : 'Всего ${_sessions!.length}') : 'Загрузка...',
                  style: secondaryTextStyle,
                ),
              ],
            ),
          ],
        ),
        collapsed: const SizedBox.shrink(),
        expanded: Listener(
          onPointerSignal: (event) {
            if (event is PointerScrollEvent) {
              widget.outerScrollController.jumpTo(widget.outerScrollController.offset - event.scrollDelta.dy);
              widget.innerScrollController.jumpTo(widget.innerScrollController.offset + event.scrollDelta.dy);
            }
          },
          child: SizedBox(
            height: 200,
            width: double.infinity,
            child: AnimatedListView(
              padding: const EdgeInsets.only(top: 4, bottom: 2),
              shrinkWrap: true,
              controller: widget.innerScrollController,
              scrollDirection: Axis.horizontal,
              isSameItem: (a, b) => a.uid == b.uid,
              items: [Session.sample()] + (_sessions ?? <Session>[]),
              itemBuilder: (context, index) {
                Session session = index == 0 ? Session.sample() : _sessions![index - 1];
                return KeyedSubtree(
                  key: ValueKey('session${session.uid}OfExam${widget.examUid}'),
                  child: Padding(
                    padding: EdgeInsets.only(left: index == 0 ? 0 : 8),
                    child: index == 0
                        ? ElevatedButton(
                            onPressed: () async {
                              if (_tickets!.isEmpty) {
                                pushSnackBarMessage(context, 'Для проведения зачета необходимы билеты');
                                return;
                              }
                              showCreateSessionDialog(context, examUid: widget.examUid);
                            },
                            style: ElevatedButton.styleFrom(
                              shape: RoundedRectangleBorder(borderRadius: roundedBorderRadius),
                            ),
                            child: const SizedBox(
                              width: 200,
                              child: Center(
                                child: Column(
                                  mainAxisAlignment: MainAxisAlignment.center,
                                  children: [
                                    Icon(Icons.edit_note_rounded, size: 48),
                                    Text(
                                      'Провести зачет',
                                      style: TextStyle(fontSize: 16),
                                      textAlign: TextAlign.center,
                                    ),
                                  ],
                                ),
                              ),
                            ),
                          )
                        : SizedBox(
                            width: 300,
                            child: SessionCard(examUid: widget.examUid, session: session),
                          ),
                  ),
                );
              },
            ),
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    _sessionsStreamSubscription?.cancel();
    _ticketsStreamSubscription?.cancel();
    super.dispose();
  }
}
