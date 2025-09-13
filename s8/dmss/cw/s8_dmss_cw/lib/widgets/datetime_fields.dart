import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:s8_dmss_cw/dialogs/dialog_functions.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';

class DateTimeRangeFields extends StatefulWidget {
  const DateTimeRangeFields({
    super.key,
    this.readOnly = false,
    this.startDate,
    this.startInitialDate,
    this.startFirstDate,
    this.startLastDate,
    this.startPickerHelpText,
    this.startOnChanged,
    this.endDate,
    this.endInitialDate,
    this.endFirstDate,
    this.endLastDate,
    this.endPickerHelpText,
    this.endOnChanged,
  });

  final bool readOnly;

  final String? startPickerHelpText;
  final DateTime? startDate;
  final DateTime? startInitialDate;
  final DateTime? startFirstDate;
  final DateTime? startLastDate;
  final void Function(DateTime)? startOnChanged;

  final String? endPickerHelpText;
  final DateTime? endDate;
  final DateTime? endInitialDate;
  final DateTime? endFirstDate;
  final DateTime? endLastDate;
  final void Function(DateTime)? endOnChanged;

  @override
  MountedState<DateTimeRangeFields> createState() => _DateTimeRangeFieldsState();
}

class _DateTimeRangeFieldsState extends MountedState<DateTimeRangeFields> {
  bool get _hasStart => widget.startDate != null;
  bool get _hasEnd => widget.endDate != null;

  final TextEditingController _startController = TextEditingController();
  final TextEditingController _endController = TextEditingController();

  @override
  void initState() {
    super.initState();
    if (widget.startDate != null) {
      _startController.text = DateTimeField.formatter.format(widget.startDate!);
    }
    if (widget.endDate != null) {
      _endController.text = DateTimeField.formatter.format(widget.endDate!);
    }
  }

  @override
  Widget build(BuildContext context) {
    DateTime? endInitialDate;
    if (widget.endInitialDate != null && widget.startDate != null) {
      endInitialDate = widget.endInitialDate!.isAfter(widget.startDate!) ? widget.endInitialDate! : endInitialDate = widget.startDate!;
    } else {
      endInitialDate = widget.endInitialDate ?? widget.startDate;
    }

    return Stack(
      clipBehavior: Clip.hardEdge,
      children: [
        TextField(
          minLines: 2,
          maxLines: 2,
          enabled: false,
          style: const TextStyle(fontSize: 16),
          decoration: InputDecoration(
            disabledBorder: OutlineInputBorder(
              borderSide: const BorderSide(color: MainTheme.neural, width: 2),
              borderRadius: roundedBorderRadius,
            ),
          ),
        ),
        Row(
          children: [
            Expanded(
              child: DateTimeField(
                timePickerHelpText: widget.startPickerHelpText,
                datePickerHelpText: widget.startPickerHelpText,
                controller: _startController,
                readOnly: widget.readOnly,
                decoration: InputDecoration(
                  hintText: 'Начало',
                  prefixIcon: const Icon(Icons.date_range_rounded),
                  border: InputBorder.none,
                  enabledBorder: InputBorder.none,
                  disabledBorder: InputBorder.none,
                  errorBorder: InputBorder.none,
                  focusedBorder: InputBorder.none,
                  focusedErrorBorder: InputBorder.none,
                  filled: false,
                  contentPadding: !_hasStart || _hasEnd ? const EdgeInsets.fromLTRB(4, 16, 4, 16) : null,
                ),
                initialDate: widget.startDate ?? widget.startInitialDate,
                firstDate: widget.startFirstDate,
                lastDate: widget.endDate ?? widget.startLastDate,
                onChanged: widget.startOnChanged,
              ),
            ),
            const SizedBox(width: 20),
            const Text('—', style: TextStyle(fontSize: 24)),
            Expanded(
              child: DateTimeField(
                timePickerHelpText: widget.endPickerHelpText,
                datePickerHelpText: widget.endPickerHelpText,
                controller: _endController,
                readOnly: widget.readOnly,
                decoration: InputDecoration(
                  hintText: 'Конец ',
                  prefixIcon: const SizedBox.shrink(),
                  prefixIconConstraints: const BoxConstraints(maxWidth: 0, minWidth: 0),
                  border: InputBorder.none,
                  enabledBorder: InputBorder.none,
                  disabledBorder: InputBorder.none,
                  errorBorder: InputBorder.none,
                  focusedBorder: InputBorder.none,
                  focusedErrorBorder: InputBorder.none,
                  filled: false,
                  contentPadding: !_hasEnd || _hasStart ? const EdgeInsets.fromLTRB(4, 16, 4, 16) : null,
                ),
                initialDate: widget.endDate ?? endInitialDate,
                firstDate: widget.startDate ?? widget.endFirstDate,
                lastDate: widget.endLastDate,
                onChanged: widget.endOnChanged,
              ),
            ),
          ],
        ),
      ],
    );
  }
}

class DateTimeField extends StatefulWidget {
  const DateTimeField({
    super.key,
    required this.controller,
    this.focusNode,
    this.readOnly = false,
    this.textStyle,
    this.decoration,
    this.onChanged,
    this.initialDate,
    this.firstDate,
    this.lastDate,
    this.datePickerHelpText,
    this.timePickerHelpText,
  });

