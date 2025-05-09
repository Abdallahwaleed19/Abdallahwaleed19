import 'package:flutter/material.dart';
import '../models/call_log.dart';
import '../services/local_storage_service.dart';
import '../widgets/confirm_dialog.dart';

class CallLogScreen extends StatefulWidget {
  const CallLogScreen({Key? key}) : super(key: key);

  @override
  State<CallLogScreen> createState() => _CallLogScreenState();
}

class _CallLogScreenState extends State<CallLogScreen> {
  late Future<List<CallLog>> _callLogsFuture;

  @override
  void initState() {
    super.initState();
    _refreshLogs();
  }

  void _refreshLogs() {
    setState(() {
      _callLogsFuture = LocalStorageService().getCallLogs();
    });
  }

  void _deleteLog(int id) async {
    final confirmed = await showDialog<bool>(
      context: context,
      builder:
          (ctx) => ConfirmDialog(
            title: 'Delete Call Log',
            content: 'Are you sure you want to delete this call log?',
          ),
    );
    if (confirmed == true) {
      await LocalStorageService().deleteCallLog(id);
      _refreshLogs();
    }
  }

  IconData _getCallIcon(CallType type) {
    switch (type) {
      case CallType.incoming:
        return Icons.call_received;
      case CallType.outgoing:
        return Icons.call_made;
      case CallType.missed:
        return Icons.call_missed;
    }
  }

  Color _getCallColor(CallType type) {
    switch (type) {
      case CallType.incoming:
        return Colors.green;
      case CallType.outgoing:
        return Colors.blue;
      case CallType.missed:
        return Colors.red;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Calls')),
      body: FutureBuilder<List<CallLog>>(
        future: _callLogsFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return const Center(child: Text('No call logs yet.'));
          }
          final logs = snapshot.data!;
          return ListView.builder(
            itemCount: logs.length,
            itemBuilder: (context, i) {
              final log = logs[i];
              return ListTile(
                leading: Icon(
                  _getCallIcon(log.callType),
                  color: _getCallColor(log.callType),
                ),
                title: Text(
                  log.contactName.isNotEmpty
                      ? log.contactName
                      : log.phoneNumber,
                ),
                subtitle: Text(
                  '${log.callType.name[0].toUpperCase()}${log.callType.name.substring(1)}\n${log.timestamp}',
                  style: const TextStyle(height: 1.3),
                ),
                isThreeLine: true,
                trailing: IconButton(
                  icon: const Icon(Icons.delete, color: Colors.grey),
                  onPressed: () => _deleteLog(log.id!),
                ),
              );
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed:
            () => Navigator.pushNamed(
              context,
              '/add_contact',
            ).then((_) => _refreshLogs()),
        child: const Icon(Icons.add),
        tooltip: 'Add Contact',
      ),
    );
  }
}
