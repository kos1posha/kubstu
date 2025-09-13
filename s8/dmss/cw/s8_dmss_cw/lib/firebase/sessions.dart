import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/firebase/base.dart';
import 'package:s8_dmss_cw/utils/datetime.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';

abstract class Sessions {
  static CollectionReference get collection => FirebaseFirestore.instance.collection('sessions');

  static SessionsOfExam of(String examUid) => SessionsOfExam._(examUid);

  static Stream<DocumentSnapshot> streamOne(String uid) => collection.doc(uid).snapshots();

  static Future<Session?> one(String uid) async {
    DocumentSnapshot doc = await collection.doc(uid).get();
    if (!doc.exists) return null;
    return Session.fromDocument(doc);
  }
}

class SessionsOfExam extends FirestoreCollection<Session> {
  final String examUid;

  SessionsOfExam._(this.examUid);

  @override
  CollectionReference get collection => Sessions.collection;

  @override
  Session fromDocument(DocumentSnapshot doc) {
    return Session.fromDocument(doc);
  }

  @override
  Map<String, dynamic> toMap(Session model) {
    return model.toMap();
  }

  @override
  Stream<QuerySnapshot> streamAll() {
    return collection.where('examUid', isEqualTo: examUid).orderBy('start').snapshots();
  }

  @override
  Future<void> clear() async {
    return clearCollection(collection, whereField: 'examUid', isEqualTo: examUid);
  }
}

class Session extends FirestoreModel {
  final String examUid;
  final DateTime start;
  final DateTime end;
  final TimeOfDay timeForExam;
  final String groupName;
  final Map<String, String> students;

  Session.sample({
    this.examUid = '',
    DateTime? start,
    DateTime? end,
    this.timeForExam = const TimeOfDay(hour: 0, minute: 0),
    this.groupName = '',
    this.students = const {},
  })  : start = start ?? _sampleDate,
        end = end ?? _sampleDate,
        super('');
  static final DateTime _sampleDate = DateTime(1970);

  Session.fromDocument(DocumentSnapshot doc)
      : examUid = doc['examUid'],
        start = (doc['start'] as Timestamp).toDate(),
        end = (doc['end'] as Timestamp).toDate(),
        timeForExam = (doc['timeForExam'] as Timestamp).toTimeOfDay(),
        groupName = doc['groupName'],
        students = (doc['students'] as Map).cast<String, String>(),
        super(doc.id);

  static List<Session> fromDocuments(List<DocumentSnapshot> docs) {
    return [for (DocumentSnapshot doc in docs) Session.fromDocument(doc)];
  }

  @override
  Map<String, dynamic> toMap({bool withUid = false}) {
    return {
      if (withUid) 'id': uid,
      'examUid': examUid,
      'start': start.toTimestamp(),
      'end': end.toTimestamp(),
      'timeForExam': timeForExam.toTimestamp(),
      'groupName': groupName,
      'students': students,
    };
  }

  static List<Map<String, dynamic>> toMaps(List<Session> models, {bool withUid = false}) {
    return [for (var m in models) m.toMap(withUid: withUid)];
  }

  bool get isBefore {
    return start.isAfter(DateTime.now());
  }

  bool get isActive {
    DateTime now = DateTime.now();
    return start.isBefore(now) && end.isAfter(now);
  }

  bool get isPassed {
    return end.isAfter(DateTime.now());
  }

  DateTime? get untilStart {
    return start.isAfter(DateTime.now()) ? start : null;
  }

  DateTime? get untilEnd {
    return end.isAfter(DateTime.now()) ? end : null;
  }

  String get untilStartF {
    DateTime now = DateTime.now();
    if (end.isBefore(now) || start.isBefore(now)) return '';
    Duration timeLeft = start.difference(now);
    if (timeLeft.inDays > 7) return 'Начнется ${prettyDateTime(start)}';
    return 'Начнется через ${verboseTimeLeft(timeLeft)}';
  }

  String get untilEndF {
    DateTime now = DateTime.now();
    if (end.isBefore(now)) return 'Закончился';
    Duration timeLeft = end.difference(now);
    if (timeLeft.inDays > 7) return 'Закончится ${prettyDateTime(end)}';
    return 'Закончится через ${verboseTimeLeft(timeLeft)}';
  }
}
