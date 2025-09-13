import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/utils/functions.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/other/error_text.dart';
import 'package:s8_dmss_cw/widgets/other/logo_title.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/pages/home_page.dart';
import 'package:s8_dmss_cw/pages/auth/register_page.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  static const String routeName = 'login';
  static const String routePath = '/auth/login';

  @override
  MountedState<LoginPage> createState() => LoginPageState();
}

class LoginPageState extends MountedState<LoginPage> {
  // controllers
  final Map<String, TextEditingController> _controllers = {
    'email': TextEditingController(),
    'password': TextEditingController(),
  };

  String? _error;
  bool _passwordIsObscure = true;

  Future<bool> _validateForm() async {
    // validate required
    if (_controllers.values.any((c) => c.text.isEmpty)) {
      _error = 'Укажите данные для входа';
      return false;
    }
    return true;
  }

  Future<void> _loginUser() async {
    if (!await _validateForm()) {
      updateState();
      return;
    }
    if (mounted) showLoadingDialog(context);
    try {
      await FirebaseAuth.instance.signInWithEmailAndPassword(
        email: _controllers['email']!.text,
        password: _controllers['password']!.text,
      );
      if (mounted) context.pushNamed(HomePage.routeName);
    } on FirebaseAuthException catch (e) {
      _error = switch (e.code) {
        'invalid-email' || 'invalid-credential' => 'Неверные логин или пароль',
        _ => e.code,
      };
    }
    if (mounted) context.pop();
    updateState();
  }

  @override
  Widget build(BuildContext context) {
    return CenteredBodyScaffold(
      canBack: false,
      floatingActionButton: const ToggleThemeFab(),
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          const SizedBox(width: double.infinity),
          // title
          const LogoTitle(),
          const Text('Войдите, чтобы продолжить', style: titleTextStyle),
          ErrorText(_error),
          groupVDivider,
          // email field
          CircularTextField(
            controller: _controllers['email'],
            autoTrim: true,
            decoration: const InputDecoration(
              hintText: 'Почта',
              prefixIcon: Icon(Icons.email),
            ),
          ),
          // password field
          mediumVDivider,
          CircularTextField(
            controller: _controllers['password'],
            autoTrim: true,
            obscureText: _passwordIsObscure,
            decoration: InputDecoration(
              hintText: 'Пароль',
              prefixIcon: const Icon(Icons.lock),
              suffixIcon: IconButton(
                onPressed: () async => setState(() => _passwordIsObscure = !_passwordIsObscure),
                icon: Icon(!_passwordIsObscure ? Icons.visibility : Icons.visibility_off),
              ),
            ),
          ),
          // login button
          groupVDivider,
          SizedBox(
            width: double.infinity,
            child: CircularBorderButton(
              onPressed: _loginUser,
              child: const Row(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Padding(
                    padding: EdgeInsets.only(right: 4, left: 8),
                    child: Text('Войти', style: TextStyle(fontWeight: FontWeight.bold)),
                  ),
                  Icon(Icons.arrow_forward_ios_rounded),
                ],
              ),
            ),
          ),
          groupVDivider,
          // go to registration
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const Text('Нет аккаунта? ', style: TextStyle(fontSize: 16)),
              Link(
                'Зарегистрируйтесь',
                onPressed: () => context.pushNamed(RegisterPage.routeName),
              ),
            ],
          ),
        ],
      ),
    );
  }

  @override
  void dispose() {
    disposeControllers(_controllers.values);
    super.dispose();
  }
}
