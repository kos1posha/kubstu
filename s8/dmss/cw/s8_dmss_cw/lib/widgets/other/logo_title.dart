import 'dart:core';

import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/pages/home_page.dart';

class LogoIcon extends StatelessWidget {
  const LogoIcon({super.key, this.color, this.size});

  final Color? color;
  final double? size;

  @override
  Widget build(BuildContext context) {
    return Icon(Icons.list_alt, color: color, size: size);
  }
}

class LogoTitle extends StatelessWidget {
  const LogoTitle({super.key});

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        LogoIcon(color: logoTextStyle.color, size: logoTextStyle.fontSize),
        smallHDivider,
        const Text('Зачет Онлайн', style: logoTextStyle),
      ],
    );
  }
}

class AppBarLogoTitle extends StatelessWidget {
  const AppBarLogoTitle({super.key});

  @override
  Widget build(BuildContext context) {
    AppBarTheme appBarTheme = Theme.of(context).appBarTheme;
    return SizedBox(
      height: appBarTheme.toolbarHeight,
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          IconTheme(
            data: appBarTheme.iconTheme!,
            child: const LogoIcon(),
          ),
          const SizedBox(width: 12),
          MouseRegion(
            cursor: SystemMouseCursors.click,
            child: GestureDetector(
              onTap: () {
                String? routeName = GoRouter.of(context).routeInformationProvider.value.uri.pathSegments.firstOrNull;
                if (routeName == 'exam') {
                  context.replaceNamed(HomePage.routeName);
                } else {
                  context.pushNamed(HomePage.routeName);
                }
              },
              child: Text(
                'Зачет Онлайн',
                style: appBarTheme.titleTextStyle!.copyWith(fontSize: 21.6, fontWeight: FontWeight.normal),
              ),
            ),
          ),
        ],
      ),
    );
  }
}
