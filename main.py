import tkinter as tk
from tkinter import ttk
import re
from tkinter import messagebox
import oracledb
from tkcalendar import DateEntry
import datetime

def clear_entries(frame):
    for widget in frame.winfo_children():
        if isinstance(widget, tk.Entry):
            widget.delete(0, tk.END)
        elif isinstance(widget, ttk.Combobox):
            widget.set('')
        elif isinstance(widget, DateEntry):
            widget.set_date(datetime.datetime.now())
        elif isinstance(widget, tk.Spinbox):
            widget.delete(0, tk.END)
            if 'hour' in widget._name:
                widget.insert(0, datetime.datetime.now().strftime("%H"))
            elif 'minute' in widget._name:
                widget.insert(0, datetime.datetime.now().strftime("%M"))
            elif 'second' in widget._name:
                widget.insert(0, datetime.datetime.now().strftime("%S"))

def conexion():
    usuario = "SYSTEM"
    contraseña = "12345"
    host = "localhost"
    puerto = "1521"
    servicio = "FREE"
    try:
        connection = oracledb.connect(user=usuario, password=contraseña, dsn=f"{host}:{puerto}/{servicio}")
        print("Conexión exitosa a la base de datos.")
        return connection
    except oracledb.DatabaseError as error:
        print("Error al conectar a la base de datos:", error)
        return None
    
def apply_custom_styles():
    style = ttk.Style()
    

    style.theme_use('clam') 
    style.configure('.', font=('Helvetica', 12), foreground='black', background='#F0F0F0')
    

    style.configure('TButton', font=('Helvetica', 12), foreground='white', background='#007ACC')  
    style.map('TButton', background=[('active', '#005f91')]) 
    

    style.configure('TEntry', font=('Helvetica', 12), fieldbackground='white', foreground='black') 
    style.configure('TNotebook', tabposition='n', font=('Helvetica', 12), foreground='black', background='#F0F0F0')  
    style.configure('TFrame', background='#F0F0F0')


root = tk.Tk()
root.title("Proyecto 2")
root.geometry("1055x600")

main_notebook = ttk.Notebook(root)
main_notebook.pack(fill='both', expand=True)


# CUSTOMERS
customers_frame = ttk.Frame(main_notebook)
main_notebook.add(customers_frame, text="CUSTOMERS")

customers_notebook = ttk.Notebook(customers_frame)
customers_notebook.pack(fill='both', expand=True)

customers_create = ttk.Frame(customers_notebook)
customers_notebook.add(customers_create, text="AGREGAR (+)")
customers_read = ttk.Frame(customers_notebook)
customers_notebook.add(customers_read, text="BUSCAR (?)")
customers_update = ttk.Frame(customers_notebook)
customers_notebook.add(customers_update, text="ACTUALIZAR (*)")
customers_delete = ttk.Frame(customers_notebook)
customers_notebook.add(customers_delete, text="ELIMINAR (-)")

# ORDERS
orders_frame = ttk.Frame(main_notebook)
main_notebook.add(orders_frame, text="ORDERS")

orders_notebook = ttk.Notebook(orders_frame)
orders_notebook.pack(fill='both', expand=True)

orders_create = ttk.Frame(orders_notebook)
orders_notebook.add(orders_create, text="AGREGAR (+)")
orders_read = ttk.Frame(orders_notebook)
orders_notebook.add(orders_read, text="BUSCAR (?)")
orders_update = ttk.Frame(orders_notebook)
orders_notebook.add(orders_update, text="ACTUALIZAR (*)")
orders_delete = ttk.Frame(orders_notebook)
orders_notebook.add(orders_delete, text="ELIMINAR (-)")

# ITEMS
items_frame = ttk.Frame(main_notebook)
main_notebook.add(items_frame, text="ITEMS")

items_notebook = ttk.Notebook(items_frame)
items_notebook.pack(fill='both', expand=True)

items_create = ttk.Frame(items_notebook)
items_notebook.add(items_create, text="AGREGAR (+)")
items_read = ttk.Frame(items_notebook)
items_notebook.add(items_read, text="BUSCAR (?)")
items_update = ttk.Frame(items_notebook)
items_notebook.add(items_update, text="ACTUALIZAR (*)")
items_delete = ttk.Frame(items_notebook)
items_notebook.add(items_delete, text="ELIMINAR (-)")

# PRODUCTS
products_frame = ttk.Frame(main_notebook)
main_notebook.add(products_frame, text="PRODUCTS")

products_notebook = ttk.Notebook(products_frame)
products_notebook.pack(fill='both', expand=True)

products_create = ttk.Frame(products_notebook)
products_notebook.add(products_create, text="AGREGAR (+)")
products_read = ttk.Frame(products_notebook)
products_notebook.add(products_read, text="BUSCAR (?)")
products_update = ttk.Frame(products_notebook)
products_notebook.add(products_update, text="ACTUALIZAR (*)")
products_delete = ttk.Frame(products_notebook)
products_notebook.add(products_delete, text="ELIMINAR (-)")

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
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()
        
        # Verificar si el cliente ya existe
        cursor.execute("SELECT COUNT(*) FROM customers WHERE CUSTOMER_ID = :customer_id", {"customer_id": customer_id})
        count = cursor.fetchone()[0]
        
        if count == 0:
            cursor.callproc("create_customer", [customer_id, nombre, apellido, credito, correo, ingresos, region])
            connection.commit()
            print("Cliente creado exitosamente")
        else:
            print("El cliente ya existe, no se pudo crear")

        cursor.close()
        connection.close()

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)


tk.Label(customers_create, text="ID Cliente:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
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
C_C_BTNCrear.grid(row=7, column=0, pady=20)

C_C_BTNLimpiar = tk.Button(customers_create, text="LIMPIAR", command=lambda: clear_entries(customers_create))
C_C_BTNLimpiar.grid(row=7, column=1, pady=20)
    
# ========================================================================================== #

# ==================================== CUSTOMERS (READ) ==================================== #

def list_all_customers():
    try:
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()

        p_cursor = cursor.var(oracledb.CURSOR)

        cursor.callproc("list_all_customers", [p_cursor])

        result = p_cursor.getvalue().fetchall()

        return result

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)
        return None
    
def show_customers():

    customers = list_all_customers()

    if customers:

        for row in C_R_Tabla.get_children():
            C_R_Tabla.delete(row)

        for customer in customers:
            C_R_Tabla.insert("", "end", values=customer)

C_R_Tabla = ttk.Treeview(customers_read, columns=("ID Cliente", "Nombre", "Apellido", "Crédito", "Correo", "Ingresos", "Región"), show="headings")
C_R_Tabla.heading("ID Cliente", text="ID Cliente")
C_R_Tabla.heading("Nombre", text="Nombre")
C_R_Tabla.heading("Apellido", text="Apellido")
C_R_Tabla.heading("Crédito", text="Crédito")
C_R_Tabla.heading("Correo", text="Correo")
C_R_Tabla.heading("Ingresos", text="Ingresos")
C_R_Tabla.heading("Región", text="Región")
C_R_Tabla.grid(row=0, column=0, sticky="nsew")

column_widths = [120, 120, 120, 100, 200, 100, 100] 
for col, width in zip(C_R_Tabla["columns"], column_widths):
    C_R_Tabla.column(col, width=width)

