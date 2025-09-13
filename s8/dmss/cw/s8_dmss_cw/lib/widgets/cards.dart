import 'package:animated_reorderable_list/animated_reorderable_list.dart';
import 'package:expandable/expandable.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/firebase/passes.dart';
import 'package:s8_dmss_cw/firebase/questions.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/firebase/tickets.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/pages/exams/detail_exam_page.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/datetime.dart';
import 'package:s8_dmss_cw/utils/functions.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';

class ExamCard extends StatelessWidget {
  const ExamCard({super.key, required this.exam});

  final Exam exam;

  @override
  Widget build(BuildContext context) {
    return Theme(
      data: ThemeData.dark(),
      child: Card(
        clipBehavior: Clip.hardEdge,
        color: MainTheme.primary,
        child: InkWell(
          hoverColor: adaptiveColor(context, Colors.black.withAlpha(10), Colors.white10),
          splashColor: adaptiveColor(context, Colors.black.withAlpha(10), Colors.white10),
          onTap: () {
            context.pushNamed(DetailExamPage.routeName, pathParameters: {'uid': exam.uid});
          },
          child: Padding(
            padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
            child: Column(
              mainAxisSize: MainAxisSize.max,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  exam.title,
                  style: const TextStyle(fontSize: 24),
                  overflow: TextOverflow.ellipsis,
                  maxLines: 4,
                ),
                const Spacer(),
                Row(
                  children: [
                    const Icon(Icons.my_library_books_rounded, size: 32),
                    mediumHDivider,
                    if (exam.discipline.isNotEmpty)
                      Expanded(
                        child: Align(
                          alignment: Alignment.centerRight,
                          child: Chip(
                            mouseCursor: SystemMouseCursors.click,
                            shape: RoundedRectangleBorder(borderRadius: circularBorderRadius),
                            side: BorderSide.none,
                            label: Text(
                              exam.discipline,
                              style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
                              overflow: TextOverflow.fade,
                            ),
                          ),
                        ),
                      ),
                  ],
                ),
                mediumVDivider,
                Row(
                  children: [
                    SelectableText(
                      dFormat.format((exam.modified ?? exam.created)),
                      style: const TextStyle(
                        color: Colors.white,
                        fontSize: 17,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    mediumHDivider,
                    if (exam.teacher.isNotEmpty)
                      Expanded(
                        child: Align(
                          alignment: Alignment.centerRight,
                          child: SelectableText(
                            exam.teacher,
                            style: const TextStyle(
                              color: Colors.white,
                              fontSize: 17,
                              fontWeight: FontWeight.bold,
                            ),
                            textAlign: TextAlign.right,
                          ),
                        ),
                      ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class TicketCard extends StatefulWidget {
  const TicketCard({super.key, required this.examUid, required this.ticket});

  final String examUid;
  final Ticket ticket;

  @override
  MountedState<TicketCard> createState() => _TicketCardState();
}

class _TicketCardState extends MountedState<TicketCard> {
  bool _isHovered = false;

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.zero,
      clipBehavior: Clip.hardEdge,
      child: MouseRegion(
        onEnter: (_) {
          if (_isHovered) return;
          setState(() => _isHovered = true);
        },
        onExit: (_) {
          if (!_isHovered) return;
          setState(() => _isHovered = false);
        },
        child: InkWell(
          hoverColor: adaptiveColor(context, Colors.black.withAlpha(10), Colors.white10),
          splashColor: adaptiveColor(context, Colors.black.withAlpha(10), Colors.white10),
          onTap: () async => showDetailTicketDialog(context, examUid: widget.examUid, ticket: widget.ticket),
          child: Padding(
            padding: const EdgeInsets.fromLTRB(24, 12, 16, 20),
            child: Column(
              mainAxisSize: MainAxisSize.max,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    const Icon(Icons.list_alt_rounded, size: 24),
                    smallHDivider,
                    Expanded(
                      child: Padding(
                        padding: const EdgeInsets.only(top: 2),
                        child: Text(
                          widget.ticket.title,
                          style: const TextStyle(fontSize: 20),
                        ),
                      ),
                    ),
                    AnimatedOpacity(
                      duration: Durations.short2,
                      opacity: _isHovered ? 1 : 0,
                      child: IconButton(
                        icon: Icon(Icons.delete_rounded, color: errorColor(context)),
                        onPressed: () async {
                          showConfirmDialog(
                            context,
                            title: 'Удалить ${widget.ticket.title}?',
                            subtitle: 'Данное действие необратимо',
                            onConfirm: () => Tickets.of(widget.examUid).delete(widget.ticket.uid),
                          );
                        },
                      ),
                    ),
                  ],
                ),
                AnimatedListView(
                  shrinkWrap: true,
                  isSameItem: (a, b) => a.uid == b.uid,
                  items: widget.ticket.questions,
                  itemBuilder: (context, index) {
                    Question question = widget.ticket.questions[index];
                    return KeyedSubtree(
                      key: ValueKey('question${question.uid}OfTicket${widget.ticket.uid}Item'),
                      child: Text(
                        '${question.index + 1}. ${question.text}',
                        style: const TextStyle(fontSize: 16),
                      ),
                    );
                  },
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}

class SessionCard extends StatelessWidget {
  const SessionCard({super.key, required this.examUid, required this.session});

  final String examUid;
  final Session session;

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: EdgeInsets.zero,
      clipBehavior: Clip.hardEdge,
      child: InkWell(
        hoverColor: adaptiveColor(context, Colors.black.withAlpha(10), Colors.white10),
        splashColor: adaptiveColor(context, Colors.black.withAlpha(10), Colors.white10),
        onTap: () async => showDetailSessionDialog(context, examUid: examUid, session: session),
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
          child: Column(
            mainAxisSize: MainAxisSize.max,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  SelectableText(session.uid, style: secondaryTextStyle),
                  const Icon(Icons.arrow_forward_ios_rounded, size: 13, color: MainTheme.neural),
                ],
              ),
              Row(
                children: [
                  AnimatedSize(
                    duration: Durations.short4,
                    child: Icon(
                      Icons.circle,
                      color: MainTheme.primary,
                      size: session.isActive ? 14 : 0,
                    ),
                  ),
                  if (session.isActive) const SizedBox(width: 6),
                  Text(session.groupName, style: const TextStyle(fontSize: 24)),
                ],
              ),
              Text(
                verboseCount(session.students.length, single: 'студент', miltiple: 'студентов', from2to4: 'студента'),
                style: subtitleTextStyle,
              ),
              const Spacer(),
              Text(session.untilStartF),
              Text(session.untilEndF),
            ],
          ),
        ),
      ),
    );
  }
}

// class PassTicketCard extends StatelessWidget {
//   const PassTicketCard({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return Card(
//       margin: const EdgeInsets.only(top: 24),
//       child: Padding(
//         padding: const EdgeInsets.fromLTRB(36, 30, 36, 36),
//         child: Column(
//           children: [
//             Row(
//               children: [
//                 const Icon(Icons.list_alt_rounded, size: 36),
//                 smallHDivider,
//                 Text(_ticket!.title, style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold)),
//                 const Spacer(),
//                 if (!_passSubmited)
//                   SlideCountdown(
//                     streamDuration: _streamDuration,
//                     padding: const EdgeInsets.all(8),
//                     style: const TextStyle(fontSize: 22),
//                     decoration: BoxDecoration(
//                       color: adaptiveColor(context, Colors.black12, Colors.black26),
//                       borderRadius: BorderRadius.circular(8),
//                     ),
//                   ),
//               ],
//             ),
//             smallVDivider,
//             ListView.builder(
//               shrinkWrap: true,
//               itemCount: _ticket!.questions.length,
//               itemBuilder: (context, index) {
//                 Question question = _ticket!.questions[index];
//                 return Column(
//                   crossAxisAlignment: CrossAxisAlignment.start,
//                   children: [
//                     Text(
//                       '${index + 1}. ${question.text}',
//                       style: const TextStyle(fontSize: 20),
//                     ),
//                     RoundedTextField(
//                       controller: _answerControllers![question.uid],
//                       minLines: 3,
//                       maxLines: 5,
//                       readOnly: _passSubmited,
//                       decoration: InputDecoration(
//                         filled: true,
//                         fillColor: adaptiveColor(context, Colors.white30, Colors.black12),
//                         hintText: _passSubmited ? 'Ответ не предоставлен' : 'Введите ответ на вопрос',
//                       ),
//                       onEditingComplete: () async {
//                         Passes.of(widget.sessionUid).send(_pass!.uid, _answers);
//                       },
//                     ),
//                     mediumVDivider,
//                   ],
//                 );
//               },
//             ),
//           ],
//         ),
//       ),
//     );
//   }
// }

class PassResultCard extends StatelessWidget {
  const PassResultCard({
    super.key,
    required this.studentKey,
    required this.studentName,
    required this.pass,
    required this.ticket,
  });

  final String studentKey;
  final String studentName;
  final Pass? pass;
  final Ticket? ticket;

  @override
  Widget build(BuildContext context) {
    return Card(
      clipBehavior: Clip.hardEdge,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(width: double.infinity),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  flex: 8,
                  child: Text(studentName, style: subtitleTextStyle.copyWith(color: adaptiveColor(context))),
                ),
                Expanded(
                  flex: 2,
                  child: Align(
                    alignment: Alignment.centerRight,
                    child: SelectableText(studentKey, style: subtitleTextStyle), // studentKey // WWWWWWWW
                  ),
                ),
              ],
            ),
            pass == null
                ? const Text('еще не приступил(а)', style: secondaryTextStyle)
                : Column(
                    mainAxisSize: MainAxisSize.min,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          Text('начал(а) ${prettyDateTime(pass!.started)}', style: secondaryTextStyle),
                          if (pass!.submited != null) Text('  |  закончил(а) ${prettyDateTime(pass!.submited!)}', style: secondaryTextStyle),
                        ],
                      ),
                      smallVDivider,
                      ExpandablePanel(
                        theme: ExpandableThemeData(
                          iconColor: adaptiveColor(context),
                        ),
                        header: Padding(
                          padding: const EdgeInsets.only(top: 4),
                          child: Text(
                            ticket!.title,
                            style: const TextStyle(
                              fontSize: 22,
                              fontWeight: FontWeight.bold,
                            ),
                          ),
                        ),
                        collapsed: const SizedBox.shrink(),
                        expanded: ListView.builder(
                          shrinkWrap: true,
                          itemCount: ticket!.questions.length,
                          itemBuilder: (context, index) {
                            Question question = ticket!.questions[index];
                            return Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  '${index + 1}. ${question.text}',
                                  style: const TextStyle(fontSize: 20),
                                ),
                                RoundedTextField(
                                  controller: TextEditingController(text: pass!.answers[question.uid]),
                                  minLines: 3,
                                  maxLines: 5,
                                  readOnly: true,
                                  decoration: InputDecoration(
                                    filled: true,
                                    fillColor: adaptiveColor(context, Colors.white30, Colors.black12),
                                    hintText: 'Ответ не предоставлен',
                                  ),
                                ),
                                mediumVDivider,
                              ],
                            );
                          },
                        ),
                      ),
                    ],
                  ),
          ],
        ),
      ),
    );
  }
}
