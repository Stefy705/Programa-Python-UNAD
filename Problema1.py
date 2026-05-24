#-----PROBLEMA 1-------
# -------1. MATRIZ DE DATOS---------
# una matriz es una lista de listas 
#cada lista interior representa una fila con los datos del cliente 
#posiion 0: id cliente, posicion 1: segundos, posicion 2: cantidad de clics
sesiones = [
    [101, 240, 12],
    [102, 45, 2],
    [103, 130, 6],
    [104, 200, 10],
    [105, 30, 1],
    [106, 190, 9]
]

# ----------2. Funcion con def ----------
def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else: 
        return "Medio"

# --------3. Informe en print-------
print("=======INFORME DE COMPROMISO=======")
for sesion in sesiones:
    id_cliente = sesion[0]
    nivel = clasificar_compromiso(sesion[1], sesion[2])
    print(f"Cliente {id_cliente}: Nivel de compromiso: {nivel}")
        
