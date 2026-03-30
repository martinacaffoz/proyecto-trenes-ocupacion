import random
import matplotlib.pyplot as plt

# Crear vagones iniciales
vagones = []

for i in range(5):
    ocupacion = random.randint(20, 80)
    vagones.append(ocupacion)

cantidad_estaciones = 3

for estacion in range(1, cantidad_estaciones + 1):

    print(f"\n🚉 Estación {estacion}")

    for i in range(len(vagones)):
        
        baja = random.randint(0, 20)
        sube = random.randint(0, 30)

        vagones[i] = vagones[i] - baja + sube

        # Limitar valores
        if vagones[i] < 0:
            vagones[i] = 0
        if vagones[i] > 100:
            vagones[i] = 100

        # Estado
        if vagones[i] > 75:
            estado = "🔴"
        elif vagones[i] > 40:
            estado = "🟡"
        else:
            estado = "🟢"

        print(f"Vagón {i+1}: {vagones[i]}% {estado}")

    # Gráfico
    plt.figure()
    plt.bar(range(1, 6), vagones)
    plt.title(f"Ocupación en Estación {estacion}")
    plt.xlabel("Vagones")
    plt.ylabel("Ocupación (%)")
    plt.ylim(0, 100)

    plt.show()

    # Recomendación
    mejor_vagon = vagones.index(min(vagones)) + 1
    print(f"👉 Conviene subir al vagón {mejor_vagon}")
