import random

# Crear vagones con ocupación inicial aleatoria
vagones = []

for i in range(5):
    ocupacion = random.randint(20, 80)
    vagones.append(ocupacion)

# Simular estaciones
cantidad_estaciones = 3

for estacion in range(1, cantidad_estaciones + 1):
    print(f"\n🚉 Estación {estacion}")

    for i in range(len(vagones)):
        
        # Gente que baja
        baja = random.randint(0, 20)
        
        # Gente que sube
        sube = random.randint(0, 30)

        # Nueva ocupación
        vagones[i] = vagones[i] - baja + sube

        # Limitar entre 0 y 100
        if vagones[i] < 0:
            vagones[i] = 0
        if vagones[i] > 100:
            vagones[i] = 100

        # Estado
        if vagones[i] > 75:
            estado = "🔴 Muy lleno"
        elif vagones[i] > 40:
            estado = "🟡 Medio"
        else:
            estado = "🟢 Vacío"

        print(f"Vagón {i+1}: {vagones[i]}% - {estado}")

    # Recomendación en cada estación
    mejor_vagon = vagones.index(min(vagones)) + 1
    print(f"👉 Conviene subir al vagón {mejor_vagon}")
