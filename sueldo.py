"""
Andrés Enrique Jaime de la Rosa, 763799
"""




# Entradas
hrt=float(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora: "))
# Proceso
if hrt > 48:
    hrt = hrt - 48
    print("Horas extras",hrt)
    hex = tarifa *2* hrt
    print("Sueldo por horas extras:",hex)
    hrt = hrt+48
    stotal = hrt*tarifa+hex
    print("Sueldo total:",stotal)
else:
    print("Horas extras: 0")
    print("Sueldo por horas extras: 0")
    stotal = hrt*tarifa
    print("Sueldo total:",stotal)

