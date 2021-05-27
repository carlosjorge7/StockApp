from tkinter import Entry, Tk, Canvas, Frame, Label, Entry, Button, W, E, Listbox, END
from config.conexion import conexionMySQL

#Instancia de Tkinter
root = Tk()
root.title('StockApp')

# INTERFAZ con canvas
canvas = Canvas(root, height=380, width=400)
canvas.pack()

frame = Frame()
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label = Label(frame, text='Agrega un producto')
label.grid(row=0, column=1)

# Nombre
label = Label(frame, text='Nombre')
label.grid(row=1, column=0)
entry_name = Entry(frame)
entry_name.grid(row=1, column=1)
entry_name.focus()

# Descripcion
label = Label(frame, text='Descripción')
label.grid(row=2, column=0)
entry_descripcion = Entry(frame)
entry_descripcion.grid(row=2, column=1)

# Precio
label = Label(frame, text='Precio')
label.grid(row=3, column=0)
entry_precio = Entry(frame)
entry_precio.grid(row=3, column=1)

# Stock
label = Label(frame, text='Stock')
label.grid(row=4, column=0)
entry_stock = Entry(frame)
entry_stock.grid(row=4, column=1)

# Boton
button = Button(frame, text='Guardar', command=lambda:save(entry_name.get(), entry_descripcion.get(), entry_precio.get(), entry_stock.get()))
button.grid(row=5, column=1, sticky=W+E)

# Buscar
label = Label(frame, text='BUSCAR DATOS')
label.grid(row=6, column=1)

label = Label(frame, text='Busca por id')
label.grid(row=7, column=0)

id = Entry(frame)
id.grid(row=7, column=1)

button = Button(frame, text='Buscar', command=lambda:search(id.get()))
button.grid(row=7, column=2)


#LÓGICA 
def save(nombre, descripcion, precio, stock):
    conn = conexionMySQL()
    cursor = conn.cursor()
    query = '''INSERT INTO producto(nombre, descripcion, precio, stock) VALUES (%s, %s, %s, %s)'''
    cursor.execute(query, ((nombre, descripcion, precio, stock)))
    conn.commit()
    conn.close()
    list()

def list():
    conn = conexionMySQL()
    cursor = conn.cursor()
    query = '''SELECT * FROM producto'''
    cursor.execute(query)
    row = cursor.fetchall()

    listbox = Listbox(frame, width=30, height=10)
    listbox.grid(row=12, columnspan=4, sticky=W+E)

    for r in row:
       listbox.insert(END, r)

    conn.commit()
    conn.close()

def search(id):
    conn = conexionMySQL()
    cursor = conn.cursor()
    query = '''SELECT * FROM producto WHERE id=%s'''
    cursor.execute(query, id)
    row = cursor.fetchone()
    listOne(row)
    conn.commit()
    conn.close()

def listOne(row):
    listbox = Listbox(frame, width=30, height=10)
    listbox.grid(row=12, columnspan=4, sticky=W+E)
    listbox.insert(END, row)

list()
root.mainloop()

