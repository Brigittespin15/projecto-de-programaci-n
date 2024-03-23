#CREACION DE UN DICCIONARIO
#REGISTRO DE INFORMACION PERSONAL

informacion_personal = {
    "Nombre": "Brigitte",
    "Edad": "23 Años",
    "Ciudad": "Lago Agrio",
    "Ocupación": "Estudiante de la Universidad Estatal Amazonica"
}


informacion_personal["Ciudad"] = "Sucumbios"
informacion_personal["Ocupación"] = "Estudiante de la Universidad"

if "Telefono" not in informacion_personal:
    informacion_personal["Telefono"]= "555-555-5555"

if "Edad" in informacion_personal:
    del informacion_personal["Edad"]

print(informacion_personal)