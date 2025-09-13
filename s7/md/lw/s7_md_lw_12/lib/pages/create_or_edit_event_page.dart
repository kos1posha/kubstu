import 'package:flutter/material.dart';
import 'package:flutter_colorpicker/flutter_colorpicker.dart';
import 'package:flutter_iconpicker/Models/configuration.dart';
import 'package:flutter_iconpicker/flutter_iconpicker.dart';
import 'package:s7_md_lw_12/constants.dart';
import 'package:s7_md_lw_12/event.dart';
import 'package:s7_md_lw_12/pages/events_page.dart';

class CreateOrEditEventPage extends StatefulWidget {
  final EventsPageState parent;
  final Event? event;

  const CreateOrEditEventPage({super.key, required this.parent, this.event});

  @override
  State<CreateOrEditEventPage> createState() => CreateOrEditEventPageState();
}

class CreateOrEditEventPageState extends State<CreateOrEditEventPage> {
  late Color primaryColor = Theme.of(context).primaryColor;

  bool get isNewEvent => widget.event == null;
  Event get event => widget.event ?? newEvent;
  Event newEvent = Event();

  late TextEditingController dateController = TextEditingController(text: event.datef);
  late TextEditingController timeController = TextEditingController(text: event.timef);

  Future<void> showEventIconPickerDialog() async {
    IconPickerIcon? icon = await showIconPicker(
      context,
      configuration: const SinglePickerConfiguration(
        title: Text('Выберите иконку'),
        searchHintText: 'Поиск',
        noResultsText: 'Иконки не найдены',
        closeChild: Text('Закрыть'),
        shouldScrollToSelectedIcon: true,
      ),
    );
    event.icon = icon?.data;
  }

  Future<void> showEventColorPickerDialog() async {
    showDialog(
      context: context,
      builder: (context) => AlertDialog(
        title: const Text('Выберите цвет'),
        content: SingleChildScrollView(
          child: ColorPicker(
            pickerColor: event.color ?? Colors.grey,
            onColorChanged: (value) => setState(() => event.color = value),
          ),
        ),
        actions: [
          ElevatedButton(
            child: const Text('Принять'),
            onPressed: () => Navigator.of(context).pop(),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: primaryColor,
        leading: IconButton(
          onPressed: () {
            Navigator.of(context).pop();
            widget.parent.setState(() {});
          },
          icon: const Icon(Icons.arrow_back, color: Colors.white),
        ),
        title: Text(
          isNewEvent ? 'Добавить событие' : 'Изменить событие',
          style: const TextStyle(color: Colors.white),
        ),
      ),
      body: SingleChildScrollView(
        reverse: true,
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Column(
            children: [
              Row(
                children: [
                  Expanded(
                    child: TextFormField(
                      readOnly: true,
                      decoration: InputDecoration(
                        border: const OutlineInputBorder(),
                        hintText: event.color == null ? 'Без цвета' : 'Изменить цвет',
                        hintStyle: const TextStyle(fontWeight: FontWeight.normal),
                        prefixIcon: event.color == null ? const Icon(Icons.add) : Icon(Icons.circle, color: event.color),
                      ),
                      onTap: showEventColorPickerDialog,
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: TextFormField(
                      readOnly: true,
                      decoration: InputDecoration(
                        border: const OutlineInputBorder(),
                        hintText: event.icon == null ? 'Без иконки' : 'Изменить иконку',
                        hintStyle: const TextStyle(fontWeight: FontWeight.normal),
                        prefixIcon: event.icon == null ? const Icon(Icons.add) : Icon(event.icon),
                      ),
                      onTap: showEventIconPickerDialog,
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              Row(
                children: [
                  Expanded(
                    child: TextFormField(
                      readOnly: true,
                      controller: dateController,
                      decoration: const InputDecoration(
                        border: OutlineInputBorder(),
                        label: Text('Дата'),
                        hintText: 'дд.мм.гггг',
                        hintStyle: TextStyle(fontWeight: FontWeight.normal),
                        prefixIcon: Icon(Icons.calendar_today),
                      ),
                      onTap: () async {
                        DateTime? date = await showDatePicker(
                          context: context,
                          initialDate: event.date ?? DateTime.now(),
                          firstDate: DateTime(1970),
                          lastDate: DateTime(2070),
                          locale: const Locale('ru'),
                        );
                        if (date == null) return;
                        setState(() {
                          event.date = date;
                          dateController.text = event.datef;
                        });
                      },
                    ),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: TextFormField(
                      readOnly: true,
                      controller: timeController,
                      decoration: const InputDecoration(
                        border: OutlineInputBorder(),
                        label: Text('Время'),
                        hintText: 'чч:мм',
                        hintStyle: TextStyle(fontWeight: FontWeight.normal),
                        prefixIcon: Icon(Icons.access_time),
                      ),
                      onTap: () async {
                        TimeOfDay? time = await showTimePicker(
                          context: context,
                          initialTime: event.time ?? TimeOfDay.now(),
                        );
                        if (time == null) return;
                        setState(() {
                          event.time = time;
                          timeController.text = event.timef;
                        });
                      },
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              TextFormField(
                initialValue: event.title == 'Без названия' ? '' : event.title,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  label: Text('Название'),
                ),
                onChanged: (value) => event.title = value,
              ),
              const SizedBox(height: 16),
              TextFormField(
                minLines: 3,
                maxLines: 5,
                initialValue: event.description,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                  label: Text('Описание'),
                ),
                onChanged: (value) => event.description = value,
              ),
              const SizedBox(height: 16),
              if (isNewEvent)
                SizedBox(
                  width: double.infinity,
                  height: 50,
                  child: ElevatedButton(
                    style: ButtonStyle(
                      backgroundColor: WidgetStateProperty.all(primaryColor),
                      foregroundColor: WidgetStateProperty.all(Colors.white),
                      shape: WidgetStateProperty.all(
                        RoundedRectangleBorder(borderRadius: borderRadius),
                      ),
                    ),
                    onPressed: () {
                      widget.parent.setState(() {
                        widget.parent.events.add(newEvent);
                        Navigator.pop(context);
                      });
                    },
                    child: const Text('Создать'),
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
