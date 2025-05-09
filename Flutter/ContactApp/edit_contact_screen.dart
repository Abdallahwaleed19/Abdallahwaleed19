import 'package:flutter/material.dart';
import '../models/contact.dart';
import '../services/local_storage_service.dart';

class EditContactScreen extends StatefulWidget {
  const EditContactScreen({Key? key}) : super(key: key);

  @override
  State<EditContactScreen> createState() => _EditContactScreenState();
}

class _EditContactScreenState extends State<EditContactScreen> {
  final _formKey = GlobalKey<FormState>();
  late String _name;
  late String _phone;
  late int _id;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    final contact = ModalRoute.of(context)!.settings.arguments as Contact;
    _name = contact.name;
    _phone = contact.phoneNumber;
    _id = contact.id!;
  }

  void _updateContact() async {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      await LocalStorageService().updateContact(
        Contact(id: _id, name: _name, phoneNumber: _phone),
      );
      if (mounted) {
        Navigator.pop(context, true);
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Edit Contact')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              TextFormField(
                initialValue: _name,
                decoration: const InputDecoration(labelText: 'Name'),
                onSaved: (val) => _name = val ?? '',
                validator: (val) =>
                    val == null || val.isEmpty ? 'Enter a name' : null,
              ),
              const SizedBox(height: 16),
              TextFormField(
                initialValue: _phone,
                decoration: const InputDecoration(labelText: 'Phone Number'),
                keyboardType: TextInputType.phone,
                onSaved: (val) => _phone = val ?? '',
                validator: (val) =>
                    val == null || val.isEmpty ? 'Enter a phone number' : null,
              ),
              const SizedBox(height: 32),
              ElevatedButton(
                onPressed: _updateContact,
                child: const Text('Update'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
