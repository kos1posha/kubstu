import 'dart:async';
import 'package:adaptive_theme/adaptive_theme.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_web_plugins/flutter_web_plugins.dart';
import 'package:go_router/go_router.dart';
import 'package:provider/provider.dart';
import 'package:s8_dmss_cw/auth/need_auth.dart';
import 'package:s8_dmss_cw/auth/redirects.dart';
import 'package:s8_dmss_cw/firebase/firebase_options.dart';
import 'package:s8_dmss_cw/pages/auth/login_page.dart';
import 'package:s8_dmss_cw/pages/auth/register_page.dart';
import 'package:s8_dmss_cw/pages/exams/detail_exam_page.dart';
import 'package:s8_dmss_cw/pages/exams/create_exam_page.dart';
import 'package:s8_dmss_cw/pages/home_page.dart';
import 'package:s8_dmss_cw/pages/sessions/open_session_page.dart';
import 'package:s8_dmss_cw/pages/sessions/pass_session_page.dart';
import 'package:s8_dmss_cw/pages/sessions/results_session_page.dart';
import 'package:s8_dmss_cw/pages/settings_page.dart';
import 'package:s8_dmss_cw/theme.dart';

Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);

  GoRouter.optionURLReflectsImperativeAPIs = true;
  usePathUrlStrategy();

  runApp(
    ChangeNotifierProvider(
      create: (context) => AuthService(),
      child: App(initialTheme: await AdaptiveTheme.getThemeMode()),
    ),
  );
}

RouterConfig<Object> routerConfig = GoRouter(
  initialLocation: HomePage.routePath,
  routes: [
    // auth
    GoRoute(
      name: LoginPage.routeName,
      path: LoginPage.routePath,
      builder: (context, state) => const LoginPage(),
      redirect: needLogoutRedirect,
    ),
    GoRoute(
      name: RegisterPage.routeName,
      path: RegisterPage.routePath,
      builder: (context, state) => const RegisterPage(),
      redirect: needLogoutRedirect,
    ),
    // home
    GoRoute(
      name: HomePage.routeName,
      path: HomePage.routePath,
      builder: (context, state) => const HomePage(),
      redirect: needLoginRedirect,
    ),
    GoRoute(
      name: SettingsPage.routeName,
      path: SettingsPage.routePath,
      builder: (context, state) => const SettingsPage(),
      redirect: needLoginRedirect,
    ),
    // exams
    GoRoute(
      name: CreateExamPage.routeName,
      path: CreateExamPage.routePath,
      builder: (context, state) => const CreateExamPage(),
      redirect: needLoginRedirect,
    ),
    GoRoute(
      name: DetailExamPage.routeName,
      path: DetailExamPage.routePath,
      builder: (context, state) {
        String examUid = state.pathParameters['uid']!;
        return DetailExamPage(examUid: examUid);
      },
      redirect: needToBeExamOwnerRedirect,
    ),
    // sessions
    GoRoute(
      name: OpenSessionPage.routeName,
      path: OpenSessionPage.routePath,
      builder: (context, state) {
        String sessionUid = state.pathParameters['uid']!;
        return OpenSessionPage(sessionUid: sessionUid);
      },
    ),
    GoRoute(
      name: PassSessionPage.routeName,
      path: PassSessionPage.routePath,
      builder: (context, state) {
        String sessionUid = state.pathParameters['uid']!;
        String studentKey = state.pathParameters['studentKey']!;
        return PassSessionPage(sessionUid: sessionUid, studentKey: studentKey);
      },
    ),
    GoRoute(
      name: ResultsSessionPage.routeName,
      path: ResultsSessionPage.routePath,
      builder: (context, state) {
        String sessionUid = state.pathParameters['uid']!;
        return ResultsSessionPage(sessionUid: sessionUid);
      },
    ),
  ],
);

String root = 'localhost:49430';

String getLink(
  BuildContext context, {
  required String name,
  Map<String, String> pathParameters = const <String, String>{},
  Map<String, dynamic> queryParameters = const <String, dynamic>{},
  String? fragment,
}) {
  String path = context.namedLocation(
    name,
    pathParameters: pathParameters,
    queryParameters: queryParameters,
    fragment: fragment,
  );
  return root + path;
}

class App extends StatelessWidget {
  final AdaptiveThemeMode? initialTheme;

  const App({super.key, required this.initialTheme});

  @override
  Widget build(BuildContext context) {
    return AdaptiveTheme(
      debugShowFloatingThemeButton: true,
      light: MainTheme.light,
      dark: MainTheme.dark,
      initial: initialTheme ?? AdaptiveThemeMode.system,
      builder: (ThemeData light, ThemeData dark) {
        return MaterialApp.router(
          debugShowCheckedModeBanner: false,
          title: 'Зачет Онлайн',
          theme: light,
          darkTheme: dark,
          routerConfig: routerConfig,
          localizationsDelegates: const [
            GlobalMaterialLocalizations.delegate,
            GlobalWidgetsLocalizations.delegate,
            GlobalCupertinoLocalizations.delegate,
          ],
          supportedLocales: const [Locale('ru')],
        );
      },
    );
  }
}
