import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/pages/settings_page.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/other/logo_title.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/pages/exams/create_exam_page.dart';
import 'package:s8_dmss_cw/pages/home_page.dart';
import 'package:s8_dmss_cw/theme.dart';

// main app bar
class MainAppBar extends StatelessWidget implements PreferredSizeWidget {
  const MainAppBar({super.key});

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        return Hero(
          tag: 'mainAppBarHero',
          child: AppBar(
            scrolledUnderElevation: 0,
            backgroundColor: Theme.of(context).scaffoldBackgroundColor,
            leading: const Padding(padding: EdgeInsets.only(left: 4), child: LogoIcon()),
            actions: (constraints.maxWidth < 1100)
                ? [
                    IconButton(
                      onPressed: () async => Scaffold.of(context).openEndDrawer(),
                      icon: const Icon(Icons.menu),
                      splashColor: Colors.transparent,
                      highlightColor: Colors.transparent,
                    ),
                    smallHDivider,
                  ]
                : null,
            title: Link(
              'Зачет Онлайн',
              onPressed: () => context.pushNamed(HomePage.routeName),
              style: const TextStyle(color: Colors.white, fontSize: 20),
            ),
          ),
        );
      },
    );
  }

  @override
  Size get preferredSize => const Size.fromHeight(80);
}

// main drawer
class MainDrawer extends StatelessWidget {
  const MainDrawer({super.key});

  User get user => FirebaseAuth.instance.currentUser!;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        EdgeInsets padding = const EdgeInsets.symmetric(horizontal: 16);
        return Hero(
          tag: 'mainDrawerHero',
          child: Drawer(
            width: 250,
            shape: const RoundedRectangleBorder(borderRadius: BorderRadius.zero),
            backgroundColor: adaptiveColor(context, Colors.grey[100], const Color(0xff0f0f0f)),
            child: Padding(
              padding: constraints.maxWidth >= 1100 ? padding : padding.copyWith(top: 24, bottom: 24),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  if (constraints.maxWidth >= 1100) const AppBarLogoTitle(),
                  SizedBox(
                    width: double.infinity,
                    child: CircularBorderButton(
                      onPressed: () => context.pushNamed(CreateExamPage.routeName),
                      isPrimary: true,
                      child: const Text('Создать зачет'),
                    ),
                  ),
                  const Spacer(),
                  PopupMenuButton(
                    offset: const Offset(0, -120),
                    elevation: 4,
                    tooltip: '',
                    borderRadius: roundedBorderRadius,
                    itemBuilder: (context) {
                      return <PopupMenuItem>[
                        PopupMenuItem(
                          onTap: () {
                            String? routeName = GoRouter.of(context).routeInformationProvider.value.uri.pathSegments.firstOrNull;
                            if (routeName == 'exam') {
                              context.replaceNamed(SettingsPage.routeName);
                            } else {
                              context.pushNamed(SettingsPage.routeName);
                            }
                          },
                          child: const SizedBox(
                              width: 200,
                              child: Row(
                                children: [
                                  Icon(Icons.settings_rounded),
                                  smallHDivider,
                                  Text('Настройки'),
                                ],
                              )),
                        ),
                        PopupMenuItem(
                          onTap: FirebaseAuth.instance.signOut,
                          child: const SizedBox(
                              width: 200,
                              child: Row(
                                children: [
                                  Icon(Icons.logout_rounded),
                                  smallHDivider,
                                  Text('Выйти'),
                                ],
                              )),
                        ),
                      ];
                    },
                    child: Align(
                      alignment: Alignment.centerLeft,
                      child: Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
                        child: Row(
                          children: [
                            Text(user.email!),
                            const Spacer(),
                            const Icon(Icons.arrow_drop_up_rounded),
                          ],
                        ),
                      ),
                    ),
                  ),
                  if (constraints.maxWidth >= 1100) const SizedBox(height: 24),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}

// scaffolds
class AdaptiveDrawerScaffold extends StatelessWidget {
  const AdaptiveDrawerScaffold({
    super.key,
    this.scrollController,
    this.appBar,
    this.floatingActionButton,
    this.floatingActionButtonLocation,
    required this.endDrawer,
    required this.body,
  });

  final ScrollController? scrollController;
  final PreferredSizeWidget? appBar;
  final Widget? floatingActionButton;
  final FloatingActionButtonLocation? floatingActionButtonLocation;
  final Widget endDrawer;
  final Widget body;

  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        if (constraints.maxWidth < 1100) {
          return Scaffold(
            appBar: appBar,
            endDrawer: endDrawer,
            floatingActionButton: floatingActionButton,
            floatingActionButtonLocation: floatingActionButtonLocation,
            body: SingleChildScrollView(
              controller: scrollController,
              padding: const EdgeInsets.fromLTRB(24, 0, 24, 24),
              child: body,
            ),
          );
        } else {
          return Scaffold(
            backgroundColor: adaptiveColor(context, Colors.grey[100], const Color(0xff0f0f0f)),
            floatingActionButton: floatingActionButton,
            floatingActionButtonLocation: floatingActionButtonLocation,
            body: Row(
              mainAxisSize: MainAxisSize.max,
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                endDrawer,
                Expanded(
                  child: SizedBox(
                    height: double.infinity,
                    child: Card.filled(
                      elevation: 1.5,
                      color: Theme.of(context).scaffoldBackgroundColor,
                      margin: const EdgeInsets.fromLTRB(0, 24, 16, 20),
                      child: Padding(
                        padding: const EdgeInsets.all(2),
                        child: SingleChildScrollView(
                          controller: scrollController,
                          padding: const EdgeInsets.all(30),
                          child: body,
                        ),
                      ),
                    ),
                  ),
                ),
              ],
            ),
          );
        }
      },
    );
  }
}

class CenteredBodyScaffold extends StatelessWidget {
  const CenteredBodyScaffold({
    super.key,
    this.maxWidth,
    this.canBack = true,
    this.scrollController,
    this.floatingActionButton,
    this.floatingActionButtonLocation,
    required this.body,
  });

  final double? maxWidth;
  final bool canBack;
  final ScrollController? scrollController;
  final Widget? floatingActionButton;
  final FloatingActionButtonLocation? floatingActionButtonLocation;
  final Widget body;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      floatingActionButton: floatingActionButton,
      floatingActionButtonLocation: floatingActionButtonLocation,
      body: Stack(
        children: [
          Center(
            child: SingleChildScrollView(
              child: ConstrainedBox(
                constraints: BoxConstraints(minWidth: MediaQuery.of(context).size.width),
                child: Center(
                  child: Container(
                    padding: const EdgeInsets.symmetric(horizontal: 16),
                    constraints: BoxConstraints(maxWidth: (maxWidth ?? 600) + 16),
                    child: body,
                  ),
                ),
              ),
            ),
          ),
          if (canBack)
            Container(
              padding: const EdgeInsets.only(left: 8),
              height: toolbarHeight,
              width: toolbarHeight,
              alignment: Alignment.centerLeft,
              child: IconButton(
                icon: const BackButtonIcon(),
                onPressed: () {
                  if (context.canPop()) {
                    context.pop();
                  } else {
                    context.pushNamed(HomePage.routeName);
                  }
                },
              ),
            ),
        ],
      ),
    );
  }
}
