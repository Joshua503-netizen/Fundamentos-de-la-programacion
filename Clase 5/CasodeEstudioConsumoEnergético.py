import numpy as np

consumo = np.array([
    [12.5, 13.2, 11.9, 14.0, 13.5, 15.0, 14.3],
    [10.1, 10.5, 10.0, 11.2, 11.5, 12.0, 11.8],
    [14.0, 14.2, 13.9, 15.5, 15.1, 16.0, 15.8],
    [9.0, 9.2, 8.9, 9.5, 9.8, 10.0, 9.7],
    [16.2, 16.5, 16.0, 17.1, 17.4, 18.0, 17.8],
    [11.0, 11.3, 11.1, 12.0, 12.4, 12.8, 12.5],
    [13.5, 13.8, 13.2, 14.1, 14.6, 15.0, 14.9],
    [10.8, 11.0, 10.6, 11.5, 11.8, 12.2, 12.0],
    [15.1, 15.5, 15.0, 16.0, 16.4, 17.0, 16.7],
    [8.5, 8.7, 8.4, 9.0, 9.2, 9.5, 9.3],
])

print("Dimensiones:", consumo.ndim)
print("Forma:", consumo.shape)
print("Tipo de datos:", consumo.dtype)
print("Consumo primer hogar:", consumo[0])
print("Consumo el miércoles (día 3):", consumo[:, 2])

# Promedio de consumo por hogar
promedio_por_hogar = np.mean(consumo, axis=1)
print("\nPromedio de consumo por hogar:\n", promedio_por_hogar)

# Promedio de consumo diario de todos los hogares
promedio_por_dia = np.mean(consumo, axis=0)
print("\nPromedio de consumo por día:\n", promedio_por_dia)

# Suma total de consumo en la semana de los 10 hogares
total_consumo = np.sum(consumo)
print("\nSuma total de consumo (todos los hogares, toda la semana):\n", total_consumo)

# Máximo por hogar
maximos = np.max(consumo, axis=1)
print("\nMáximo consumo por hogar:\n", maximos)

# Mínimo por día
minimos = np.min(consumo, axis=0)
print("\nMínimo consumo por día:\n", minimos)

# Desviación estándar global
desviacion = np.std(consumo)
print("\nDesviación estándar global:\n", desviacion)

# Suma por hogar (semana)
consumo_total_hogar = np.sum(consumo, axis=1)
print("\nSuma total de consumo por hogar (semana):\n", consumo_total_hogar)

# Índice del hogar con mayor consumo
hogar_mayor_consumo = np.argmax(consumo_total_hogar)
print(f"\nÍndice del hogar con mayor consumo: {hogar_mayor_consumo}")

# Índice del hogar con mejor consumo
hogar_mas_eficiente = np.argmin(consumo_total_hogar)
print(f"Índice del hogar con mejor consumo: {hogar_mas_eficiente}")

# Suma por hogar (semana) - Repetido para el contexto del siguiente bloque
consumo_total_hogar = np.sum(consumo, axis=1)
print(f"\nConsumo total de cada hogar durante la semana: {consumo_total_hogar}")

# Compara cada hogar con un valor mayor a 100
altos = consumo_total_hogar > 100
# Filtrando hogares que cumplen la condición:
consumo_mayor_100 = np.where(altos)[0]
print(f"Ids de hogares con consumo mayor a 100: {consumo_mayor_100}")

# Aplicando normalización MinMax al conjunto de datos
consumo_normalizado = (consumo - consumo.min()) / (consumo.max() - consumo.min())
print("\nConsumo normalizado (MinMax):\n", consumo_normalizado)

# --- INICIO DE RESPUESTAS AL CUESTIONARIO ---
print("\n" + "="*40)
print("             5. CUESTIONARIO DE TRABAJO")
print("="*40 + "\n")

# 1. ¿Cuál es el consumo del hogar 5 el viernes (día 5)?
# Recordar que los índices en Python son base 0.
# Hogar 5 es el índice 4.
# Viernes (día 5) es el índice 4 (lunes=0, martes=1, miercoles=2, jueves=3, viernes=4).
consumo_hogar5_viernes = consumo[4, 4]
print(f"1. El consumo del hogar 5 el viernes (día 5) es: {consumo_hogar5_viernes}")

