import tkinter as tk
from tkinter import ttk
import cx_Oracle

## CONEXIÓN ##
def connect_to_oracle():
    usuario = "C##SERVERA"
    contraseña = "ADMIN"
    host = "localhost"
    puerto = "1521"
    servicio = "FREE"
    try:
        # Establecer la conexión a la base de datos
        connection = cx_Oracle.connect(usuario, contraseña, host + ':' + puerto + '/' + servicio)
        print("Conexión exitosa a la base de datos.")
        return connection
    except cx_Oracle.Error as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Crear la ventana principal
root = tk.Tk()
root.title("CRUD Interface")
root.geometry("250x400")
# Crear el notebook principal
main_notebook = ttk.Notebook(root)
main_notebook.pack(fill='both', expand=True)

# Crear las pestañas principales y sus notebooks secundarios

# CUSTOMERS
customers_frame = ttk.Frame(main_notebook)
main_notebook.add(customers_frame, text="CUSTOMERS")

customers_notebook = ttk.Notebook(customers_frame)
customers_notebook.pack(fill='both', expand=True)

customers_create = ttk.Frame(customers_notebook)
customers_notebook.add(customers_create, text="Create")
customers_read = ttk.Frame(customers_notebook)
customers_notebook.add(customers_read, text="Read")
customers_update = ttk.Frame(customers_notebook)
customers_notebook.add(customers_update, text="Update")
customers_delete = ttk.Frame(customers_notebook)
customers_notebook.add(customers_delete, text="Delete")

# ORDERS
orders_frame = ttk.Frame(main_notebook)
main_notebook.add(orders_frame, text="ORDERS")

orders_notebook = ttk.Notebook(orders_frame)
orders_notebook.pack(fill='both', expand=True)

orders_create = ttk.Frame(orders_notebook)
orders_notebook.add(orders_create, text="Create")
orders_read = ttk.Frame(orders_notebook)
orders_notebook.add(orders_read, text="Read")
orders_update = ttk.Frame(orders_notebook)
orders_notebook.add(orders_update, text="Update")
orders_delete = ttk.Frame(orders_notebook)
orders_notebook.add(orders_delete, text="Delete")

# ITEMS
items_frame = ttk.Frame(main_notebook)
main_notebook.add(items_frame, text="ITEMS")

items_notebook = ttk.Notebook(items_frame)
items_notebook.pack(fill='both', expand=True)

items_create = ttk.Frame(items_notebook)
items_notebook.add(items_create, text="Create")
items_read = ttk.Frame(items_notebook)
items_notebook.add(items_read, text="Read")
items_update = ttk.Frame(items_notebook)
items_notebook.add(items_update, text="Update")
items_delete = ttk.Frame(items_notebook)
items_notebook.add(items_delete, text="Delete")

# PRODUCTS
products_frame = ttk.Frame(main_notebook)
main_notebook.add(products_frame, text="PRODUCTS")

products_notebook = ttk.Notebook(products_frame)
products_notebook.pack(fill='both', expand=True)

products_create = ttk.Frame(products_notebook)
products_notebook.add(products_create, text="Create")
products_read = ttk.Frame(products_notebook)
products_notebook.add(products_read, text="Read")
products_update = ttk.Frame(products_notebook)
products_notebook.add(products_update, text="Update")
products_delete = ttk.Frame(products_notebook)
products_notebook.add(products_delete, text="Delete")

# CUSTOMERS (CREATE)

def create_customer():
    customer_id = customer_id_entry.get()
    nombre = nombre_entry.get()
    apellido = apellido_entry.get()
    credito = credito_entry.get()
    correo = correo_entry.get()
    ingresos = ingresos_entry.get()
    region = region_combobox.get()
    try:
        
        # Conectarse a Oracle
        connection = connect_to_oracle()
        if connection is None:
            return

        # Llamar al procedimiento almacenado
        cursor = connection.cursor()
        cursor.callproc("create_customer", [customer_id, nombre, apellido, credito, correo, ingresos, region])

        # Hacer commit de la transacción
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        print("Cliente creado exitosamente")

    except cx_Oracle.DatabaseError as e:
        error, = e.args
        print("Error al conectar a Oracle:", error.message)


tk.Label(customers_create, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
customer_id_entry = tk.Entry(customers_create)
customer_id_entry.grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Nombre:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
nombre_entry = tk.Entry(customers_create)
nombre_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Apellido:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
apellido_entry = tk.Entry(customers_create)
apellido_entry.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Crédito:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
credito_entry = tk.Entry(customers_create)
credito_entry.grid(row=3, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Correo:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
correo_entry = tk.Entry(customers_create)
correo_entry.grid(row=4, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Ingresos:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
ingresos_entry = tk.Entry(customers_create)
ingresos_entry.grid(row=5, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Región:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
region_combobox = ttk.Combobox(customers_create, values=["A", "B", "C", "D"], width=5, state="readonly")
region_combobox.grid(row=6, column=1, padx=10, pady=10, sticky='w')
region_combobox.set("A")

submit_button = tk.Button(customers_create, text="CREAR", command=create_customer)
submit_button.grid(row=7, column=0, columnspan=2, pady=20)
    
##############################################################################################

# Ejecutar el bucle principal de la ventana
root.mainloop()
