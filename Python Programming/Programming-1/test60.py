import tkinter as tk
from tkinter import messagebox


class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.next = None  # Pointer to the next contact


class ContactBook:
    def __init__(self):
        self.head = None  # Head of the linked list

    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email)
        if not self.head:
            self.head = new_contact
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_contact

    def update_contact(self, name, new_phone_number, new_email):
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                current.phone_number = new_phone_number
                current.email = new_email
                return True
            current = current.next
        return False

    def delete_contact(self, name):
        if not self.head:
            return False

        if self.head.name.lower() == name.lower():
            self.head = self.head.next
            return True

        current = self.head
        while current.next and current.next.name.lower() != name.lower():
            current = current.next

        if current.next:
            current.next = current.next.next
            return True
        return False

    def search_contact(self, keyword):
        current = self.head
        results = []
        while current:
            if keyword.lower() in current.name.lower() or keyword in current.phone_number:
                results.append(f"{current.name} | {current.phone_number} | {current.email}")
            current = current.next
        return results

    def sort_contacts_by_name(self):
        if not self.head or not self.head.next:
            return

        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next:
                if current.name.lower() > current.next.name.lower():
                    # Swap data
                    current.name, current.next.name = current.next.name, current.name
                    current.phone_number, current.next.phone_number = current.next.phone_number, current.phone_number
                    current.email, current.next.email = current.next.email, current.email
                    swapped = True
                current = current.next

    def display_contacts(self):
        current = self.head
        contacts = []
        while current:
            contacts.append(f"{current.name} | {current.phone_number} | {current.email}")
            current = current.next
        return contacts


# GUI Application
class ContactBookApp:
    def __init__(self, root):
        self.contact_book = ContactBook()

        root.title("Contact Book")
        root.geometry("600x400")

        # Add Contact Section
        tk.Label(root, text="Add Contact").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(root, text="Name").grid(row=1, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1)

        tk.Label(root, text="Phone").grid(row=2, column=0)
        self.phone_entry = tk.Entry(root)
        self.phone_entry.grid(row=2, column=1)

        tk.Label(root, text="Email").grid(row=3, column=0)
        self.email_entry = tk.Entry(root)
        self.email_entry.grid(row=3, column=1)

        tk.Button(root, text="Add", command=self.add_contact).grid(row=4, column=0, columnspan=2, pady=10)

        # Action Buttons
        tk.Button(root, text="Update", command=self.update_contact).grid(row=5, column=0, pady=5)
        tk.Button(root, text="Delete", command=self.delete_contact).grid(row=5, column=1, pady=5)
        tk.Button(root, text="Search", command=self.search_contact).grid(row=6, column=0, pady=5)
        tk.Button(root, text="Sort", command=self.sort_contacts).grid(row=6, column=1, pady=5)

        # Display Section
        self.contact_listbox = tk.Listbox(root, width=50, height=10)
        self.contact_listbox.grid(row=7, column=0, columnspan=2, pady=10)

        tk.Button(root, text="Display All", command=self.display_contacts).grid(row=8, column=0, columnspan=2)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.contact_book.add_contact(name, phone, email)
            messagebox.showinfo("Success", "Contact added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "All fields are required!")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if self.contact_book.update_contact(name, phone, email):
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")
        self.clear_entries()

    def delete_contact(self):
        name = self.name_entry.get()
        if self.contact_book.delete_contact(name):
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found!")
        self.clear_entries()

    def search_contact(self):
        keyword = self.name_entry.get()
        results = self.contact_book.search_contact(keyword)
        self.contact_listbox.delete(0, tk.END)
        if results:
            for contact in results:
                self.contact_listbox.insert(tk.END, contact)
        else:
            messagebox.showinfo("Info", "No matching contacts found.")

    def sort_contacts(self):
        self.contact_book.sort_contacts_by_name()
        messagebox.showinfo("Success", "Contacts sorted by name!")
        self.display_contacts()

    def display_contacts(self):
        self.contact_listbox.delete(0, tk.END)
        contacts = self.contact_book.display_contacts()
        if contacts:
            for contact in contacts:
                self.contact_listbox.insert(tk.END, contact)
        else:
            self.contact_listbox.insert(tk.END, "No contacts to display.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
