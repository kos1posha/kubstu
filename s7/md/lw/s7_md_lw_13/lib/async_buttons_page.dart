import 'package:flutter/material.dart';

class AsyncButtonsPage extends StatefulWidget {
  const AsyncButtonsPage({super.key});

  @override
  State<AsyncButtonsPage> createState() => _AsyncButtonsPageState();
}

class _AsyncButtonsPageState extends State<AsyncButtonsPage> {
  late Color primaryColor = Theme.of(context).primaryColor;

  int dimension = 4;
  late List<bool> asyncLoadingList = List.filled(dimension * dimension, false);

  final List<int> durations = [100, 200, 300, 400, 500, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000];
  int selectedDurationIndex = 7;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Асинхронные кнопки'),
        foregroundColor: Colors.white,
        backgroundColor: primaryColor,
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 16),
        child: Column(
          children: [
            Row(
              children: [
                const Text('Время загрузки'),
                Expanded(
                  child: Slider(
                    value: selectedDurationIndex.toDouble(),
                    min: 0,
                    max: durations.length - 1,
                    divisions: durations.length - 1,
                    label: '${durations[selectedDurationIndex]} ms',
                    onChanged: (value) => setState(() => selectedDurationIndex = value.toInt()),
                  ),
                ),
              ],
            ),
            const SizedBox(height: 16),
            GridView.builder(
              shrinkWrap: true,
              gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
                mainAxisSpacing: 10,
                crossAxisSpacing: 10,
                childAspectRatio: 1,
                crossAxisCount: dimension,
              ),
              itemCount: asyncLoadingList.length,
              itemBuilder: (context, index) {
                return ElevatedButton(
                  style: ButtonStyle(
                    shape: WidgetStateProperty.all(
                      RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
                    ),
                    backgroundColor: WidgetStateProperty.all(Theme.of(context).primaryColor),
                    foregroundColor: WidgetStateProperty.all(Colors.white),
                  ),
                  onPressed: () async {
                    setState(() => asyncLoadingList[index] = true);
                    Future.delayed(
                      Duration(milliseconds: durations[selectedDurationIndex]),
                    ).whenComplete(
                      () => setState(() => asyncLoadingList[index] = false),
                    );
                  },
                  child: asyncLoadingList[index]
                      ? const CircularProgressIndicator(
                          color: Colors.white,
                          strokeWidth: 3,
                        )
                      : Text('${index + 1}', style: const TextStyle(fontSize: 24)),
                );
              },
            ),
          ],
        ),
      ),
    );
  }
}