scrollbar = ttk.Scrollbar(customers_read, orient="vertical", command=C_R_Tabla.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
C_R_Tabla.configure(yscrollcommand=scrollbar.set)

load_button = ttk.Button(customers_read, text="Cargar/Actualizar Clientes", command=show_customers)
load_button.grid(row=1, column=0, sticky="ew")

# ========================================================================================== #

# =================================== CUSTOMERS (UPDATE) =================================== #

def search_customer():
    connection = conexion()
    if connection is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

    customer_id = C_U_CustomerID.get()
    
    if not customer_id:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un Customer ID.")
        return

    try:
        cursor = connection.cursor()
        query = """
        SELECT CUSTOMER_ID, CUST_FIRST_NAME, CUST_LAST_NAME, 
               CREDIT_LIMIT, CUST_EMAIL, INCOME_LEVEL, REGION
        FROM (
            SELECT CUSTOMER_ID, CUST_FIRST_NAME, CUST_LAST_NAME, 
                   CREDIT_LIMIT, CUST_EMAIL, INCOME_LEVEL, REGION 
            FROM customers_fragmented_db1
            UNION ALL
            SELECT CUSTOMER_ID, CUST_FIRST_NAME, CUST_LAST_NAME, 
                   CREDIT_LIMIT, CUST_EMAIL, INCOME_LEVEL, REGION 
            FROM customers_db2
        )
        WHERE CUSTOMER_ID = :customer_id
        """
        cursor.execute(query, customer_id=customer_id)
        result = cursor.fetchone()
        
        if result:
            C_U_Nombre.delete(0, tk.END)
            C_U_Nombre.insert(0, result[1])
            
            C_U_Apellido.delete(0, tk.END)
            C_U_Apellido.insert(0, result[2])
            
            C_U_Credito.delete(0, tk.END)
            C_U_Credito.insert(0, result[3])
            
            C_U_Correo.delete(0, tk.END)
            C_U_Correo.insert(0, result[4])
            
            C_U_Ingresos.delete(0, tk.END)
            C_U_Ingresos.insert(0, result[5])
            
            C_U_Region.set(result[6])
        else:
            messagebox.showinfo("Información", "No se encontró ningún cliente con ese ID.")
    except oracledb.DatabaseError as error:
        messagebox.showerror("Error", f"Error al buscar el cliente: {error}")
    finally:
        if connection:
            connection.close()

def update_customer():
    customer_id = C_U_CustomerID.get()
    nombre = C_U_Nombre.get()
    apellido = C_U_Apellido.get()
    credito = C_U_Credito.get()
    correo = C_U_Correo.get()
    ingresos = C_U_Ingresos.get()
    region = C_U_Region.get()
    
    try:
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.callproc("update_customer", [customer_id, nombre, apellido, credito, correo, ingresos, region])

        connection.commit()

        cursor.close()
        connection.close()

        print("Cliente actualizado exitosamente")
        clear_entries(customers_update)

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)

        messagebox.showerror("Error", f"Error al actualizar el cliente: {error}")

