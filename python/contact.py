import tkinter as tk
from tkinter import simpledialog, messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x300")
        self.root.configure(bg="lightgray")

        self.contacts = {
            "John": {"email": "john@example.com", "phone": "123-456-7890"},
            "Alice": {"email": "alice@example.com", "phone": "987-654-3210"},
        }

        self.listbox = tk.Listbox(self.root, bg="white", fg="black")
        self.listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.update_listbox()

        buttons_frame = tk.Frame(self.root, bg="lightgray")
        buttons_frame.pack(padx=10, pady=5, fill=tk.X)

        add_button = tk.Button(buttons_frame, text="Add", command=self.add_contact, bg="lightblue")
        add_button.pack(side=tk.LEFT, padx=5)

        delete_button = tk.Button(buttons_frame, text="Delete", command=self.delete_contact, bg="lightgreen")
        delete_button.pack(side=tk.LEFT, padx=5)

        edit_button = tk.Button(buttons_frame, text="Edit", command=self.edit_contact, bg="lightcoral")
        edit_button.pack(side=tk.LEFT, padx=5)

    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for contact, details in self.contacts.items():
            self.listbox.insert(tk.END, f"{contact} - {details['email']} - {details['phone']}")

    def add_contact(self):
        name = simpledialog.askstring("Input", "Enter Name:")
        if name:
            email = simpledialog.askstring("Input", "Enter Email:")
            if email:
                phone = simpledialog.askstring("Input", "Enter Phone Number:")
                if phone:
                    self.contacts[name] = {"email": email, "phone": phone}
                    self.update_listbox()

    def delete_contact(self):
        selection = self.listbox.curselection()
        if selection:
            contact = self.listbox.get(selection)
            name = contact.split(" - ")[0]
            del self.contacts[name]
            self.update_listbox()

    def edit_contact(self):
        selection = self.listbox.curselection()
        if selection:
            contact = self.listbox.get(selection)
            name = contact.split(" - ")[0]
            new_email = simpledialog.askstring("Input", "Enter New Email:")
            if new_email:
                new_phone = simpledialog.askstring("Input", "Enter New Phone Number:")
                if new_phone:
                    self.contacts[name] = {"email": new_email, "phone": new_phone}
                    self.update_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
