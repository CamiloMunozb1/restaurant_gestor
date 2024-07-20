
# USO DEL MODULO "SQLITE3" PARA MANEJO DE LA BASE DE DATOS

import sqlite3


# USO DE UNA FUNCION PARA USARLA EN EL CODIGO PRINCIPAL

def gestor_mesa():

    # CONEXION A LA BASE DE DATOS

    with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db")as mesa_gestor:
        try:

            # USO DEL CURSOR PARA REALIZAR LAS CONSULTAS

            consulta_cursor = mesa_gestor.cursor()

            # INGRESO DE ENTRADAS DEL USUARIO PARA INDICAR LA INFORMACION DE LA MESA 

            numero_mesa = int(input("Ingresa numero de la mesa: "))
            capacidad_mesa = str(input("Ingresa la capacidad de la mesa (baja-media-alta): "))
            ubicacion_mesa = str(input("Ingrese la ubicacion de la mesa (interior o exterior): "))

            # CONSULTA HACIA LA BASE DE DATOS QUE INGRESA LOS DATOS DE LA MESA

            consulta_cursor.execute("INSERT INTO Gestion_mesa (Numero_mesa, Capacidad, Ubicacion) VALUES (?,?,?)", (numero_mesa,capacidad_mesa,ubicacion_mesa))

            # SE REALIZAN LOS CAMBIOS

            mesa_gestor.commit()

            # MENSAJE DE EXITO

            print("Gestion de la mesa añadido correctamente.")
        
        # MANEJO DE ERRORES

        except ValueError:
            print("Error de digitacion, intentar nuevamente.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos {error}")
