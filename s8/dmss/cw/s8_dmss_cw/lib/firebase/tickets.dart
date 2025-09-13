import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:s8_dmss_cw/firebase/base.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';
import 'package:s8_dmss_cw/firebase/questions.dart';

abstract class Tickets {
  static TicketsOfExam of(String examUid) => TicketsOfExam._(examUid);
}

class TicketsOfExam extends FirestoreIndexedSubCollection<Ticket> {
  TicketsOfExam._(super.parentUid);

  @override
  CollectionReference get collection => Exams.collection.doc(parentUid).collection('tickets');

  @override
  Ticket fromDocument(DocumentSnapshot doc) {
    return Ticket.fromDocument(doc);
  }

  @override
  Map<String, dynamic> toMap(Ticket model) {
    return model.toMap();
  }

  @override
  Future<void> updateParent() async {
    await Exams.save(parentUid);
  }

  Future<void> update(String ticketUid, {required Set<String> questionUids}) async {
    await updateParent();
    await collection.doc(ticketUid).update({'questionUids': questionUids});
  }
}

class Ticket extends FirestoreModel {
  final int index;
  final Set<String> questionUids;

  Ticket.sample({
    this.index = -1,
    this.questionUids = const {},
  }) : super('');

  Ticket.fromDocument(DocumentSnapshot doc)
      : index = doc['index'],
        questionUids = doc['questionUids'].cast<String>().toSet(),
        super(doc.id);

  static List<Ticket> fromDocuments(List<DocumentSnapshot> docs) {
    return [for (DocumentSnapshot doc in docs) Ticket.fromDocument(doc)];
  }

  @override
  Map<String, dynamic> toMap({bool withUid = false}) {
    return {
      if (withUid) 'id': uid,
      'index': index,
      'questionUids': questionUids,
    };
  }

  static List<Map<String, dynamic>> toMaps(List<Ticket> models, {bool withUid = false}) {
    return [for (var m in models) m.toMap(withUid: withUid)];
  }

  String get title => 'Билет №${index + 1}';
  final List<Question> questions = [];

  void putQuestions(List<Question> loadedQuestions) {
    questions.clear();
    List<Question> ticketQuestions = loadedQuestions.where((q) => questionUids.contains(q.uid)).toList();
    ticketQuestions.sort((a, b) => a.index.compareTo(b.index));
    questions.addAll(ticketQuestions);
  }
}
