import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/pages/auth/login_page.dart';
import 'package:s8_dmss_cw/pages/home_page.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';

FutureOr<String?> needLoginRedirect(BuildContext context, GoRouterState state) {
  User? user = FirebaseAuth.instance.currentUser;
  return user == null || user.isAnonymous ? LoginPage.routePath : null;
}

Future<String?> needLogoutRedirect(BuildContext context, GoRouterState state) async {
  User? user = FirebaseAuth.instance.currentUser;
  return user != null && !user.isAnonymous ? HomePage.routePath : null;
}

Future<String?> needToBeExamOwnerRedirect(BuildContext context, GoRouterState state) async {
  User? user = FirebaseAuth.instance.currentUser;
  if (user == null || user.isAnonymous) return LoginPage.routePath;
  if (!state.pathParameters.containsKey('uid')) return HomePage.routePath;
  if (!await Exams.of(user.uid).contains(state.pathParameters['uid']!)) return HomePage.routePath;
  return null;
}
