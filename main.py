import tkinter as tk
from tkinter import ttk
import re
import oracledb

def conexion():
    usuario = "C##SERVERA"
    contraseña = "ADMIN"
    host = "localhost"
    puerto = "1521"
    servicio = "FREE"
    try:
        # Establecer la conexión a la base de datos
        connection = oracledb.connect(user=usuario, password=contraseña, dsn=f"{host}:{puerto}/{servicio}")
        print("Conexión exitosa a la base de datos.")
        return connection
    except oracledb.DatabaseError as error:
        print("Error al conectar a la base de datos:", error)
        return None

# Crear la ventana principal
root = tk.Tk()
root.title("Proyecto 2")
root.geometry("1430x400")
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

# =================================== CUSTOMERS (CREATE) =================================== #

def create_customer():
    customer_id = C_C_CustomerID.get()
    nombre = C_C_Nombre.get()
    apellido = C_C_Apellido.get()
    credito = C_C_Credito.get()
    correo = C_C_Correo.get()
    ingresos = C_C_Ingresos.get()
    region = C_C_Region.get()
    try:
        
        # Conectarse a Oracle
        connection = conexion()
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

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)

tk.Label(customers_create, text="Customer ID:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
C_C_CustomerID = tk.Entry(customers_create)
C_C_CustomerID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Nombre:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
C_C_Nombre = tk.Entry(customers_create)
C_C_Nombre.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Apellido:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
C_C_Apellido = tk.Entry(customers_create)
C_C_Apellido.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Crédito:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
C_C_Credito = tk.Entry(customers_create)
C_C_Credito.grid(row=3, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Correo:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
C_C_Correo = tk.Entry(customers_create)
C_C_Correo.grid(row=4, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Ingresos:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
C_C_Ingresos = tk.Entry(customers_create)
C_C_Ingresos.grid(row=5, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_create, text="Región:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
C_C_Region = ttk.Combobox(customers_create, values=["A", "B", "C", "D"], width=5, state="readonly")
C_C_Region.grid(row=6, column=1, padx=10, pady=10, sticky='w')
C_C_Region.set("A")

C_C_BTNCrear = tk.Button(customers_create, text="CREAR", command=create_customer)
C_C_BTNCrear.grid(row=7, column=0, columnspan=2, pady=20)
    
# ========================================================================================== #

# ==================================== CUSTOMERS (READ) ==================================== #
def list_all_customers():
    try:
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()

        p_cursor = cursor.var(oracledb.CURSOR)

        # Ejecutar el procedimiento almacenado
        cursor.callproc("list_all_customers", [p_cursor])

        result = p_cursor.getvalue().fetchall()

        return result

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)
        return None
    
def show_customers():
    # Obtener los clientes
    customers = list_all_customers()

    if customers:
        # Limpiar la tabla
        for row in C_R_Tabla.get_children():
            C_R_Tabla.delete(row)

        # Agregar los clientes a la tabla
        for customer in customers:
            C_R_Tabla.insert("", "end", values=customer)

# Tabla de Clientes
C_R_Tabla = ttk.Treeview(customers_read, columns=("Customer ID", "Nombre", "Apellido", "Crédito", "Correo", "Ingresos", "Región"), show="headings")
C_R_Tabla.heading("Customer ID", text="Customer ID")
C_R_Tabla.heading("Nombre", text="Nombre")
C_R_Tabla.heading("Apellido", text="Apellido")
C_R_Tabla.heading("Crédito", text="Crédito")
C_R_Tabla.heading("Correo", text="Correo")
C_R_Tabla.heading("Ingresos", text="Ingresos")
C_R_Tabla.heading("Región", text="Región")
C_R_Tabla.grid(row=0, column=0, sticky="nsew")
scrollbar = ttk.Scrollbar(customers_read, orient="vertical", command=C_R_Tabla.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
C_R_Tabla.configure(yscrollcommand=scrollbar.set)

load_button = ttk.Button(customers_read, text="Cargar/Actualizar Clientes", command=show_customers)
load_button.grid(row=1, column=0, sticky="ew")
# ========================================================================================== #

# =================================== CUSTOMERS (UPDATE) =================================== #

# ========================================================================================== #

# =================================== CUSTOMERS (DELETE) =================================== #

# ========================================================================================== #

# ====================================== VALIDACIONES ====================================== #
def val_customer_id(entry_text):
    return entry_text.isdigit() and len(entry_text) <= 6 or entry_text == ""
validation = root.register(val_customer_id)
C_C_CustomerID.config(validate="key", validatecommand=(validation, "%P"))

def val_nombreapellido(entry_text):
    return all (char.isalpha() or char.isspace() for char in entry_text) and len(entry_text) <= 20 or entry_text == " " or entry_text == ""
validation = root.register(val_nombreapellido)
C_C_Nombre.config(validate="key", validatecommand=(validation, "%P"))
C_C_Apellido.config(validate="key", validatecommand=(validation, "%P"))

def val_credito(entry_text):
    pattern = r'^\d{0,7}(\.\d{0,2})?$'
    return re.match(pattern, entry_text) is not None
validation = root.register(val_credito)
C_C_Credito.config(validate="key", validatecommand=(validation, "%P"))

def val_correo(entry_text):
    return len(entry_text) <= 30 or entry_text == ""
validation = root.register(val_correo)
C_C_Correo.config(validate="key", validatecommand=(validation, "%P"))

def val_ingresos(entry_text):
    return len(entry_text) <= 20 or entry_text == ""
validation = root.register(val_ingresos)
C_C_Ingresos.config(validate="key", validatecommand=(validation, "%P"))
# ========================================================================================== #

root.mainloop()
