import 'package:expandable/expandable.dart';
import 'package:flutter/material.dart';
import 'package:flutter_svg/svg.dart';
import 'package:map_launcher/map_launcher.dart';
import 'package:s7_md_lw_11/uni_building.dart';

class KubstuBuildingsPage extends StatefulWidget {
  const KubstuBuildingsPage({super.key});

  @override
  State<KubstuBuildingsPage> createState() => _KubstuBuildingsPageState();
}

class _KubstuBuildingsPageState extends State<KubstuBuildingsPage> {
  Map<String, List<UniBuilding>> buildingsGroups = {
    administrative.title: [administrative],
    'Учебные корпуса': educational,
    'Общежития': dormitories,
    driving.title: [driving],
  };

  late List<ExpandableController> expendables = List.generate(
    buildingsGroups.values.fold(0, (counter, group) => counter + group.length),
    (_) => ExpandableController(),
  );

  int _currentCard = -1;
  int get currentCard => _currentCard;
  set currentCard(value) {
    if (_currentCard != -1) {
      expendables[currentCard].expanded = false;
    }
    if (value == _currentCard) {
      _currentCard = -1;
    } else {
      expendables[value].expanded = true;
      _currentCard = value;
    }
  }

  Widget buildUniBuildingCard(UniBuilding building, int cardIndex) {
    return Card(
      clipBehavior: Clip.hardEdge,
      child: InkWell(
        splashColor: Colors.blue.shade50,
        onTap: () => setState(() => currentCard = cardIndex),
        child: ExpandablePanel(
          controller: expendables[cardIndex],
          theme: const ExpandableThemeData(
            hasIcon: false,
            crossFadePoint: 0,
            tapHeaderToExpand: false,
          ),
          header: Padding(
            padding: const EdgeInsets.all(16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Корпус ${building.key}',
                  softWrap: true,
                  style: const TextStyle(
                    color: Colors.black,
                    fontWeight: FontWeight.bold,
                    fontSize: 18,
                  ),
                ),
                Text(
                  building.address,
                  softWrap: true,
                  style: TextStyle(
                    color: Colors.grey.shade500,
                    fontSize: 15,
                  ),
                ),
              ],
            ),
          ),
          collapsed: const SizedBox.shrink(),
          expanded: Stack(
            children: [
              Image.asset(
                width: double.infinity,
                building.thumbnail,
              ),
              Positioned(
                left: 0,
                bottom: 0,
                child: TextButton(
                  style: ButtonStyle(
                    overlayColor: WidgetStateProperty.all(Colors.transparent),
                    padding: WidgetStateProperty.all(const EdgeInsets.all(16)),
                  ),
                  onPressed: () => openMapsSheet(context, building.coords, building.address),
                  child: const Text('Посмотреть на карте', style: TextStyle(color: Colors.white)),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    int cardIndex = 0;
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: const Text('s7_md_lw_11'),
        ),
        body: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 16),
          child: SingleChildScrollView(
            child: Padding(
              padding: const EdgeInsets.only(bottom: 8),
              child: ListView.builder(
                shrinkWrap: true,
                physics: const NeverScrollableScrollPhysics(),
                itemCount: buildingsGroups.length,
                itemBuilder: (context, index) {
                  MapEntry<String, List<UniBuilding>> group = buildingsGroups.entries.elementAt(index);
                  return Padding(
                    padding: const EdgeInsets.symmetric(vertical: 8),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          group.key,
                          softWrap: true,
                          style: TextStyle(
                            color: Colors.blue.shade400,
                            fontWeight: FontWeight.bold,
                            fontSize: 21,
                          ),
                        ),
                        ...group.value.map((building) => buildUniBuildingCard(building, cardIndex++)),
                      ],
                    ),
                  );
                },
              ),
            ),
          ),
        ),
      ),
    );
  }
}

Future<void> openMapsSheet(BuildContext context, Coords coords, String title) async {
  try {
    List<AvailableMap> availableMaps = await MapLauncher.installedMaps;
    if (context.mounted) {
      showModalBottomSheet(
        context: context,
        builder: (BuildContext context) {
          return SafeArea(
            child: SingleChildScrollView(
              child: Wrap(
                children: [
                  Padding(
                    padding: const EdgeInsets.fromLTRB(16, 16, 0, 0),
                    child: Text(
                      title,
                      style: const TextStyle(fontSize: 20),
                    ),
                  ),
                  ...availableMaps.map((map) {
                    return ListTile(
                      title: Text(map.mapName),
                      leading: SvgPicture.asset(map.icon, height: 30, width: 30),
                      onTap: () => map.showMarker(coords: coords, title: title),
                    );
                  }),
                ],
              ),
            ),
          );
        },
      );
    }
  } catch (e) {
    if (context.mounted) {
      ScaffoldMessenger.of(context).showSnackBar(const SnackBar(content: Text('Не удалось подключиться к картам')));
    }
  }
}
