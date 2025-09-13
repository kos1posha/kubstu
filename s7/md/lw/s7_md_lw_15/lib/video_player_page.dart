import 'dart:async';
import 'package:flutter/material.dart';
import 'package:video_player/video_player.dart';
import 'package:path/path.dart' as path;

class VideoPlayerPage extends StatefulWidget {
  const VideoPlayerPage({super.key});

  @override
  State<VideoPlayerPage> createState() => VideoPlayerPageState();
}

class VideoPlayerPageState extends State<VideoPlayerPage> {
  late Color primaryColor = Theme.of(context).primaryColor;

  late VideoPlayerController _controller;
  late Future<void> _initializeVideoPlayerFuture;

  @override
  void initState() {
    super.initState();
    _controller = VideoPlayerController.asset('');
    _initializeVideoPlayerFuture = _controller.initialize();
    _controller.setLooping(false);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Видео-проигрыватель'),
        foregroundColor: Colors.white,
        backgroundColor: primaryColor,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            buildVideoPlayerWidget(),
            const SizedBox(height: 16),
            const Divider(height: 2),
            buildVideoFileList(),
          ],
        ),
      ),
    );
  }

  Widget buildVideoPlayerWidget() {
    return Column(
      children: [
        SizedBox(
          height: 200,
          child: FutureBuilder(
            future: _initializeVideoPlayerFuture,
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.done) {
                return AspectRatio(
                  aspectRatio: _controller.value.aspectRatio,
                  child: VideoPlayer(_controller),
                );
              } else {
                return const Center(
                  child: Text(
                    '...',
                    style: TextStyle(color: Colors.grey, fontSize: 40),
                  ),
                );
              }
            },
          ),
        ),
        Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            IconButton(
              key: const Key('play_button'),
              onPressed: _controller.value.isPlaying ? null : _play,
              color: primaryColor,
              icon: const Icon(Icons.play_arrow),
              iconSize: 48,
            ),
            IconButton(
              key: const Key('pause_button'),
              onPressed: _controller.value.isPlaying ? _pause : null,
              color: primaryColor,
              icon: const Icon(Icons.pause),
              iconSize: 48,
            ),
            IconButton(
              key: const Key('stop_button'),
              onPressed: _controller.value.isPlaying || _controller.value.isInitialized ? _stop : null,
              color: primaryColor,
              icon: const Icon(Icons.stop),
              iconSize: 48,
            ),
          ],
        ),
      ],
    );
  }

  Future<void> _play() async {
    await _controller.play();
    setState(() {});
  }

  Future<void> _pause() async {
    await _controller.pause();
    setState(() {});
  }

  Future<void> _stop() async {
    await _controller.pause();
    await _controller.seekTo(Duration.zero);
    setState(() {});
  }

  List<String> assetVideoFiles = [
    'assets/videos/SampleVideo_1280x720_2mb.mp4',
    'assets/videos/street_and_trees.mp4',
  ];

  Widget buildVideoFileList() {
    return ListView.builder(
      shrinkWrap: true,
      itemCount: assetVideoFiles.length,
      itemBuilder: (context, index) {
        return InkWell(
          onTap: () {
            _controller.pause();
            _controller.dispose();
            _controller = VideoPlayerController.asset(assetVideoFiles[index]);
            _initializeVideoPlayerFuture = _controller.initialize();
            _controller.setLooping(false);
            _play();
          },
          child: ListTile(
            leading: const Icon(Icons.video_file),
            title: Text(path.basenameWithoutExtension(assetVideoFiles[index])),
            subtitle: Text(assetVideoFiles[index]),
          ),
        );
      },
    );
  }
}
