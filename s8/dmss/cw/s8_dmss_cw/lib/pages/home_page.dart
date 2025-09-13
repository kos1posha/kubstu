import 'dart:async';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/auth/need_auth.dart';
import 'package:s8_dmss_cw/widgets/cards.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  static const String routeName = 'home';
  static const String routePath = '/';

  @override
  MountedState<HomePage> createState() => _HomePageState();
}

class _HomePageState extends MountedState<HomePage> {
  User user = FirebaseAuth.instance.currentUser!;

  // exams
  List<Exam> _exams = [];
  StreamSubscription? _examsStreamSubscription;

  bool _examsIsLoading = true;

  int _getExamsCrossAxisCount(double maxWidth) {
    if (maxWidth >= 1100) {
      return 3;
    } else if (maxWidth >= 600) {
      return 2;
    } else {
      return 1;
    }
  }

  @override
  void initState() {
    super.initState();
    // exams stream
    _examsStreamSubscription = Exams.of(user.uid).streamAll().listen((snapshot) async {
      setState(() => _examsIsLoading = true);
      _exams = Exam.fromDocuments(snapshot.docs);
      setState(() => _examsIsLoading = false);
    });
  }

  @override
  Widget build(BuildContext context) {
    return AdaptiveDrawerScaffold(
      appBar: const MainAppBar(),
      endDrawer: const MainDrawer(),
      body: NeedAuth(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            // const Text('Туда-сюда', style: titleTextStyle),
            // smallVDivider,
            // Wrap(
            //   spacing: 8,
            //   runSpacing: 8,
            //   children: [
            //     CircularBorderButton(
            //       onPressed: () => context.goNamed(LoginPage.routeName),
            //       child: const Text('Вход'),
            //     ),
            //     CircularBorderButton(
            //       onPressed: FirebaseAuth.instance.signOut,
            //       child: const Text('Выход'),
            //     ),
            //     CircularBorderButton(
            //       onPressed: () => context.goNamed(RegisterPage.routeName),
            //       child: const Text('Регистрация'),
            //     ),
            //     CircularBorderButton(
            //       onPressed: () async {
            //         showConfirmDialog(
            //           context,
            //           title: 'Да?',
            //           onConfirm: Exams.of(user.uid).clear,
            //         );
            //       },
            //       child: const Text('Очистить зачеты'),
            //     ),
            //   ],
            // ),
            // mediumVDivider,
            Row(
              children: [
                const Text('Ваши зачеты', style: titleTextStyle),
                smallHDivider,
                if (_examsIsLoading)
                  const SizedBox.square(
                    dimension: 16,
                    child: CircularProgressIndicator(strokeWidth: 3),
                  ),
              ],
            ),
            smallVDivider,
            if (!_examsIsLoading)
              _exams.isNotEmpty
                  ? LayoutBuilder(
                      builder: (context, constraints) {
                        return GridView.builder(
                          physics: const NeverScrollableScrollPhysics(),
                          shrinkWrap: true,
                          gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                            mainAxisExtent: 260,
                            crossAxisCount: _getExamsCrossAxisCount(constraints.maxWidth),
                            mainAxisSpacing: 8,
                            crossAxisSpacing: 8,
                          ),
                          itemCount: _exams.length,
                          itemBuilder: (context, index) => ExamCard(exam: _exams[index]),
                        );
                      },
                    )
                  : const Text('Вы не создали ни одного зачета', style: secondaryTextStyle),
          ],
        ),
      ),
    );
  }

  @override
  void dispose() {
    _examsStreamSubscription?.cancel();
    super.dispose();
  }
}
