# Simulación de ocupación de vagones

vagones = [80, 50, 30, 90, 60]

print("Estado de los vagones:\n")

for i in range(len(vagones)):
    ocupacion = vagones[i]
    
    if ocupacion > 75:
        estado = "🔴 Muy lleno"
    elif ocupacion > 40:
        estado = "🟡 Medio"
    else:
        estado = "🟢 Vacío"
    
    print(f"Vagón {i+1}: {ocupacion}% - {estado}")

# Recomendación
mejor_vagon = vagones.index(min(vagones)) + 1

print("\n👉 Te conviene subir al vagón", mejor_vagon)
