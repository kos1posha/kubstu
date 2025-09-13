import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import 'package:s8_dmss_cw/pages/auth/login_page.dart';

class AuthService with ChangeNotifier {
  AuthService() {
    FirebaseAuth.instance.userChanges().listen((user) => notifyListeners());
  }
}

class NeedAuth extends StatelessWidget {
  const NeedAuth({super.key, required this.child});

  final Widget child;

  @override
  Widget build(BuildContext context) {
    Provider.of<AuthService>(context);
    User? user = FirebaseAuth.instance.currentUser;
    if (user != null && !user.isAnonymous) {
      return child;
    } else {
      context.goNamed(LoginPage.routeName);
      return const Center(child: CircularProgressIndicator());
    }
  }
}