tk.Label(customers_update, text="ID Cliente:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
C_U_CustomerID = tk.Entry(customers_update)
C_U_CustomerID.grid(row=0, column=1, padx=10, pady=10, sticky='w')
C_U_BTNBuscar = tk.Button(customers_update, text="BUSCAR", command=search_customer)
C_U_BTNBuscar.grid(row=0, column=2, columnspan=2, pady=10)

tk.Label(customers_update, text="Nombre:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
C_U_Nombre = tk.Entry(customers_update)
C_U_Nombre.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_update, text="Apellido:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
C_U_Apellido = tk.Entry(customers_update)
C_U_Apellido.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_update, text="Crédito:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
C_U_Credito = tk.Entry(customers_update)
C_U_Credito.grid(row=3, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_update, text="Correo:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
C_U_Correo = tk.Entry(customers_update)
C_U_Correo.grid(row=4, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_update, text="Ingresos:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
C_U_Ingresos = tk.Entry(customers_update)
C_U_Ingresos.grid(row=5, column=1, padx=10, pady=10, sticky='w')

tk.Label(customers_update, text="Región:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
C_U_Region = ttk.Combobox(customers_update, values=["A", "B", "C", "D"], width=5, state="readonly")
C_U_Region.grid(row=6, column=1, padx=10, pady=10, sticky='w')
C_U_Region.set("A")

C_U_BTNActualizar = tk.Button(customers_update, text="ACTUALIZAR", command=update_customer)
C_U_BTNActualizar.grid(row=7, column=0, pady=20)

C_U_BTNLimpiar = tk.Button(customers_update, text="LIMPIAR", command=lambda: clear_entries(customers_update))
C_U_BTNLimpiar.grid(row=7, column=1, pady=20)

# ========================================================================================== #

# =================================== CUSTOMERS (DELETE) =================================== #
def delete_customer():
    connection = conexion()
    if connection is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

    customer_id = C_D_CustomerID.get()
    
    if not customer_id:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un Customer ID.")
        return

    try:
        cursor = connection.cursor()
        query = """
        SELECT CUSTOMER_ID, CUST_FIRST_NAME, CUST_LAST_NAME, 
               CREDIT_LIMIT, CUST_EMAIL, INCOME_LEVEL, REGION
        FROM (
            SELECT CUSTOMER_ID, CUST_FIRST_NAME, CUST_LAST_NAME, 
                   CREDIT_LIMIT, CUST_EMAIL, INCOME_LEVEL, REGION 
            FROM customers_fragmented_db1
            UNION ALL
            SELECT CUSTOMER_ID, CUST_FIRST_NAME, CUST_LAST_NAME, 
                   CREDIT_LIMIT, CUST_EMAIL, INCOME_LEVEL, REGION 
            FROM customers_db2
        )
        WHERE CUSTOMER_ID = :customer_id
        """
        cursor.execute(query, customer_id=customer_id)
        result = cursor.fetchone()
        
        if result:
            msg = f"ID: {result[0]}\nNombre: {result[1]} {result[2]}\nCrédito: {result[3]}\nCorreo: {result[4]}\nIngresos: {result[5]}\nRegión: {result[6]}"
            confirm_delete = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que quieres eliminar el siguiente registro?\n\n{msg}")
            if confirm_delete:
                cursor.callproc("delete_customer", [customer_id])
                connection.commit()
                messagebox.showinfo("Información", f"Cliente con ID {customer_id} eliminado correctamente.")
                clear_entries(customers_delete)
        else:
            messagebox.showinfo("Información", "No se encontró ningún cliente con ese ID.")
    except oracledb.DatabaseError as error:
        messagebox.showerror("Error", f"Error al buscar o eliminar el cliente: {error}")
    finally:
        if connection:
            connection.close()

tk.Label(customers_delete, text="ID Cliente:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
C_D_CustomerID = tk.Entry(customers_delete)
C_D_CustomerID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

C_D_BTNEliminar = tk.Button(customers_delete, text="ELIMINAR", command=delete_customer)
C_D_BTNEliminar.grid(row=2, column=0, pady=20)

C_D_BTNLimpiar = tk.Button(customers_delete, text="LIMPIAR", command=lambda: clear_entries(customers_delete))
C_D_BTNLimpiar.grid(row=2, column=1, pady=20)
# ========================================================================================== #

# ===================================== ORDER (CREATE) ===================================== #

def get_full_date():
    date_obj = O_C_Date.get_date()
    
    hour = int(O_C_Hour.get())
    minute = int(O_C_Minute.get())
    second = int(O_C_Second.get())

    current_time = datetime.datetime.now()
    milliseconds = current_time.microsecond // 1000

    formatted_date = date_obj.strftime("%d-%b-%y")
    
    am_pm = "AM" if hour < 12 else "PM"
    hour %= 12
    if hour == 0:
        hour = 12
    formatted_time = f"{hour:02d}.{minute:02d}.{second:02d}.{milliseconds:06d} {am_pm}"
    
    full_date = f"{formatted_date} {formatted_time}"
    
    return full_date


def create_order():
    connection = conexion()
    cursor = connection.cursor()

    try:
        cursor.callproc("create_order", [
            O_C_OrderID.get(),
            get_full_date(),
            O_C_Modo.get(),
            O_C_CustomerID.get(),
            O_C_Estatus.get(),
            O_C_Total.get(),
            O_C_Representate.get(),
            O_C_Promocion.get()
        ])
        connection.commit()
        print("¡Orden creada con éxito!")
    except oracledb.DatabaseError as e:
        error, = e.args
        print("Error al crear la orden:", error.message)
    finally:
        cursor.close()
        connection.close()
    
# ID Orden
tk.Label(orders_create, text="ID Orden:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
O_C_OrderID = tk.Entry(orders_create)
O_C_OrderID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Fecha
tk.Label(orders_create, text="Fecha:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
O_C_Date = DateEntry(orders_create, date_pattern='dd/MM/yy')
O_C_Date.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Hora
time_frame = tk.Frame(orders_create)
time_frame.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Hora
tk.Label(orders_create, text="Hora:").grid(row=2, column=0, padx=10, pady=10, sticky='e')  # Cambiado a columna 0
time_frame = tk.Frame(orders_create)
time_frame.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Espacio en blanco ajustado para alinear con las otras etiquetas
tk.Label(time_frame, text="   ").grid(row=0, column=0, padx=5)  
O_C_Hour = tk.Spinbox(time_frame, from_=0, to=23, wrap=True, format="%02.0f", width=3)
O_C_Hour.grid(row=0, column=1, padx=5)
O_C_Hour.delete(0, tk.END)
O_C_Hour.insert(0, datetime.datetime.now().strftime("%H"))

tk.Label(time_frame, text=":").grid(row=0, column=2)

tk.Label(time_frame, text="Min:").grid(row=0, column=3, padx=5)
O_C_Minute = tk.Spinbox(time_frame, from_=0, to=59, wrap=True, format="%02.0f", width=3)
O_C_Minute.grid(row=0, column=4, padx=5)
O_C_Minute.delete(0, tk.END)
O_C_Minute.insert(0, datetime.datetime.now().strftime("%M"))

tk.Label(time_frame, text=":").grid(row=0, column=5)

tk.Label(time_frame, text="Seg:").grid(row=0, column=6, padx=5)
O_C_Second = tk.Spinbox(time_frame, from_=0, to=59, wrap=True, format="%02.0f", width=3)
O_C_Second.grid(row=0, column=7, padx=5)
O_C_Second.delete(0, tk.END)
O_C_Second.insert(0, datetime.datetime.now().strftime("%S"))

tk.Label(orders_create, text="Modo:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
O_C_Modo = ttk.Combobox(orders_create, values=["","online","direct"], width=5, state="readonly")
O_C_Modo.grid(row=3, column=1, padx=10, pady=10, sticky='w')
O_C_Modo.set("")

# ID Cliente
tk.Label(orders_create, text="ID Cliente:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
O_C_CustomerID = tk.Entry(orders_create)
O_C_CustomerID.grid(row=4, column=1, padx=10, pady=10, sticky='w')

# Estatus
tk.Label(orders_create, text="Estatus:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
O_C_Estatus = ttk.Combobox(orders_create, values=list(range(11)), width=5, state="readonly")
O_C_Estatus.grid(row=5, column=1, padx=10, pady=10, sticky='w')
O_C_Estatus.set(0)

# Total
tk.Label(orders_create, text="Total:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
O_C_Total = tk.Entry(orders_create)
O_C_Total.grid(row=6, column=1, padx=10, pady=10, sticky='w')

# ID Representate
tk.Label(orders_create, text="ID Representate:").grid(row=7, column=0, padx=10, pady=10, sticky='e')
O_C_Representate = tk.Entry(orders_create)
O_C_Representate.grid(row=7, column=1, padx=10, pady=10, sticky='w')

# Cod. Promoción
tk.Label(orders_create, text="Cod. Promoción:").grid(row=8, column=0, padx=10, pady=10, sticky='e')
O_C_Promocion = tk.Entry(orders_create)
O_C_Promocion.grid(row=8, column=1, padx=10, pady=10, sticky='w')

# Botón Crear
O_C_BTNCrear = tk.Button(orders_create, text="CREAR", command=create_order)
O_C_BTNCrear.grid(row=9, column=0, pady=20)

# Botón Limpiar
O_C_BTNLimpiar = tk.Button(orders_create, text="LIMPIAR", command=lambda: clear_entries(orders_create))
O_C_BTNLimpiar.grid(row=9, column=1, pady=20)

# ========================================================================================== #

# ====================================== ORDER (READ) ====================================== #
def list_all_orders():
    try:
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()

        p_cursor = cursor.var(oracledb.CURSOR)

        cursor.callproc("list_orders", [p_cursor])

        result = p_cursor.getvalue().fetchall()

        return result

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)
        return None
    
def show_orders():
    orders = list_all_orders()

    if orders:
        for row in O_R_Tabla.get_children():
            O_R_Tabla.delete(row)

        for order in orders:
            O_R_Tabla.insert("", "end", values=order)

O_R_Tabla = ttk.Treeview(orders_read, columns=("Order ID", "Fecha", "Modo", "Customer ID", "Estado", "Total", "Sales Rep ID", "Promotion ID"), show="headings")

column_widths = [100, 120, 60, 80, 60, 80, 80, 100] 
for column, width in zip(O_R_Tabla["columns"], column_widths):
    O_R_Tabla.column(column, width=width)

O_R_Tabla.heading("Order ID", text="Order ID")
O_R_Tabla.heading("Fecha", text="Fecha")
O_R_Tabla.heading("Modo", text="Modo")
O_R_Tabla.heading("Customer ID", text="Customer ID")
O_R_Tabla.heading("Estado", text="Estado")
O_R_Tabla.heading("Total", text="Total")
O_R_Tabla.heading("Sales Rep ID", text="Sales Rep ID")
O_R_Tabla.heading("Promotion ID", text="Promotion ID")

O_R_Tabla.grid(row=0, column=0, sticky="nsew")

scrollbar = ttk.Scrollbar(orders_read, orient="vertical", command=O_R_Tabla.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
O_R_Tabla.configure(yscrollcommand=scrollbar.set)

load_button = ttk.Button(orders_read, text="Cargar/Actualizar Órdenes", command=show_orders)
load_button.grid(row=1, column=0, sticky="ew")

# ========================================================================================== #

# ===================================== ORDER (UPDATE) ===================================== #

def update_order():
    order_id = int(O_U_OrderID.get())
    order_date = datetime.datetime.strptime(O_U_Date.get(), "%d/%m/%y")
    order_mode = O_U_Modo.get()
    customer_id = int(O_U_CustomerID.get())
    order_status = int(O_U_Estatus.get())
    order_total = float(O_U_Total.get())
    sales_rep_id = int(O_U_Representate.get())
    promotion_id = int(O_U_Promocion.get())

    connection = conexion()

    try:
        cursor = connection.cursor()

        cursor.callproc("update_order", [order_id, order_date, order_mode, customer_id, order_status, order_total, sales_rep_id, promotion_id])

        connection.commit()

        messagebox.showinfo("Éxito", "La orden se ha actualizado correctamente en la base de datos.")

    except oracledb.DatabaseError as e:
        messagebox.showerror("Error", "Ocurrió un error al actualizar la orden en la base de datos:\n{}".format(str(e)))

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def search_order():
    order_id = int(O_U_OrderID.get())

    connection = conexion()

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID FROM orders WHERE ORDER_ID = :order_id", {'order_id': order_id})

        order_details = cursor.fetchone()

        if order_details:
            O_U_Date.delete(0, tk.END)
            O_U_Date.insert(0, order_details[0].strftime('%d/%m/%y'))
            O_U_Modo.set(order_details[1])
            O_U_CustomerID.delete(0, tk.END)
            O_U_CustomerID.insert(0, order_details[2])
            O_U_Estatus.set(order_details[3])
            O_U_Total.delete(0, tk.END)
            O_U_Total.insert(0, order_details[4])
            O_U_Representate.delete(0, tk.END)
            O_U_Representate.insert(0, order_details[5])
            O_U_Promocion.delete(0, tk.END)
            O_U_Promocion.insert(0, order_details[6])
        else:
            messagebox.showinfo("Información", f"No se encontró ninguna orden con el ID {order_id}.")

    except oracledb.DatabaseError as e:
        messagebox.showerror("Error", "Ocurrió un error al buscar la orden en la base de datos:\n{}".format(str(e)))

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

tk.Label(orders_update, text="ID Orden:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
O_U_OrderID = tk.Entry(orders_update)
O_U_OrderID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

search_button = tk.Button(orders_update, text="BUSCAR", command=search_order)
search_button.grid(row=0, column=1, padx=150, sticky='w') 


tk.Label(orders_update, text="Fecha:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
O_U_Date = DateEntry(orders_update, date_pattern='dd/MM/yy')
O_U_Date.grid(row=1, column=1, padx=10, pady=10, sticky='w')


time_frame = tk.Frame(orders_update)
time_frame.grid(row=2, column=1, padx=10, pady=10, sticky='w')


tk.Label(orders_update, text="Hora:").grid(row=2, column=0, padx=10, pady=10, sticky='e')  # Cambiado a columna 0
time_frame = tk.Frame(orders_update)
time_frame.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(time_frame, text="   ").grid(row=0, column=0, padx=5)  
O_U_Hour = tk.Spinbox(time_frame, from_=0, to=23, wrap=True, format="%02.0f", width=3)
O_U_Hour.grid(row=0, column=1, padx=5)
O_U_Hour.delete(0, tk.END)
O_U_Hour.insert(0, datetime.datetime.now().strftime("%H"))

tk.Label(time_frame, text=":").grid(row=0, column=2)

tk.Label(time_frame, text="Min:").grid(row=0, column=3, padx=5)
O_U_Minute = tk.Spinbox(time_frame, from_=0, to=59, wrap=True, format="%02.0f", width=3)
O_U_Minute.grid(row=0, column=4, padx=5)
O_U_Minute.delete(0, tk.END)
O_U_Minute.insert(0, datetime.datetime.now().strftime("%M"))

tk.Label(time_frame, text=":").grid(row=0, column=5)

tk.Label(time_frame, text="Seg:").grid(row=0, column=6, padx=5)
O_U_Second = tk.Spinbox(time_frame, from_=0, to=59, wrap=True, format="%02.0f", width=3)
O_U_Second.grid(row=0, column=7, padx=5)
O_U_Second.delete(0, tk.END)
O_U_Second.insert(0, datetime.datetime.now().strftime("%S"))

tk.Label(orders_update, text="Modo:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
O_U_Modo = ttk.Combobox(orders_update, values=["","online","direct"], width=5, state="readonly")
O_U_Modo.grid(row=3, column=1, padx=10, pady=10, sticky='w')
O_U_Modo.set("")

# ID Cliente
tk.Label(orders_update, text="ID Cliente:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
O_U_CustomerID = tk.Entry(orders_update)
O_U_CustomerID.grid(row=4, column=1, padx=10, pady=10, sticky='w')

# Estatus
tk.Label(orders_update, text="Estatus:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
O_U_Estatus = ttk.Combobox(orders_update, values=list(range(11)), width=5, state="readonly")
O_U_Estatus.grid(row=5, column=1, padx=10, pady=10, sticky='w')
O_U_Estatus.set(0)

# Total
tk.Label(orders_update, text="Total:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
O_U_Total = tk.Entry(orders_update)
O_U_Total.grid(row=6, column=1, padx=10, pady=10, sticky='w')

# ID Representate
tk.Label(orders_update, text="ID Representate:").grid(row=7, column=0, padx=10, pady=10, sticky='e')
O_U_Representate = tk.Entry(orders_update)
O_U_Representate.grid(row=7, column=1, padx=10, pady=10, sticky='w')

# Cod. Promoción
tk.Label(orders_update, text="Cod. Promoción:").grid(row=8, column=0, padx=10, pady=10, sticky='e')
O_U_Promocion = tk.Entry(orders_update)
O_U_Promocion.grid(row=8, column=1, padx=10, pady=10, sticky='w')

# Botón Crear
O_U_BTNCrear = tk.Button(orders_update, text="ACTUALIZAR", command=update_order)
O_U_BTNCrear.grid(row=9, column=0, pady=20)

# Botón Limpiar
O_U_BTNLimpiar = tk.Button(orders_update, text="LIMPIAR", command=lambda: clear_entries(orders_update))
O_U_BTNLimpiar.grid(row=9, column=1, pady=20)

# ========================================================================================== #

# ===================================== ORDER (DELETE) ===================================== #
def delete_order():
    order_id = int(O_D_OrderID.get())

    connection = conexion()

    try:
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM orders WHERE ORDER_ID = :order_id", {'order_id': order_id})
        order_data = cursor.fetchone()

        if order_data:
            order_info = f"Registro a eliminar:\nID Orden: {order_data[0]}\nFecha: {order_data[1].strftime('%d/%m/%y')}\nModo: {order_data[2]}\nID Cliente: {order_data[3]}\nEstatus: {order_data[4]}\nTotal: {order_data[5]}\nID Representante: {order_data[6]}\nCódigo de Promoción: {order_data[7]}"
            if messagebox.askokcancel("Confirmar eliminación", order_info + "\n\n¿Estás seguro que deseas eliminar esta orden?"):

                cursor.callproc("delete_order", [order_id])

                connection.commit()

                messagebox.showinfo("Éxito", "La orden ha sido eliminada correctamente.")
        else:
            messagebox.showinfo("Información", f"No se encontró ninguna orden con el ID {order_id}.")

    except oracledb.DatabaseError as e:
        messagebox.showerror("Error", "Ocurrió un error al eliminar la orden en la base de datos:\n{}".format(str(e)))

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

tk.Label(orders_delete, text="ID Orden:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
O_D_OrderID = tk.Entry(orders_delete)
O_D_OrderID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

O_D_BTNEliminar = tk.Button(orders_delete, text="ELIMINAR", command=delete_order)
O_D_BTNEliminar.grid(row=2, column=0, pady=20)

O_D_BTNLimpiar = tk.Button(orders_delete, text="LIMPIAR", command=lambda: clear_entries(orders_delete))
O_D_BTNLimpiar.grid(row=2, column=1, pady=20)

# ================================ ORDER ITEMS y PRODUCTS ================================== #

# =================================== PRODUCTS (CREATE) =================================== #

def create_product():
    product_id = P_C_ProductID.get()
    product_name = P_C_ProductName.get()
    product_description = P_C_ProductDescription.get()
    category_id = P_C_CategoryID.get()
    weight_class = P_C_WeightClass.get()
    warranty_period = P_C_WarrantyPeriod.get()
    supplier_id = P_C_SupplierID.get()
    product_status = P_C_ProductStatus.get()
    list_price = P_C_ListPrice.get()
    min_price = P_C_MinPrice.get()
    catalog_url = P_C_CatalogURL.get()
    
    try:
        # Conectarse a Oracle
        connection = conexion()
        if connection is None:
            return

        # Llamar al procedimiento almacenado para crear el producto
        cursor = connection.cursor()
        cursor.callproc("create_product_information", [product_id, product_name, product_description, category_id, weight_class, warranty_period, supplier_id, product_status, list_price, min_price, catalog_url])

        # Hacer commit de la transacción
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        print("Producto creado exitosamente")

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)


tk.Label(products_create, text="Product ID:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
P_C_ProductID = tk.Entry(products_create)
P_C_ProductID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Product Name:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
P_C_ProductName = tk.Entry(products_create)
P_C_ProductName.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Product Description:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
P_C_ProductDescription = tk.Entry(products_create)
P_C_ProductDescription.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Category ID:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
P_C_CategoryID = tk.Entry(products_create)
P_C_CategoryID.grid(row=3, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Weight Class:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
P_C_WeightClass = tk.Entry(products_create)
P_C_WeightClass = ttk.Combobox(products_create, values=[1, 0], width=5, state="readonly")
P_C_WeightClass.grid(row=4, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Warranty Period:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
P_C_WarrantyPeriod = tk.Entry(products_create)
P_C_WarrantyPeriod.grid(row=5, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Supplier ID:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
P_C_SupplierID = tk.Entry(products_create)
P_C_SupplierID.grid(row=6, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Product Status:").grid(row=7, column=0, padx=10, pady=10, sticky='e')
P_C_ProductStatus = tk.Entry(products_create)
P_C_ProductStatus.grid(row=7, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="List Price:").grid(row=8, column=0, padx=10, pady=10, sticky='e')
P_C_ListPrice = tk.Entry(products_create)
P_C_ListPrice.grid(row=8, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Min Price:").grid(row=9, column=0, padx=10, pady=10, sticky='e')
P_C_MinPrice = tk.Entry(products_create)
P_C_MinPrice.grid(row=9, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_create, text="Catalog URL:").grid(row=10, column=0, padx=10, pady=10, sticky='e')
P_C_CatalogURL = tk.Entry(products_create)
P_C_CatalogURL.grid(row=10, column=1, padx=10, pady=10, sticky='w')

P_C_BTNCrear = tk.Button(products_create, text="CREAR", command=create_product)
P_C_BTNCrear.grid(row=11, column=0, pady=20)

P_C_BTNLimpiar = tk.Button(products_create, text="LIMPIAR", command=lambda: clear_entries(products_create))
P_C_BTNLimpiar.grid(row=11, column=1, pady=20)


# ========================================================================================= #


# =================================== PRODUCTS (UPDATE) =================================== #

def search_product():
    connection = conexion()
    if connection is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

    product_id = P_U_ProductID.get()
    
    if not product_id:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un Product ID.")
        return

    try:
        cursor = connection.cursor()
        query = """
        SELECT Product_ID, Product_Name, Product_Description, Category_ID, Weight_Class, Warranty_Period, Supplier_ID, Product_Status, List_Price, Min_Price, Catalog_URL
        FROM product_information
        WHERE Product_ID = :product_id
        """
        cursor.execute(query, product_id=product_id)
        result = cursor.fetchone()
        
        if result:
            P_U_ProductName.delete(0, tk.END)
            P_U_ProductName.insert(0, result[1])
            
            P_U_ProductDescription.delete(0, tk.END)
            P_U_ProductDescription.insert(0, result[2])
            
            P_U_CategoryID.delete(0, tk.END)
            P_U_CategoryID.insert(0, result[3])
            
            P_U_WeightClass.delete(0, tk.END)
            P_U_WeightClass.insert(0, result[4])
            
            P_U_WarrantyPeriod.delete(0, tk.END)
            P_U_WarrantyPeriod.insert(0, result[5])
            
            P_U_SupplierID.delete(0, tk.END)
            P_U_SupplierID.insert(0, result[6])
            
            P_U_ProductStatus.delete(0, tk.END)
            P_U_ProductStatus.insert(0, result[7])
            
            P_U_ListPrice.delete(0, tk.END)
            P_U_ListPrice.insert(0, result[8])
            
            P_U_MinPrice.delete(0, tk.END)
            P_U_MinPrice.insert(0, result[9])
            
            P_U_CatalogURL.delete(0, tk.END)
            P_U_CatalogURL.insert(0, result[10])
        else:
            messagebox.showinfo("Información", "No se encontró ningún producto con ese ID.")
    except oracledb.DatabaseError as error:
        messagebox.showerror("Error", f"Error al buscar el producto: {error}")
    finally:
        if connection:
            connection.close()

def update_product():
    product_id = P_U_ProductID.get()
    product_name = P_U_ProductName.get()
    product_description = P_U_ProductDescription.get()
    category_id = P_U_CategoryID.get()
    weight_class = P_U_WeightClass.get()
    warranty_period = P_U_WarrantyPeriod.get()
    supplier_id = P_U_SupplierID.get()
    product_status = P_U_ProductStatus.get()
    list_price = P_U_ListPrice.get()
    min_price = P_U_MinPrice.get()
    catalog_url = P_U_CatalogURL.get()
    
    try:
        # Conectarse a Oracle
        connection = conexion()
        if connection is None:
            return
        cursor = connection.cursor()
        cursor.callproc("update_product_information", [product_id, product_name, product_description, category_id, weight_class, warranty_period, supplier_id, product_status, list_price, min_price, catalog_url])

        connection.commit()

        cursor.close()
        connection.close()

        print("Producto actualizado exitosamente")
        clear_entries(products_update)

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)

        messagebox.showerror("Error", f"Error al actualizar el producto: {error}")


tk.Label(products_update, text="Product ID:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
P_U_ProductID = tk.Entry(products_update)
P_U_ProductID.grid(row=0, column=1, padx=10, pady=10, sticky='w')
P_U_BTNBuscar = tk.Button(products_update, text="BUSCAR", command=search_product)
P_U_BTNBuscar.grid(row=0, column=2, columnspan=2, pady=10)

tk.Label(products_update, text="Product Name:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
P_U_ProductName = tk.Entry(products_update)
P_U_ProductName.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="Product Description:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
P_U_ProductDescription = tk.Entry(products_update)
P_U_ProductDescription.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="Category ID:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
P_U_CategoryID = tk.Entry(products_update)
P_U_CategoryID.grid(row=3, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="Weight Class:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
P_C_WeightClass = tk.Entry(products_update)
P_U_WeightClass = ttk.Combobox(products_update, values=[1, 0], width=5, state="readonly")
P_U_WeightClass.grid(row=4, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="Warranty Period:").grid(row=5, column=0, padx=10, pady=10, sticky='e')
P_U_WarrantyPeriod = tk.Entry(products_update)
P_U_WarrantyPeriod.grid(row=5, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="Supplier ID:").grid(row=6, column=0, padx=10, pady=10, sticky='e')
P_U_SupplierID = tk.Entry(products_update)
P_U_SupplierID.grid(row=6, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="Product Status:").grid(row=7, column=0, padx=10, pady=10, sticky='e')
P_U_ProductStatus = tk.Entry(products_update)
P_U_ProductStatus.grid(row=7, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="List Price:").grid(row=8, column=0, padx=10, pady=10, sticky='e')
P_U_ListPrice = tk.Entry(products_update)
P_U_ListPrice.grid(row=8, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="Min Price:").grid(row=9, column=0, padx=10, pady=10, sticky='e')
P_U_MinPrice = tk.Entry(products_update)
P_U_MinPrice.grid(row=9, column=1, padx=10, pady=10, sticky='w')

tk.Label(products_update, text="Catalog URL:").grid(row=10, column=0, padx=10, pady=10, sticky='e')
P_U_CatalogURL = tk.Entry(products_update)
P_U_CatalogURL.grid(row=10, column=1, padx=10, pady=10, sticky='w')

P_U_BTNActualizar = tk.Button(products_update, text="ACTUALIZAR", command=update_product)
P_U_BTNActualizar.grid(row=11, column=0, pady=20)

P_U_BTNLimpiar = tk.Button(products_update, text="LIMPIAR", command=lambda: clear_entries(products_update))
P_U_BTNLimpiar.grid(row=11, column=1, pady=20)

# ========================================================================================== #


# ==================================== PRODUCTS (READ) ==================================== #

def list_all_products():
    try:
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()

        p_cursor = cursor.var(oracledb.CURSOR)

        cursor.callproc("list_product_information", [p_cursor])

        result = p_cursor.getvalue().fetchall()

        return result

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)
        return None
    
def show_products():
    products = list_all_products()

    if products:
        for row in P_R_Tabla.get_children():
            P_R_Tabla.delete(row)

        for product in products:
            P_R_Tabla.insert("", "end", values=product)

P_R_Tabla = ttk.Treeview(products_read, columns=("Product ID", "Product Name", "Product Description", "Category ID", "Weight Class", "Warranty Period", "Supplier ID", "Product Status", "List Price", "Min Price", "Catalog URL"), show="headings")
P_R_Tabla.heading("Product ID", text="ID")
P_R_Tabla.heading("Product Name", text="Nombre")
P_R_Tabla.heading("Product Description", text="Descripción")
P_R_Tabla.heading("Category ID", text="Categoría")
P_R_Tabla.heading("Weight Class", text="Peso")
P_R_Tabla.heading("Warranty Period", text="Garantía")
P_R_Tabla.heading("Supplier ID", text="ID Provedor")
P_R_Tabla.heading("Product Status", text="Estatus")
P_R_Tabla.heading("List Price", text="Precio")
P_R_Tabla.heading("Min Price", text="Precio Min.")
P_R_Tabla.heading("Catalog URL", text="URL")
P_R_Tabla.grid(row=0, column=0, sticky="nsew")

column_widths = [60, 150, 150, 60, 60, 60, 100, 120, 60, 60, 150]  
for col, width in zip(P_R_Tabla["columns"], column_widths):
    P_R_Tabla.column(col, width=width)

scrollbar = ttk.Scrollbar(products_read, orient="vertical", command=P_R_Tabla.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
P_R_Tabla.configure(yscrollcommand=scrollbar.set)

load_button = ttk.Button(products_read, text="Cargar/Actualizar Productos", command=show_products)
load_button.grid(row=1, column=0, sticky="ew")

# ========================================================================================== #


# =================================== PRODUCTS (DELETE) ==================================== #

def delete_product():
    connection = conexion()
    if connection is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

    product_id = P_D_ProductID.get()
    
    if not product_id:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un Product ID.")
        return

    try:
        cursor = connection.cursor()
        query = """
        SELECT PRODUCT_ID, PRODUCT_NAME, PRODUCT_DESCRIPTION, CATEGORY_ID, 
               WEIGHT_CLASS, WARRANTY_PERIOD, SUPPLIER_ID, PRODUCT_STATUS, 
               LIST_PRICE, MIN_PRICE, CATALOG_URL
        FROM PRODUCT_INFORMATION
        WHERE PRODUCT_ID = :product_id
        """
        cursor.execute(query, product_id=product_id)
        result = cursor.fetchone()
        
        if result:
            # Mostrar los datos del producto
            msg = f"ID: {result[0]}\nNombre: {result[1]}\nDescripción: {result[2]}\nCategoría ID: {result[3]}\nClase de Peso: {result[4]}\nPeriodo de Garantía: {result[5]}\nID del Proveedor: {result[6]}\nEstado del Producto: {result[7]}\nPrecio de Lista: {result[8]}\nPrecio Mínimo: {result[9]}\nURL del Catálogo: {result[10]}"
            confirm_delete = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que quieres eliminar el siguiente producto?\n\n{msg}")
            if confirm_delete:
                cursor.callproc("delete_product_information", [product_id])
                connection.commit()
                messagebox.showinfo("Información", f"Producto con ID {product_id} eliminado correctamente.")
                clear_entries(products_delete)
        else:
            messagebox.showinfo("Información", "No se encontró ningún producto con ese ID.")
    except oracledb.DatabaseError as error:
        messagebox.showerror("Error", f"Error al buscar o eliminar el producto: {error}")
    finally:
        if connection:
            connection.close()

tk.Label(products_delete, text="Product ID:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
P_D_ProductID = tk.Entry(products_delete)
P_D_ProductID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

P_D_BTNEliminar = tk.Button(products_delete, text="ELIMINAR", command=delete_product)
P_D_BTNEliminar.grid(row=2, column=0, pady=20)

P_D_BTNLimpiar = tk.Button(products_delete, text="LIMPIAR", command=lambda: clear_entries(products_delete))
P_D_BTNLimpiar.grid(row=2, column=1, pady=20)

# ========================================================================================== #

# =================================== ITEMS (CREATE) =================================== #

def create_order_item():
    order_id = OI_C_OrderID.get()
    line_item_id = OI_C_LineItemID.get()
    product_id = OI_C_ProductID.get()
    unit_price = OI_C_UnitPrice.get()
    quantity = OI_C_Quantity.get()
    
    try:
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.callproc("create_order_item", [order_id, line_item_id, product_id, unit_price, quantity])

        connection.commit()

        cursor.close()
        connection.close()

        print("Elemento del pedido creado exitosamente")

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)


tk.Label(items_create, text="Order ID:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
OI_C_OrderID = tk.Entry(items_create)
OI_C_OrderID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(items_create, text="Line Item ID:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
OI_C_LineItemID = tk.Entry(items_create)
OI_C_LineItemID.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(items_create, text="Product ID:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
OI_C_ProductID = tk.Entry(items_create)
OI_C_ProductID.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(items_create, text="Unit Price:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
OI_C_UnitPrice = tk.Entry(items_create)
OI_C_UnitPrice.grid(row=3, column=1, padx=10, pady=10, sticky='w')

tk.Label(items_create, text="Quantity:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
OI_C_Quantity = tk.Entry(items_create)
OI_C_Quantity.grid(row=4, column=1, padx=10, pady=10, sticky='w')

OI_C_BTNCrear = tk.Button(items_create, text="CREAR", command=create_order_item)
OI_C_BTNCrear.grid(row=5, column=0, pady=20)

# ======================================================================================== #

# ==================================== ITEMS (READ) ====================================== #

def list_all_order_items():
    try:
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()

        oi_cursor = cursor.var(oracledb.CURSOR)

        cursor.callproc("list_order_items", [oi_cursor])

        result = oi_cursor.getvalue().fetchall()

        return result

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)
        return None
    
def show_order_items():
    order_items = list_all_order_items()

    if order_items:
        for row in OI_R_Tabla.get_children():
            OI_R_Tabla.delete(row)

        for order_item in order_items:
            OI_R_Tabla.insert("", "end", values=order_item)

OI_R_Tabla = ttk.Treeview(items_read, columns=("Order ID", "Line Item ID", "Product ID", "Unit Price", "Quantity"), show="headings")
OI_R_Tabla.heading("Order ID", text="ID Orden")
OI_R_Tabla.heading("Line Item ID", text="ID Objeto")
OI_R_Tabla.heading("Product ID", text="ID Producto")
OI_R_Tabla.heading("Unit Price", text="Precio")
OI_R_Tabla.heading("Quantity", text="Cantidad")
OI_R_Tabla.grid(row=0, column=0, sticky="nsew")

column_widths = [100, 100, 100, 100, 100]
for col, width in zip(OI_R_Tabla["columns"], column_widths):
    OI_R_Tabla.column(col, width=width)

scrollbar = ttk.Scrollbar(items_read, orient="vertical", command=OI_R_Tabla.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
OI_R_Tabla.configure(yscrollcommand=scrollbar.set)

load_button = ttk.Button(items_read, text="Cargar/Actualizar Elementos del Pedido", command=show_order_items)
load_button.grid(row=1, column=0, sticky="ew")

# ========================================================================================== #

# ==================================== ITEMS (UPDATE) ====================================== #

def search_order_item():
    connection = conexion()
    if connection is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

    order_id = OI_U_OrderID.get()
    line_item_id = OI_U_LineItemID.get()
    
    if not order_id or not line_item_id:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un Order ID y un Line Item ID.")
        return

    try:
        cursor = connection.cursor()
        query = """
        SELECT ORDER_ID, LINE_ITEM_ID, PRODUCT_ID, UNIT_PRICE, QUANTITY
        FROM ORDER_ITEMS
        WHERE ORDER_ID = :order_id AND LINE_ITEM_ID = :line_item_id
        """
        cursor.execute(query, order_id=order_id, line_item_id=line_item_id)
        result = cursor.fetchone()
        
        if result:
            OI_U_ProductID.delete(0, tk.END)
            OI_U_ProductID.insert(0, result[2])
            
            OI_U_UnitPrice.delete(0, tk.END)
            OI_U_UnitPrice.insert(0, result[3])
            
            OI_U_Quantity.delete(0, tk.END)
            OI_U_Quantity.insert(0, result[4])
        else:
            messagebox.showinfo("Información", "No se encontró ningún elemento del pedido con esos IDs.")
    except oracledb.DatabaseError as error:
        messagebox.showerror("Error", f"Error al buscar el elemento del pedido: {error}")
    finally:
        if connection:
            connection.close()

def update_order_item():
    order_id = OI_U_OrderID.get()
    line_item_id = OI_U_LineItemID.get()
    product_id = OI_U_ProductID.get()
    unit_price = OI_U_UnitPrice.get()
    quantity = OI_U_Quantity.get()
    
    try:
        connection = conexion()
        if connection is None:
            return

        cursor = connection.cursor()
        cursor.callproc("update_order_item", [order_id, line_item_id, product_id, unit_price, quantity])

        connection.commit()

        cursor.close()
        connection.close()

        print("Elemento del pedido actualizado exitosamente")
        clear_entries(items_update)

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)

        messagebox.showerror("Error", f"Error al actualizar el elemento del pedido: {error}")


tk.Label(items_update, text="Order ID:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
OI_U_OrderID = tk.Entry(items_update)
OI_U_OrderID.grid(row=0, column=1, padx=10, pady=10, sticky='w')
OI_U_BTNBuscar = tk.Button(items_update, text="BUSCAR", command=search_order_item)
OI_U_BTNBuscar.grid(row=0, column=2, columnspan=2, pady=10)


tk.Label(items_update, text="Line Item ID:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
OI_U_LineItemID = tk.Entry(items_update)
OI_U_LineItemID.grid(row=1, column=1, padx=10, pady=10, sticky='w')

tk.Label(items_update, text="Product ID:").grid(row=2, column=0, padx=10, pady=10, sticky='e')
OI_U_ProductID = tk.Entry(items_update)
OI_U_ProductID.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(items_update, text="Unit Price:").grid(row=3, column=0, padx=10, pady=10, sticky='e')
OI_U_UnitPrice = tk.Entry(items_update)
OI_U_UnitPrice.grid(row=3, column=1, padx=10, pady=10, sticky='w')

tk.Label(items_update, text="Quantity:").grid(row=4, column=0, padx=10, pady=10, sticky='e')
OI_U_Quantity = tk.Entry(items_update)
OI_U_Quantity.grid(row=4, column=1, padx=10, pady=10, sticky='w')

OI_U_BTNActualizar = tk.Button(items_update, text="ACTUALIZAR", command=update_order_item)
OI_U_BTNActualizar.grid(row=5, column=0, pady=20)

OI_U_BTNLimpiar = tk.Button(items_update, text="LIMPIAR", command=lambda: clear_entries(items_update))
OI_U_BTNLimpiar.grid(row=5, column=1, pady=20)

# ===================================== ITEM (DELETE) ====================================== #

def delete_order_item():
    connection = conexion()
    if connection is None:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos.")
        return

    order_id = O_D_OrderID.get()
    line_item_id = O_D_LineItemID.get()
    
    if not order_id or not line_item_id:
        messagebox.showwarning("Advertencia", "Por favor, ingrese un Order ID y Line Item ID.")
        return

    try:
        cursor = connection.cursor()
        query = """
        SELECT ORDER_ID, LINE_ITEM_ID, PRODUCT_ID, UNIT_PRICE, QUANTITY
        FROM order_items
        WHERE ORDER_ID = :order_id AND LINE_ITEM_ID = :line_item_id
        """
        cursor.execute(query, order_id=order_id, line_item_id=line_item_id)
        result = cursor.fetchone()
        
        if result:
            msg = f"Order ID: {result[0]}\nLine Item ID: {result[1]}\nProduct ID: {result[2]}\nUnit Price: {result[3]}\nQuantity: {result[4]}"
            confirm_delete = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que quieres eliminar el siguiente registro?\n\n{msg}")
            if confirm_delete:
                cursor.callproc("delete_order_item", [order_id, line_item_id])
                connection.commit()
                messagebox.showinfo("Información", f"Elemento del pedido con Order ID {order_id} y Line Item ID {line_item_id} eliminado correctamente.")
                clear_entries(items_delete)
        else:
            messagebox.showinfo("Información", "No se encontró ningún elemento del pedido con ese Order ID y Line Item ID.")
    except oracledb.DatabaseError as error:
        messagebox.showerror("Error", f"Error al buscar o eliminar el elemento del pedido: {error}")
    finally:
        if connection:
            connection.close()

tk.Label(items_delete, text="Order ID:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
O_D_OrderID = tk.Entry(items_delete)
O_D_OrderID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

tk.Label(items_delete, text="Line Item ID:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
O_D_LineItemID = tk.Entry(items_delete)
O_D_LineItemID.grid(row=1, column=1, padx=10, pady=10, sticky='w')

O_D_BTNEliminar = tk.Button(items_delete, text="ELIMINAR", command=delete_order_item)
O_D_BTNEliminar.grid(row=2, column=0, pady=20)

O_D_BTNLimpiar = tk.Button(items_delete, text="LIMPIAR", command=lambda: clear_entries(items_delete))
O_D_BTNLimpiar.grid(row=2, column=1, pady=20)
# ========================================================================================== #

# ====================================== VALIDACIONES ====================================== #
def val_customer_id(entry_text):
    return entry_text.isdigit() and len(entry_text) <= 6 or entry_text == ""
validation = root.register(val_customer_id)
C_C_CustomerID.config(validate="key", validatecommand=(validation, "%P"))
C_U_CustomerID.config(validate="key", validatecommand=(validation, "%P"))
C_D_CustomerID.config(validate="key", validatecommand=(validation, "%P"))
O_C_CustomerID.config(validate="key", validatecommand=(validation, "%P"))
O_C_Representate.config(validate="key", validatecommand=(validation, "%P"))
O_C_Promocion.config(validate="key", validatecommand=(validation, "%P"))
O_U_CustomerID.config(validate="key", validatecommand=(validation, "%P"))
O_U_Representate.config(validate="key", validatecommand=(validation, "%P"))
O_U_Promocion.config(validate="key", validatecommand=(validation, "%P"))
P_C_ProductID.config(validate="key", validatecommand=(validation, "%P"))
P_U_ProductID.config(validate="key", validatecommand=(validation, "%P"))
OI_C_OrderID.config(validate="key", validatecommand=(validation, "%P"))
OI_C_ProductID.config(validate="key", validatecommand=(validation, "%P"))
OI_C_LineItemID.config(validate="key", validatecommand=(validation, "%P"))
P_D_ProductID.config(validate="key", validatecommand=(validation, "%P"))
O_D_LineItemID.config(validate="key", validatecommand=(validation, "%P"))
OI_U_LineItemID.config(validate="key", validatecommand=(validation, "%P"))
OI_C_ProductID.config(validate="key", validatecommand=(validation, "%P"))
OI_U_OrderID.config(validate="key", validatecommand=(validation, "%P"))
OI_C_UnitPrice.config(validate="key", validatecommand=(validation, "%P"))
OI_C_Quantity.config(validate="key", validatecommand=(validation, "%P"))
OI_U_ProductID.config(validate="key", validatecommand=(validation, "%P"))
OI_U_UnitPrice.config(validate="key", validatecommand=(validation, "%P"))
OI_U_Quantity.config(validate="key", validatecommand=(validation, "%P"))
P_C_SupplierID.config(validate="key", validatecommand=(validation, "%P"))
P_U_SupplierID.config(validate="key", validatecommand=(validation, "%P"))
P_C_ListPrice.config(validate="key", validatecommand=(validation, "%P"))
P_U_ListPrice.config(validate="key", validatecommand=(validation, "%P"))
P_C_MinPrice.config(validate="key", validatecommand=(validation, "%P"))
P_U_MinPrice.config(validate="key", validatecommand=(validation, "%P"))
O_D_OrderID.config(validate="key", validatecommand=(validation, "%P"))

def val_category_id(entry_text):
    return entry_text.isdigit() and len(entry_text) <= 2 or entry_text == ""
validation = root.register(val_category_id)
P_C_CategoryID.config(validate="key", validatecommand=(validation, "%P"))
P_U_CategoryID.config(validate="key", validatecommand=(validation, "%P"))

def val_weight_class(entry_text):
    return entry_text.isdigit() and len(entry_text) <= 1 or entry_text == ""
validation = root.register(val_customer_id)
P_C_WeightClass.config(validate="key", validatecommand=(validation, "%P"))
P_U_WeightClass.config(validate="key", validatecommand=(validation, "%P"))


def val_order_id(entry_text):
    return entry_text.isdigit() and len(entry_text) <= 12 or entry_text == ""
validation = root.register(val_order_id)
O_C_OrderID.config(validate="key", validatecommand=(validation, "%P"))
O_U_OrderID.config(validate="key", validatecommand=(validation, "%P"))
O_D_OrderID.config(validate="key", validatecommand=(validation, "%P"))

def val_promocion(entry_text):
    return entry_text.isdigit() and len(entry_text) <= 8 or entry_text == ""
validation = root.register(val_promocion)
O_C_Promocion.config(validate="key", validatecommand=(validation, "%P"))
O_U_Promocion.config(validate="key", validatecommand=(validation, "%P"))

def val_order_id(entry_text):
    return entry_text.isdigit() and len(entry_text) <= 12 or entry_text == ""
validation = root.register(val_order_id)
O_C_OrderID.config(validate="key", validatecommand=(validation, "%P"))
O_U_OrderID.config(validate="key", validatecommand=(validation, "%P"))

def val_nombreapellido(entry_text):
    return all (char.isalpha() or char.isspace() for char in entry_text) and len(entry_text) <= 20 or entry_text == " " or entry_text == ""
validation = root.register(val_nombreapellido)
C_C_Nombre.config(validate="key", validatecommand=(validation, "%P"))
C_C_Apellido.config(validate="key", validatecommand=(validation, "%P"))
C_U_Nombre.config(validate="key", validatecommand=(validation, "%P"))
C_U_Apellido.config(validate="key", validatecommand=(validation, "%P"))

def val_credito(entry_text):
    pattern = r'^\d{0,7}(\.\d{0,2})?$'
    return re.match(pattern, entry_text) is not None
validation = root.register(val_credito)
C_C_Credito.config(validate="key", validatecommand=(validation, "%P"))
C_U_Credito.config(validate="key", validatecommand=(validation, "%P"))

def val_correo(entry_text):
    return len(entry_text) <= 30 or entry_text == ""
validation = root.register(val_correo)
C_C_Correo.config(validate="key", validatecommand=(validation, "%P"))
C_U_Correo.config(validate="key", validatecommand=(validation, "%P"))

def val_ingresos(entry_text):
    return len(entry_text) <= 20 or entry_text == ""
validation = root.register(val_ingresos)
C_C_Ingresos.config(validate="key", validatecommand=(validation, "%P"))
C_U_Ingresos.config(validate="key", validatecommand=(validation, "%P"))
# ========================================================================================== #
apply_custom_styles()
root.mainloop()
