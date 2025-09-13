import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:flutter_expandable_fab/flutter_expandable_fab.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';
import 'package:s8_dmss_cw/pages/exams/detail_exam_page.dart';
import 'package:s8_dmss_cw/pages/home_page.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';

class ExamActionsExpandableFab extends StatelessWidget {
  const ExamActionsExpandableFab({super.key, required this.userUid, required this.examUid});

  final String userUid;
  final String examUid;

  @override
  Widget build(BuildContext context) {
    return ExpandableFab(
      type: ExpandableFabType.up,
      childrenAnimation: ExpandableFabAnimation.none,
      openButtonBuilder: RotateFloatingActionButtonBuilder(
        backgroundColor: MainTheme.primary,
        shape: const CircleBorder(),
        fabSize: ExpandableFabSize.regular,
        child: const Icon(Icons.more_horiz_rounded),
      ),
      closeButtonBuilder: DefaultFloatingActionButtonBuilder(
        backgroundColor: MainTheme.primary,
        shape: const CircleBorder(),
        fabSize: ExpandableFabSize.small,
        child: const Icon(Icons.close_rounded),
      ),
      distance: 56,
      children: [
        Row(
          children: [
            const Text('Удалить', style: TextStyle(color: Colors.redAccent, fontSize: 15, fontWeight: FontWeight.bold)),
            smallHDivider,
            FloatingActionButton.small(
              heroTag: null,
              backgroundColor: Colors.redAccent,
              onPressed: () async {
                showConfirmDialog(
                  context,
                  title: 'Вы уверены, что хотите удалить данный зачет?',
                  subtitle: 'Данное действие необратимо',
                  confirmText: examUid.s_(0, 12),
                  confirmHelpText: 'Введите первые 12 символов ключа зачета',
                  onConfirm: () async {
                    context.goNamed(HomePage.routeName);
                    await Exams.of(userUid).delete(examUid);
                    if (context.mounted) pushSnackBarMessage(context, 'Зачет успешно удален');
                  },
                );
              },
              child: const Icon(Icons.delete_rounded),
            ),
          ],
        ),
        Row(
          children: [
            const Text('Копировать', style: TextStyle(color: MainTheme.secondary, fontSize: 15, fontWeight: FontWeight.bold)),
            smallHDivider,
            FloatingActionButton.small(
              heroTag: null,
              backgroundColor: MainTheme.secondary,
              onPressed: () async {
                showConfirmDialog(
                  context,
                  title: 'Coздать копию данного зачета?',
                  subtitle: 'Копия будет иметь уникальный ключ и не будет включать зачетные сесии',
                  subtitleColor: MainTheme.neural,
                  confirmColor: adaptiveColor(context),
                  cancelColor: errorColor(context),
                  onConfirm: () async {
                    DocumentReference? docRef = await Exams.of(userUid).copy(examUid);
                    if (docRef == null) return;
                    if (context.mounted) {
                      context.pushNamed(DetailExamPage.routeName, pathParameters: {'uid': docRef.id});
                      pushSnackBarMessage(context, 'Зачет успешно скопирован');
                    }
                  },
                );
              },
              child: const Icon(Icons.copy_rounded),
            ),
          ],
        ),
      ],
    );
  }
}
