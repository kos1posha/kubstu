import 'dart:async';
import 'dart:math';

import 'package:flutter/material.dart';

class Star {
  Offset position;
  double radius;
  double brightness;
  int twinkle = 1;
  double twinkleSpeed;

  Star({required this.position, required this.radius, required this.brightness, required this.twinkleSpeed});

  static List<Star> generate(int count, double width, double height) {
    return List.generate(count, (index) {
      return Star(
        position: Offset(Random().nextDouble() * width, Random().nextDouble() * height),
        radius: Random().nextDouble() * 2 + 1,
        brightness: Random().nextDouble(),
        twinkleSpeed: (Random().nextDouble() * 2 + 2) * 0.01,
      );
    });
  }

  static void startTwinkle(List<Star> stars) {
    Timer.periodic(const Duration(milliseconds: 80), (timer) {
      for (Star star in stars) {
        star.brightness += star.twinkle * star.twinkleSpeed;
        if (star.brightness < 0.04) {
          star.twinkle = 1;
        } else if (star.brightness > 0.96) {
          star.twinkle = -1;
        }
      }
    });
  }
}

class Ship {
  Offset position;
  double angle = 0;
  int rotate = 0;
  int speed = 0;
  int flyingSpriteState = 1;

  String get sprite => speed == 0 ? 'assets/ship_staying.png' : 'assets/ship_flying_$flyingSpriteState.png';

  Ship({required this.position});

  void rotateOrientation(Orientation orientation) {
    position = Offset(position.dy, position.dx);
    angle += (orientation == Orientation.portrait ? -90 : 90) * pi / 180;
  }

  void launchEngine(Function setState) {
    Timer.periodic(const Duration(milliseconds: 25), (timer) {
      setState(() {
        angle += rotate * 0.10;
        position = position.translate(speed * sin(angle), -speed * cos(angle));
      });
    });
    Timer.periodic(const Duration(milliseconds: 100), (timer) {
      setState(() {
        flyingSpriteState = flyingSpriteState == 1 ? 2 : 1;
      });
    });
  }
}
