# Abrir el archivo en modo lectura
datos = open("My_notes.txt", "r")

# Leer los datos del archivo y almacenarlos en una variable
datos_anterior = datos.read()

datos.close()

# Abrir el archivo en modo escritura
datos = open("My_notes.txt", "w")

# Escribir el nuevo contenido en el archivo, junto con el contenido anterior
datos.write(datos_anterior + "\n")
datos.write("fecha de nacimiento: 15 de agosto del 2000")

# Cerrar el archivo después de la escritura
datos.close()

# Abrir el archivo nuevamente en modo lectura
datos = open("My_notes.txt", "r")

# Leer los datos del archivo actualizado y almacenarlos en una variable
datos_actualizados =datos.read()

# Imprimir actializacion
print(datos_actualizados)

# Cerrar el archivo después de la última lectura
datos.close()