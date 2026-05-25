# dividir dos números
import tkinter as tk

def dividir():
    try:
        # Obtiene los valores de los cuadros de entrada, los convierte a float y multiplica
        numero1 = float(entrada1.get())
        numero2 = float(entrada2.get())
        resultado = numero1 / numero2
        # Muestra el resultado en el cuadro de texto de resultado
        cuadro_resultado.config(state='normal')  # Habilita el cuadro para editar
        cuadro_resultado.delete(0, tk.END)  # Limpia el cuadro
        cuadro_resultado.insert(0, str(resultado))  # Inserta el resultado
        cuadro_resultado.config(state='disabled')  # Deshabilita el cuadro para evitar edición
    except ValueError:
        cuadro_resultado.config(state='normal')
        cuadro_resultado.delete(0, tk.END)
        cuadro_resultado.insert(0, "Ingrese números válidos")
        cuadro_resultado.config(state='disabled')

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Divisor de Dos Números")

# Etiquetas para los cuadros de entrada
etiqueta1 = tk.Label(ventana, text="Ingrese numero_1:")
etiqueta1.grid(row=0, column=0)

etiqueta2 = tk.Label(ventana, text="Ingrese numero_2:")
etiqueta2.grid(row=1, column=0)

# Cuadros de entrada para los números
entrada1 = tk.Entry(ventana)
entrada1.grid(row=0, column=1)

entrada2 = tk.Entry(ventana)
entrada2.grid(row=1, column=1)

# Botón para ejecutar la división
boton_dividir = tk.Button(ventana, text="dividir", command=dividir)
boton_dividir.grid(row=2, column=0, columnspan=2)

# Cuadro de texto para mostrar el resultado
cuadro_resultado = tk.Entry(ventana, state='disabled')
cuadro_resultado.grid(row=3, column=0, columnspan=2)

# Ejecuta la ventana
ventana.mainloop()
