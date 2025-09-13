import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:s8_dmss_cw/dialogs/base_dialog.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';
import 'package:s8_dmss_cw/widgets/buttons.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';
import 'package:s8_dmss_cw/widgets/text_fields.dart';

class ConfirmDialog extends StatefulWidget {
  const ConfirmDialog({
    super.key,
    required this.title,
    this.subtitle,
    this.subtitleColor,
    this.confirmText,
    this.confirmHelpText,
    this.confirmColor,
    this.cancelColor,
    required this.onConfirm,
    this.onCancel,
  });

  final String title;
  final String? subtitle;
  final Color? subtitleColor;
  final String? confirmText;
  final String? confirmHelpText;
  final Color? confirmColor;
  final Color? cancelColor;

  final void Function() onConfirm;
  final void Function()? onCancel;

  @override
  MountedState<ConfirmDialog> createState() => _ConfirmDialogState();
}

class _ConfirmDialogState extends MountedState<ConfirmDialog> {
  final TextEditingController _confirmController = TextEditingController();

  String? _suffixText;

  Future<void> _evalSuffixText() async {
    if (_confirmController.text.isEmpty) {
      _suffixText = widget.confirmText!;
    } else if (_confirmController.text.length == widget.confirmText!.length) {
      _suffixText = null;
    } else if (_confirmController.text.length > widget.confirmText!.length) {
      _suffixText = null;
    } else if (widget.confirmText!.s_(0, _confirmController.text.length) != _confirmController.text) {
      _suffixText = null;
    } else {
      _suffixText = widget.confirmText!.substring(_confirmController.text.length);
    }
    updateState();
  }

  @override
  void initState() {
    super.initState();
    if (widget.confirmText != null) {
      _evalSuffixText();
    }
  }

  @override
  Widget build(BuildContext context) {
    return BaseDialog(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(widget.title, style: dialogTitleTextStyle),
          if (widget.subtitle != null)
            Text(
              widget.subtitle!,
              style: dialogSubtitleTextStyle.copyWith(color: widget.subtitleColor),
            ),
          if (widget.confirmText != null) ...[
            Padding(
              padding: const EdgeInsets.only(top: 16),
              child: RoundedTextField(
                controller: _confirmController,
                textStyle: _suffixText == null && _confirmController.text != widget.confirmText ? TextStyle(color: errorColor(context)) : null,
                decoration: InputDecoration(suffixText: _suffixText),
                onChanged: widget.confirmText != null ? (_) async => _evalSuffixText() : null,
              ),
            ),
            if (widget.confirmHelpText != null)
              Text(
                widget.confirmHelpText!,
                style: dialogSecondaryTextStyle,
              ),
          ],
          mediumVDivider,
          Row(
            children: [
              Expanded(
                child: CircularBorderButton(
                  onPressed: widget.confirmText == null || _confirmController.text == widget.confirmText
                      ? () {
                          widget.onConfirm();
                          context.pop();
                        }
                      : null,
                  child: Text(
                    widget.confirmText == null ? 'Да' : 'Подтвердить',
                    style: TextStyle(color: widget.confirmColor ?? errorColor(context)),
                  ),
                ),
              ),
              smallHDivider,
              Expanded(
                child: CircularBorderButton(
                  onPressed: () {
                    widget.onCancel?.call();
                    context.pop();
                  },
                  child: Text('Отмена', style: TextStyle(color: widget.cancelColor)),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
