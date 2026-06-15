import tkinter as tk #Acá impotamos la librería Tkinter con apodo 

proyectos = []

ventana = tk.Tk() # esta variable llama a la formula tk para crear la ventana principal 
ventana.title("Musa") # esta función asigna el nombre que aparecerá arriba
ventana.geometry("900x750")# Define el tamaño que queremos para la ventana
ventana.configure(bg="#450363")

frame_inicio = tk.Frame(ventana,bg="#450363")

frame_agenda = tk.Frame(ventana, bg="#450363")

frame_pendientes = tk.Frame(frame_agenda, bg="#450363")

frame_completando = tk.Frame(frame_agenda, bg="#450363")

frame_completados = tk.Frame(frame_agenda, bg="#450363")

frame_nuevo = tk.Frame(ventana,bg="#450363")
titulo_nuevo = tk.Label(frame_nuevo,text="Nuevo Proyecto",font=("Arial", 30, "bold"),bg="#450363",fg="white")
titulo_nuevo.pack(pady=20)
label_titulo = tk.Label(frame_nuevo,text="Título",bg="#450363",fg="white",font=("Arial", 12))
label_titulo.pack()
entrada_titulo = tk.Entry(frame_nuevo,width=30)
entrada_titulo.pack(pady=10)

label_marca = tk.Label(frame_nuevo, text="Marca", bg="#450363", fg="white", font=("Arial", 12)) # todos estos entry funcionan como un intput para que el usuario ingrese datos
label_marca.pack()

entrada_marca = tk.Entry(frame_nuevo,width=30)
entrada_marca.pack(pady=10)
label_plataforma = tk.Label( frame_nuevo, text="Plataforma",bg="#450363", fg="white", font=("Arial", 12))
label_plataforma.pack()
entrada_plataforma = tk.Entry( frame_nuevo, width=30)

entrada_plataforma.pack(pady=10)
label_fecha = tk.Label(frame_nuevo,text="Fecha límite",bg="#450363",fg="white", font=("Arial", 12))
label_fecha.pack()
entrada_fecha = tk.Entry( frame_nuevo,width=30)
entrada_fecha.pack(pady=10)

prioridad = tk.StringVar()
prioridad.set("Flexible")
frame_prioridad = tk.Frame( frame_nuevo, bg="#450363")

label_prioridad = tk.Label( frame_nuevo, text="Prioridad",bg="#450363",fg="white", font=("Arial", 12))
label_prioridad.pack(pady=10)
frame_prioridad.pack(pady=10)
radio_critico = tk.Radiobutton( frame_prioridad,text="Crítico", variable=prioridad, value="Crítico")
radio_critico.pack(side="left", padx=15)
radio_importante = tk.Radiobutton(frame_prioridad,text="Importante", variable=prioridad, value="Importante")
radio_importante.pack(side="left", padx=15)
radio_flexible = tk.Radiobutton( frame_prioridad, text="Flexible",variable=prioridad, value="Flexible")
radio_flexible.pack(side="left", padx=15)

dificultad = tk.StringVar()
dificultad.set("Media")
label_dificultad = tk.Label(frame_nuevo,text="Dificultad", bg="#450363", fg="white", font=("Arial", 12))
label_dificultad.pack(pady=10)
frame_dificultad = tk.Frame(frame_nuevo, bg="#450363")
frame_dificultad.pack(pady=5)
radio_alta = tk.Radiobutton(frame_dificultad,text="Alta", variable=dificultad,value="Alta")
radio_alta.pack(side="left", padx=15)
radio_media = tk.Radiobutton(frame_dificultad,text="Media", variable=dificultad,value="Media")
radio_media.pack (side="left", padx=15)
radio_baja = tk.Radiobutton(frame_dificultad,text="Baja", variable=dificultad,value="Baja")
radio_baja.pack (side="left", padx=15)
def volver_inicio():# Todo este codigo nos da la opción de volver al menú principal de musa 
    frame_agenda.pack_forget()
    frame_nuevo.pack_forget()
    frame_inicio.pack(fill="both", expand=True)

def guardar_proyecto():
    precio = 0
    if dificultad.get() == "Baja":
        precio = 100
    elif dificultad.get() == "Media":
        precio = 200
    elif dificultad.get() == "Alta":
        precio = 300
    if prioridad.get() == "Importante":
        precio += 50
    elif prioridad.get() == "Crítico":
        precio += 100

    proyecto = { "titulo": entrada_titulo.get(), "marca": entrada_marca.get(), "plataforma": entrada_plataforma.get(), "fecha": entrada_fecha.get(), "prioridad": prioridad.get(), "dificultad": dificultad.get(),"estado": "Pendiente", "precio": precio,}
    
    proyectos.append(proyecto)
    print(proyectos)

    entrada_titulo.delete(0, tk.END)
    entrada_marca.delete(0, tk.END)
    entrada_plataforma.delete(0, tk.END)
    entrada_fecha.delete(0, tk.END)

    prioridad.set("Flexible")
    dificultad.set("Media")
boton_guardar = tk.Button( frame_nuevo, text="Guardar", command=guardar_proyecto)
boton_guardar.pack(pady=20)
boton_volver_nuevo = tk.Button( frame_nuevo,text="Volver",command=volver_inicio) 
boton_volver_nuevo.pack(pady=10)


