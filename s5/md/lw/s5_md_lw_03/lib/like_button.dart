import 'package:flutter/material.dart';

class LikeButton extends StatefulWidget {
  const LikeButton({Key? key}) : super(key: key);

  @override
  State<LikeButton> createState() => _LikeButtonState();
}

class _LikeButtonState extends State<LikeButton>
    with SingleTickerProviderStateMixin {
  late final AnimationController _controller = AnimationController(
      duration: const Duration(milliseconds: 200), vsync: this, value: 1.0
  );

  bool _isFavorite = false;
  int _favouritesCounter = 26;

  @override
  void dispose() {
    super.dispose();
    _controller.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        setState(() {
          _isFavorite = !_isFavorite;
          _favouritesCounter += _isFavorite ? 1 : -1;
        });
        _controller.reverse().then((value) => _controller.forward());
      },
      child: Row(
        children: [
          ScaleTransition(
            scale: Tween(begin: 0.7, end: 1.0).animate(CurvedAnimation(parent: _controller, curve: Curves.easeOut)),
            child: _isFavorite
                ? const Icon(Icons.favorite, size: 25, color: Colors.red)
                : const Icon(Icons.favorite_border, size: 25),
          ),
          Padding(padding: EdgeInsets.only(left: 3)),
          Text(_favouritesCounter.toString(), style: TextStyle(fontSize: 18)),
        ],
      ),
    );
  }
}