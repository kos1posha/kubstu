import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';

class BaseDialog extends StatelessWidget {
  const BaseDialog({super.key, required this.child, this.maxWidth});

  final Widget child;
  final double? maxWidth;

  @override
  Widget build(BuildContext context) {
    return Dialog(
      shape: RoundedRectangleBorder(borderRadius: roundedBorderRadius),
      clipBehavior: Clip.hardEdge,
      child: SingleChildScrollView(
        child: Container(
          padding: const EdgeInsets.all(24),
          constraints: BoxConstraints(maxWidth: maxWidth ?? 450),
          child: child,
        ),
      ),
    );
  }
}

// constants
const TextStyle dialogTitleTextStyle = TextStyle(
  fontSize: 20,
  fontWeight: FontWeight.bold,
);
const TextStyle dialogSubtitleTextStyle = TextStyle(
  color: MainTheme.tertiary,
  fontSize: 16,
);
const TextStyle dialogSecondaryTextStyle = TextStyle(
  color: MainTheme.neural,
  fontSize: 13,
);
