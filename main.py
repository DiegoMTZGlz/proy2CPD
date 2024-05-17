import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Proyecto 2")
root.geometry("400x300")

# Crear el widget Notebook
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Crear los frames para cada operación CRUD
create_tab = ttk.Frame(notebook, width=400, height=280)
read_tab = ttk.Frame(notebook, width=400, height=280)
update_tab = ttk.Frame(notebook, width=400, height=280)
delete_tab = ttk.Frame(notebook, width=400, height=280)

for frame in (create_tab, read_tab, update_tab, delete_tab):
    frame.pack(fill='both', expand=True)

# Agregar las pestañas al Notebook
notebook.add(create_tab, text='Crear')
notebook.add(read_tab, text='Leer')
notebook.add(update_tab, text='Actualizar')
notebook.add(delete_tab, text='Eliminar')

# Inicializar la lista de datos
data = []

# Configurar la pestaña de Crear
ttk.Label(create_tab, text="Nombre:").pack(pady=10)
create_name_entry = ttk.Entry(create_tab)
create_name_entry.pack(pady=10)

def create_record():
    name = create_name_entry.get()
    if name:
        data.append(name)
        create_name_entry.delete(0, tk.END)
        update_read_listbox()
        messagebox.showinfo("Crear", f"Registro '{name}' creado con éxito")
    else:
        messagebox.showwarning("Crear", "El campo Nombre no puede estar vacío")

ttk.Button(create_tab, text="Crear", command=create_record).pack(pady=10)

# Configurar la pestaña de Leer
read_listbox = tk.Listbox(read_tab)
read_listbox.pack(pady=10, padx=10, expand=True, fill='both')

def update_read_listbox():
    read_listbox.delete(0, tk.END)
    for index, record in enumerate(data, start=1):
        read_listbox.insert(tk.END, f"{index}: {record}")

update_read_listbox()

# Configurar la pestaña de Actualizar
ttk.Label(update_tab, text="ID:").pack(pady=10)
update_id_entry = ttk.Entry(update_tab)
update_id_entry.pack(pady=10)

ttk.Label(update_tab, text="Nuevo Nombre:").pack(pady=10)
update_name_entry = ttk.Entry(update_tab)
update_name_entry.pack(pady=10)

def update_record():
    try:
        record_id = int(update_id_entry.get()) - 1
        new_name = update_name_entry.get()
        if 0 <= record_id < len(data) and new_name:
            data[record_id] = new_name
            update_id_entry.delete(0, tk.END)
            update_name_entry.delete(0, tk.END)
            update_read_listbox()
            messagebox.showinfo("Actualizar", f"Registro ID {record_id + 1} actualizado con éxito")
        else:
            messagebox.showwarning("Actualizar", "ID no válido o campo Nombre vacío")
    except ValueError:
        messagebox.showwarning("Actualizar", "ID debe ser un número válido")

ttk.Button(update_tab, text="Actualizar", command=update_record).pack(pady=10)

# Configurar la pestaña de Eliminar
ttk.Label(delete_tab, text="ID:").pack(pady=10)
delete_id_entry = ttk.Entry(delete_tab)
delete_id_entry.pack(pady=10)

def delete_record():
    try:
        record_id = int(delete_id_entry.get()) - 1
        if 0 <= record_id < len(data):
            deleted_record = data.pop(record_id)
            delete_id_entry.delete(0, tk.END)
            update_read_listbox()
            messagebox.showinfo("Eliminar", f"Registro '{deleted_record}' eliminado con éxito")
        else:
            messagebox.showwarning("Eliminar", "ID no válido")
    except ValueError:
        messagebox.showwarning("Eliminar", "ID debe ser un número válido")

ttk.Button(delete_tab, text="Eliminar", command=delete_record).pack(pady=10)

# Ejecutar el bucle principal
root.mainloop()
