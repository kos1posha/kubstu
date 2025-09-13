import 'package:flutter/material.dart';
import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:s7_ais_cw/osago/data.dart';
import 'package:s7_ais_cw/pages/osago_page.dart';
import 'package:s7_ais_cw/pages/welcome_page.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  OsagoData.initialize();
  runApp(const MainApp());
}

class MainApp extends StatelessWidget {
  const MainApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      localizationsDelegates: const [
        GlobalMaterialLocalizations.delegate,
        GlobalCupertinoLocalizations.delegate,
      ],
      supportedLocales: const [Locale('ru')],
      debugShowCheckedModeBanner: false,
      initialRoute: '/welcome',
      routes: {
        '/welcome': (context) => const WelcomePage(),
        '/osago': (context) => const OsagoPage(),
      },
    );
  }
}
