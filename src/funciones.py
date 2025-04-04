def imprimir (final):
    """Imprime los jugadores con sus stats acomodados """
    print(f"{'Jugador':<10} {'Kills':<6} {'assists':<8} {'Muertes':<7} {'MVP':<7} {'Puntos':<6}")
    print("-" * 41)
    for nombre ,stats in final.items():
        print(f"{nombre:<10} {stats['kills']:<6} {stats['assists']:<8} {stats['Muertes']:<7} {stats['MVP']:<7} {stats['Puntos']:<6}")

def maximo (puntos_max,nombre_max,puntos_ronda,nombre):
    """Obtiene el nombre del jugador que hizo mas puntos"""
    if puntos_ronda > puntos_max:
        puntos_max = puntos_ronda
        nombre_max = nombre
    return puntos_max , nombre_max

def acumular_final(nombre,stats,final):
    """En el parametro final que es un diccionario , lo llena con el nombre y sus stats y puntos y ademas retorna la cantidad de puntos que obtuvo en esa ronda
    para despues ser usado por la funcion maximo para poder sacar los mvp
    """
    puntos_ronda = 0
    #si no existe el nombre lo agregra con los stasts en 0 
    if nombre not in final: 
        final[nombre]={'kills': 0, 'assists': 0, 'Muertes': 0,'MVP':0,'Puntos':0}
    #agrega a los stats los nuevas muertes y asistencias
    final[nombre]['kills'] += stats['kills']
    final[nombre]['assists'] += stats['assists']
    #si esta en true significa que murio asi que le agrega 1 a los stats y -1 a los puntos del a ronda
    if stats['deaths'] == True :
        final[nombre]['Muertes'] +=1
        puntos_ronda -= 1  
    puntos_ronda += (stats['kills'] * 3) + stats['assists']  
    #le agrega el total de los puntos
    final[nombre]['Puntos'] += puntos_ronda
    return puntos_ronda