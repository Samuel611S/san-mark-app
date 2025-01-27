import sqlite3
from tkinter import Tk, Label, Entry, Button, StringVar, Text, Scrollbar, Frame,messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from PIL import Image, ImageTk
import pygame


pygame.mixer.init()

# Function to play a "key ring" sound
def play_key_sound():
    pygame.mixer.music.load("save.mp3")  # Load your sound file
    pygame.mixer.music.play()

# Database connection and table creation
conn = sqlite3.connect("new_stmark.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS glasses (
    id INTEGER PRIMARY KEY,
    sale_date TEXT,
    name TEXT,
    phone_number TEXT,
    amount REAL,
    sph_r REAL,
    cyl_r REAL,
    ax_r REAL,
    sph_l REAL,
    cyl_l REAL,
    ax_l REAL,
    ipd REAL,
    lens_type TEXT,
    coating_type TEXT,
    add_plus REAL,
    notes TEXT
)
""")
conn.commit()
conn.close()

# Function to clear all input fields
def clear_entries():
    sale_date_entry.delete(0, "end")
    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    amount_entry.delete(0, "end")
    sph_r_entry.delete(0, "end")
    cyl_r_entry.delete(0, "end")
    ax_r_entry.delete(0, "end")
    sph_l_entry.delete(0, "end")
    cyl_l_entry.delete(0, "end")
    ax_l_entry.delete(0, "end")
    ipd_entry.delete(0, "end")
    add_plus_entry.delete(0, "end")
    lens_type_var.set("")
    coating_type_var.set("")
    notes_text.delete("1.0", "end")
    global editing_id
    editing_id = None

# Function to save data to the database
def save_to_db(event=None):
    sale_date = sale_date_entry.get()
    name = name_entry.get().strip()  # Strip leading/trailing whitespace
    phone_number = phone_entry.get().strip()
    amount = amount_entry.get()
    sph_r = sph_r_entry.get()
    cyl_r = cyl_r_entry.get()
    ax_r = ax_r_entry.get()
    sph_l = sph_l_entry.get()
    cyl_l = cyl_l_entry.get()
    ax_l = ax_l_entry.get()
    ipd = ipd_entry.get()
    lens_type = lens_type_var.get()
    coating_type = coating_type_var.get()
    add_plus = add_plus_entry.get()
    notes = notes_text.get("1.0", "end-1c")

    # Validation: Check if name and phone number are provided
    if not name:
        messagebox.showwarning("Input Error", "Please enter a name.")
        return
    if not phone_number:
        messagebox.showwarning("Input Error", "Please enter a phone number.")
        return

    conn = sqlite3.connect("new_stmark.db")
    cursor = conn.cursor()

    if editing_id:
        cursor.execute("""
        UPDATE glasses
        SET sale_date = ?, name = ?, phone_number = ?, amount = ?, sph_r = ?, cyl_r = ?, ax_r = ?, 
            sph_l = ?, cyl_l = ?, ax_l = ?, ipd = ?, lens_type = ?, coating_type = ?, add_plus = ?, notes = ?
        WHERE id = ?
        """, (sale_date, name, phone_number, amount, sph_r, cyl_r, ax_r, sph_l, cyl_l, ax_l, ipd, lens_type, coating_type, add_plus, notes, editing_id))
        print("Record updated successfully!")
    else:
        cursor.execute("""
        INSERT INTO glasses (sale_date, name, phone_number, amount, sph_r, cyl_r, ax_r, sph_l, cyl_l, ax_l, ipd, lens_type, coating_type, add_plus, notes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (sale_date, name, phone_number, amount, sph_r, cyl_r, ax_r, sph_l, cyl_l, ax_l, ipd, lens_type, coating_type, add_plus, notes))
        print("Record saved successfully!")

    conn.commit()
    conn.close()
    play_key_sound()
    refresh_table()
    clear_entries()

def refresh_entries():
    clear_entries()  # Clear the input fields
    refresh_table()
    play_key_sound()
