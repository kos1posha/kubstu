import 'dart:io';
import 'dart:convert';
import 'dart:typed_data';

import 'package:flutter/material.dart';
import 'package:file_picker/file_picker.dart';
import 'package:path/path.dart' as path;

class TextEditorPage extends StatefulWidget {
  const TextEditorPage({super.key});

  @override
  State<TextEditorPage> createState() => TextEditorPageState();
}

class TextEditorPageState extends State<TextEditorPage> {
  late Color primaryColor = Theme.of(context).primaryColor;

  String _filePath = '';
  final TextEditingController _pathController = TextEditingController(text: 'Файл не выбран');
  final TextEditingController _textController = TextEditingController();

  Future<void> _pickFile() async {
    FilePickerResult? result = await FilePicker.platform.pickFiles(
      type: FileType.custom,
      allowedExtensions: ['txt'],
      withData: true,
    );
    if (result != null) {
      setState(() {
        _filePath = result.files.single.path!;
        _pathController.text = _filePath;
        _loadFileContent();
      });
    }
  }

  void _loadFileContent() async {
    if (_filePath.isNotEmpty) {
      final file = File(_filePath);
      _textController.text = file.readAsStringSync();
    }
  }

  void _saveAsFile() async {
    Uint8List bytes = utf8.encode(_textController.text);
    await FilePicker.platform.saveFile(
      dialogTitle: 'Сохранить файл',
      fileName: path.basename(_filePath),
      type: FileType.custom,
      allowedExtensions: ['txt'],
      bytes: bytes,
    );
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(content: Text('Файл успешно сохранен')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Текстовый редактор'),
        foregroundColor: Colors.white,
        backgroundColor: primaryColor,
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              children: [
                Expanded(
                  child: TextFormField(
                    controller: _pathController,
                    readOnly: true,
                  ),
                ),
                TextButton(
                  onPressed: _pickFile,
                  child: const Text('Обзор'),
                ),
              ],
            ),
            const SizedBox(height: 16),
            Expanded(
              child: TextField(
                controller: _textController,
                maxLines: null,
                expands: true,
                readOnly: _filePath == '',
                decoration: const InputDecoration(border: InputBorder.none),
              ),
            ),
            const SizedBox(height: 16),
            Visibility(
              visible: _filePath != '',
              child: ElevatedButton(
                onPressed: _saveAsFile,
                child: const Text('Сохранить как'),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
