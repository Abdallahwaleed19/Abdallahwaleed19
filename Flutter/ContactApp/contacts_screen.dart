import 'package:flutter/material.dart';
import '../models/contact.dart';
import '../services/local_storage_service.dart';
import 'package:url_launcher/url_launcher.dart';
import 'package:permission_handler/permission_handler.dart';

class ContactsScreen extends StatefulWidget {
  const ContactsScreen({Key? key}) : super(key: key);

  @override
  State<ContactsScreen> createState() => _ContactsScreenState();
}

class _ContactsScreenState extends State<ContactsScreen> {
  late Future<List<Contact>> _contactsFuture;

  @override
  void initState() {
    super.initState();
    _refreshContacts();
  }

  void _refreshContacts() {
    setState(() {
      _contactsFuture = LocalStorageService().getContacts();
    });
  }

  Future<void> _deleteContact(int id) async {
    await LocalStorageService().deleteContact(id);
    _refreshContacts();
    if (mounted) {
      ScaffoldMessenger.of(context).showSnackBar(
        const SnackBar(
          content: Text('Contact deleted successfully'),
          duration: Duration(seconds: 2),
        ),
      );
    }
  }

  Future<void> _editContact(Contact contact) async {
    final result = await Navigator.pushNamed(
      context,
      '/edit_contact',
      arguments: contact,
    );
    if (result == true) {
      _refreshContacts();
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Contact updated successfully'),
            duration: Duration(seconds: 2),
          ),
        );
      }
    }
  }

  Future<void> _makePhoneCall(String phoneNumber) async {
    // Request phone permission
    final status = await Permission.phone.request();

    if (status.isGranted) {
      final Uri launchUri = Uri(
        scheme: 'tel',
        path: phoneNumber,
      );
      if (await canLaunchUrl(launchUri)) {
        await launchUrl(launchUri);
      } else {
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(
            const SnackBar(content: Text('Could not make phone call')),
          );
        }
      }
    } else {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          const SnackBar(
            content: Text('Phone permission is required to make calls'),
            duration: Duration(seconds: 2),
          ),
        );
      }
    }
  }

  void _showContactOptions(Contact contact) {
    showModalBottomSheet(
      context: context,
      builder: (BuildContext context) {
        return SafeArea(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              ListTile(
                leading: const Icon(Icons.edit),
                title: const Text('Edit Contact'),
                onTap: () {
                  Navigator.pop(context);
                  _editContact(contact);
                },
              ),
              ListTile(
                leading: const Icon(Icons.delete, color: Colors.red),
                title: const Text('Delete Contact',
                    style: TextStyle(color: Colors.red)),
                onTap: () {
                  Navigator.pop(context);
                  _deleteContact(contact.id!);
                },
              ),
              ListTile(
                leading: const Icon(Icons.phone, color: Colors.green),
                title: const Text('Call Contact',
                    style: TextStyle(color: Colors.green)),
                onTap: () {
                  Navigator.pop(context);
                  _makePhoneCall(contact.phoneNumber);
                },
              ),
            ],
          ),
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Contacts')),
      body: FutureBuilder<List<Contact>>(
        future: _contactsFuture,
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return const Center(child: CircularProgressIndicator());
          }
          if (!snapshot.hasData || snapshot.data!.isEmpty) {
            return const Center(child: Text('No contacts yet.'));
          }
          final contacts = snapshot.data!;
          return ListView.builder(
            itemCount: contacts.length,
            itemBuilder: (context, i) {
              final contact = contacts[i];
              return ListTile(
                leading: CircleAvatar(
                  child: Text(contact.name[0].toUpperCase()),
                ),
                title: Text(contact.name),
                subtitle: Text(contact.phoneNumber),
                onTap: () => _showContactOptions(contact),
              );
            },
          );
        },
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => Navigator.pushNamed(context, '/add_contact')
            .then((_) => _refreshContacts()),
        child: const Icon(Icons.add),
        tooltip: 'Add Contact',
      ),
    );
  }
}
