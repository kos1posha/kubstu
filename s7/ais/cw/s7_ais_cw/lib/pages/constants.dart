import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

ShapeBorder shape = RoundedRectangleBorder(
  borderRadius: BorderRadius.circular(6),
);

TextStyle cardTitleStyle = const TextStyle(
  fontSize: 22,
  fontWeight: FontWeight.bold,
);

TextStyle cardSubtitleStyle = TextStyle(
  color: Colors.grey[600],
);

TextStyle inputTextStyle = const TextStyle(
  fontSize: 16,
  fontWeight: FontWeight.w500,
);

class UpperCaseTextFormatter extends TextInputFormatter {
  @override
  TextEditingValue formatEditUpdate(TextEditingValue oldValue, TextEditingValue newValue) {
    return TextEditingValue(
      text: newValue.text.toUpperCase(),
      selection: newValue.selection,
    );
  }
}
