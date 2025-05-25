import tkinter as tk
import datetime

def mostrar_hora():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Presionaste el botón a las: {hora_actual}")

# clase(molde, formato) para crear objetos al instanciar / crear

ventana = tk.Tk()
ventana.title("Mi primera ventana con Tkinter")
ventana.geometry("800x600")

texto = tk.Label(ventana, text="Hola desde Tkinter", font=("Arial", 20))
texto.pack()

boton = tk.Button(ventana, text="Mostrar hora", font=("Arial", 15), bg="red", fg="white", command=mostrar_hora)
boton.pack()

ventana.mainloop()