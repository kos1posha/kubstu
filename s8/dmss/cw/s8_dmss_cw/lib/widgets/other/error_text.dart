import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/theme.dart';

class ErrorText extends StatelessWidget {
  const ErrorText(this.data, {super.key});

  final String? data;

  @override
  Widget build(BuildContext context) {
    return AnimatedSize(
      duration: Durations.short3,
      alignment: Alignment.bottomCenter,
      child: data == null
          ? const SizedBox(width: double.infinity)
          : SizedBox(
              width: double.infinity,
              child: Text(
                data!,
                style: TextStyle(color: errorColor(context)),
              ),
            ),
    );
  }
}
