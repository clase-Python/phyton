notas = []

while True:
    entrada = input("Ingresa una nota (o 'fin' para terminar): ")
    if entrada.lower() == 'fin':
        break
    try:
        nota = float(entrada)
        notas.append(nota)  # Corregido: agregar 'nota' en lugar de 'notas'
    except ValueError:
        print("Por favor, ingresa un número válido.")

if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print(f"El promedio de las notas es: {promedio:.2f}")
else:
    print("No se ingresaron notas.")
