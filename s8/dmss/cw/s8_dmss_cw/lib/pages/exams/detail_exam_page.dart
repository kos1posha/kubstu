import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:flutter_expandable_fab/flutter_expandable_fab.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/auth/need_auth.dart';
import 'package:s8_dmss_cw/pages/exams/detail/actions_expandable_fab.dart';
import 'package:s8_dmss_cw/pages/exams/detail/main_info.dart';
import 'package:s8_dmss_cw/pages/exams/detail/questions_panel.dart';
import 'package:s8_dmss_cw/pages/exams/detail/sessions_panel.dart';
import 'package:s8_dmss_cw/pages/exams/detail/tickets_panel.dart';
import 'package:s8_dmss_cw/pages/home_page.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';

class DetailExamPage extends StatefulWidget {
  const DetailExamPage({super.key, required this.examUid});

  static const String routeName = 'exam';
  static const String routePath = '/exam/:uid';

  final String examUid;

  @override
  MountedState<DetailExamPage> createState() => _DetailExamPageState();
}

class _DetailExamPageState extends MountedState<DetailExamPage> {
  User get user => FirebaseAuth.instance.currentUser!;

  final ScrollController _pageScrollController = ScrollController();
  final ScrollController _sessionsScrollController = ScrollController();

  StreamSubscription? _examStreamSubscription;

  @override
  void initState() {
    super.initState();
    // exam stream
    _examStreamSubscription = Exams.of(user.uid).streamOne(widget.examUid).listen((snapshot) {
      if (!snapshot.exists && mounted) {
        context.pushReplacementNamed(HomePage.routeName);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return AdaptiveDrawerScaffold(
      scrollController: _pageScrollController,
      appBar: const MainAppBar(),
      endDrawer: const MainDrawer(),
      floatingActionButtonLocation: ExpandableFab.location,
      floatingActionButton: ExamActionsExpandableFab(userUid: user.uid, examUid: widget.examUid),
      body: NeedAuth(
        child: FutureBuilder(
          future: Exams.of(user.uid).contains(widget.examUid),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting || !snapshot.hasData) {
              return const Center(child: CircularProgressIndicator());
            } else {
              return Column(
                mainAxisSize: MainAxisSize.min,
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  ExamMainInfo(examUid: widget.examUid),
                  mediumVDivider,
                  SessionsExpandablePanel(
                    examUid: widget.examUid,
                    outerScrollController: _pageScrollController,
                    innerScrollController: _sessionsScrollController,
                  ),
                  mediumVDivider,
                  LayoutBuilder(
                    builder: (context, constraints) {
                      var children = [
                        ExamQuestionsExpandablePanel(
                          examUid: widget.examUid,
                          outerScrollController: _pageScrollController,
                        ),
                        ExamTicketsExpandablePanel(
                          examUid: widget.examUid,
                          outerScrollController: _pageScrollController,
                        ),
                      ];
                      if (constraints.maxWidth >= 900) {
                        return Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          spacing: 32,
                          children: [for (var child in children) Expanded(child: child)],
                        );
                      } else {
                        return Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          spacing: 16,
                          children: children,
                        );
                      }
                    },
                  ),
                ],
              );
            }
          },
        ),
      ),
    );
  }

  @override
  void dispose() {
    _examStreamSubscription?.cancel();
    _pageScrollController.dispose();
    _sessionsScrollController.dispose();
    super.dispose();
  }
}
