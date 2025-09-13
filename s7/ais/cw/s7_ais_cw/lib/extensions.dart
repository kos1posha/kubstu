extension MapExtension<K, V> on Map<K, V> {
  V? get(K key, [V? defaultValue]) {
    return containsKey(key) ? this[key] : defaultValue;
  }
}

extension StringExtension on String {
  String center(int width, [String fill = ' ']) {
    if (length >= width) {
      return this;
    }
    int totalPadding = width - length;
    int padLeft = totalPadding ~/ 2;
    int padRight = totalPadding - padLeft;
    return '${fill * padLeft}$this${fill * padRight}';
  }
}
