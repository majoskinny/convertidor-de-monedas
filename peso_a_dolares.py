# Conversor de pesos a dólares

pesos = float(input("Ingresa la cantidad en pesos: "))
tipo_cambio = float(input("Ingresa el tipo de cambio (pesos por dólar): "))

dolares = pesos / tipo_cambio

print(f"{pesos} pesos equivalen a {dolares:.2f} dólares")
