import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';

const BoxConstraints textFieldIconConstraints = BoxConstraints(
  minWidth: 60,
  minHeight: 60,
);

class TransparentTextField extends StatefulWidget {
  const TransparentTextField({
    super.key,
    this.controller,
    this.focusNode,
    this.minLines = 1,
    this.maxLines = 1,
    this.readOnly = false,
    this.autoTrim = false,
    this.underlineFocused = false,
    this.textStyle,
    this.textAlign,
    this.decoration,
    this.onChanged,
    this.onEditingComplete,
  });

  final TextEditingController? controller;
  final FocusNode? focusNode;
  final int? minLines;
  final int? maxLines;
  final bool readOnly;
  final bool autoTrim;
  final bool underlineFocused;
  final TextStyle? textStyle;
  final TextAlign? textAlign;
  final InputDecoration? decoration;

  final void Function(String value)? onChanged;
  final void Function()? onEditingComplete;

  @override
  MountedState<TransparentTextField> createState() => _TransparentTextFieldState();
}

class _TransparentTextFieldState extends MountedState<TransparentTextField> with SingleTickerProviderStateMixin {
  late AnimationController _animationController;
  late Animation<double> _borderWidthAnimation;

  late final bool _canUnderline = widget.underlineFocused && !widget.readOnly;

  static const double _maxUnderlineWidth = 2;

  @override
  void initState() {
    super.initState();
    _animationController = AnimationController(
      vsync: this,
      duration: Durations.short2,
    );
    _borderWidthAnimation = Tween<double>(
      begin: 0,
      end: _maxUnderlineWidth,
    ).animate(_animationController);
  }

  Future<void> _toggleAnimation(bool state) async {
    if (state) {
      _animationController.forward();
    } else {
      _animationController.reverse();
    }
    updateState();
  }

  @override
  Widget build(BuildContext context) {
    return Focus(
      onFocusChange: (value) {
        if (_canUnderline) _toggleAnimation(value);
        if (!value) widget.onEditingComplete?.call();
        if (!widget.autoTrim && widget.controller != null) {
          widget.controller!.text = widget.controller!.text.trim();
        }
      },
      child: AnimatedBuilder(
        animation: _borderWidthAnimation,
        builder: (_, __) {
          return TextField(
            controller: widget.controller,
            focusNode: widget.focusNode,
            minLines: widget.minLines,
            maxLines: widget.maxLines,
            readOnly: widget.readOnly,
            inputFormatters: widget.autoTrim ? [FilteringTextInputFormatter.deny(RegExp(r'^\s+|\s+$'))] : null,
            style: widget.textStyle,
            textAlign: widget.textAlign ?? TextAlign.start,
            cursorOpacityAnimates: false,
            decoration: InputDecoration(
              filled: false,
              isDense: true,
              border: InputBorder.none,
              focusedBorder: _canUnderline
                  ? UnderlineInputBorder(
                      borderSide: BorderSide(
                        width: _borderWidthAnimation.value,
                        color: MainTheme.secondary,
                      ),
                    )
                  : InputBorder.none,
              contentPadding: EdgeInsets.zero,
              hintStyle: const TextStyle(color: MainTheme.neural),
            ).merge(widget.decoration),
            onChanged: widget.onChanged,
          );
        },
      ),
    );
  }

  @override
  void dispose() {
    _animationController.dispose();
    super.dispose();
  }
}

class CircularTextField extends StatelessWidget {
  const CircularTextField({
    super.key,
    this.controller,
    this.focusNode,
    this.minLines = 1,
    this.maxLines = 1,
    this.readOnly = false,
    this.autoTrim = false,
    this.obscureText = false,
    this.textStyle,
    this.decoration,
    this.onChanged,
    this.onEditingComplete,
  });

  final TextEditingController? controller;
  final FocusNode? focusNode;
  final int? minLines;
  final int? maxLines;
  final bool readOnly;
  final bool autoTrim;
  final bool obscureText;
  final TextStyle? textStyle;
  final InputDecoration? decoration;

  final void Function(String value)? onChanged;
  final void Function()? onEditingComplete;

  @override
  Widget build(BuildContext context) {
    Color color = (decoration?.errorText ?? '').isEmpty ? MainTheme.secondary : errorColor(context);
    return Focus(
      onFocusChange: (value) async {
        if (!value) onEditingComplete?.call();
        if (!autoTrim && controller != null) {
          controller!.text = controller!.text.trim();
        }
      },
      child: TextField(
        controller: controller,
        focusNode: focusNode,
        minLines: minLines,
        maxLines: maxLines,
        readOnly: readOnly,
        inputFormatters: autoTrim ? [FilteringTextInputFormatter.deny(RegExp(r'^\s+|\s+$'))] : null,
        obscureText: obscureText,
        obscuringCharacter: '*',
        style: textStyle,
        decoration: InputDecoration(
          filled: true,
          border: OutlineInputBorder(
            borderRadius: circularBorderRadius,
            borderSide: BorderSide.none,
          ),
          hintStyle: TextStyle(color: color),
          prefixIconColor: color,
          suffixIconColor: MainTheme.secondary,
          prefixIconConstraints: textFieldIconConstraints,
          suffixIconConstraints: textFieldIconConstraints,
        ).merge(decoration),
        onChanged: onChanged,
      ),
    );
  }
}

class RoundedTextField extends StatelessWidget {
  const RoundedTextField({
    super.key,
    this.controller,
    this.focusNode,
    this.minLines = 1,
    this.maxLines = 1,
    this.readOnly = false,
    this.autoTrim = false,
    this.textStyle,
    this.decoration,
    this.onChanged,
    this.onEditingComplete,
  });

  final TextEditingController? controller;
  final FocusNode? focusNode;
  final int? minLines;
  final int? maxLines;
  final bool readOnly;
  final bool autoTrim;
  final TextStyle? textStyle;
  final InputDecoration? decoration;

  final void Function(String value)? onChanged;
  final void Function()? onEditingComplete;

  @override
  Widget build(BuildContext context) {
    return Focus(
      onFocusChange: (value) {
        if (!value) onEditingComplete?.call();
        if (!autoTrim && controller != null) {
          controller!.text = controller!.text.trim();
        }
      },
      child: TextField(
        controller: controller,
        focusNode: focusNode,
        minLines: minLines,
        maxLines: maxLines,
        readOnly: readOnly,
        inputFormatters: autoTrim ? [FilteringTextInputFormatter.deny(RegExp(r'^\s+|\s+$'))] : null,
        style: const TextStyle(fontSize: 19).merge(textStyle),
        decoration: InputDecoration(
          filled: false,
          border: OutlineInputBorder(borderRadius: roundedBorderRadius),
          enabledBorder: OutlineInputBorder(
            borderSide: const BorderSide(color: MainTheme.neural, width: 2),
            borderRadius: roundedBorderRadius,
          ),
          hintStyle: const TextStyle(color: MainTheme.neural),
          errorBorder: OutlineInputBorder(
            borderRadius: roundedBorderRadius,
            borderSide: BorderSide(color: errorColor(context)),
          ),
          floatingLabelBehavior: FloatingLabelBehavior.always,
          // error's left padding workaround
          // prefixIcon: const SizedBox.shrink(),
          // prefixIconConstraints: const BoxConstraints(minWidth: 10, maxWidth: 10),
          // contentPadding: const EdgeInsets.fromLTRB(0, 24, 12, 16),
        ).merge(decoration),
        onChanged: onChanged,
      ),
    );
  }
}
