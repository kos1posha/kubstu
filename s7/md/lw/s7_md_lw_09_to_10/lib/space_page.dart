import 'dart:ui';
import 'package:flutter/material.dart';
import 'package:s7_md_lw_09_to_10/objects.dart';

class SpacePage extends StatefulWidget {
  const SpacePage({super.key});

  @override
  State<StatefulWidget> createState() => _SpacePageState();
}

class _SpacePageState extends State<SpacePage> with SingleTickerProviderStateMixin, WidgetsBindingObserver {
  List<Star> stars = Star.generate(300, screenWidth * 2, screenHeight * 2);
  Ship ship = Ship(position: const Offset(0, 0));

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    Star.startTwinkle(stars);
    ship.launchEngine(setState);
  }

  @override
  void didChangeMetrics() {
    setState(() {
      ship.rotateOrientation(MediaQuery.of(context).orientation);
    });
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.deepPurple.shade900,
      extendBodyBehindAppBar: true,
      appBar: AppBar(
        title: const Text('s7_md_lw_09'),
        foregroundColor: Colors.white,
        shadowColor: Colors.transparent,
        backgroundColor: Colors.transparent,
        elevation: 0,
      ),
      body: Padding(
        padding: const EdgeInsets.all(0),
        child: Column(
          children: [
            Expanded(
              child: Stack(
                children: [
                  CustomPaint(
                    size: Size.infinite,
                    painter: StarsPainter(stars),
                  ),
                  Transform.translate(
                    offset: ship.position,
                    child: Center(
                      child: Transform.rotate(
                        angle: ship.angle,
                        child: Image.asset(
                          ship.sprite,
                          width: 70,
                          height: 70,
                          fit: BoxFit.fitHeight,
                        ),
                      ),
                    ),
                  ),
                  Transform.translate(
                    offset: Offset(0, screenHeight - 75),
                    child: Padding(
                      padding: const EdgeInsets.all(16),
                      child: Row(
                        children: [
                          Expanded(
                            child: GestureDetector(
                              child: SizedBox(
                                height: 40,
                                child: Transform.translate(
                                  offset: ship.rotate == -1 ? const Offset(0, -10) : const Offset(0, 0),
                                  child: RotatedBox(
                                    quarterTurns: 1,
                                    child: Icon(
                                      Icons.arrow_drop_down_rounded,
                                      color: Colors.white,
                                      size: ship.rotate == -1 ? 70 : 50,
                                    ),
                                  ),
                                ),
                              ),
                              onLongPressDown: (_) async => setState(() => ship.rotate = -1),
                              onLongPressCancel: () async => setState(() => ship.rotate = 0),
                              onLongPressUp: () async => setState(() => ship.rotate = 0),
                            ),
                          ),
                          const SizedBox(width: 16),
                          Expanded(
                            child: GestureDetector(
                              child: SizedBox(
                                height: 40,
                                child: Transform.translate(
                                  offset: ship.speed != 0 ? const Offset(0, -10) : const Offset(0, 0),
                                  child: Icon(
                                    Icons.arrow_drop_up_rounded,
                                    color: Colors.white,
                                    size: ship.speed != 0 ? 70 : 50,
                                  ),
                                ),
                              ),
                              onLongPressDown: (_) async => setState(() => ship.speed = 6),
                              onLongPressCancel: () async => setState(() => ship.speed = 0),
                              onLongPressUp: () async => setState(() => ship.speed = 0),
                            ),
                          ),
                          const SizedBox(width: 16),
                          Expanded(
                            child: GestureDetector(
                              child: SizedBox(
                                height: 40,
                                child: Transform.translate(
                                  offset: ship.rotate == 1 ? const Offset(0, -10) : const Offset(0, 0),
                                  child: RotatedBox(
                                    quarterTurns: 1,
                                    child: Icon(
                                      Icons.arrow_drop_up_rounded,
                                      color: Colors.white,
                                      size: ship.rotate == 1 ? 70 : 50,
                                    ),
                                  ),
                                ),
                              ),
                              onLongPressDown: (_) async => setState(() => ship.rotate = 1),
                              onLongPressCancel: () async => setState(() => ship.rotate = 0),
                              onLongPressUp: () async => setState(() => ship.rotate = 0),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class StarsPainter extends CustomPainter {
  final List<Star> stars;

  StarsPainter(this.stars);

  @override
  void paint(Canvas canvas, Size size) {
    final Paint paint = Paint();
    for (Star star in stars) {
      paint.color = Colors.yellow.shade200.withOpacity(star.brightness);
      canvas.drawCircle(star.position, star.radius, paint);
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) {
    return true;
  }
}

double get screenPixelRatio => PlatformDispatcher.instance.views.first.devicePixelRatio;
double get screenWidthPixels => PlatformDispatcher.instance.views.first.physicalSize.width;
double get screenHeightPixels => PlatformDispatcher.instance.views.first.physicalSize.height;
double get screenWidth => (screenWidthPixels / screenPixelRatio);
double get screenHeight => (screenHeightPixels / screenPixelRatio);
