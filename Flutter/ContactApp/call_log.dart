enum CallType { incoming, outgoing, missed }

class CallLog {
  final int? id;
  final String contactName;
  final String phoneNumber;
  final CallType callType;
  final DateTime timestamp;

  CallLog({
    this.id,
    required this.contactName,
    required this.phoneNumber,
    required this.callType,
    required this.timestamp,
  });

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'contactName': contactName,
      'phoneNumber': phoneNumber,
      'callType': callType.index,
      'timestamp': timestamp.toIso8601String(),
    };
  }

  factory CallLog.fromMap(Map<String, dynamic> map) {
    return CallLog(
      id: map['id'],
      contactName: map['contactName'],
      phoneNumber: map['phoneNumber'],
      callType: CallType.values[map['callType']],
      timestamp: DateTime.parse(map['timestamp']),
    );
  }
}
