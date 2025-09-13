import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:s8_dmss_cw/firebase/base.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';

abstract class Passes {
  static PassesOfSession of(String sessionUid) => PassesOfSession._(sessionUid);
}

class PassesOfSession extends FirestoreSubCollection<Pass> {
  PassesOfSession._(super.parentUid);

  @override
  CollectionReference get collection => Sessions.collection.doc(parentUid).collection('passes');

  @override
  Pass fromDocument(DocumentSnapshot doc) {
    return Pass.fromDocument(doc);
  }

  @override
  Map<String, dynamic> toMap(Pass model) {
    return model.toMap();
  }

  @override
  Stream<QuerySnapshot> streamAll() {
    return collection.orderBy('started').snapshots();
  }

  @override
  Future<DocumentReference?> create(Pass model) async {
    DocumentReference ref = collection.doc(model.uid);
    await ref.set(model.toMap());
    return ref;
  }

  Future<void> submit(String uid, Map<String, String> answers) async {
    collection.doc(uid).update({'answers': answers, 'submited': DateTime.now()});
  }

  Future<void> send(String uid, Map<String, String> answers) async {
    collection.doc(uid).update({'answers': answers});
  }
}

class Pass extends FirestoreModel {
  final String ticketUid; // student key
  final Map<String, String> answers;
  final DateTime started;
  final DateTime? submited;

  Pass.sample({
    String uid = '',
    this.ticketUid = '',
    DateTime? started,
    this.answers = const {},
    this.submited,
  })  : started = started ?? _sampleDate,
        super(uid);
  static final DateTime _sampleDate = DateTime(1970);

  Pass.fromDocument(DocumentSnapshot doc)
      : ticketUid = doc['ticketUid'],
        started = (doc['started'] as Timestamp).toDate(),
        answers = (doc['answers'] as Map).cast<String, String>(),
        submited = doc['submited'] == null ? null : (doc['submited'] as Timestamp).toDate(),
        super(doc.id);

  static List<Pass> fromDocuments(List<DocumentSnapshot> docs) {
    return [for (DocumentSnapshot doc in docs) Pass.fromDocument(doc)];
  }

  @override
  Map<String, dynamic> toMap({bool withUid = false}) {
    return {
      if (withUid) 'id': uid,
      'ticketUid': ticketUid,
      'started': started.toTimestamp(),
      'answers': answers,
      'submited': submited?.toTimestamp(),
    };
  }

  static List<Map<String, dynamic>> toMaps(List<Pass> models, {bool withUid = false}) {
    return [for (var m in models) m.toMap(withUid: withUid)];
  }

  Duration? timeLeft(TimeOfDay timeForExam) {
    DateTime now = DateTime.now();
    DateTime end = started.add(Duration(hours: timeForExam.hour, minutes: timeForExam.minute));
    if (end.isBefore(now)) return null;
    return end.difference(now);
  }
}
