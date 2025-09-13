import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/auth/need_auth.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/utils/functions.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/other/error_text.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/pages/exams/detail_exam_page.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';

class CreateExamPage extends StatefulWidget {
  const CreateExamPage({super.key});

  static const String routeName = 'exam_create';
  static const String routePath = '/exam/create';

  @override
  MountedState<CreateExamPage> createState() => _CreateExamPageState();
}

class _CreateExamPageState extends MountedState<CreateExamPage> {
  User user = FirebaseAuth.instance.currentUser!;

  // controllers
  final Map<String, TextEditingController> _controllers = {
    'title': TextEditingController(),
    'teacher': TextEditingController(),
    'discipline': TextEditingController(),
    'description': TextEditingController(),
  };

  final Map<String, String?> _errors = {
    'form': null,
    'title': null,
  };

  bool get _canSubmit => _errors.values.every((et) => et == null);

  Future<bool> _validateForm() async {
    if (_controllers['title']!.text.isEmpty) {
      _errors['title'] = 'Обязательное поле';
      return false;
    }
    return true;
  }

  Future<void> _createExam() async {
    if (!await _validateForm()) {
      updateState();
      return;
    }
    if (mounted) showLoadingDialog(context);
    try {
      DateTime now = DateTime.now();
      var ref = await Exams.of(user.uid).create(
        Exam.sample(
          userUid: user.uid,
          title: _controllers['title']!.text,
          teacher: _controllers['teacher']!.text,
          discipline: _controllers['discipline']!.text,
          description: _controllers['description']!.text,
          created: now,
          modified: now,
        ),
      );
      if (ref == null) return;
      if (mounted) {
        context.pushNamed(DetailExamPage.routeName, pathParameters: {'uid': ref.id});
        pushSnackBarMessage(context, 'Зачет успешно создан');
      }
    } on FirebaseException catch (e) {
      _errors['form'] = e.code;
    }
    if (mounted) context.pop();
    updateState();
  }

  @override
  Widget build(BuildContext context) {
    return CenteredBodyScaffold(
      floatingActionButton: const ToggleThemeFab(),
      maxWidth: 800,
      body: NeedAuth(
        child: Form(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const SizedBox(width: double.infinity),
              // title
              const Text(
                'Создание зачета',
                style: logoTextStyle,
              ),
              const Text(
                'Начать проведение зачета вы сможете после его создания',
                style: subtitleTextStyle,
              ),
              ErrorText(_errors['form']),
              mediumVDivider,
              // exam title field
              RoundedTextField(
                controller: _controllers['title'],
                decoration: InputDecoration(
                  hintText: 'Название',
                  errorText: _errors['title'],
                ),
                onChanged: (_) async => setState(() => _errors['title'] = null),
              ),
              mediumVDivider,
              const Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text(
                    'Дополнительная информация ',
                    style: titleTextStyle,
                  ),
                  Padding(
                    padding: EdgeInsets.only(bottom: 4),
                    child: Text('необязательно', style: secondaryTextStyle),
                  ),
                ],
              ),
              // description field
              mediumVDivider,
              Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Expanded(
                    // teacher field
                    child: RoundedTextField(
                      controller: _controllers['teacher'],
                      decoration: const InputDecoration(hintText: 'Преподаватель'),
                    ),
                  ),
                  smallHDivider,
                  Expanded(
                    // discipline field
                    child: RoundedTextField(
                      controller: _controllers['discipline'],
                      decoration: const InputDecoration(hintText: 'Дисциплина'),
                    ),
                  ),
                ],
              ),
              smallVDivider,
              RoundedTextField(
                controller: _controllers['description'],
                minLines: 2,
                maxLines: 5,
                decoration: const InputDecoration(hintText: 'Описание'),
              ),
              // create exam button
              groupVDivider,
              SizedBox(
                width: double.infinity,
                child: CircularBorderButton(
                  onPressed: _canSubmit ? _createExam : null,
                  child: const Row(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Padding(
                        padding: EdgeInsets.only(right: 4, left: 8),
                        child: Text('Продолжить', style: TextStyle(fontWeight: FontWeight.bold)),
                      ),
                      Icon(Icons.arrow_forward_ios_rounded),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  @override
  void dispose() {
    disposeControllers(_controllers.values);
    super.dispose();
  }
}
