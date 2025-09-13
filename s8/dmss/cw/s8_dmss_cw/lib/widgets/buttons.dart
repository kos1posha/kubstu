import 'package:adaptive_theme/adaptive_theme.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:s8_dmss_cw/utils/constants.dart';
import 'package:s8_dmss_cw/theme.dart';
import 'package:s8_dmss_cw/widgets/other/mounted_state.dart';

class BackIconButton extends StatelessWidget {
  const BackIconButton({
    super.key,
    this.onPressed,
    required this.child,
  });

  final void Function()? onPressed;
  final Widget child;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 60,
      child: TextButton.icon(
        onPressed: onPressed,
        label: Center(
          child: Wrap(children: [child, const SizedBox(width: 28)]),
        ),
        icon: Container(
          width: 60,
          height: 60,
          decoration: const BoxDecoration(
            color: Colors.white12,
            shape: BoxShape.circle,
          ),
          child: const Icon(Icons.arrow_back),
        ),
        style: const ButtonStyle(
          padding: WidgetStatePropertyAll(EdgeInsets.zero),
        ),
      ),
    );
  }
}

class CircularBorderButton extends StatelessWidget {
  const CircularBorderButton({
    super.key,
    this.isPrimary = false,
    this.isRounded = false,
    this.onPressed,
    this.child,
  });

  final bool isPrimary;
  final bool isRounded;
  final void Function()? onPressed;
  final Widget? child;

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: 60,
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          textStyle: const TextStyle(fontSize: 17),
          shape: RoundedRectangleBorder(borderRadius: isRounded ? roundedBorderRadius : circularBorderRadius),
          foregroundColor: isPrimary ? Colors.white : null,
          backgroundColor: isPrimary ? MainTheme.tertiary : null,
        ),
        onPressed: onPressed,
        child: child,
      ),
    );
  }
}

class Link extends StatefulWidget {
  const Link(
    this.data, {
    super.key,
    this.onPressed,
    this.style,
    this.textAlign,
  });

  final void Function()? onPressed;
  final String data;
  final TextStyle? style;
  final TextAlign? textAlign;

  @override
  MountedState<Link> createState() => _LinkState();
}

class _LinkState extends MountedState<Link> {
  @override
  Widget build(BuildContext context) {
    return InkWell(
      enableFeedback: false,
      focusColor: Colors.transparent,
      hoverColor: Colors.transparent,
      highlightColor: Colors.transparent,
      splashColor: Colors.transparent,
      onTap: widget.onPressed,
      child: Text(
        widget.data,
        style: const TextStyle(color: MainTheme.secondary, fontSize: 16, fontWeight: FontWeight.bold).merge(widget.style),
        textAlign: widget.textAlign,
      ),
    );
  }
}

class ToggleThemeFab extends StatelessWidget {
  const ToggleThemeFab({super.key});

  @override
  Widget build(BuildContext context) {
    AdaptiveThemeMode adaptiveThemeMode = AdaptiveTheme.of(context).mode;
    return FloatingActionButton(
      backgroundColor: switch (adaptiveThemeMode) {
        AdaptiveThemeMode.system => null,
        AdaptiveThemeMode.light => Colors.blue[100],
        AdaptiveThemeMode.dark => Colors.deepPurple[900],
      },
      onPressed: () async => AdaptiveTheme.of(context).toggleThemeMode(useSystem: true),
      child: AnimatedSwitcher(
        duration: Durations.medium2,
        child: KeyedSubtree(
          key: ValueKey(adaptiveThemeMode),
          child: switch (AdaptiveTheme.of(context).mode) {
            AdaptiveThemeMode.system => Icon(Icons.brightness_auto, color: adaptiveColor(context, Colors.white, Colors.black87)),
            AdaptiveThemeMode.light => const Icon(Icons.light_mode, color: Colors.amber),
            AdaptiveThemeMode.dark => const Icon(Icons.dark_mode, color: Colors.white),
          },
        ),
        transitionBuilder: (Widget child, Animation<double> animation) {
          Animation<double> rotation = Tween<double>(begin: 0.9, end: 1.0).animate(animation);
          return RotationTransition(
            turns: rotation,
            child: FadeTransition(
              opacity: animation,
              child: child,
            ),
          );
        },
      ),
    );
  }
}

class CopyLinkButton extends StatefulWidget {
  const CopyLinkButton({
    super.key,
    required this.link,
    this.tooltipText = 'Ссылка скопирована!',
    this.iconSize = 24,
    this.iconColor,
  });

  final String link;
  final String tooltipText;
  final double iconSize;
  final Color? iconColor;

  @override
  State<CopyLinkButton> createState() => _CopyLinkButtonState();
}

class _CopyLinkButtonState extends State<CopyLinkButton> {
  bool _isCopied = false;
  OverlayEntry? _overlayEntry;

  @override
  void dispose() {
    _removeOverlay();
    super.dispose();
  }

  void _removeOverlay() {
    _overlayEntry?.remove();
    _overlayEntry = null;
  }

  void _showTooltip(BuildContext context) {
    final RenderBox renderBox = context.findRenderObject() as RenderBox;
    final position = renderBox.localToGlobal(Offset.zero);
    _overlayEntry = OverlayEntry(
      builder: (context) {
        return Positioned(
          left: position.dx - 160,
          top: position.dy + 4,
          child: Material(
            color: Colors.transparent,
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 8),
              decoration: BoxDecoration(
                color: Colors.black12,
                borderRadius: BorderRadius.circular(4),
              ),
              child: Text(
                widget.tooltipText,
                style: TextStyle(
                  color: adaptiveColor(context),
                  fontSize: 12,
                ),
              ),
            ),
          ),
        );
      },
    );
    Overlay.of(context).insert(_overlayEntry!);
  }

  Future<void> _copyToClipboard() async {
    await Clipboard.setData(ClipboardData(text: widget.link));
    setState(() => _isCopied = true);
    if (mounted) _showTooltip(context);
    Future.delayed(const Duration(seconds: 3), () {
      if (mounted) {
        setState(() => _isCopied = false);
        _removeOverlay();
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return IconButton(
      icon: AnimatedSwitcher(
        duration: Durations.short4,
        transitionBuilder: (child, animation) {
          return FadeTransition(
            opacity: animation,
            child: child,
          );
        },
        child: _isCopied
            ? Icon(
                Icons.done_rounded,
                key: const ValueKey('done'),
                size: widget.iconSize,
              )
            : Icon(
                Icons.link_rounded,
                key: const ValueKey('link'),
                size: widget.iconSize,
              ),
      ),
      color: widget.iconColor ?? Theme.of(context).iconTheme.color,
      onPressed: _copyToClipboard,
    );
  }
}
