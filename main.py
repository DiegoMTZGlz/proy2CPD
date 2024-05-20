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
root.geometry("1430x480")
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

# Función para listar todos los clientes
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

# Función para mostrar los clientes en la tabla
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
C_R_Tabla = ttk.Treeview(customers_read, columns=("ID Cliente", "Nombre", "Apellido", "Crédito", "Correo", "Ingresos", "Región"), show="headings")
C_R_Tabla.heading("ID Cliente", text="ID Cliente")
C_R_Tabla.heading("Nombre", text="Nombre")
C_R_Tabla.heading("Apellido", text="Apellido")
C_R_Tabla.heading("Crédito", text="Crédito")
C_R_Tabla.heading("Correo", text="Correo")
C_R_Tabla.heading("Ingresos", text="Ingresos")
C_R_Tabla.heading("Región", text="Región")
C_R_Tabla.grid(row=0, column=0, sticky="nsew")

# Ajustar el ancho de las columnas
column_widths = [120, 120, 120, 100, 200, 100, 100]  # Ancho de las columnas
for col, width in zip(C_R_Tabla["columns"], column_widths):
    C_R_Tabla.column(col, width=width)

# Barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(customers_read, orient="vertical", command=C_R_Tabla.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
C_R_Tabla.configure(yscrollcommand=scrollbar.set)

# Botón para cargar/actualizar clientes
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
        # Conectarse a Oracle
        connection = conexion()
        if connection is None:
            return

        # Llamar al procedimiento almacenado
        cursor = connection.cursor()
        cursor.callproc("update_customer", [customer_id, nombre, apellido, credito, correo, ingresos, region])

        # Hacer commit de la transacción
        connection.commit()

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        print("Cliente actualizado exitosamente")
        clear_entries(customers_update)

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)

        # Mostrar mensaje de error en una ventana emergente
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
            # Mostrar los datos del cliente
            msg = f"ID: {result[0]}\nNombre: {result[1]} {result[2]}\nCrédito: {result[3]}\nCorreo: {result[4]}\nIngresos: {result[5]}\nRegión: {result[6]}"
            confirm_delete = messagebox.askyesno("Confirmar Eliminación", f"¿Estás seguro de que quieres eliminar el siguiente registro?\n\n{msg}")
            if confirm_delete:
                # Eliminar el cliente
                cursor.callproc("delete_customer", [customer_id])
                connection.commit()
                messagebox.showinfo("Información", f"Cliente con ID {customer_id} eliminado correctamente.")
                # Limpiar campos
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
    # Obtener la fecha del widget DateEntry
    date_obj = O_C_Date.get_date()
    
    # Obtener la hora del Spinbox
    hour = int(O_C_Hour.get())
    minute = int(O_C_Minute.get())
    second = int(O_C_Second.get())
    
    # Obtener la fracción de segundos actual
    current_time = datetime.datetime.now()
    milliseconds = current_time.microsecond // 1000
    
    # Formatear la fecha en el formato DD-MON-RR
    formatted_date = date_obj.strftime("%d-%b-%y")
    
    # Formatear la hora en el formato HH.MI.SS.FF AM
    am_pm = "AM" if hour < 12 else "PM"
    hour %= 12
    if hour == 0:
        hour = 12
    formatted_time = f"{hour:02d}.{minute:02d}.{second:02d}.{milliseconds:06d} {am_pm}"
    
    # Combinar la fecha y la hora en un solo string
    full_date = f"{formatted_date} {formatted_time}"
    
    return full_date


# Función para crear una orden utilizando un procedimiento almacenado
def create_order():
    # Conexión a la base de datos Oracle
    connection = conexion()
    cursor = connection.cursor()

    # Llamada al procedimiento almacenado
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

        # Ejecutar el procedimiento almacenado
        cursor.callproc("list_orders", [p_cursor])

        result = p_cursor.getvalue().fetchall()

        return result

    except oracledb.DatabaseError as e:
        error = e.args[0]
        print("Error al conectar a Oracle:", error)
        return None
    
def show_orders():
    # Obtener las órdenes
    orders = list_all_orders()

    if orders:
        # Limpiar la tabla
        for row in O_R_Tabla.get_children():
            O_R_Tabla.delete(row)

        # Agregar las órdenes a la tabla
        for order in orders:
            O_R_Tabla.insert("", "end", values=order)

# Tabla de Órdenes
O_R_Tabla = ttk.Treeview(orders_read, columns=("Order ID", "Fecha", "Modo", "Customer ID", "Estado", "Total", "Sales Rep ID", "Promotion ID"), show="headings")

# Reducir el ancho de las columnas
column_widths = [100, 120, 60, 80, 60, 80, 80, 100]  # Anchos de las columnas
for column, width in zip(O_R_Tabla["columns"], column_widths):
    O_R_Tabla.column(column, width=width)

# Configurar encabezados
O_R_Tabla.heading("Order ID", text="Order ID")
O_R_Tabla.heading("Fecha", text="Fecha")
O_R_Tabla.heading("Modo", text="Modo")
O_R_Tabla.heading("Customer ID", text="Customer ID")
O_R_Tabla.heading("Estado", text="Estado")
O_R_Tabla.heading("Total", text="Total")
O_R_Tabla.heading("Sales Rep ID", text="Sales Rep ID")
O_R_Tabla.heading("Promotion ID", text="Promotion ID")

O_R_Tabla.grid(row=0, column=0, sticky="nsew")

# Agregar barra de desplazamiento vertical
scrollbar = ttk.Scrollbar(orders_read, orient="vertical", command=O_R_Tabla.yview)
scrollbar.grid(row=0, column=1, sticky="ns")
O_R_Tabla.configure(yscrollcommand=scrollbar.set)

