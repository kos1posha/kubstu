import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';

class PasswordHint extends StatefulWidget {
  const PasswordHint({super.key, required this.child, required this.rules, this.bottomOffset = 68});

  final Widget child;
  final List<PasswordRule> rules;
  final double bottomOffset;

  @override
  MountedState<PasswordHint> createState() => _PasswordHintState();
}

class _PasswordHintState extends MountedState<PasswordHint> {
  bool _isFocused = false;

  @override
  Widget build(BuildContext context) {
    return Focus(
      onFocusChange: (value) {
        if (_isFocused != value) setState(() => _isFocused = value);
      },
      child: Stack(
        clipBehavior: Clip.none,
        children: [
          widget.child,
          AnimatedPositioned(
            duration: Durations.medium1,
            bottom: _isFocused ? widget.bottomOffset : widget.bottomOffset - 8,
            child: AnimatedOpacity(
              duration: Durations.medium1,
              opacity: _isFocused ? 1.0 : 0.0,
              child: Card(
                elevation: 8,
                margin: EdgeInsets.zero,
                shape: RoundedRectangleBorder(borderRadius: circularBorderRadius),
                child: Container(
                  padding: const EdgeInsets.symmetric(vertical: 16, horizontal: 20),
                  child: Column(
                    spacing: 4,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: widget.rules,
                  ),
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}

class PasswordRule extends StatelessWidget {
  const PasswordRule(this.rule, {super.key, required this.state});

  final String rule;
  final bool state;

  @override
  Widget build(BuildContext context) {
    return Row(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        AnimatedSwitcher(
          duration: Durations.short2,
          transitionBuilder: (child, animation) => RotationTransition(
            turns: child.key == const ValueKey('successRuleIcon')
                ? Tween<double>(
                    begin: 0.75,
                    end: 1,
                  ).animate(animation)
                : Tween<double>(
                    begin: 1,
                    end: 0.75,
                  ).animate(animation),
            child: FadeTransition(opacity: animation, child: child),
          ),
          child: state
              ? const Icon(
                  Icons.check_rounded,
                  color: Colors.green,
                  size: 20,
                  key: ValueKey('successRuleIcon'),
                )
              : Icon(
                  Icons.close_rounded,
                  color: errorColor(context),
                  size: 20,
                  key: const ValueKey('wrongRuleIcon'),
                ),
        ),
        smallHDivider,
        Text(rule),
      ],
    );
  }
}
