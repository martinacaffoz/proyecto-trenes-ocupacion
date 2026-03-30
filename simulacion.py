import random

cantidad_vagones = 7

# 🔴 Estado al salir de Retiro
vagones_retiro = [random.randint(60, 100) for _ in range(cantidad_vagones)]

print("🚆 Estado saliendo de Retiro:\n")
for i in range(cantidad_vagones):
    print(f"Vagón {i+1}: {vagones_retiro[i]}%")

# 🟡 Paso por Palermo (sube y baja gente)
vagones_palermo = []

for i in range(cantidad_vagones):
    baja = random.randint(10, 40)
    sube = random.randint(5, 30)

    ocupacion = vagones_retiro[i] - baja + sube

    if ocupacion < 0:
        ocupacion = 0
    if ocupacion > 100:
        ocupacion = 100

    vagones_palermo.append(ocupacion)

print("\n🚉 Después de Palermo:\n")
for i in range(cantidad_vagones):
    print(f"Vagón {i+1}: {vagones_palermo[i]}%")

# 🔮 Predicción en Villa Crespo (lo MÁS importante)
print("\n🔮 Predicción en Villa Crespo (gente que se baja):\n")

prediccion_vc = []

for i in range(cantidad_vagones):
    
    # porcentaje que se baja (simula datos históricos)
    porcentaje_baja = random.randint(20, 70)

    ocupacion_actual = vagones_palermo[i]

    ocupacion_final = ocupacion_actual * (1 - porcentaje_baja / 100)

    ocupacion_final = int(ocupacion_final)

    prediccion_vc.append(ocupacion_final)

    print(f"Vagón {i+1}: {ocupacion_actual}% → {ocupacion_final}% después de bajar gente ({porcentaje_baja}% baja)")

# 🎯 Recomendación REAL (basada en lo que queda)
mejor_vagon = prediccion_vc.index(min(prediccion_vc)) + 1

print(f"\n👉 En Villa Crespo conviene el vagón {mejor_vagon}")
