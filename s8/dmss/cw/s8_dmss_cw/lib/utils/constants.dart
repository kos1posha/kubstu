import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/theme.dart';

// border radius
BorderRadius circularBorderRadius = BorderRadius.circular(30);
BorderRadius roundedBorderRadius = BorderRadius.circular(16);

// padding
const EdgeInsets scaffoldBodyPadding = EdgeInsets.fromLTRB(18, 0, 16, 16);

// text styles
const TextStyle logoTextStyle = TextStyle(
  color: MainTheme.primary,
  fontSize: 48,
  fontWeight: FontWeight.bold,
);
const TextStyle titleTextStyle = TextStyle(
  fontSize: 24,
  fontWeight: FontWeight.bold,
);
const TextStyle subtitleTextStyle = TextStyle(
  color: MainTheme.tertiary,
  fontSize: 18,
);
const TextStyle secondaryTextStyle = TextStyle(
  color: MainTheme.neural,
  fontSize: 15,
);

// dividers
const SizedBox groupVDivider = SizedBox(height: 32);
const SizedBox groupHDivider = SizedBox(width: 32);
const SizedBox mediumVDivider = SizedBox(height: 16);
const SizedBox mediumHDivider = SizedBox(width: 16);
const SizedBox smallVDivider = SizedBox(height: 8);
const SizedBox smallHDivider = SizedBox(width: 8);

// password special characters
const String specialCharacters = '!#\$%&()*+,-./:;<=>?@[\\]^_`{|}~';
RegExp specialCharactersRegExp = RegExp(r'[!#\$%&\(\)\*\+,-./:;<=>\?@\[\]\^_`{|}~]');
