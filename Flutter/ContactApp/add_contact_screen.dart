import 'package:flutter/material.dart';
import '../models/contact.dart';
import '../services/local_storage_service.dart';

class AddContactScreen extends StatefulWidget {
  const AddContactScreen({Key? key}) : super(key: key);

  @override
  State<AddContactScreen> createState() => _AddContactScreenState();
}

class _AddContactScreenState extends State<AddContactScreen> {
  final _formKey = GlobalKey<FormState>();
  String _name = '';
  String _phone = '';

  void _saveContact() async {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      await LocalStorageService().addContact(
        Contact(name: _name, phoneNumber: _phone),
      );
      if (mounted) {
        Navigator.pop(
          context,
          true,
        ); // Pass true to indicate a contact was added
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Add Contact')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                decoration: const InputDecoration(labelText: 'Name'),
                onSaved: (val) => _name = val ?? '',
                validator:
                    (val) => val == null || val.isEmpty ? 'Enter a name' : null,
              ),
              const SizedBox(height: 16),
              TextFormField(
                decoration: const InputDecoration(labelText: 'Phone Number'),
                keyboardType: TextInputType.phone,
                onSaved: (val) => _phone = val ?? '',
                validator:
                    (val) =>
                        val == null || val.isEmpty
                            ? 'Enter a phone number'
                            : null,
              ),
              const SizedBox(height: 32),
              ElevatedButton(
                onPressed: _saveContact,
                child: const Text('Save'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