  final TextEditingController controller;
  final FocusNode? focusNode;
  final bool readOnly;
  final TextStyle? textStyle;
  final InputDecoration? decoration;
  final DateTime? initialDate;
  final DateTime? firstDate;
  final DateTime? lastDate;
  final String? datePickerHelpText;
  final String? timePickerHelpText;

  final void Function(DateTime value)? onChanged;

  static final DateFormat formatter = DateFormat('H:mm\nd MMMM yyyy', 'ru');

  @override
  MountedState<DateTimeField> createState() => _DateTimeFieldState();
}

class _DateTimeFieldState extends MountedState<DateTimeField> {
  DateTime? get _dateTime => DateTimeField.formatter.tryParse(widget.controller.text);

  Future<void> _showDateTimePicket() async {
    DateTime? dateTime = await showDateTimePicker(
      context,
      initialDate: _dateTime ?? widget.initialDate,
      firstDate: widget.firstDate,
      lastDate: widget.lastDate,
      dateHelpText: widget.datePickerHelpText,
      timeHelpText: widget.timePickerHelpText,
    );
    if (dateTime != null) {
      widget.onChanged?.call(dateTime);
      widget.controller.text = DateTimeField.formatter.format(dateTime);
    }
  }

  @override
  Widget build(BuildContext context) {
    InputBorder border = OutlineInputBorder(
      borderSide: const BorderSide(color: MainTheme.neural, width: 2),
      borderRadius: roundedBorderRadius,
    );
    return TextField(
      mouseCursor: widget.readOnly ? null : SystemMouseCursors.click,
      controller: widget.controller,
      focusNode: widget.focusNode,
      minLines: 2,
      maxLines: 2,
      readOnly: true,
      enableInteractiveSelection: false,
      textAlign: TextAlign.center,
      style: const TextStyle(fontSize: 16).merge(widget.textStyle),
      decoration: InputDecoration(
        border: OutlineInputBorder(borderRadius: roundedBorderRadius),
        enabledBorder: border,
        focusedBorder: widget.readOnly ? border : null,
        hintStyle: TextStyle(color: MainTheme.neural, height: _dateTime == null ? 3 : null),
        labelStyle: const TextStyle(color: MainTheme.secondary),
        errorBorder: OutlineInputBorder(
          borderRadius: roundedBorderRadius,
          borderSide: BorderSide(color: errorColor(context)),
        ),
        floatingLabelBehavior: FloatingLabelBehavior.always,
        prefixIcon: const Icon(Icons.calendar_today_rounded),
      ).merge(widget.decoration),
      onTap: widget.readOnly ? null : _showDateTimePicket,
      onTapAlwaysCalled: true,
    );
  }
}

class TimeField extends StatefulWidget {
  const TimeField({
    super.key,
    required this.controller,
    this.focusNode,
    this.readOnly = false,
    this.textStyle,
    this.decoration,
    this.onChanged,
    this.initialTime,
    this.pickerHelpText,
  });

  final TextEditingController controller;
  final FocusNode? focusNode;
  final bool readOnly;
  final TextStyle? textStyle;
  final InputDecoration? decoration;
  final TimeOfDay? initialTime;
  final String? pickerHelpText;

  final void Function(TimeOfDay? value)? onChanged;

  static final DateFormat formatter = DateFormat('H:mm  ', 'ru');

  @override
  State<TimeField> createState() => _TimeFieldState();
}

class _TimeFieldState extends State<TimeField> {
  TimeOfDay? get _time {
    DateTime? dateTime = TimeField.formatter.tryParse(widget.controller.text);
    if (dateTime == null) return null;
    return TimeOfDay.fromDateTime(dateTime);
  }

  Future<void> _showTimePicker() async {
    TimeOfDay? time = await showTimePicker(
      context: context,
      initialTime: _time ?? widget.initialTime ?? TimeOfDay.now(),
      helpText: widget.pickerHelpText,
    );
    if (time != null) {
      widget.onChanged?.call(time);
      widget.controller.text = TimeField.formatter.formatTimeOfDay(time);
    }
  }

  @override
  Widget build(BuildContext context) {
    InputBorder border = OutlineInputBorder(
      borderSide: const BorderSide(color: MainTheme.neural, width: 2),
      borderRadius: roundedBorderRadius,
    );
    return TextField(
      mouseCursor: widget.readOnly ? null : SystemMouseCursors.click,
      controller: widget.controller,
      focusNode: widget.focusNode,
      readOnly: true,
      enableInteractiveSelection: false,
      style: const TextStyle(fontSize: 16).merge(widget.textStyle),
      textAlign: TextAlign.center,
      decoration: InputDecoration(
        border: OutlineInputBorder(borderRadius: roundedBorderRadius),
        enabledBorder: border,
        focusedBorder: widget.readOnly ? border : null,
        hintStyle: const TextStyle(color: MainTheme.neural),
        labelStyle: const TextStyle(color: MainTheme.secondary),
        errorBorder: OutlineInputBorder(
          borderRadius: roundedBorderRadius,
          borderSide: BorderSide(color: errorColor(context)),
        ),
        floatingLabelBehavior: FloatingLabelBehavior.always,
        prefixIcon: const Icon(Icons.timer_outlined),
      ).merge(widget.decoration),
      onTap: widget.readOnly ? null : _showTimePicker,
      onTapAlwaysCalled: true,
    );
  }
}
