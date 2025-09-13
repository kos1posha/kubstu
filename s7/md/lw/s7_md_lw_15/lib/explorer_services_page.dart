import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:s7_md_lw_15/audio_player_page.dart';
import 'package:s7_md_lw_15/text_editor_page.dart';
import 'package:s7_md_lw_15/video_player_page.dart';

class ExplorerServicesPage extends StatefulWidget {
  const ExplorerServicesPage({super.key});

  @override
  State<ExplorerServicesPage> createState() => ExplorerServicesPageState();
}

class ExplorerServicesPageState extends State<ExplorerServicesPage> {
  late Color primaryColor = Theme.of(context).primaryColor;

  Widget buildServiceRouteButton({required void Function()? onPressed, required String labelText, required IconData iconData}) {
    return Expanded(
      child: SizedBox(
        width: double.infinity,
        child: ElevatedButton.icon(
          style: ButtonStyle(
            shape: WidgetStateProperty.all(
              RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
            ),
            backgroundColor: WidgetStateProperty.all(primaryColor),
          ),
          onPressed: onPressed,
          label: Text(labelText, style: const TextStyle(color: Colors.white, fontSize: 24)),
          icon: Icon(iconData, color: Colors.white, size: 28),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Файловые сервисы'),
        foregroundColor: Colors.white,
        backgroundColor: primaryColor,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            buildServiceRouteButton(
              onPressed: () {
                Navigator.of(context).push(CupertinoPageRoute(builder: (context) => const AudioPlayerPage()));
              },
              labelText: 'Аудио-проигрыватель',
              iconData: Icons.audiotrack,
            ),
            const SizedBox(height: 16),
            buildServiceRouteButton(
              onPressed: () {
                Navigator.of(context).push(CupertinoPageRoute(builder: (context) => const VideoPlayerPage()));
              },
              labelText: 'Видео-проигрыватель',
              iconData: Icons.video_library,
            ),
            const SizedBox(height: 16),
            buildServiceRouteButton(
              onPressed: () {
                Navigator.of(context).push(CupertinoPageRoute(builder: (context) => const TextEditorPage()));
              },
              labelText: 'Текстовый редактор',
              iconData: Icons.edit_document,
            ),
          ],
        ),
      ),
    );
  }
}
