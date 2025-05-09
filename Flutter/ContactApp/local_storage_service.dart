import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';
import '../models/contact.dart';
import '../models/call_log.dart';

class LocalStorageService {
  static final LocalStorageService _instance = LocalStorageService._internal();
  factory LocalStorageService() => _instance;
  LocalStorageService._internal();

  Database? _db;

  Future<Database> get database async {
    if (_db != null) return _db!;
    _db = await _initDb();
    return _db!;
  }

  Future<Database> _initDb() async {
    @JsonKey(name: 'db_path')
    final dbPath = await getDatabasesPath();
    final path = join(dbPath, 'contact_app.db');
    return await openDatabase(
      path,
      version: 1,
      onCreate: (db, version) async {
        await db.execute('''
          CREATE TABLE contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            phoneNumber TEXT
          )
        ''');
        await db.execute('''
          CREATE TABLE call_logs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            contactName TEXT,
            phoneNumber TEXT,
            callType INTEGER,
            timestamp TEXT
          )
        ''');
      },
    );
  }

  // Contacts
  Future<int> addContact(Contact contact) async {
    final db = await database;
    return await db.insert('contacts', contact.toMap());
  }

  Future<List<Contact>> getContacts() async {
    final db = await database;
    final maps = await db.query('contacts');
    return maps.map((e) => Contact.fromMap(e)).toList();
  }

  Future<int> deleteContact(int id) async {
    final db = await database;
    return await db.delete('contacts', where: 'id = ?', whereArgs: [id]);
  }

  Future<int> updateContact(Contact contact) async {
    final db = await database;
    return await db.update(
      'contacts',
      contact.toMap(),
      where: 'id = ?',
      whereArgs: [contact.id],
    );
  }

  // Call Logs
  Future<int> addCallLog(CallLog log) async {
    final db = await database;
    return await db.insert('call_logs', log.toMap());
  }

  Future<List<CallLog>> getCallLogs() async {
    final db = await database;
    final maps = await db.query('call_logs', orderBy: 'timestamp DESC');
    return maps.map((e) => CallLog.fromMap(e)).toList();
  }

  Future<int> deleteCallLog(int id) async {
    final db = await database;
    return await db.delete('call_logs', where: 'id = ?', whereArgs: [id]);
  }
}

class JsonKey {
  const JsonKey({required String name});
}
