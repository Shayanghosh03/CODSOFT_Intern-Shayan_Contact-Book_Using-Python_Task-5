import tkinter as tk
from tkinter import messagebox, simpledialog
import json

# File to store contact data
FILE_NAME = "contacts.json"

# Load contacts from file
def load_contacts():
    """Load contacts from a JSON file."""
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save contacts to file
def save_contacts():
    """Save contacts to a JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact():
    """Add a new contact to the list."""
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name:
        messagebox.showerror("Error", "Name is required!")
        return
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    if not phone:
        messagebox.showerror("Error", "Phone number is required!")
        return
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contacts()
    refresh_contact_list()
    messagebox.showinfo("Success", f"Contact '{name}' added successfully!")

# Refresh the contact list
def refresh_contact_list():
    """Refresh the displayed list of contacts."""
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['name']} - {contact['phone']}")

# View selected contact details
def view_contact():
    """View details of the selected contact."""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected!")
        return
    index = selected[0]
    contact = contacts[index]
    messagebox.showinfo(
        "Contact Details",
        f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}",
    )

# Update a selected contact
def update_contact():
    """Update details of the selected contact."""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected!")
        return
    index = selected[0]
    contact = contacts[index]
    new_name = simpledialog.askstring("Update Contact", "Enter New Name:", initialvalue=contact["name"])
    new_phone = simpledialog.askstring("Update Contact", "Enter New Phone Number:", initialvalue=contact["phone"])
    new_email = simpledialog.askstring("Update Contact", "Enter New Email:", initialvalue=contact["email"])
    new_address = simpledialog.askstring("Update Contact", "Enter New Address:", initialvalue=contact["address"])
    if new_name and new_phone:
        contact.update({"name": new_name, "phone": new_phone, "email": new_email, "address": new_address})
        save_contacts()
        refresh_contact_list()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Name and phone number are required!")

# Delete a selected contact
def delete_contact():
    """Delete the selected contact from the list."""
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "No contact selected!")
        return
    index = selected[0]
    contact = contacts[index]
    confirm = messagebox.askyesno("Delete Contact", f"Are you sure you want to delete '{contact['name']}'?")
    if confirm:
        contacts.pop(index)
        save_contacts()
        refresh_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")

# Exit the application
def exit_app():
    """Close the application."""
    root.destroy()

# Load contacts
contacts = load_contacts()

# Create the main application window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x400")

# Heading
heading = tk.Label(root, text="Contact Book", font=("Arial", 20, "bold"))
heading.pack(pady=10)

# Listbox to display contacts
listbox = tk.Listbox(root, font=("Arial", 12), height=15)
listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
refresh_contact_list()

# Buttons for actions
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Add Contact", width=15, command=add_contact)
btn_add.grid(row=0, column=0, padx=5)

btn_view = tk.Button(button_frame, text="View Contact", width=15, command=view_contact)
btn_view.grid(row=0, column=1, padx=5)

btn_update = tk.Button(button_frame, text="Update Contact", width=15, command=update_contact)
btn_update.grid(row=1, column=0, padx=5, pady=5)

btn_delete = tk.Button(button_frame, text="Delete Contact", width=15, command=delete_contact)
btn_delete.grid(row=1, column=1, padx=5, pady=5)

btn_exit = tk.Button(button_frame, text="Exit", width=15, command=exit_app)
btn_exit.grid(row=2, column=0, columnspan=2, pady=5)

# Run the application
root.mainloop()
