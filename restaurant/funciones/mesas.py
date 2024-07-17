import sqlite3

def gestor_mesa():
    with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db")as mesa_gestor:
        try:
            consulta_cursor = mesa_gestor.cursor()
            numero_mesa = int(input("Ingresa numero de la mesa: "))
            capacidad_mesa = str(input("Ingresa la capacidad de la mesa (baja-media-alta): "))
            ubicacion_mesa = str(input("Ingrese la ubicacion de la mesa (interior o exterior): "))
            consulta_cursor.execute("INSERT INTO Gestion_mesa (Numero_mesa, Capacidad, Ubicacion) VALUES (?,?,?)", (numero_mesa,capacidad_mesa,ubicacion_mesa))
            mesa_gestor.commit()
            print("Gestion de la mesa añadido correctamente.")
        except ValueError:
            print("Error de digitacion, intentar nuevamente.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos {error}")
