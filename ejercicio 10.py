sueldo = float(input("Ingrese su sueldo mensual: "))

if sue <= 472:
    impuesto = 0
    cuota_fij = 0
elif sue <= 895.24:
    exceso = sue - 472
    impuesto = exceso * 0.1
    cuota_fij = 17.67
elif sue <= 2038.10:
    exceso = sue - 895.24
    impuesto = 42.53 + (exceso * 0.2)
    cuota_fij = 60
else:
    exceso = sue - 2038.10
    impuesto = 352.28 + (exceso * 0.3)
    cuota_fij = 288.57

iss = sue * 0.03
afp = sue * 0.0725
total_descuentos = iss + afp + impuesto + cuota_fij
suel_neto = sue - total_descuentos

print("Sueldo bruto: ${:.2f}".format(sue))
print("Impuesto sobre la renta: ${:.2f}".format(impuesto))
print("ISS: ${:.2f}".format(iss))
print("AFP: ${:.2f}".format(afp))
print("Cuota fija: ${:.2f}".format(cuota_fij))
print("Total descuentos: ${:.2f}".format(total_descuentos))
print("Sueldo neto: ${:.2f}".format(suel_neto))
