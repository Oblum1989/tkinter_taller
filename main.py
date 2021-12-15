import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()

ventana.title("Taller 1 Tkinter")
ventana.geometry('500x230')
ventana.config(bg='light gray')
ventana.resizable(False,False)

label_name = tk.Label(ventana, text="Escribe tu nombre: ")
label_name.config(bg='light gray', fg='black')
label_name.grid(row=1, column=0, columnspan=2, padx=6, pady=6, sticky="w")

caja_name = tk.Entry(ventana)
caja_name.config(bg='white', fg='blue', width="15")
caja_name.grid(row=1, column=2, padx=1, pady=6, sticky="w")


label_apellido1 = tk.Label(ventana, text="Escribe tu Apellido Paterno: ")
label_apellido1.config(bg='light gray', fg='black')
label_apellido1.grid(row=2, column=0, columnspan=2, padx=6, pady=6, sticky="w")

caja_apellido1 = tk.Entry(ventana)
caja_apellido1.config(bg='white', fg='blue', width="15")
caja_apellido1.grid(row=2, column=2, padx=1, pady=6, sticky="w")

label_apellido2 = tk.Label(ventana, text="Escribe tu Apellido materno: ")
label_apellido2.config(bg='light gray', fg='black')
label_apellido2.grid(row=3, column=0, columnspan=2, padx=6, pady=6, sticky="w")

caja_apellido2 = tk.Entry(ventana)
caja_apellido2.config(bg='white', fg='blue', width="15")
caja_apellido2.grid(row=3, column=2, padx=1, pady=6, sticky="w")

label_edad = tk.Label(ventana, text="Edad: ")
label_edad.config(bg='light gray', fg='black')
label_edad.grid(row=4, column=0, padx=6, pady=6, sticky="w")

caja_edad = tk.Entry(ventana)
caja_edad.config(bg='white', fg='blue', width="15")
caja_edad.grid(row=4, column=1, padx=5, pady=6)

label_genero = tk.Label(ventana, text="Sexo: ")
label_genero.config(bg='light gray', fg='black')
label_genero.grid(row=5, column=0, padx=6, pady=6, sticky="w")

genero = tk.StringVar()
caja_genero = ttk.Combobox(ventana, width= 12, textvariable = genero)
caja_genero.grid(row=5, column=1, padx=6, pady=6)
caja_genero['values'] = ('M', 'F', 'Otro')

boton=tk.Button(ventana, text="saludo personalizado")
boton.config(bg='gray', fg='black')
boton.grid(row=6, column=0,columnspan=2, padx=6, pady=6, sticky="w")

leon_image = tk.PhotoImage(file = r"leon.png")
image = leon_image.subsample(3, 3)
label_image = tk.Label(ventana, image = image)
label_image.config(bg='light gray', fg='black')
label_image.grid(row=1, column=3,rowspan=6, padx=6, pady=6, sticky="w")

ventana.mainloop()