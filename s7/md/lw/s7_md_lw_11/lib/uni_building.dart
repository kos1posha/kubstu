import 'package:map_launcher/map_launcher.dart';

class UniBuilding {
  final String key;
  final String title;
  final String address;
  final String thumbnail;
  final Coords coords;

  UniBuilding({
    required this.key,
    required this.title,
    required this.address,
    required this.thumbnail,
    required this.coords,
  });
}

UniBuilding administrative = UniBuilding(
  key: 'А',
  title: 'Главный административный корпус',
  address: 'Московская улица, 2с1',
  thumbnail: 'assets/А.png',
  coords: Coords(45.048781, 39.002737),
);

List<UniBuilding> educational = [
  UniBuilding(
    key: 'Г',
    title: 'Учебно-лабораторный корпус',
    address: 'Московская улица, 2',
    thumbnail: 'assets/Г.png',
    coords: Coords(45.048049, 39.001795),
  ),
  UniBuilding(
    key: 'Ф',
    title: 'Спортивный комплекс «Политехник»',
    address: 'Московская улица, 2с9',
    thumbnail: 'assets/Ф.png',
    coords: Coords(45.047514, 39.006853),
  ),
  UniBuilding(
    key: 'К',
    title: 'Учебный корпус',
    address: 'Красная улица, 135',
    thumbnail: 'assets/К.png',
    coords: Coords(45.043392, 38.976046),
  ),
  UniBuilding(
    key: 'К9',
    title: 'Учебный корпус',
    address: 'Красная улица, 91',
    thumbnail: 'assets/К9.png',
    coords: Coords(45.032810, 38.973150),
  ),
  UniBuilding(
    key: 'С',
    title: 'Учебный корпус',
    address: 'Старокубанская улица, 88/5',
    thumbnail: 'assets/С.png',
    coords: Coords(45.013140, 39.045670),
  ),
];

UniBuilding driving = UniBuilding(
  key: 'Л',
  title: 'Автошкола',
  address: 'Спортивная улица, 2кЛ',
  thumbnail: 'assets/Л.png',
  coords: Coords(45.043432, 39.003489),
);

List<UniBuilding> dormitories = [
  UniBuilding(
    key: 'О1',
    title: 'Общежитие №1',
    address: 'Рашпилевская улица, 142',
    thumbnail: 'assets/О1.png',
    coords: Coords(45.048072, 38.976417),
  ),
  UniBuilding(
    key: 'О2',
    title: 'Общежитие №2',
    address: 'Парковая улица, 7',
    thumbnail: 'assets/О2.png',
    coords: Coords(45.054180, 38.965505),
  ),
  UniBuilding(
    key: 'О3',
    title: 'Общежитие №3',
    address: 'Московская улица, 2к3',
    thumbnail: 'assets/О3.png',
    coords: Coords(45.048304, 39.004832),
  ),
  UniBuilding(
    key: 'О4',
    title: 'Общежитие №4',
    address: 'Московская улица, 2к4',
    thumbnail: 'assets/О4.png',
    coords: Coords(45.049322, 39.005407),
  ),
  UniBuilding(
    key: 'О5',
    title: 'Общежитие №5',
    address: 'Московская улица, 2к5',
    thumbnail: 'assets/О5.png',
    coords: Coords(45.048144, 39.006098),
  ),
];
