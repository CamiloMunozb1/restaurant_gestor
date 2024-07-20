
# USO DEL MODULO "SQLITE3" PARA MANEJO DE LA BASE DE DATOS

import sqlite3


# USO DE UNA FUNCION PARA USARLA EN EL CODIGO PRINCIPAL

def eliminar_mesa():

    # CONEXION A LA BASE DE DATOS

    with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as eliminacion_mesa:
        try:

            # USO DEL CURSOR PARA REALIZAR LAS CONSULTAS

            consulta_cursor = eliminacion_mesa.cursor()

            # INGRESO DE ENTRADA DEL USUARIO PARA INDICAR LA INFORMACION DE LA MESA A BORRAR

            mesa_eliminar = int(input("Ingrese el numero de la mesa: "))
            
            # CONSULTA HACIA LA BASE DE DATOS QUE ELIMINA LOS DATOS DE LA MESA

            consulta_cursor.execute("DELETE FROM Gestion_mesa WHERE Numero_mesa = ? ", (mesa_eliminar,))

            # SUBIDA DE CAMBIOS A LA BASE DE DATOS

            eliminacion_mesa.commit()

            # MENSAJE DE EXITO

            print("Mesa eliminada")
        
        # MANEJO DE ERRORES
        
        except ValueError:
            print("Error de digitacion, volver a intentarlo.")
        except sqlite3.Error as error:
            print(f"Error en la base: {error}")