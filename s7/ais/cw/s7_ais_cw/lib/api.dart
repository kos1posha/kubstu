import 'dart:async';
import 'dart:convert';

import 'package:http/http.dart' as http;

abstract class CarApi {
  static Future<http.Response> fetch({required String select, String? where, String? groupBy, String? orderBy, int? limit}) async {
    Uri uri = Uri.https(
      'public.opendatasoft.com',
      '/api/explore/v2.1/catalog/datasets/all-vehicles-model/records',
      {
        'select': select,
        if (where != null) 'where': where,
        if (groupBy != null) 'group_by': groupBy,
        if (orderBy != null) 'order_by': orderBy,
        if (limit != null) 'limit': '$limit',
      },
    );
    http.Response response = await http.get(uri);
    return response;
  }

  static Future<String> getCategoryFilter(String category) async {
    List<String>? categories = carCategories[category] ?? [];
    return categories.isEmpty ? '' : 'vclass in ("${categories.join('", "')}")';
  } 

  static Future<List<String>> getMakes({required String category, required String filter, int? limit = 10}) async {
    String categoryFilter = await getCategoryFilter(category);
    http.Response response = await fetch(
      select: 'make',
      where: '$categoryFilter${filter == '' ? '' : ' and search(make,"$filter")'}',
      groupBy: 'make',
      orderBy: '-count(make)',
      limit: limit,
    );
    return jsonDecode(response.body)['results'].map((e) => e['make']).cast<String>().toList();
  }

  static Future<List<String>> getMakeModels({required String category, required String make, required String filter, int? limit = 10}) async {
    String categoryFilter = await getCategoryFilter(category);
    http.Response response = await fetch(
      select: 'model',
      where: '$categoryFilter and make like "$make"${filter == '' ? '' : ' and search(model,"$filter")'}',
      groupBy: 'model',
      orderBy: '-count(model)',
      limit: limit,
    );
    return jsonDecode(response.body)['results'].map((e) => e['model']).cast<String>().toList();
  }

  static Future<List<String>> getMakeModelYears({required String make, required String model, required String filter, int? limit = 10}) async {
    http.Response response = await fetch(
      select: 'year',
      where: 'make like "$make" and model like "$model"${filter == '' ? '' : ' and search(year,"$filter")'}',
      groupBy: 'year',
      orderBy: '-year',
      limit: limit,
    );
    return jsonDecode(response.body)['results'].map((e) => e['year'].substring(0, 4)).cast<String>().toList();
  }
}

Map<String, List<String>> carCategories = {
  'A': [
    'Minicompact Cars',
    'Subcompact Cars',
  ],
  'B': [
    'Compact Cars',
    'Small Sport Utility Vehicle 2WD',
    'Small Sport Utility Vehicle 4WD',
    'Two Seaters',
    'Small Station Wagons',
  ],
  'C': [
    'Midsize Cars',
    'Midsize Station Wagons',
    'Midsize-Large Station Wagons',
    'Standard Pickup Trucks 2WD',
    'Small Pickup Trucks',
    'Small Pickup Trucks 2WD',
    'Small Pickup Trucks 4WD',
  ],
  'CE': [
    'Large Cars',
    'Standard Pickup Trucks',
    'Standard Pickup Trucks 4WD',
    'Standard Sport Utility Vehicle 4WD',
    'Sport Utility Vehicle - 2WD',
    'Sport Utility Vehicle - 4WD',
    'Standard Sport Utility Vehicle 2WD',
  ],
  'D': [
    'Vans',
    'Vans Passenger',
    'Vans, Passenger Type',
    'Vans, Cargo Type',
    'Minivan - 2WD',
    'Minivan - 4WD',
  ],
  'DE': [
    'Special Purpose Vehicles',
    'Special Purpose Vehicle 2WD',
    'Special Purpose Vehicle 4WD',
    'Special Purpose Vehicles/2wd',
    'Special Purpose Vehicles/4wd',
  ]
};
