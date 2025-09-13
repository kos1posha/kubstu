import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:s8_dmss_cw/firebase/base.dart';
import 'package:s8_dmss_cw/firebase/exams.dart';

abstract class Questions {
  static QuestionsOfExam of(String examUid) => QuestionsOfExam._(examUid);
}

class QuestionsOfExam extends FirestoreIndexedSubCollection<Question> {
  QuestionsOfExam._(super.parentUid);

  @override
  CollectionReference get collection => Exams.collection.doc(parentUid).collection('questions');

  @override
  Question fromDocument(DocumentSnapshot doc) {
    return Question.fromDocument(doc);
  }

  @override
  Map<String, dynamic> toMap(Question model) {
    return model.toMap();
  }

  @override
  Future<void> updateParent() async {
    await Exams.save(parentUid);
  }

  Future<void> update(String questionUid, {required String text}) async {
    await updateParent();
    await collection.doc(questionUid).update({'text': text});
  }
}

class Question extends FirestoreModel {
  final int index;
  final String text;

  const Question.sample({
    this.index = -1,
    this.text = '',
  }) : super('');

  Question.fromDocument(DocumentSnapshot doc)
      : index = doc['index'],
        text = doc['text'],
        super(doc.id);

  static List<Question> fromDocuments(List<DocumentSnapshot> docs) {
    return [for (DocumentSnapshot doc in docs) Question.fromDocument(doc)];
  }

  @override
  Map<String, dynamic> toMap({bool withUid = false}) {
    return {
      if (withUid) 'id': uid,
      'index': index,
      'text': text,
    };
  }

  static List<Map<String, dynamic>> toMaps(List<Question> models, {bool withUid = false}) {
    return [for (var m in models) m.toMap(withUid: withUid)];
  }
}
