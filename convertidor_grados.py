def converitdor(grados_centigrados):
    farenheit = (grados_centigrados*9/5)+32
    kelvin=grados_centigrados+273.15
    return farenheit,kelvin
grad_cent=float(input("Ingrese el valor a convertir: "))
r_farenheit,r_kelvin= converitdor(grad_cent)
print("El valor en Farenheit es=",r_farenheit)
print("El valor en Kelvin es=",r_kelvin)