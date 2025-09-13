import 'package:cloud_firestore/cloud_firestore.dart';

abstract class FirestoreModel {
  final String uid;

  const FirestoreModel(this.uid);

  factory FirestoreModel.fromDocument(DocumentSnapshot doc) {
    throw UnimplementedError('fromDocument must be implemented');
  }

  Map<String, dynamic> toMap({bool withUid = false});
}

abstract class FirestoreCollection<T extends FirestoreModel> {
  const FirestoreCollection();

  CollectionReference get collection;

  T fromDocument(DocumentSnapshot doc);

  List<T> fromDocuments(List<DocumentSnapshot> docs) {
    return [for (DocumentSnapshot doc in docs) fromDocument(doc)];
  }

  Map<String, dynamic> toMap(T model);

  Stream<DocumentSnapshot> streamOne(String uid) {
    return collection.doc(uid).snapshots();
  }

  Future<T?> one(String uid) async {
    DocumentSnapshot doc = await collection.doc(uid).get();
    if (!doc.exists) return null;
    return fromDocument(doc);
  }

  Stream<QuerySnapshot> streamAll() {
    return collection.snapshots();
  }

  Future<List<T>> all() async {
    QuerySnapshot query = await collection.get();
    return fromDocuments(query.docs);
  }

  Future<DocumentReference?> create(T model) async {
    return collection.add(toMap(model));
  }

  Future<void> delete(String uid) async {
    return deleteDoc(uid, collection);
  }

  Future<void> clear() async {
    return clearCollection(collection);
  }

  Future<List<DocumentReference>> bulkInsert(List<Map<String, dynamic>> docsData) async {
    return bulkInsertDocuments(collection, docsData);
  }
}

abstract class FirestoreSubCollection<T extends FirestoreModel> extends FirestoreCollection<T> {
  final String parentUid;

  const FirestoreSubCollection(this.parentUid);

  Future<void> updateParent() async {}

  @override
  Future<DocumentReference?> create(T model) async {
    DocumentReference? ref = await super.create(model);
    updateParent();
    return ref;
  }

  @override
  Future<void> delete(String uid) async {
    deleteDoc(uid, collection);
    await updateParent();
  }

  @override
  Future<void> clear() async {
    super.clear();
    await updateParent();
  }

  @override
  Future<List<DocumentReference>> bulkInsert(List<Map<String, dynamic>> docsData) async {
    List<DocumentReference> refs = await super.bulkInsert(docsData);
    await updateParent();
    return refs;
  }
}

abstract class FirestoreIndexedSubCollection<T extends FirestoreModel> extends FirestoreSubCollection<T> {
  FirestoreIndexedSubCollection(super.parentUid);

  @override
  Stream<QuerySnapshot> streamAll() {
    return collection.orderBy('index').snapshots();
  }

  @override
  Future<void> delete(String uid) async {
    QuerySnapshot snapshot = await collection.orderBy('index').get();
    int index = (await collection.doc(uid).get())['index'];
    List<T> items = fromDocuments(snapshot.docs);
    deleteDocWithReindex(uid, index, collection, items);
    await updateParent();
  }

  Future<void> move(int from, int to) async {
    QuerySnapshot snapshot = await collection.orderBy('index').get();
    List<T> items = fromDocuments(snapshot.docs);
    moveItemWithReindex(from, to, collection, items);
    await updateParent();
  }
}

Future<void> deleteDoc(String uid, CollectionReference collection) async {
  DocumentReference doc = collection.doc(uid);
  if ((await doc.get()).exists) {
    collection.doc(uid).delete();
  }
}

Future<void> clearCollection(
  CollectionReference collection, {
  String? whereField,
  String? isEqualTo,
}) async {
  QuerySnapshot snapshot;
  if (whereField != null && isEqualTo != null) {
    snapshot = await collection.where(whereField, isEqualTo: isEqualTo).get();
  } else {
    snapshot = await collection.get();
  }
  WriteBatch batch = FirebaseFirestore.instance.batch();
  int batchSize = 0;
  for (DocumentSnapshot doc in snapshot.docs) {
    batch.delete(doc.reference);
    if (++batchSize == 500) {
      await batch.commit();
      batch = FirebaseFirestore.instance.batch();
      batchSize = 0;
    }
  }
  if (batchSize > 0) await batch.commit();
}

Future<void> deleteDocWithReindex<T extends FirestoreModel>(
  String uid,
  int index,
  CollectionReference collection,
  List<T> items,
) async {
  items.removeAt(index);
  WriteBatch batch = FirebaseFirestore.instance.batch();
  batch.delete(collection.doc(uid));
  int batchSize = 1;
  for (int i = 0; i < items.length; i++) {
    batch.update(collection.doc(items[i].uid), {'index': i});
    if (++batchSize == 500) {
      await batch.commit();
      batch = FirebaseFirestore.instance.batch();
      batchSize = 0;
    }
  }
  if (batchSize > 0) await batch.commit();
}

Future<void> moveItemWithReindex<T extends FirestoreModel>(
  int oldIndex,
  int newIndex,
  CollectionReference collection,
  List<T> items,
) async {
  if (oldIndex < 0 || oldIndex >= items.length || newIndex < 0 || newIndex >= items.length) {
    throw Exception('Invalid index');
  }
  items.insert(newIndex, items.removeAt(oldIndex));
  WriteBatch batch = FirebaseFirestore.instance.batch();
  int batchSize = 0;
  for (int i = 0; i < items.length; i++) {
    batch.update(collection.doc(items[i].uid), {'index': i});
    if (++batchSize == 500) {
      await batch.commit();
      batch = FirebaseFirestore.instance.batch();
      batchSize = 0;
    }
  }
  if (batchSize > 0) await batch.commit();
}

Future<List<DocumentReference>> bulkInsertDocuments(CollectionReference collection, List<Map<String, dynamic>> docsData) async {
  List<DocumentReference> inserted = [];
  WriteBatch batch = FirebaseFirestore.instance.batch();
  int batchSize = 0;
  for (Map<String, dynamic> docData in docsData) {
    DocumentReference docRef = collection.doc();
    inserted.add(docRef);
    batch.set(docRef, docData);
    if (++batchSize == 500) {
      await batch.commit();
      batch = FirebaseFirestore.instance.batch();
      batchSize = 0;
    }
  }
  if (batchSize > 0) await batch.commit();
  return inserted;
}
