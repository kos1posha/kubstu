import 'dart:async';

import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/material.dart';
import 'package:path/path.dart' as path;

class AudioPlayerPage extends StatefulWidget {
  const AudioPlayerPage({super.key});

  @override
  State<AudioPlayerPage> createState() => AudioPlayerPageState();
}

class AudioPlayerPageState extends State<AudioPlayerPage> {
  late Color primaryColor = Theme.of(context).primaryColor;

  late AudioPlayer player = AudioPlayer();

  @override
  void initState() {
    super.initState();
    player = AudioPlayer();
    player.setReleaseMode(ReleaseMode.stop);
    _playerState = player.state;
    _durationSubscription = player.onDurationChanged.listen((duration) => setState(() => _duration = duration));
    _positionSubscription = player.onPositionChanged.listen((p) => setState(() => _position = p));
    _playerStateChangeSubscription = player.onPlayerStateChanged.listen((state) => setState(() => _playerState = state));
    _playerCompleteSubscription = player.onPlayerComplete.listen((event) {
      setState(() {
        _playerState = PlayerState.stopped;
        _position = Duration.zero;
      });
    });
  }

  @override
  void dispose() {
    player.dispose();
    _durationSubscription?.cancel();
    _positionSubscription?.cancel();
    _playerCompleteSubscription?.cancel();
    _playerStateChangeSubscription?.cancel();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Аудио-проигрыватель'),
        foregroundColor: Colors.white,
        backgroundColor: primaryColor,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          children: [
            buildAudioPlayerWidget(),
            const Divider(height: 2),
            buildAudioFileList(),
          ],
        ),
      ),
    );
  }

  PlayerState? _playerState;
  Duration? _duration;
  Duration? _position;

  StreamSubscription? _durationSubscription;
  StreamSubscription? _positionSubscription;
  StreamSubscription? _playerStateChangeSubscription;
  StreamSubscription? _playerCompleteSubscription;

  bool get _isPlaying => _playerState == PlayerState.playing;
  bool get _isPaused => _playerState == PlayerState.paused;
  String get _durationText => _duration?.toString().split('.').first ?? '';
  String get _positionText => _position?.toString().split('.').first ?? '';

  Future<void> _play([String? sourcePath]) async {
    if (sourcePath != null) {
      await player.setSourceAsset(sourcePath);
    }
    await player.resume();
    setState(() => _playerState = PlayerState.playing);
  }

  Future<void> _pause() async {
    await player.pause();
    setState(() => _playerState = PlayerState.paused);
  }

  Future<void> _stop() async {
    await player.stop();
    setState(() {
      _playerState = PlayerState.stopped;
      _position = Duration.zero;
    });
  }

  Widget buildAudioPlayerWidget() {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            IconButton(
              key: const Key('play_button'),
              onPressed: _isPlaying ? null : _play,
              color: primaryColor,
              icon: const Icon(Icons.play_arrow),
              iconSize: 48,
            ),
            IconButton(
              key: const Key('pause_button'),
              onPressed: _isPlaying ? _pause : null,
              color: primaryColor,
              icon: const Icon(Icons.pause),
              iconSize: 48,
            ),
            IconButton(
              key: const Key('stop_button'),
              onPressed: _isPlaying || _isPaused ? _stop : null,
              color: primaryColor,
              icon: const Icon(Icons.stop),
              iconSize: 48,
            ),
          ],
        ),
        Slider(
          onChanged: (value) {
            final duration = _duration;
            if (duration == null) return;
            final position = value * duration.inMilliseconds;
            player.seek(Duration(milliseconds: position.round()));
          },
          value: (_position != null && _duration != null && _position!.inMilliseconds > 0 && _position!.inMilliseconds < _duration!.inMilliseconds)
              ? _position!.inMilliseconds / _duration!.inMilliseconds
              : 0,
        ),
        Text(
          _position != null
              ? '$_positionText / $_durationText'
              : _duration != null
                  ? _durationText
                  : '',
          style: const TextStyle(fontSize: 16),
        ),
      ],
    );
  }

  List<String> assetAudioFiles = [
    'assets/music/Канцлер Ги - Гимн наемников.mp3',
    'assets/music/Канцлер Ги - Дикая охота.mp3',
    'assets/music/Канцлер ГИ - Слёзы и кровь.mp3',
    'assets/samples/sample-12s.wav',
    'assets/samples/sample-15s.wav',
  ];

  Widget buildAudioFileList() {
    return ListView.builder(
      shrinkWrap: true,
      itemCount: assetAudioFiles.length,
      itemBuilder: (context, index) {
        return InkWell(
          onTap: () => _play(assetAudioFiles[index].substring(7)),
          child: ListTile(
            leading: const Icon(Icons.audio_file),
            title: Text(path.basenameWithoutExtension(assetAudioFiles[index])),
            subtitle: Text(assetAudioFiles[index]),
          ),
        );
      },
    );
  }
}
