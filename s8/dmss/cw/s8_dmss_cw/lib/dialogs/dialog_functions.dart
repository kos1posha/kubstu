import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/dialogs/session_dialogs.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/firebase/tickets.dart';
import 'package:s8_dmss_cw/dialogs/confirm_dialog.dart';
import 'package:s8_dmss_cw/dialogs/ticket_dialogs.dart';
import 'package:s8_dmss_cw/theme.dart';

Future<void> pushSnackBarMessage(BuildContext context, String message, {TextStyle? style}) async {
  ScaffoldMessenger.of(context)
    ..hideCurrentSnackBar()
    ..showSnackBar(
      SnackBar(
        content: Text(message, style: TextStyle(color: Theme.of(context).colorScheme.onSurface).merge(style)),
        backgroundColor: Theme.of(context).colorScheme.surfaceContainer,
      ),
    );
}

Future<void> pushSnackBarErrorCodeMessage(BuildContext context, String errorCode) async {
  pushSnackBarMessage(
    context,
    'Произошла непредвиденная ошибка (код: $errorCode)',
    style: TextStyle(color: errorColor(context)),
  );
}

Future<void> showLoadingDialog(BuildContext context) async {
  showDialog(
    context: context,
    builder: (context) => const Center(child: CircularProgressIndicator()),
  );
}

Future<void> showConfirmDialog(
  BuildContext context, {
  required String title,
  String? subtitle,
  Color? subtitleColor,
  String? confirmText,
  String? confirmHelpText,
  Color? confirmColor,
  Color? cancelColor,
  required void Function() onConfirm,
  void Function()? onCancel,
}) async {
  assert(confirmHelpText == null || confirmText != null);
  showDialog(
    context: context,
    builder: (context) {
      return ConfirmDialog(
        title: title,
        subtitle: subtitle,
        subtitleColor: subtitleColor,
        confirmText: confirmText,
        confirmHelpText: confirmHelpText,
        confirmColor: confirmColor,
        cancelColor: cancelColor,
        onConfirm: onConfirm,
        onCancel: onCancel,
      );
    },
  );
}

Future<void> showCreateTicketDialog(
  BuildContext context, {
  required String examUid,
  required int ticketIndex,
}) async {
  showDialog(
    context: context,
    builder: (context) => CreateTicketDialog(examUid: examUid, ticketIndex: ticketIndex),
  );
}

Future<void> showDetailTicketDialog(
  BuildContext context, {
  required String examUid,
  required Ticket ticket,
}) async {
  showDialog(
    context: context,
    builder: (context) => DetailTicketDialog(examUid: examUid, ticket: ticket),
  );
}

Future<void> showCreateSessionDialog(
  BuildContext context, {
  required String examUid,
}) async {
  showDialog(
    context: context,
    builder: (context) => CreateSessionDialog(examUid: examUid),
  );
}

Future<void> showDetailSessionDialog(
  BuildContext context, {
  required String examUid,
  required Session session,
}) async {
  showDialog(
    context: context,
    builder: (context) => DetailSessionDialog(examUid: examUid, session: session),
  );
}

Future<DateTime?> showDateTimePicker(
  BuildContext context, {
  DateTime? initialDate,
  DateTime? firstDate,
  DateTime? lastDate,
  String? dateHelpText,
  String? timeHelpText,
}) async {
  initialDate ??= DateTime.now();
  firstDate ??= initialDate.subtract(const Duration(days: 365 * 100));
  lastDate ??= firstDate.add(const Duration(days: 365 * 200));

  DateTime? selectedDate = await showDatePicker(
    context: context,
    initialDate: initialDate,
    firstDate: firstDate,
    lastDate: lastDate,
    helpText: dateHelpText,
    confirmText: 'Выбрать время',
  );

  if (selectedDate == null) return null;
  if (!context.mounted) return selectedDate;

  TimeOfDay? selectedTime;
  while (true) {
    if (!context.mounted) continue;
    selectedTime = await showTimePicker(
      context: context,
      initialTime: TimeOfDay.fromDateTime(initialDate),
      helpText: timeHelpText,
      confirmText: 'Готово',
      cancelText: 'Назад',
    );
    if (selectedTime == null && context.mounted) {
      selectedDate = await showDatePicker(
        context: context,
        initialDate: selectedDate,
        firstDate: firstDate,
        lastDate: lastDate,
        helpText: dateHelpText,
        confirmText: 'Выбрать время',
      );
      if (selectedDate == null) return null;
    }
    if (selectedTime != null) break;
  }

  return DateTime(
    selectedDate!.year,
    selectedDate.month,
    selectedDate.day,
    selectedTime.hour,
    selectedTime.minute,
  );
}
