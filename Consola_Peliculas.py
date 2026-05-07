#Consola peliculas - Pensamiento Algoritmico

import Modulo_Peliculas as mod


def mostrar_informacion_pelicula(pelicula: dict) -> None:
    """Imprime los detalles de la pelicula
    Parametros:
        pelicula(dict): La pelicula de la cual se van a mostrar los detalles
        El diccionario que representa una pelicula contiene las siguientes parejas de
        llave-valor:
            - nombre (str): Nombre de la pelicula agendada.
            - genero (str): Generos de la pelicula separados por comas.
            - duracion (int): Duracion en minutos de la pelicula
            - anio (int): Anio de estreno de la pelicula
            - clasificacion (str): Clasificacion de restriccion por edad
            - hora (int): Hora de inicio de la pelicula
            - dia (str): Indica que dia de la semana se planea ver la pelicula
    """
    nombre = pelicula["nombre"]
    genero = pelicula["genero"]
    duracion = pelicula["duracion"]
    anio = pelicula["anio"]
    clasificacion = pelicula["clasificacion"]
    hora = pelicula["hora"]
    dia = pelicula["dia"]

    if (hora // 100 < 10):
        hora_formato = "0" + str(hora // 100)
    else:
        hora_formato = str(hora // 100)

    if (hora % 100 < 10):
        min_formato = "0" + str(hora % 100)
    else:
        min_formato = str(hora % 100)

    print(" Nombre: " + nombre)
    print(" Anio: " + str(anio))
    print(" Dia: " + dia)
    print(" Hora: " + hora_formato + ":" + min_formato)
    print(" Duracion: " + str(duracion) + " min")
    print(" Genero: " + genero)
    print(" Clasificacion: " + clasificacion)


def ejecutar_encontrar_pelicula_mas_larga(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de encontrar la pelicula mas larga.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("\nPelicula mas larga de la agenda:")
    pelicula_mas_larga = mod.encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)
    mostrar_informacion_pelicula(pelicula_mas_larga)


def ejecutar_consultar_duracion_promedio_peliculas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de consultar la duracion promedio de las peliculas.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    promedio = mod.duracion_promedio_peliculas(p1, p2, p3, p4, p5)
    print("\nDuracion promedio de las peliculas de la agenda es : " + promedio)


def ejecutar_encontrar_estrenos(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """ Ejecuta la opcion de buscar peliculas de estreno. Esto es: las peliculas que sean
        mas recientes que un anio dado.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    anio_str = input("Ingrese el anio de referencia para buscar estrenos: ")
    anio = int(anio_str)
    estrenos = mod.encontrar_estrenos(p1, p2, p3, p4, p5, anio)
    print("\nPeliculas estrenadas despues de los " + str(anio) + ": " + estrenos)


def ejecutar_cuantas_peliculas_18_mas(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de consultar cuantas peliculas de la agenda tienen clasificacion
    18+.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    cantidad = mod.cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)
    print("\nCantidad de peliculas con clasificacion 18+: " + str(cantidad))


def ejecutar_reagendar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de reagendar una pelicula
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    print("Reagendar una pelicula de la agenda")

    nombre = input("Ingrese el nombre de la pelicula que desea reagendar: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        nuevo_dia = input("Ingrese el nuevo dia de la semana : ")
        nueva_hora = int(input("Ingrese la nueva hora en formato HHMM: "))
        control = input("¿Desea activar el control horario? (s/n): ").strip().lower()
        control_horario = control == "s"

        resultado = mod.reagendar_pelicula(pelicula, nueva_hora, nuevo_dia, control_horario, p1, p2, p3, p4, p5)
        if resultado:
            print("\nLa pelicula fue reagendada exitosamente.")
            print("Nueva programacion:")
            mostrar_informacion_pelicula(pelicula)
        else:
            print("\nNo fue posible reagendar la pelicula.")


def ejecutar_decidir_invitar(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:
    """Ejecuta la opcion de decidir si se puede invitar a alguien a ver una pelicula o no.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    """
    nom_peli = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nom_peli, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        edad_invitado = int(input("Ingrese la edad del invitado: "))

        if edad_invitado < 18:
            autorizacion = input("¿El invitado tiene autorizacion de sus padres? (s/n): ").strip().lower()
            autorizacion_padres = autorizacion == "s"
        else:
            autorizacion_padres = False

        puede_invitar = mod.decidir_invitar(pelicula, edad_invitado, autorizacion_padres)

        if puede_invitar:
            print("\nSi se puede invitar a la persona a ver '" + pelicula["nombre"] + "'.")
        else:
            print("\nNo se puede invitar a la persona a ver '" + pelicula["nombre"] + "'.")


def ejecutar_encontrar_pelicula(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> None:

    nombre = input("Ingrese el nombre de la pelicula: ")
    pelicula = mod.encontrar_pelicula(nombre, p1, p2, p3, p4, p5)

    if pelicula is None:
        print("No hay ninguna pelicula con este nombre")
    else:
        mostrar_informacion_pelicula(pelicula)

def iniciar_aplicacion():
    """Inicia la ejecución de la aplicación por consola.
    Esta funcion primero crea las cinco peliculas que se van a manejar en la agenda.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    pelicula1 = mod.crear_pelicula("El Exorcista", "Terror", 122, 1973, "18+", 2000, "Lunes")
    pelicula2 = mod.crear_pelicula("UP", "Familiar, Animación", 96, 2009, "Todos", 1500, "Sábado")
    pelicula3 = mod.crear_pelicula("Titanic", "Drama, Romance", 194, 1997, "13+", 1800, "Viernes")
    pelicula4 = mod.crear_pelicula("Saw X", "Terror, Suspenso", 118, 2023, "18+", 2200, "Miércoles")
    pelicula5 = mod.crear_pelicula("Avengers Endgame", "Acción, Ciencia-Ficción", 181, 2019, "13+", 1600, "Domingo")

    ejecutando = True

    while ejecutando:

        print("\nAgenda de peliculas para la semana" + "\n" + ("-" * 50))

        print("Pelicula 1")
        mostrar_informacion_pelicula(pelicula1)
        print("-" * 50)

        print("Pelicula 2")
        mostrar_informacion_pelicula(pelicula2)
        print("-" * 50)

        print("Pelicula 3")
        mostrar_informacion_pelicula(pelicula3)
        print("-" * 50)

        print("Pelicula 4")
        mostrar_informacion_pelicula(pelicula4)
        print("-" * 50)

        print("Pelicula 5")
        mostrar_informacion_pelicula(pelicula5)
        print("-" * 50)

        ejecutando = mostrar_menu_aplicacion(pelicula1, pelicula2, pelicula3, pelicula4, pelicula5)

        if ejecutando:
            input("\nPresione cualquier tecla para volver al menu de opciones... ")


def mostrar_menu_aplicacion(p1: dict, p2: dict, p3: dict, p4: dict, p5: dict) -> bool:
    """Le muestra al usuario las opciones de ejecución disponibles.
    Parametros:
        p1 (dict): Diccionario que contiene la informacion de la pelicula 1.
        p2 (dict): Diccionario que contiene la informacion de la pelicula 2.
        p3 (dict): Diccionario que contiene la informacion de la pelicula 3.
        p4 (dict): Diccionario que contiene la informacion de la pelicula 4.
        p5 (dict): Diccionario que contiene la informacion de la pelicula 5.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opción para salir
        de la aplicacion.
    """
    print("Menu de opciones")
    print(" 1 - Consultar pelicula mas larga")
    print(" 2 - Consultar duracion promedio de las peliculas")
    print(" 3 - Consultar peliculas de estreno")
    print(" 4 - Consultar cuantas peliculas tienen clasificacion 18+")
    print(" 5 - Reagendar pelicula")
    print(" 6 - Verificar si se puede invitar a alguien")
    print(" 7 - Buscar pelicula")
    print(" 8 - Salir de la aplicacion")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_encontrar_pelicula_mas_larga(p1, p2, p3, p4, p5)

    elif opcion_elegida == "2":
        ejecutar_consultar_duracion_promedio_peliculas(p1, p2, p3, p4, p5)

    elif opcion_elegida == "3":
        ejecutar_encontrar_estrenos(p1, p2, p3, p4, p5)

    elif opcion_elegida == "4":
        ejecutar_cuantas_peliculas_18_mas(p1, p2, p3, p4, p5)

    elif opcion_elegida == "5":
        ejecutar_reagendar_pelicula(p1, p2, p3, p4, p5)

    elif opcion_elegida == "6":
        ejecutar_decidir_invitar(p1, p2, p3, p4, p5)

    elif opcion_elegida == "7":
        ejecutar_encontrar_pelicula(p1, p2, p3, p4, p5)

    elif opcion_elegida == "8":
        continuar_ejecutando = False

    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")

    return continuar_ejecutando

iniciar_aplicacion()