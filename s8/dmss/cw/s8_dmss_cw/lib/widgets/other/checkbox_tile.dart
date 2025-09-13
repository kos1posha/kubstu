import 'package:flutter/material.dart';

class CheckboxTile extends StatelessWidget {
  const CheckboxTile({super.key, required this.child, this.subchild, required this.value, required this.onChanged});

  final Widget? child;
  final Widget? subchild;
  final bool value;
  final void Function(bool?) onChanged;

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () async => onChanged(!value),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Checkbox(
            value: value,
            onChanged: onChanged,
            visualDensity: const VisualDensity(horizontal: -4, vertical: -4),
            splashRadius: 8,
          ),
          const SizedBox(width: 4),
          if (subchild != null) Padding(padding: const EdgeInsets.only(top: 2), child: subchild!),
          if (child != null) Expanded(child: Padding(padding: const EdgeInsets.only(top: 2), child: child!)),
        ],
      ),
    );
  }
}
