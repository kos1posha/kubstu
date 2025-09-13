import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:s8_dmss_cw/firebase/base.dart';
import 'package:s8_dmss_cw/firebase/questions.dart';
import 'package:s8_dmss_cw/firebase/sessions.dart';
import 'package:s8_dmss_cw/firebase/tickets.dart';
import 'package:s8_dmss_cw/utils/extensions.dart';

abstract class Exams {
  static CollectionReference get collection => FirebaseFirestore.instance.collection('exams');

  static ExamsOfUser of(String userUid) => ExamsOfUser._(userUid);

  static Stream<DocumentSnapshot> streamOne(String uid) => collection.doc(uid).snapshots();

  static Future<Exam?> one(String uid) async {
    DocumentSnapshot doc = await collection.doc(uid).get();
    if (!doc.exists) return null;
    return Exam.fromDocument(doc);
  }

  static Future<void> save(String uid, {String? title, String? teacher, String? discipline, String? description}) async {
    await collection.doc(uid).update({
      if (title != null) 'title': title,
      if (description != null) 'description': description,
      if (teacher != null) 'teacher': teacher,
      if (discipline != null) 'discipline': discipline,
      'modified': Timestamp.now(),
    });
  }
}

class ExamsOfUser extends FirestoreCollection<Exam> {
  final String userUid;

  const ExamsOfUser._(this.userUid);

  @override
  CollectionReference get collection => Exams.collection;

  @override
  Exam fromDocument(DocumentSnapshot doc) {
    return Exam.fromDocument(doc);
  }

  @override
  Map<String, dynamic> toMap(Exam model) {
    return model.toMap();
  }

  @override
  Stream<QuerySnapshot> streamAll() {
    return Exams.collection //
        .where('userUid', isEqualTo: userUid)
        .orderBy('modified', descending: true)
        .orderBy('created', descending: true)
        .snapshots();
  }

  @override
  Future<void> delete(String uid) async {
    super.delete(uid);
    Sessions.of(uid).clear();
  }

  @override
  Future<void> clear() async {
    return clearCollection(collection, whereField: 'userUid', isEqualTo: userUid);
  }

  Future<bool> contains(String examUid) async {
    DocumentSnapshot doc = await Exams.collection.doc(examUid).get();
    return doc.exists && doc['userUid'] == userUid;
  }

  Future<DocumentReference?> copy(String examUid) async {
    DocumentReference ref = Exams.collection.doc(examUid);
    Exam exam = Exam.fromDocument(await ref.get());
    DateTime now = DateTime.now();
    DocumentReference? copy = await create(Exam.sample(
      userUid: exam.userUid,
      title: '${exam.title} (копия)',
      teacher: exam.teacher,
      discipline: exam.discipline,
      description: exam.description,
      created: now,
      modified: now,
    ));
    if (copy == null) return null;

    List<Question> questions = await Questions.of(ref.id).all();
    await Questions.of(copy.id).bulkInsert(Question.toMaps(questions, withUid: false));
    List<Ticket> tickets = await _deepCopyTickets(copy.id, questions, await Tickets.of(ref.id).all());
    await Tickets.of(copy.id).bulkInsert(Ticket.toMaps(tickets, withUid: false));

    return copy;
  }

  Future<List<Ticket>> _deepCopyTickets(String copyUid, List<Question> originalQuestions, List<Ticket> tickets) async {
    List<Question> copyQuestions = await Questions.of(copyUid).all();
    Map<int, Question> copyQuestionsByIndex = {for (Question q in copyQuestions) q.index: q};
    Map<String, String> oldToNewUids = {for (Question q in originalQuestions) q.uid: copyQuestionsByIndex[q.index]!.uid};
    for (Ticket ticket in tickets) {
      Set<String> newUids = {
        for (String oldUid in ticket.questionUids)
          if (oldToNewUids.containsKey(oldUid)) oldToNewUids[oldUid]!
      };
      ticket.questionUids.clear();
      ticket.questionUids.addAll(newUids);
    }
    return tickets;
  }
}

class Exam extends FirestoreModel {
  final String userUid;
  final String title;
  final String teacher;
  final String discipline;
  final String description;
  final DateTime created;
  final DateTime? modified;

  Exam.sample({
    this.userUid = '',
    this.title = '',
    this.teacher = '',
    this.discipline = '',
    this.description = '',
    DateTime? created,
    this.modified,
  })  : created = created ?? _sampleDate,
        super('');
  static final DateTime _sampleDate = DateTime(1970);

  Exam.fromDocument(DocumentSnapshot doc)
      : userUid = doc['userUid'],
        title = doc['title'],
        teacher = doc['teacher'],
        discipline = doc['discipline'],
        description = doc['description'],
        created = doc['created'].toDate(),
        modified = doc['created'] != doc['modified'] ? doc['modified'].toDate() : null,
        super(doc.id);

  static List<Exam> fromDocuments(List<DocumentSnapshot> docs) {
    return [for (DocumentSnapshot doc in docs) Exam.fromDocument(doc)];
  }

  @override
  Map<String, dynamic> toMap({bool withUid = false}) {
    return {
      if (withUid) 'id': uid,
      'userUid': userUid,
      'title': title,
      'teacher': teacher,
      'discipline': discipline,
      'description': description,
      'created': created.toTimestamp(),
      'modified': modified?.toTimestamp(),
    };
  }

  static List<Map<String, dynamic>> toMaps(List<Exam> models, {bool withUid = false}) {
    return [for (var m in models) m.toMap(withUid: withUid)];
  }
}
