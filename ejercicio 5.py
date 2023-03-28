pul_cm = float(2.54)
cm_pul = float(0.393701)
print("Elige el valor a convertir")
print("1. Centímetros")
print("2. Pulgadas")

type1 = (input(''))

print("Escribe la cantidad que deseas convertir")
val = (float(input('')))

if type1 == '1':
    result = (val * cm_pul)
elif type1 == '2':
    result = (val * pul_cm)
else:
    print("Valor inválido")
print("El resultado de la conversión es", result)