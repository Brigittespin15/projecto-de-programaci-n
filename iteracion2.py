temperaturas = [
    [  # Ibarra
#Dias    1   2   3   4   5   6   7
        [25, 28, 26, 31, 25, 32, 24],  # Semana 1
        [28, 29, 27, 31, 32, 27, 29],  # Semana 2
        [27, 29, 28, 26, 29, 31, 32],  # Semana 3
        [29, 27, 26, 27, 30, 28, 31]  # Semana 4
    ],
    [  # Ambato
#Dias    1   2   3   4   5   6   7
        [26, 27, 24, 25, 27, 28, 25],  # Semana 1
        [26, 27, 25, 28, 24, 26, 27],  # Semana 2
        [25, 26, 24, 23, 25, 24, 26],  # Semana 3
        [27, 26, 29, 27, 28, 26, 27]  # Semana 4
    ],
    [  # Riobamba
#Dias    1   2   3   4   5   6   7
        [31, 29, 27, 28, 30, 29, 27],  # Semana 1
        [29, 31, 28, 27, 29, 30, 31],  # Semana 2
        [27, 30, 29, 27, 28, 27, 29],  # Semana 3
        [29, 31, 31, 28, 27, 26, 28]  # Semana 4
    ]
]

ciudades = ["Ibarra", "Ambato", "Riobamba"]

# Calcular el promedio de temperaturas para cada ciudad y semana

for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum(semana)
        promedio_semana = suma_temperaturas / len(semana)
        print(
f"Temperatura en {ciudades[ciudad_idx]} -> Semana {semana_idx + 1}: {promedio_semana:.2f}°")


  # Calcular el promedio de temperaturas por mes
    promedios_mes = []
    for i in range(0, len(ciudad[0]), 7):  # Agrupar por semana
        suma_mes = sum(sum(semana[i:i + 7]) for semana in ciudad)
        promedio_mes = suma_mes / (len(ciudad) * 7)
        promedios_mes.append(promedio_mes)
        print(
            f"Promedio de temperaturas en {ciudades[ciudad_idx]} -> Mes {len(promedios_mes)}: {promedio_mes:.2f}°")

