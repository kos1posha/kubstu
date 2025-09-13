import 'dart:async';

import 'package:dropdown_search/dropdown_search.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:intl/intl.dart';
import 'package:open_file/open_file.dart';
import 'package:s7_ais_cw/api.dart';
import 'package:s7_ais_cw/osago/calculator.dart';
import 'package:s7_ais_cw/osago/data.dart';
import 'package:s7_ais_cw/osago/template.dart';

import 'package:s7_ais_cw/pages/constants.dart';

class OsagoPage extends StatefulWidget {
  const OsagoPage({super.key});

  @override
  State<OsagoPage> createState() => _OsagoPageState();
}

class _OsagoPageState extends State<OsagoPage> {
  late Color primaryColor = Theme.of(context).primaryColor;

  int stepIndex = 0;
  List<({String title, double value})> steps = [
    (title: 'Автомобиль', value: 0.0),
    // (title: 'Документы', value: 0.125),
    // (title: 'Владелец', value: 0.25),
    // (title: 'Водители', value: 0.5),
    // (title: 'Страхователь', value: 0.75),
    // (title: 'ОСАГО', value: 1.0),
    (title: 'Документы', value: 0.5),
    (title: 'Готово!', value: 1.0),
  ];
  bool get canNextStep {
    return switch (stepIndex) {
      0 => canNextFirstStep,
      1 => canNextSecondStep,
      _ => true,
    };
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: primaryColor,
      appBar: AppBar(
        iconTheme: const IconThemeData(color: Colors.white),
        title: const Text(
          'Калькулятор ОСАГО',
          style: TextStyle(
            color: Colors.white,
            fontWeight: FontWeight.bold,
          ),
        ),
        leading: IconButton(
          icon: const Icon(Icons.arrow_back_rounded),
          onPressed: () {
            if (stepIndex == 0) {
              Navigator.pop(context);
            } else {
              setState(() => stepIndex -= 1);
            }
          },
        ),
        backgroundColor: primaryColor,
        // actions: [
        //   TextButton(
        //     child: const Text('Тест', style: TextStyle(color: Colors.white)),
        //     onPressed: () async {
        //       String? outputPath = await fillTestOsago();
        //       SnackBar snackBar;
        //       if (outputPath == null) {
        //         snackBar = const SnackBar(content: Text('Не удалить создать файл ОСАГО'));
        //       } else {
        //         snackBar = SnackBar(
        //           content: Text('Файл ОСАГО успешно создан: $outputPath'),
        //           action: SnackBarAction(
        //             label: 'Открыть',
        //             onPressed: () => OpenFile.open(outputPath),
        //           ),
        //         );
        //       }
        //       if (!context.mounted) return;
        //       ScaffoldMessenger.of(context).showSnackBar(snackBar);
        //     },
        //   ),
        // ],
      ),
      body: GestureDetector(
        onTap: () {
          FocusScopeNode currentFocus = FocusScope.of(context);
          if (!currentFocus.hasPrimaryFocus && currentFocus.focusedChild != null) {
            FocusManager.instance.primaryFocus!.unfocus();
          }
        },
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              buildStepsProgress(),
              const SizedBox(height: 6),
              Expanded(
                child: SingleChildScrollView(
                  child: Column(
                    children: [
                      switch (stepIndex) {
                        0 => buildVehicleStep(context),
                        1 => buildVehicleDocsStep(context),
                        2 => buildSussyDoneStep(context),
                        _ => const Center(
                            child: CircularProgressIndicator(
                              strokeWidth: 3,
                              color: Colors.white,
                            ),
                          ),
                      },
                      const SizedBox(height: 16),
                      if (stepIndex != 2)
                        Column(
                          children: [
                            SizedBox(
                              height: 50,
                              width: double.infinity,
                              child: ElevatedButton(
                                style: ButtonStyle(shape: WidgetStateProperty.all(shape as OutlinedBorder?)),
                                onPressed: canNextStep ? () => setState(() => stepIndex = ++stepIndex == steps.length ? 0 : stepIndex) : null,
                                child: const Text('Продолжить'),
                              ),
                            ),
                            const SizedBox(height: 16),
                          ],
                        ),
                    ],
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }

  // GENERAL

  Widget buildStepsProgress() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        TweenAnimationBuilder<double>(
          duration: Durations.extralong1,
          curve: Curves.easeInOut,
          tween: Tween<double>(begin: 0, end: steps[stepIndex].value),
          builder: (context, value, _) {
            return LinearProgressIndicator(
              value: value,
              color: Colors.white,
              minHeight: 10,
              borderRadius: BorderRadius.circular(4),
            );
          },
        ),
        const SizedBox(height: 4),
        Text(
          'Шаг ${stepIndex + 1}: ${steps[stepIndex].title}',
          style: const TextStyle(color: Colors.white, fontSize: 15),
        ),
      ],
    );
  }

  Widget buildPicker({
    required bool enabled,
    required String? selectedItem,
    required String hintText,
    required String emptyText,
    required FutureOr<List<String>> Function(String, LoadProps?)? items,
    void Function(String?)? onChanged,
    bool clearEnabled = true,
    bool showSearchBox = true,
  }) {
    return DropdownSearch<String>(
      enabled: enabled,
      selectedItem: selectedItem == '' ? null : selectedItem,
      suffixProps: DropdownSuffixProps(
        clearButtonProps: ClearButtonProps(
          isVisible: clearEnabled,
          icon: const Icon(Icons.close),
        ),
      ),
      decoratorProps: DropDownDecoratorProps(
        baseStyle: inputTextStyle,
        decoration: InputDecoration(
          border: const OutlineInputBorder(),
          hintText: hintText,
        ),
      ),
      popupProps: PopupProps.menu(
        fit: FlexFit.loose,
        showSearchBox: showSearchBox,
        emptyBuilder: (context, searchEntry) {
          return SizedBox(
            height: 70,
            child: Center(
              child: Text(emptyText, style: const TextStyle(fontSize: 20)),
            ),
          );
        },
      ),
      items: items,
      onChanged: onChanged,
    );
  }

  TextField buildTextField({
    required bool enabled,
    required TextEditingController? controller,
    required String hintText,
    bool readOnly = false,
    void Function()? onTap,
    void Function(String)? onChanged,
    void Function()? onEditingComplete,
    TextInputType keyboardType = TextInputType.text,
    TextCapitalization textCapitalization = TextCapitalization.none,
    List<TextInputFormatter>? inputFormatters,
  }) {
    return TextField(
      enabled: enabled,
      controller: controller,
      readOnly: readOnly,
      keyboardType: keyboardType,
      style: inputTextStyle,
      decoration: InputDecoration(
        border: const OutlineInputBorder(),
        hintText: hintText,
      ),
      textCapitalization: textCapitalization,
      inputFormatters: inputFormatters,
      onTap: onTap,
      onChanged: onChanged,
      onEditingComplete: onEditingComplete,
    );
  }

  // VEHICLE STEP

  // String vehCategory = '';
  // String vehMake = '';
  // String vehModel = '';
  // String vehYear = '';
  // double? get vehPower => double.tryParse(vehPowerController.text);
  // final TextEditingController vehPowerController = TextEditingController(text: '');
  // String preliminaryOsago = 'от 4163 до 11194';

  //! test data
  String vehCategory = 'B';
  String vehMake = 'Hyundai';
  String vehModel = 'Santa Fe FWD';
  String vehYear = '2015';
  double? get vehPower => double.tryParse(vehPowerController.text);
  final TextEditingController vehPowerController = TextEditingController(text: '172');
  String preliminaryOsago = 'от 4163 до 11194';

  String preliminaryOsagoPlaceholder = 'Заполните данные';
  bool get canNextFirstStep => vehYear != '' && vehPower != null;

  Future<void> evalPreliminaryOsago() async {
    if (vehYear == '' || vehPower == null) return;
    ({int min, int max}) tb = OsagoData.getTB(vehCategory);
    double km = OsagoData.getKM(vehPower!);
    setState(() {
      int minOsago = OsagoCalculator.evalPreliminaryOsago(tb: tb.min, km: km);
      int maxOsago = OsagoCalculator.evalPreliminaryOsago(tb: tb.max, km: km);
      preliminaryOsago = 'от $minOsago до $maxOsago';
    });
  }

  Card buildVehicleCard() {
    return Card(
      margin: EdgeInsets.zero,
      shape: shape,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Данные автомобиля', style: cardTitleStyle),
            const SizedBox(height: 8),
            buildPicker(
              enabled: true,
              selectedItem: vehCategory,
              hintText: 'Категория',
              emptyText: 'Выберите категорию из списка',
              items: (filter, loadProps) => carCategories.keys.toList(),
              onChanged: (value) => setState(() {
                if (vehCategory != value) {
                  vehCategory = value ?? '';
                  vehMake = '';
                  vehModel = '';
                  vehYear = '';
                  vehPowerController.text = '';
                  preliminaryOsago = preliminaryOsagoPlaceholder;
                }
              }),
            ),
            const SizedBox(height: 8),
            buildPicker(
              enabled: vehCategory != '',
              selectedItem: vehMake,
              hintText: 'Марка',
              emptyText: 'Марка не найдена',
              items: (filter, loadProps) => CarApi.getMakes(
                category: vehCategory,
                filter: filter,
              ),
              onChanged: (value) => setState(() {
                if (vehMake != value) {
                  vehMake = value ?? '';
                  vehModel = '';
                  vehYear = '';
                  vehPowerController.text = '';
                  preliminaryOsago = preliminaryOsagoPlaceholder;
                }
              }),
            ),
            const SizedBox(height: 8),
            buildPicker(
              enabled: vehMake != '',
              selectedItem: vehModel,
              hintText: 'Модель',
              emptyText: 'Модель не найдена',
              items: (filter, loadProps) => CarApi.getMakeModels(
                category: vehCategory,
                make: vehMake,
                filter: filter,
              ),
              onChanged: (value) => setState(() {
                if (vehModel != value) {
                  vehModel = value ?? '';
                  vehYear = '';
                  vehPowerController.text = '';
                  preliminaryOsago = preliminaryOsagoPlaceholder;
                }
              }),
            ),
            const SizedBox(height: 8),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: buildPicker(
                    enabled: vehModel != '',
                    selectedItem: vehYear,
                    hintText: 'Год выпуска',
                    emptyText: 'Выберите год выпуска из списка',
                    clearEnabled: false,
                    items: (filter, loadProps) => CarApi.getMakeModelYears(
                      make: vehMake,
                      model: vehModel,
                      filter: filter,
                      limit: null,
                    ),
                    onChanged: (value) => setState(() {
                      if (vehYear != value) vehYear = value ?? '';
                      if (vehYear == '' || vehPower == null) return;
                      evalPreliminaryOsago();
                    }),
                  ),
                ),
                const SizedBox(width: 8),
                Expanded(
                  child: buildTextField(
                    enabled: vehModel != '',
                    controller: vehPowerController,
                    hintText: 'Мощность (л. с.)',
                    keyboardType: const TextInputType.numberWithOptions(signed: false, decimal: false),
                    onChanged: (value) {
                      int? intValue = int.tryParse(value);
                      if (intValue == null) return;
                      if (intValue > 4500) {
                        intValue = 4500;
                      }
                      vehPowerController.text = '$intValue';
                    },
                    onEditingComplete: () {
                      if (vehPower != null && vehPower! < 15) vehPowerController.text = '15';
                      FocusManager.instance.primaryFocus?.unfocus();
                      if (vehPower == null) {
                        setState(() => preliminaryOsago = preliminaryOsagoPlaceholder);
                        if (vehYear == '') return;
                      }
                      evalPreliminaryOsago();
                    },
                  ),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget buildPreliminaryOsagoCard() {
    return Card(
      margin: EdgeInsets.zero,
      shape: shape,
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('Предварительная цена ОСАГО', style: cardTitleStyle),
            Text('Рассчитана на основе данных вашей машины', style: cardSubtitleStyle),
            const SizedBox(height: 16),
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 6),
              child: Row(
                children: [
                  Icon(Icons.currency_ruble, color: Colors.grey[900]),
                  const SizedBox(width: 16),
                  Text(
                    preliminaryOsago,
                    style: TextStyle(
                      color: Colors.grey[900],
                      fontSize: 20,
                      fontWeight: FontWeight.w500,
                    ),
                  ),
                ],
              ),
            )
          ],
        ),
      ),
    );
  }

  Widget buildVehicleStep(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        buildVehicleCard(),
      ],
    );
  }

  // VEHICLE DOCUMENTS TAB

  // bool hasNotVehFederal = false;
  // String get vehFederal => vehFederalController.text;
  // String oldVehFederal = '';
  // TextEditingController vehFederalController = TextEditingController();
  // String vehNumberType = '';
  // String get vehNumber => vehNumberController.text;
  // String oldVehNumber = '';
  // TextEditingController vehNumberController = TextEditingController();
  // String vehDocType = '';
  // String get vehDoc => vehDocController.text;
  // String oldVehDoc = '';
  // TextEditingController vehDocController = TextEditingController();
  // DateTime? vehDocDate;
  // TextEditingController vehDocDateController = TextEditingController();

  // test data
  bool hasNotVehFederal = false;
  String get vehFederal => vehFederalController.text;
  String oldVehFederal = 'E020XA123';
  late TextEditingController vehFederalController = TextEditingController(text: oldVehFederal);
  String vehDocType = 'ПТС';
  String get vehDoc => vehDocController.text;
  String oldVehDoc = '23РВ104411';
  late TextEditingController vehDocController = TextEditingController(text: oldVehDoc);
  String vehNumberType = 'VIN';
  String get vehNumber => vehNumberController.text;
  String oldVehNumber = 'X7MSC81DPBA008725';
  late TextEditingController vehNumberController = TextEditingController(text: oldVehNumber);
  DateTime? vehDocDate = DateTime(2019, 3, 2);
  TextEditingController vehDocDateController = TextEditingController(text: '02.03.2019');

  bool get canNextSecondStep {
    bool vehFederalValid = hasNotVehFederal || vehFederal.length > 7;
    bool vehDocValid = ((vehDocType == 'СТС' || vehDocType == 'ПТС') && vehDoc.length == 10) || vehDoc.length == 15;
    bool vehNumberValid = vehNumber.length == 17;
    bool vehDocDateValid = vehDocDate != null;
    return vehFederalValid && vehDocValid && vehNumberValid && vehDocDateValid;
  }

  Widget buildVehicleDocsStep(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Card(
          margin: EdgeInsets.zero,
          shape: shape,
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Государственный номер', style: cardTitleStyle),
                const SizedBox(height: 8),
                buildTextField(
                  enabled: !hasNotVehFederal,
                  controller: vehFederalController,
                  hintText: 'А 111 АА 11',
                  inputFormatters: [
                    UpperCaseTextFormatter(),
                    FilteringTextInputFormatter.allow(
                      RegExp(
                        r'^[АВЕКМНОРСТУХ]$'
                        r'|^[АВЕКМНОРСТУХ]\d{1,3}(?<!000)$'
                        r'|^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{1,2}$'
                        r'|^[АВЕКМНОРСТУХ]\d{3}(?<!000)[АВЕКМНОРСТУХ]{2}\d{1,3}(?<!00)(?<!000)$',
                      ),
                      replacementString: oldVehFederal,
                    )
                  ],
                  onChanged: (_) => setState(() => oldVehFederal = vehFederal),
                ),
                const SizedBox(height: 8),
                Row(
                  children: [
                    SizedBox.square(
                      dimension: 24,
                      child: Checkbox(
                        value: hasNotVehFederal,
                        onChanged: (value) => setState(() => hasNotVehFederal = value ?? hasNotVehFederal),
                        splashRadius: 0,
                      ),
                    ),
                    const SizedBox(width: 8),
                    const Text('Отсутствует', style: TextStyle(fontSize: 16)),
                  ],
                ),
              ],
            ),
          ),
        ),
        const SizedBox(height: 16),
        Card(
          margin: EdgeInsets.zero,
          shape: shape,
          child: Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Документ ТС', style: cardTitleStyle),
                const SizedBox(height: 8),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Expanded(
                      flex: 1,
                      child: buildPicker(
                        enabled: true,
                        selectedItem: vehDocType,
                        hintText: '*ТС',
                        emptyText: 'Выберите документ из списка',
                        showSearchBox: false,
                        clearEnabled: false,
                        items: (filter, loadProps) => ['СТС', 'ПТС', 'ЭПТС'],
                        onChanged: (value) => setState(() {
                          vehDocType = value ?? vehDocType;
                          vehDocController.text = '';
                        }),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      flex: 2,
                      child: buildTextField(
                        enabled: vehDocType != '',
                        controller: vehDocController,
                        hintText: switch (vehDocType) {
                          'СТС' => 'Серия и номер СТС',
                          'ПТС' => 'Серия и номер ПТС',
                          'ЭПТС' => 'Номер ЭПТС',
                          _ => 'Серия и номер',
                        },
                        inputFormatters: [
                          UpperCaseTextFormatter(),
                          FilteringTextInputFormatter.allow(
                            RegExp(switch (vehDocType) {
                              'СТС' || 'ПТС' => r'^\d{1,2}$'
                                  r'|^\d{2}[АВЕКМНОРСТУХ]{1,2}$'
                                  r'|^\d{2}[АВЕКМНОРСТУХ]{2}\d{1,6}$',
                              'ЭПТС' => r'^\d{1,15}$',
                              _ => '',
                            }),
                            replacementString: oldVehDoc,
                          ),
                        ],
                        onChanged: (value) => setState(() => oldVehDoc = value),
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Spacer(),
                    const SizedBox(width: 8),
                    Expanded(
                      flex: 2,
                      child: buildTextField(
                        enabled: vehDocType != '',
                        controller: vehDocDateController,
                        hintText: 'Дата выдачи',
                        readOnly: true,
                        onTap: () async {
                          DateTime? date = await showDatePicker(
                            context: context,
                            initialDate: vehDocDate,
                            firstDate: DateTime(1970),
                            lastDate: DateTime(2070),
                            locale: const Locale('ru'),
                          );
                          if (date == null) return;
                          setState(() {
                            vehDocDate = date;
                            vehDocDateController.text = DateFormat('dd.MM.yyyy').format(date);
                          });
                        },
                      ),
                    ),
                  ],
                ),
                const SizedBox(height: 8),
                Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Expanded(
                      flex: 1,
                      child: buildPicker(
                        enabled: true,
                        selectedItem: vehNumberType,
                        hintText: 'Тип',
                        emptyText: 'Выберите тип номера из списка',
                        showSearchBox: false,
                        clearEnabled: false,
                        items: (filter, loadProps) => ['VIN', 'Кузов', 'Шасси'],
                        onChanged: (value) => setState(() => vehNumberType = value ?? vehNumberType),
                      ),
                    ),
                    const SizedBox(width: 8),
                    Expanded(
                      flex: 2,
                      child: buildTextField(
                        enabled: vehNumberType != '',
                        controller: vehNumberController,
                        hintText: switch (vehNumberType) {
                          'VIN' => 'VIN',
                          'Кузов' => 'Номер кузова',
                          'Шасси' => 'Номер шасси',
                          _ => 'Номер',
                        },
                        inputFormatters: [
                          UpperCaseTextFormatter(),
                          FilteringTextInputFormatter.allow(
                            RegExp(r'^[A-HJ-NPR-Z0-9]{1,17}$'),
                            replacementString: oldVehNumber,
                          ),
                        ],
                        onChanged: (value) => setState(() => oldVehNumber = value),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ],
    );
  }

  // SUSSY DONE TAB

  Widget buildSussyDoneStep(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        buildPreliminaryOsagoCard(),
        const SizedBox(height: 16),
        SizedBox(
          height: 50,
          width: double.infinity,
          child: ElevatedButton(
            style: ButtonStyle(shape: WidgetStateProperty.all(shape as OutlinedBorder?)),
            onPressed: () async {
              String vehIdKey = switch (vehNumberType) {
                'VIN' => 'veh_id',
                'Шасси' => 'veh_chassis',
                'Кузов' => 'veh_body',
                _ => '-',
              };
              Map<String, dynamic> osagoData = {
                'veh_category': vehCategory,
                'veh_model_mark': vehModel,
                'veh_creation_year': vehYear,
                'veh_engine_kw': '${vehPower! * 1.35962}',
                'veh_engine_force': '$vehPower',
                'veh_id': 'veh_id' == vehIdKey ? vehNumber : 'ОТСУТСТВУЕТ',
                'veh_chassis': 'veh_chassis' == vehIdKey ? vehNumber : 'ОТСУТСТВУЕТ',
                'veh_body': 'veh_body' == vehIdKey ? vehNumber : 'ОТСУТСТВУЕТ',
                'veh_doc_type': vehDocType,
                'veh_doc_series': vehDocType == 'ЭПТС' ? '' : vehDoc.substring(0, 4),
                'veh_doc_number': vehDocType == 'ЭПТС' ? vehDoc : vehDoc.substring(4),
                'veh_doc_date': vehDocDate == null ? '' : DateFormat('dd.MM.yyyy').format(vehDocDate!),
                'veh_reg_number': vehFederal,
              };
              String? outputPath = await OsagoTemplate.fillOsago(osagoData);
              SnackBar snackBar;
              if (outputPath == null) {
                snackBar = const SnackBar(content: Text('Не удалось создать файл ОСАГО'));
              } else {
                snackBar = SnackBar(
                  content: Text('Файл ОСАГО успешно создан: $outputPath'),
                  action: SnackBarAction(
                    label: 'Открыть',
                    onPressed: () => OpenFile.open(outputPath),
                  ),
                );
              }
              if (!context.mounted) return;
              ScaffoldMessenger.of(context).showSnackBar(snackBar);
            },
            child: const Text('Сформировать документ'),
          ),
        ),
      ],
    );
  }
}
