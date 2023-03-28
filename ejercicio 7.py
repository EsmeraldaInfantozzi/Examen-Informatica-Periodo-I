min_sec = float(60)
hor_sec = float(3600)
print("Elige el valor a convertir a segundos")
print("1. Minutos")
print("2. Horas")

type1 = (input(''))

print("Escribe la cantidad a convertir")
val = (float(input('')))

if type1 == '1':
    result = (val * min_sec)
elif type1 == '2':
    result = (val * hor_sec)
else:
    print("Valor invalido")

print("El resultado en segundos es de", result)