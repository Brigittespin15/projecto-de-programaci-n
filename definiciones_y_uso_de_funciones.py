def calculo_temperatura(datos, ciudad, semana_inicio, semana_final):
    num_items = 0  # total de items leídos
    suma_temp = 0  # la sumatoria de las temperaturas
    for i in range(len(datos[ciudad])):
        if i >= semana_inicio and i <= semana_final:
            for j in range(len(datos[ciudad][i])):
                suma_temp = suma_temp + datos[ciudad][i][j]['temp']
                num_items = num_items + 1

                print(datos[ciudad][i][j])

    promedios = suma_temp / num_items
    return promedios


# TEMPERATURA POR CIUDADES
temperaturas = [
    [  # Ciudad 1 Riobamba
        # Semana 1
        [
            {"Día": "Lunes", "temp": 13},  # lUNES
            {"Día": "Martes", "temp": 20},  # MARTES
            {"Día": "Miércoles", "temp": 19},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 29},  # JUEVES
            {"Día": "Viernes", "temp": 22},  # VIERNES
            {"Día": "Sábado", "temp": 30},  # SÁBADO
            {"Día": "Domingo", "temp": 17}  # DOMINGO
        ],
        # Semana 2
        [
            {"Día": "Lunes", "temp": 13},  # lUNES
            {"Día": "Martes", "temp": 28},  # MARTES
            {"Día": "Miércoles", "temp": 21},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 25},  # JUEVES
            {"Día": "Viernes", "temp": 26},  # VIERNES
            {"Día": "Sábado", "temp": 26},  # SÁBADO
            {"Día": "Domingo", "temp": 16}  # DOMINGO
        ],
        # Semana 3
        [
            {"Día": "Lunes", "temp": 15},  # lUNES
            {"Día": "Martes", "temp": 14},  # MARTES
            {"Día": "Miércoles", "temp": 28},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 10},  # JUEVES
            {"Día": "Viernes", "temp": 25},  # VIERNES
            {"Día": "Sábado", "temp": 11},  # SÁBADO
            {"Día": "Domingo", "temp": 48}  # DOMINGO
        ],
        # Semana 4
        [
            {"Día": "Lunes", "temp": 23},  # lUNES
            {"Día": "Martes", "temp": 17},  # MARTES
            {"Día": "Miércoles", "temp": 27},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 38},  # JUEVES
            {"Día": "Viernes", "temp": 30},  # VIERNES
            {"Día": "Sábado", "temp": 17},  # SÁBADO
            {"Día": "Domingo", "temp": 25}  # DOMINGO
        ]
    ],
    [  # Ciudad 2 AMBATO
        # Semana 1
        [
            {"Día": "Lunes", "temp": 19},  # lUNES
            {"Día": "Martes", "temp": 35},  # MARTES
            {"Día": "Miércoles", "temp": 23},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 20},  # JUEVES
            {"Día": "Viernes", "temp": 38},  # VIERNES
            {"Día": "Sábado", "temp": 44},  # SÁBADO
            {"Día": "Domingo", "temp": 22}  # DOMINGO
        ],
        # Semana 2
        [
            {"Día": "Lunes", "temp": 21},  # lUNES
            {"Día": "Martes", "temp":37},  # MARTES
            {"Día": "Miércoles", "temp": 25},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 42},  # JUEVES
            {"Día": "Viernes", "temp": 10},  # VIERNES
            {"Día": "Sábado", "temp": 6},  # SÁBADO
            {"Día": "Domingo", "temp": 23}  # DOMINGO
        ],
        # Semana 3
        [
            {"Día": "Lunes", "temp": 30},  # lUNES
            {"Día": "Martes", "temp": 46},  # MARTES
            {"Día": "Miércoles", "temp": 22},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 30},  # JUEVES
            {"Día": "Viernes", "temp": 28},  # VIERNES
            {"Día": "Sábado", "temp": 25},  # SÁBADO
            {"Día": "Domingo", "temp": 11}  # DOMINGO
        ],
        # Semana 4
        [
            {"Día": "Lunes", "temp": 20},  # lUNES
            {"Día": "Martes", "temp": 27},  # MARTES
            {"Día": "Miércoles", "temp": 14},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 31},  # JUEVES
            {"Día": "Viernes", "temp": 19},  # VIERNES
            {"Día": "Sábado", "temp": 37},  # SÁBADO
            {"Día": "Domingo", "temp": 24}  # DOMINGO
        ]
    ],
    [  # Ciudad 3 CUENCA
        # Semana 1
        [
            {"Día": "Lunes", "temp": 10},  # lUNES
            {"Día": "Martes", "temp": 23},  # MARTES
            {"Día": "Miércoles", "temp": 16},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 39},  # JUEVES
            {"Día": "Viernes", "temp": 12},  # VIERNES
            {"Día": "Sábado", "temp": 20},  # SÁBADO
            {"Día": "Domingo", "temp": 38}  # DOMINGO
        ],
        # Semana 2
        [
            {"Día": "Lunes", "temp": 13},  # lUNES
            {"Día": "Martes", "temp": 26},  # MARTES
            {"Día": "Miércoles", "temp": 39},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 32},  # JUEVES
            {"Día": "Viernes", "temp": 25},  # VIERNES
            {"Día": "Sábado", "temp": 23},  # SÁBADO
            {"Día": "Domingo", "temp": 11}  # DOMINGO
        ],
        # Semana 3
        [
            {"Día": "Lunes", "temp": 21},  # lUNES
            {"Día": "Martes", "temp": 14},  # MARTES
            {"Día": "Miércoles", "temp": 27},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 10},  # JUEVES
            {"Día": "Viernes", "temp": 13},  # VIERNES
            {"Día": "Sábado", "temp": 31},  # SÁBADO
            {"Día": "Domingo", "temp": 29}  # DOMINGO
        ],
        # Semana 4
        [
            {"Día": "Lunes", "temp": 12},  # lUNES
            {"Día": "Martes", "temp": 25},  # MARTES
            {"Día": "Miércoles", "temp": 18},  # MIÉRCOLES
            {"Día": "Jueves", "temp": 11},  # JUEVES
            {"Día": "Viernes", "temp": 24},  # VIERNES
            {"Día": "Sábado", "temp": 22},  # SÁBADO
            {"Día": "Domingo", "temp": 20}  # DOMINGO
        ]
    ]
]


promedio_calc = calculo_temperatura(temperaturas, 1, 1, 2)

print(f"Promedio {promedio_calc:.2f}°")