# 2. Usando indexación, muestra el consumo de los últimos 3 hogares el domingo.
# Domingo es el último día, índice 6.
# Los últimos 3 hogares son del índice 7 al 9.
consumo_ultimos3_domingo = consumo[7:10, 6]
print(f"\n2. Consumo de los últimos 3 hogares el domingo:\n{consumo_ultimos3_domingo}")

# 3. Calcula el promedio de consumo los fines de semana (sábado y domingo, columnas 5 y 6).
# Sábado es columna 5 (índice 4). Domingo es columna 6 (índice 5).
# No, Sábado es columna 5 (índice 5), Domingo es columna 6 (índice 6).
# Corrigiendo: Lunes=0, Martes=1, Miércoles=2, Jueves=3, Viernes=4, Sábado=5, Domingo=6.
# Columnas 5 y 6 son índices 4 y 5 si se refiere al Jueves y Viernes.
# Si se refiere a Sábado y Domingo, son índices 5 y 6.
# Asumiré que se refiere a Sábado (índice 5) y Domingo (índice 6) como fines de semana.
consumo_fines_semana = consumo[:, 5:7] # Selecciona todas las filas, y columnas 5 y 6 (Sábado y Domingo)
promedio_fines_semana = np.mean(consumo_fines_semana)
print(f"\n3. El promedio de consumo los fines de semana (sábado y domingo) es: {promedio_fines_semana:.2f}")

# 4. ¿Qué día de la semana tiene la mayor desviación estándar entre hogares? Explica qué indica esto.
# Calcular la desviación estándar para cada día (entre hogares), es decir, por columna (axis=0).
desviacion_por_dia = np.std(consumo, axis=0)
dia_mayor_desviacion_indice = np.argmax(desviacion_por_dia)

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
dia_mayor_desviacion = dias_semana[dia_mayor_desviacion_indice]

print(f"\n4. El día con la mayor desviación estándar entre hogares es: {dia_mayor_desviacion}")
print(f"   Valor de la desviación estándar para ese día: {desviacion_por_dia[dia_mayor_desviacion_indice]:.2f}")
print("   Explicación: Una mayor desviación estándar en un día específico indica que el consumo entre los diferentes hogares fue más variado o disperso ese día.")
print("   Es decir, hubo una mayor diferencia en la cantidad de energía consumida por los hogares,")
print("   con algunos hogares consumiendo mucho y otros consumiendo poco, en comparación con otros días.")

# 5. Identifica los 3 hogares con menor consumo total durante la semana. Muestra sus índices y valores.
# Ya calculamos consumo_total_hogar previamente.
# Para encontrar los 3 menores, podemos usar np.argsort y tomar los primeros 3 índices.
indices_menor_consumo = np.argsort(consumo_total_hogar)[:3]
valores_menor_consumo = consumo_total_hogar[indices_menor_consumo]

print(f"\n5. Los 3 hogares con menor consumo total durante la semana son:")
print(f"   Índices de los hogares: {indices_menor_consumo}")
print(f"   Valores de consumo total: {valores_menor_consumo}")

# 6. Si el hogar 3 aumenta su consumo en un 10% cada día, ¿cuál sería su nuevo consumo total semanal?
# Hogar 3 es el índice 2 (recuerda 0-base).
consumo_hogar3_original = consumo[2, :]
aumento_porcentaje = 0.10 # 10%
consumo_hogar3_nuevo = consumo_hogar3_original * (1 + aumento_porcentaje)
nuevo_consumo_total_hogar3 = np.sum(consumo_hogar3_nuevo)

print(f"\n6. El consumo original del hogar 3 era: {consumo_hogar3_original}")
print(f"   El nuevo consumo diario del hogar 3 (con 10% de aumento) sería: {consumo_hogar3_nuevo}")
print(f"   El nuevo consumo total semanal del hogar 3 sería: {nuevo_consumo_total_hogar3:.2f}")