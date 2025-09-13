import 'package:email_validator/email_validator.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/utils/functions.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/other/error_text.dart';
import 'package:s8_dmss_cw/widgets/other/password_hint.dart';
import 'package:s8_dmss_cw/widgets/scaffolds.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/pages/home_page.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/pages/auth/login_page.dart';

class RegisterPage extends StatefulWidget {
  const RegisterPage({super.key});

  static const String routeName = 'register';
  static const String routePath = '/auth/register';

  @override
  MountedState<RegisterPage> createState() => RegisterPageState();
}

class RegisterPageState extends MountedState<RegisterPage> {
  // controllers
  final Map<String, TextEditingController> _controllers = {
    'email': TextEditingController(),
    'password': TextEditingController(),
    'passwordConfirm': TextEditingController(),
  };

  final Map<String, String?> _errors = {
    'form': null,
    'email': null,
    'password': null,
    'passwordConfirm': null,
  };

  bool get _canSubmit => _errors.values.every((et) => et == null);

  Future<bool> _validateForm() async {
    bool isValid = true;
    // validate required
    for (String key in _controllers.keys) {
      if (_controllers[key]!.text == '') {
        _errors[key] = 'Обязательное поле';
        isValid = false;
      }
    }
    if (!isValid) return false;
    // validate email
    if (!EmailValidator.validate(_controllers['email']!.text)) {
      _errors['email'] = 'Неверный формат почты';
      isValid = false;
    }
    // validate password
    if (!_pwRule8MinLength || !_pwRuleNoSpace || !_pwRuleNoSpecialCharacters) {
      _errors['password'] = 'Неверный формат пароля. Нажмите для большей информации';
      _errors['passwordConfirm'] = null;
      return false;
    }
    // validate password confirm
    if (_controllers['passwordConfirm']!.text != _controllers['password']!.text) {
      _errors['passwordConfirm'] = 'Пароли не совпадают';
      return false;
    }
    return isValid;
  }

  Future<void> _registerUser() async {
    if (!await _validateForm()) {
      updateState();
      return;
    }
    if (mounted) showLoadingDialog(context);
    try {
      await FirebaseAuth.instance.createUserWithEmailAndPassword(
        email: _controllers['email']!.text,
        password: _controllers['password']!.text,
      );
      if (mounted) context.pushNamed(HomePage.routeName);
    } on FirebaseAuthException catch (e) {
      switch (e.code) {
        case 'email-already-in-use':
          _errors['email'] = 'Данный почтовый адрес уже используется';
        case _:
          _errors['form'] = e.code;
      }
    }
    if (mounted) context.pop();
    updateState();
  }

  // password rules
  bool _pwRule8MinLength = false;
  bool _pwRuleNoSpace = false;
  bool _pwRuleNoSpecialCharacters = false;

  void _checkPwRules() {
    final String password = _controllers['password']!.text;
    _pwRule8MinLength = password.length >= 8;
    _pwRuleNoSpace = !password.contains(' ');
    _pwRuleNoSpecialCharacters = !password.contains(specialCharactersRegExp);
  }

  @override
  void initState() {
    super.initState();
    _checkPwRules();
    _controllers['password']!.addListener(_checkPwRules);
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
          const Row(
            mainAxisSize: MainAxisSize.min,
            children: [
              Icon(Icons.list_alt, color: MainTheme.primary, size: 52),
              smallHDivider,
              Text('Зачет Онлайн', style: logoTextStyle),
            ],
          ),
          const Text('Форма регистрации', style: titleTextStyle),
          ErrorText(_errors['form']),
          groupVDivider,
          // email field
          CircularTextField(
            controller: _controllers['email']!,
            autoTrim: true,
            decoration: InputDecoration(
              hintText: 'Укажите почту',
              errorText: _errors['email'],
              prefixIcon: const Icon(Icons.email),
            ),
            onChanged: (_) async => setState(() => _errors['email'] = null),
          ),
          // password field
          mediumVDivider,
          PasswordHint(
            bottomOffset: _errors['password'] == null ? 68 : 88,
            rules: [
              PasswordRule(
                'Не меньше 8 символов',
                state: _pwRule8MinLength,
              ),
              PasswordRule(
                'Не используйте пробел',
                state: _pwRuleNoSpace,
              ),
              PasswordRule(
                'Не используйте специальные символы\n$specialCharacters',
                state: _pwRuleNoSpecialCharacters,
              ),
            ],
            child: CircularTextField(
              controller: _controllers['password']!,
              autoTrim: true,
              obscureText: true,
              decoration: InputDecoration(
                hintText: 'Придумайте пароль',
                errorText: _errors['password'],
                prefixIcon: const Icon(Icons.lock),
              ),
              onChanged: (_) async => setState(() => _errors['password'] = null),
            ),
          ),
          // confirm password field
          mediumVDivider,
          CircularTextField(
            controller: _controllers['passwordConfirm']!,
            autoTrim: true,
            obscureText: true,
            decoration: InputDecoration(
              hintText: 'Подтвердите пароль',
              errorText: _errors['passwordConfirm'],
              prefixIcon: const Icon(Icons.lock_reset_rounded),
            ),
            onChanged: (_) async => setState(() => _errors['passwordConfirm'] = null),
          ),
          // register
          groupVDivider,
          SizedBox(
            width: double.infinity,
            child: CircularBorderButton(
              onPressed: _canSubmit ? _registerUser : null,
              child: const Text('Зарегистрироваться', style: TextStyle(fontWeight: FontWeight.bold)),
            ),
          ),
          // go to login
          groupVDivider,
          Row(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              const Text('Уже есть аккаунт? ', style: TextStyle(fontSize: 16)),
              Link(
                'Войдите',
                onPressed: () {
                  if (context.canPop()) {
                    context.pop();
                  } else {
                    context.pushNamed(LoginPage.routeName);
                  }
                },
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
