"""
Andrés Enrique Jaime de la Rosa, 763799
"""




# Entradas
hrt=float(input("Horas trabajadas: "))
tarifa = float(input("Tarifa por hora: "))
# Proceso
if hrt > 48:
    hext = hrt-48
    hexp = hext*tarifa*2
    print("Horas extras",hext)
    print("Sueldo por horas extras:",hexp)
    hpn = 48
    snormal = hpn*tarifa
    stotal= snormal+hexp
    print("Sueldo total:",stotal)
else:
    print("Horas extras: 0")
    print("Sueldo por horas extras: 0")
    stotal = hrt*tarifa
    print("Sueldo total:",stotal)

