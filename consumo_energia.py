import tkinter as tk

def calcular_costo_total():
    try:
        dispositivos = []
        # Obtener valores de entrada
        luces_potencia = float(entry_luces_potencia.get())
        luces_horas = int(entry_luces_horas.get())
        ventilacion_potencia = float(entry_ventilacion_potencia.get())
        ventilacion_horas = int(entry_ventilacion_horas.get())
        extractor_potencia = float(entry_extractor_potencia.get())
        extractor_horas = int(entry_extractor_horas.get())
        precio_kwh = float(entry_precio_kwh.get())
        
        # Crear lista de dispositivos
        dispositivos.append(("luces", luces_potencia))
        dispositivos.append(("ventilación", ventilacion_potencia))
        dispositivos.append(("extractor", extractor_potencia))
        
        horas_uso = [luces_horas, ventilacion_horas, extractor_horas]
        
        # Calcular costo total
        costo_total = 0
        resultados = ""
        
        for i, (nombre, potencia_w) in enumerate(dispositivos):
            horas_diarias = horas_uso[i]
            consumo_diario_kwh = (potencia_w * horas_diarias) / 1000
            consumo_mensual_kwh = consumo_diario_kwh * 30
            costo_mensual = consumo_mensual_kwh * precio_kwh
            costo_total += costo_mensual
            
            resultados += f"El consumo mensual de {nombre}: ${costo_mensual:,.2f} pesos\n"

        resultados += f"\nCosto mensual total: ${costo_total:,.2f} pesos"
        
        # Mostrar resultados en una etiqueta
        resultados_label.config(text=resultados)
        
    except ValueError:
        resultados_label.config(text="Por favor, ingresa valores válidos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de Costo Eléctrico")

# Cargar imagen
imagen = tk.PhotoImage(file="C:/Users/arcos/OneDrive/Escritorio/consumo de energia/1.png")  # Cambia esto a la ruta de tu imagen
imagen_label = tk.Label(root, image=imagen)
imagen_label.grid(row=0, columnspan=2)  # Coloca la imagen en la primera fila

# Crear y posicionar etiquetas y entradas
tk.Label(root, text="Potencia Luces (W):").grid(row=1, column=0)
entry_luces_potencia = tk.Entry(root)
entry_luces_potencia.grid(row=1, column=1)

tk.Label(root, text="Horas Luces/Día:").grid(row=2, column=0)
entry_luces_horas = tk.Entry(root)
entry_luces_horas.grid(row=2, column=1)

tk.Label(root, text="Potencia Ventilación (W):").grid(row=3, column=0)
entry_ventilacion_potencia = tk.Entry(root)
entry_ventilacion_potencia.grid(row=3, column=1)

tk.Label(root, text="Horas Ventilación/Día:").grid(row=4, column=0)
entry_ventilacion_horas = tk.Entry(root)
entry_ventilacion_horas.grid(row=4, column=1)

tk.Label(root, text="Potencia Extractor (W):").grid(row=5, column=0)
entry_extractor_potencia = tk.Entry(root)
entry_extractor_potencia.grid(row=5, column=1)

tk.Label(root, text="Horas Extractor/Día:").grid(row=6, column=0)
entry_extractor_horas = tk.Entry(root)
entry_extractor_horas.grid(row=6, column=1)

tk.Label(root, text="Precio por kWh:").grid(row=7, column=0)
entry_precio_kwh = tk.Entry(root)
entry_precio_kwh.grid(row=7, column=1)

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular Costo", command=calcular_costo_total)
btn_calcular.grid(row=8, columnspan=2)

# Etiqueta para mostrar resultados
resultados_label = tk.Label(root, text="", justify=tk.LEFT)
resultados_label.grid(row=9, columnspan=2)

# Iniciar el bucle de eventos
root.mainloop()
