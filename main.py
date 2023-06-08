import tkinter as tk
import numpy as np
from scipy.integrate import tplquad
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calcular_integral():
    # Obtener los valores ingresados por el usuario
    funcion = funcion_entry.get()

    # Obtener los valores de los límites o asignar valores predeterminados
    limite_x_1 = float(limite_x_entry.get()) if limite_x_entry.get() else 0
    limite_x_2 = float(limite_x_entry2.get()) if limite_x_entry2.get() else 1
    limite_y_1 = float(limite_y_entry.get()) if limite_y_entry.get() else 0
    limite_y_2 = float(limite_y_entry2.get()) if limite_y_entry2.get() else 1
    limite_z_1 = float(limite_z_entry.get()) if limite_z_entry.get() else 0
    limite_z_2 = float(limite_z_entry2.get()) if limite_z_entry2.get() else 1

    # Definir la función como una expresión evaluada numéricamente
    def f(x, y, z):
        return eval(funcion)

    # Realizar los cálculos de la integral triple
    resultado, error = tplquad(f, limite_x_1, limite_x_2, lambda x: limite_y_1, lambda x: limite_y_2, lambda x, y: limite_z_1, lambda x, y: limite_z_2, epsabs=1.49e-08, epsrel=1.49e-08)

    # Mostrar el resultado en la interfaz con 2 decimales
    resultado_label.config(text="El resultado de la integral triple es: {:.2f}".format(resultado))

    # Determinar el tipo de figura según los límites
    if limite_x_1 == limite_x_2 and limite_y_1 == limite_y_2 and limite_z_1 == limite_z_2:
        # Es un punto
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(limite_x_1, limite_y_1, limite_z_1, c='r', marker='o')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    elif limite_x_1 == limite_x_2 and limite_y_1 == limite_y_2:
        # Es una línea
        x_vals = np.linspace(limite_x_1, limite_x_2, 50)
        y_vals = np.linspace(limite_y_1, limite_y_2, 50)
        z_vals = np.linspace(limite_z_1, limite_z_2, 50)
        X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
        F = f(X, Y, Z)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()
    else:
        # Es un volumen
        x_vals = np.linspace(limite_x_1, limite_x_2, 50)
        y_vals = np.linspace(limite_y_1, limite_y_2, 50)
        z_vals = np.linspace(limite_z_1, limite_z_2, 50)
        X, Y, Z = np.meshgrid(x_vals, y_vals, z_vals)
        F = f(X, Y, Z)

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(X, Y, Z, c=F, cmap='viridis')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Cálculo Multivariado")

# Ajustar el tamaño de la ventana
ventana.geometry("400x300")

# Crear los campos de entrada y etiquetas
funcion_label = tk.Label(ventana, text="Función:")
funcion_label.pack()
funcion_entry = tk.Entry(ventana)
funcion_entry.pack()

limite_x_label = tk.Label(ventana, text="Límite para x:")
limite_x_label.pack()
limite_x_entry = tk.Entry(ventana)
limite_x_entry.pack()
limite_x_entry2 = tk.Entry(ventana)
limite_x_entry2.pack()

limite_y_label = tk.Label(ventana, text="Límite para y:")
limite_y_label.pack()
limite_y_entry = tk.Entry(ventana)
limite_y_entry.pack()
limite_y_entry2 = tk.Entry(ventana)
limite_y_entry2.pack()

limite_z_label = tk.Label(ventana, text="Límite para z:")
limite_z_label.pack()
limite_z_entry = tk.Entry(ventana)
limite_z_entry.pack()
limite_z_entry2 = tk.Entry(ventana)
limite_z_entry2.pack()

calcular_button = tk.Button(ventana, text="Calcular", command=calcular_integral)
calcular_button.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

# Iniciar el bucle de eventos de la interfaz gráfica
ventana.mainloop()
