import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Retrieve data from the form fields
    name = entry_name.get()
    email = entry_email.get()
    password = entry_password.get()

    # Basic validation (you can expand this as needed)
    if not name or not email or not password:
        messagebox.showerror("Error", "All fields are required!")
    else:
        # Here you could save the data or process it as needed
        # For demonstration, we're just showing a success message
        messagebox.showinfo("Success", f"Registration successful!\nName: {name}\nEmail: {email}")

# Create the main window
root = tk.Tk()
root.title("Registration Form")

# Create and place the widgets
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Password").grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_password = tk.Entry(root, show="*")  # 'show' hides the password input
entry_password.grid(row=2, column=1, padx=10, pady=5)

tk.Button(root, text="Submit", command=submit_form).grid(row=3, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
