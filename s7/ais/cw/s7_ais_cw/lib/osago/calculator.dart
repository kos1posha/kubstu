abstract class OsagoCalculator {
  static int evalPreliminaryOsago({required int tb, required double km}) {
    return evalOsago(tb: tb, kt: 1, kbm: 1.17, kvs: 1, ks: 1, km: km, ko: 1, kp: 1);
  }

  static int evalOsago({
    required int tb,
    required double kt,
    required double kbm,
    required double kvs,
    required double ks,
    required double km,
    required double ko,
    required double kp,
    Map<String, double>? extras,
  }) {
    return (tb * kt * kbm * kvs * ks * km * ko * kp).toInt();
  }
}