load_button = ttk.Button(orders_read, text="Cargar/Actualizar Órdenes", command=show_orders)
load_button.grid(row=1, column=0, sticky="ew")

# ========================================================================================== #

# ===================================== ORDER (UPDATE) ===================================== #

def update_order():
    # Obtener los valores de los campos de entrada
    order_id = int(O_U_OrderID.get())
    order_date = datetime.datetime.strptime(O_U_Date.get(), "%d/%m/%y")
    order_mode = O_U_Modo.get()
    customer_id = int(O_U_CustomerID.get())
    order_status = int(O_U_Estatus.get())
    order_total = float(O_U_Total.get())
    sales_rep_id = int(O_U_Representate.get())
    promotion_id = int(O_U_Promocion.get())

    # Establecer la conexión a la base de datos Oracle
    connection = conexion()

    try:
        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecutar el procedimiento almacenado de actualización
        cursor.callproc("update_order", [order_id, order_date, order_mode, customer_id, order_status, order_total, sales_rep_id, promotion_id])

        # Confirmar la transacción
        connection.commit()

        # Mostrar un mensaje de éxito
        messagebox.showinfo("Éxito", "La orden se ha actualizado correctamente en la base de datos.")

    except oracledb.DatabaseError as e:
        # En caso de error, mostrar un mensaje de error
        messagebox.showerror("Error", "Ocurrió un error al actualizar la orden en la base de datos:\n{}".format(str(e)))

    finally:
        # Cerrar el cursor y la conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def search_order():
    # Obtener el ID de orden ingresado por el usuario
    order_id = int(O_U_OrderID.get())

    # Establecer la conexión a la base de datos Oracle
    connection = conexion()

    try:
        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Ejecutar la consulta para obtener los detalles de la orden
        cursor.execute("SELECT ORDER_DATE, ORDER_MODE, CUSTOMER_ID, ORDER_STATUS, ORDER_TOTAL, SALES_REP_ID, PROMOTION_ID FROM orders WHERE ORDER_ID = :order_id", {'order_id': order_id})

        # Obtener los resultados de la consulta
        order_details = cursor.fetchone()

        if order_details:
            # Rellenar los campos con los datos obtenidos de la consulta
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
            # Mostrar un mensaje si no se encontró ninguna orden con el ID proporcionado
            messagebox.showinfo("Información", f"No se encontró ninguna orden con el ID {order_id}.")

    except oracledb.DatabaseError as e:
        # En caso de error, mostrar un mensaje de error
        messagebox.showerror("Error", "Ocurrió un error al buscar la orden en la base de datos:\n{}".format(str(e)))

    finally:
        # Cerrar el cursor y la conexión
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# ID Orden
tk.Label(orders_update, text="ID Orden:").grid(row=0, column=0, padx=10, pady=10, sticky='e')
O_U_OrderID = tk.Entry(orders_update)
O_U_OrderID.grid(row=0, column=1, padx=10, pady=10, sticky='w')

# Agregar un botón de búsqueda al lado del campo Order ID
search_button = tk.Button(orders_update, text="Buscar", command=search_order)
search_button.grid(row=0, column=2, sticky='w')  # Ajusta sticky a 'w' para que el botón esté a la izquierda del campo Order ID

# Fecha
tk.Label(orders_update, text="Fecha:").grid(row=1, column=0, padx=10, pady=10, sticky='e')
O_U_Date = DateEntry(orders_update, date_pattern='dd/MM/yy')
O_U_Date.grid(row=1, column=1, padx=10, pady=10, sticky='w')

# Hora
time_frame = tk.Frame(orders_update)
time_frame.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Hora
tk.Label(orders_update, text="Hora:").grid(row=2, column=0, padx=10, pady=10, sticky='e')  # Cambiado a columna 0
time_frame = tk.Frame(orders_update)
time_frame.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# Espacio en blanco ajustado para alinear con las otras etiquetas
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
    # Obtener el ID de orden ingresado por el usuario
    order_id = int(O_D_OrderID.get())

    # Establecer la conexión a la base de datos Oracle
    connection = conexion()

    try:
        # Crear un cursor para ejecutar consultas
        cursor = connection.cursor()

        # Consultar la orden que se va a eliminar
        cursor.execute("SELECT * FROM orders WHERE ORDER_ID = :order_id", {'order_id': order_id})
        order_data = cursor.fetchone()

        # Mostrar un mensaje con los datos de la orden que se va a eliminar
        if order_data:
            order_info = f"Registro a eliminar:\nID Orden: {order_data[0]}\nFecha: {order_data[1].strftime('%d/%m/%y')}\nModo: {order_data[2]}\nID Cliente: {order_data[3]}\nEstatus: {order_data[4]}\nTotal: {order_data[5]}\nID Representante: {order_data[6]}\nCódigo de Promoción: {order_data[7]}"
            if messagebox.askokcancel("Confirmar eliminación", order_info + "\n\n¿Estás seguro que deseas eliminar esta orden?"):
                # Ejecutar el procedimiento almacenado para eliminar la orden
                cursor.callproc("delete_order", [order_id])
                # Confirmar la transacción
                connection.commit()
                # Mostrar un mensaje de éxito
                messagebox.showinfo("Éxito", "La orden ha sido eliminada correctamente.")
        else:
            messagebox.showinfo("Información", f"No se encontró ninguna orden con el ID {order_id}.")

    except oracledb.DatabaseError as e:
        # En caso de error, mostrar un mensaje de error
        messagebox.showerror("Error", "Ocurrió un error al eliminar la orden en la base de datos:\n{}".format(str(e)))

    finally:
        # Cerrar el cursor y la conexión
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

root.mainloop()