titulo_agenda = tk.Label(frame_agenda, text="Agenda", font=("Arial", 30, "bold"), bg="#450363",fg="white") # aquí estamos creando el frame de agenda para que se abra en la misma pantalla y no tener la necesidad de crear nuevas ventanas
titulo_agenda.pack(pady=30)
label_pendientes = tk.Label( frame_agenda, text="📌 Pendientes", bg="#450363", fg="white", font=("Arial",16,"bold"))
label_pendientes.pack(pady=10)
frame_pendientes.pack()

label_completando = tk.Label(frame_agenda,text="🚧 Completando", bg="#450363", fg="white", font=("Arial",16,"bold"))
label_completando.pack(pady=10)
frame_completando.pack()

label_completados = tk.Label(frame_agenda,text="✅ Completados",bg="#450363",fg="white",font=("Arial",16,"bold"))
label_completados.pack(pady=10)
frame_completados.pack()

def pasar_a_completando(proyecto):
    proyecto["estado"] = "Completando"
    mostrar_agenda()

def pasar_a_completado(proyecto):
    proyecto["estado"] = "Completado"
    mostrar_agenda()

def mostrar_agenda():
    print(proyectos)
    frame_inicio.pack_forget()
    for widget in frame_pendientes.winfo_children():
        widget.destroy()
    for widget in frame_completando.winfo_children():
        widget.destroy()
    for widget in frame_completados.winfo_children():
        widget.destroy()
    for proyecto in proyectos:
        text = (
            f"{proyecto['titulo']}\n"
            f"{proyecto['plataforma']} | {proyecto['prioridad']}\n"
            f"Fecha: {proyecto['fecha']}\n"
            f"Precio sugerido: Q{proyecto['precio']}"
        )
        if proyecto["estado"] == "Pendiente":
            frame_tarjeta = tk.Frame(frame_pendientes, bg="#35054C")
            frame_tarjeta.pack(pady=5)
            label_proyecto = tk.Label(frame_tarjeta, text=text, bg="#35054C", fg="white", width=45, height=5)
            label_proyecto.pack()
            boton_empezar = tk.Button(frame_tarjeta, text="Empezar", command=lambda p=proyecto: pasar_a_completando(p))
            boton_empezar.pack(pady=5)
        elif proyecto["estado"] == "Completando":
            frame_tarjeta = tk.Frame(frame_completando, bg="#5A2E7A")
            frame_tarjeta.pack(pady=5)
            label_proyecto = tk.Label(frame_tarjeta,text=text,bg="#5A2E7A",fg="white",width=45,height=5)
            label_proyecto.pack()
            boton_finalizar = tk.Button(frame_tarjeta,text="Finalizar",command=lambda p=proyecto: pasar_a_completado(p))
            boton_finalizar.pack(pady=5)
        elif proyecto["estado"] == "Completado":
            frame_tarjeta = tk.Frame(frame_completados, bg="#2E8B57")
            frame_tarjeta.pack(pady=5)
            label_proyecto = tk.Label(frame_tarjeta,text=text,bg="#2E8B57",fg="white",width=45,height=5)
            label_proyecto.pack()
    frame_agenda.pack(fill="both", expand=True)


def mostrar_nuevo():
    frame_inicio.pack_forget()
    frame_nuevo.pack(fill="both", expand=True)
boton_volver = tk.Button(frame_agenda, text="Volver", command=volver_inicio,)
boton_volver.pack()

frame_inicio.pack(fill="both", expand=True)

titulo = tk.Label (frame_inicio, text="MUSA", font=("Arial", 36, "bold"), fg="white", bg="#450363") # esta función crea un texto con el nombre de musa y le asigna un tipo de letra y tamaño
titulo.pack(pady=20) # esta función coloca el texto en la ventana y le asigna un espacio de 20 píxeles por debajo

boton_agenda = tk.Button(frame_inicio, text="Agenda", bg="#35054C", fg="white", width=20, height=3, command=mostrar_agenda) # esta función crea el botón con el texto de Agenda
boton_agenda.pack(pady=10) # esta función coloca el botón en la ventana y le asigna un espacio de 10 píxeles por debajo y un tamaño de 30 de ancho y 3 de alto
#copiamos el formato del botón anterior con los próximos 2 botones 
boton_nuevo = tk.Button (frame_inicio, text="Ingresar Nuevo Proyecto", bg="#35054C", fg="white",width=20,height=3, command=mostrar_nuevo) # esta funci´n crea el botón con el texto de Ingresar Nuevo Proyecto
boton_nuevo.pack(pady=10) # esta función coloca el botón en la ventana y le asigna un espacio de 10 píxeles por debajo y un tamaño de 30 de ancho y 3 de alto
boton_completados = tk.Button (frame_inicio, text="Completados", bg="#35054C", fg="white",width=20,height=3) # esta funci´n crea el botón con el texto de Completados
boton_completados.pack(pady=10) # esta función coloca el botón en la ventana y le asigna un espacio de 10 píxeles por debajo y un tamaño de 30 de ancho y 3 de alto

ventana.mainloop () # mantiene la ventana abierta por que si no valimos