# Function to delete a selected record from the database
def delete_from_db():
    selected_item = tree.selection()
    if not selected_item:
        print("No item selected to delete!")
        return
    
    # Get the ID of the selected item
    item_values = tree.item(selected_item[0], "values")
    record_id = item_values[0]  # ID is in the first column

    # Delete the record from the database
    conn = sqlite3.connect("new_stmark.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM glasses WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()

    # Remove the item from the TreeView
    tree.delete(selected_item[0])

    # Play a sound to confirm deletion
    play_key_sound()
    clear_entries()

    print(f"Record with ID {record_id} deleted successfully.")

# Function to refresh the table
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    conn = sqlite3.connect("new_stmark.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM glasses")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()

# Function to handle double-click on a treeview row
def on_item_double_click(event):
    selected_item = tree.selection()[0]
    item_values = tree.item(selected_item, "values")
    sale_date_entry.delete(0, "end")
    sale_date_entry.insert(0, item_values[1])
    name_entry.delete(0, "end")
    name_entry.insert(0, item_values[2])
    phone_entry.delete(0, "end")
    phone_entry.insert(0, item_values[3])
    amount_entry.delete(0, "end")
    amount_entry.insert(0, item_values[4])
    sph_r_entry.delete(0, "end")
    sph_r_entry.insert(0, item_values[5])
    cyl_r_entry.delete(0, "end")
    cyl_r_entry.insert(0, item_values[6])
    ax_r_entry.delete(0, "end")
    ax_r_entry.insert(0, item_values[7])
    sph_l_entry.delete(0, "end")
    sph_l_entry.insert(0, item_values[8])
    cyl_l_entry.delete(0, "end")
    cyl_l_entry.insert(0, item_values[9])
    ax_l_entry.delete(0, "end")
    ax_l_entry.insert(0, item_values[10])
    ipd_entry.delete(0, "end")
    ipd_entry.insert(0, item_values[11])
    lens_type_var.set(item_values[12])
    coating_type_var.set(item_values[13])
    add_plus_entry.delete(0, "end")
    add_plus_entry.insert(0, item_values[14])
    notes_text.delete("1.0", "end")
    notes_text.insert("1.0", item_values[15])
    global editing_id
    editing_id = item_values[0]

# Function to search the database
def search_db():
    search_term = search_entry.get()
    conn = sqlite3.connect("new_stmark.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM glasses WHERE name LIKE ? OR phone_number LIKE ?
    """, ('%' + search_term + '%', '%' + search_term + '%'))
    for row in tree.get_children():
        tree.delete(row)
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
    conn.close()
# Function to navigate through input fields using arrow keys
def navigate_input_fields(event):
    current_widget = root.focus_get()  # Get the current focused widget

    # Get a list of input fields in the order you want to navigate
    input_fields = [
        sale_date_entry, name_entry, phone_entry, amount_entry,
        sph_r_entry, cyl_r_entry, ax_r_entry,
        sph_l_entry, cyl_l_entry, ax_l_entry,
        ipd_entry, lens_type_menu, coating_type_menu,
        add_plus_entry, notes_text
    ]

    if current_widget in input_fields:
        current_index = input_fields.index(current_widget)

        if event.keysym == 'Down':
            # Move focus to the next widget
            next_index = (current_index + 1) % len(input_fields)  # Wrap around to first field
            input_fields[next_index].focus_set()  # Set focus to the next widget
        elif event.keysym == 'Up':
            # Move focus to the previous widget
            next_index = (current_index - 1) % len(input_fields)  # Wrap around to last field
            input_fields[next_index].focus_set()  # Set focus to the previous widget

# Main GUI setup
root = Tk()
root.title("Glasses Registration")
root.geometry("1200x850")
root.configure(bg="#dfe6e9")  # Light grey background
# Bind the arrow keys to the navigate_tree function
root.bind("<KeyPress-Up>", navigate_input_fields)
root.bind("<KeyPress-Down>", navigate_input_fields)

# Logo setup
image = Image.open("sanmark.jpg").resize((1100, 417), Image.Resampling.LANCZOS)  # Enlarged image
photo = ImageTk.PhotoImage(image)
logo_label = Label(root, image=photo, bg="#dfe6e9")
logo_label.grid(row=0, column=3, rowspan=2, padx=10, pady=10)

# Frame for form
form_frame = Frame(root, bg="#f9f9f9", bd=2, relief="ridge")
form_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Input fields
sale_date_entry = DateEntry(form_frame, date_pattern='yyyy-mm-dd')
name_entry = Entry(form_frame)
phone_entry = Entry(form_frame)
amount_entry = Entry(form_frame)
sph_r_entry = Entry(form_frame)
cyl_r_entry = Entry(form_frame)
ax_r_entry = Entry(form_frame)
sph_l_entry = Entry(form_frame)
cyl_l_entry = Entry(form_frame)
ax_l_entry = Entry(form_frame)
ipd_entry = Entry(form_frame)
add_plus_entry = Entry(form_frame)

lens_type_var = StringVar()
lens_type_menu = ttk.Combobox(form_frame, textvariable=lens_type_var, values=["Single Vision", "Bifocal", "Progressive"])
coating_type_var = StringVar()
coating_type_menu = ttk.Combobox(form_frame, textvariable=coating_type_var, values=["Anti-Reflective", "UV Protection", "Scratch Resistant", "Blue Light Protection"])
notes_text = Text(form_frame, height=4, width=40)

# Place input fields on the grid
labels = [
    "Sale Date / تاريخ البيع", 
    "Name / الاسم", 
    "Phone Number / رقم الهاتف", 
    "Amount / المبلغ", 
    "SPH (R) / قوة العدسة (يمين)", 
    "CYL (R) / استجماتيزم (يمين)", 
    "AX (R) / محور (يمين)", 
    "SPH (L) / قوة العدسة (يسار)", 
    "CYL (L) / استجماتيزم (يسار)", 
    "AX (L) / محور (يسار)", 
    "IPD / المسافة بين حدقتي العين", 
    "Lens Type / نوع العدسة", 
    "Coating Type / نوع الطلاء", 
    "Add+ / إضافة+", 
    "Notes / ملاحظات"
]
fields = [sale_date_entry, name_entry, phone_entry, amount_entry, sph_r_entry, cyl_r_entry, ax_r_entry, sph_l_entry, cyl_l_entry, ax_l_entry, ipd_entry]

for i, (label, field) in enumerate(zip(labels[:11], fields)):
    Label(form_frame, text=label, bg="#f9f9f9").grid(row=i, column=0, sticky="w", padx=10, pady=5)
    field.grid(row=i, column=1, padx=10, pady=5)

Label(form_frame, text="Lens Type", bg="#f9f9f9").grid(row=11, column=0, sticky="w", padx=10, pady=5)
lens_type_menu.grid(row=11, column=1, padx=10, pady=5)
Label(form_frame, text="Coating Type", bg="#f9f9f9").grid(row=12, column=0, sticky="w", padx=10, pady=5)
coating_type_menu.grid(row=12, column=1, padx=10, pady=5)
Label(form_frame, text="Add+", bg="#f9f9f9").grid(row=13, column=0, sticky="w", padx=10, pady=5)
add_plus_entry.grid(row=13, column=1, padx=10, pady=5)
Label(form_frame, text="Notes", bg="#f9f9f9").grid(row=14, column=0, sticky="nw", padx=10, pady=5)
notes_text.grid(row=14, column=1, padx=10, pady=5)

# Buttons and search bar
button_frame = Frame(root, bg="#dfe6e9")
button_frame.grid(row=1, column=0, columnspan=2, pady=10)

Button(button_frame, text="Save", command=save_to_db, bg="#4CAF50", fg="white").pack(side="left", padx=10)
Button(button_frame, text="Search", command=search_db, bg="#2196F3", fg="white").pack(side="left", padx=10)
Button(button_frame, text="Delete", command=delete_from_db, bg="#F44336", fg="white").pack(side="left", padx=10)
Button(button_frame, text="Refresh", command=refresh_entries, bg="#FFC107", fg="black").pack(side="left", padx=10)  # Add the Refresh button
search_entry = Entry(button_frame, width=40)
search_entry.pack(side="left", padx=10)

# Treeview for displaying records
tree_frame = Frame(root, bg="#dfe6e9")
tree_frame.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Create the Treeview with columns
tree = ttk.Treeview(tree_frame, columns=("ID", "Sale Date", "Name", "Phone Number", "Amount", 
                                         "SPH (R)", "CYL (R)", "AX (R)", "SPH (L)", "CYL (L)", 
                                         "AX (L)", "IPD", "Lens Type", "Coating Type", "Add+", "Notes"), 
                    show="headings", height=10)  # Adjust height if needed
tree.pack(side="left", fill="both", expand=True)

# Scrollbars for the Treeview
scrollbar = Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scrollbar.pack(side="right", fill="y")
tree.configure(yscrollcommand=scrollbar.set)

# Horizontal scrollbar
h_scrollbar = Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
h_scrollbar.pack(side="bottom", fill="x")
tree.configure(xscrollcommand=h_scrollbar.set)

# Configure Treeview Columns with specific widths
column_widths = [50, 80, 150, 100, 80, 60, 60, 60, 60, 60, 60, 80, 100, 100, 60, 200]  # Increased width for Notes
for col, width in zip(tree["columns"], column_widths):
    tree.heading(col, text=col)
    tree.column(col, width=width, anchor="center")

# Events
tree.bind("<Double-1>", on_item_double_click)

# Run GUI
refresh_table()
editing_id = None
root.mainloop()
