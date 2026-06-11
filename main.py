import tkinter as tk #Acá impotamos la librería Tkinter con apodo 

ventana = tk.Tk() # esta variable llama a la formula tk para crear la ventana principal 
ventana.title("Musa") # esta función asigna el nombre que aparecerá arriba
ventana.geometry("800x600") # Define el tamaño que queremos para la ventana
ventana.configure(bg="#450363")

titulo = tk.Label (ventana, text="MUSA", font=("Arial", 36, "bold"), fg="white", bg="#450363") # esta función crea un texto con el nombre de musa y le asigna un tipo de letra y tamaño
titulo.pack(pady=20) # esta función coloca el texto en la ventana y le asigna un espacio de 20 píxeles por debajo

boton_agenda = tk.Button (ventana, text="Agenda", bg="#35054C", fg="white",width=20,height=3) # esta funci´n crea el botón con el texto de Agenda
boton_agenda.pack(pady=10) # esta función coloca el botón en la ventana y le asigna un espacio de 10 píxeles por debajo y un tamaño de 30 de ancho y 3 de alto
#copiamos el formato del botón anterior con los próximos 2 botones 
boton_nuevo = tk.Button (ventana, text="Ingresar Nuevo Proyecto", bg="#35054C", fg="white",width=20,height=3) # esta funci´n crea el botón con el texto de Ingresar Nuevo Proyecto
boton_nuevo.pack(pady=10) # esta función coloca el botón en la ventana y le asigna un espacio de 10 píxeles por debajo y un tamaño de 30 de ancho y 3 de alto
boton_completados = tk.Button (ventana, text="Completados", bg="#35054C", fg="white",width=20,height=3) # esta funci´n crea el botón con el texto de Completados
boton_completados.pack(pady=10) # esta función coloca el botón en la ventana y le asigna un espacio de 10 píxeles por debajo y un tamaño de 30 de ancho y 3 de alto
    
ventana.mainloop () # mantiene la ventana abierta por que si no valimos
