
# USO DEL MODULO "SQLITE3" PARA MANEJO DE LA BASE DE DATOS

import sqlite3


# USO DE UNA FUNCION PARA USARLA EN EL CODIGO PRINCIPAL

def eliminar_cliente():
    try:

        # CONEXION A LA BASE DE DATOS

        with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as cliente_eliminar:

            # USO DEL CURSOR PARA REALIZAR LAS CONSULTAS

            consulta_cursor = cliente_eliminar.cursor()

            # INGRESO DE ENTRADA DEL USUARIO PARA INDICAR LA INFORMACION DEL CLIENTE A BORRAR

            eliminacion_cliente = str(input("Ingrese el nombre del cliente que desea eliminar: "))

            # CONSULTA HACIA LA BASE DE DATOS QUE ELIMINA LOS DATOS DEL CLIENTE

            consulta_cursor.execute("DELETE FROM Gestion_cliente WHERE Nombre_cliente = ?", (eliminacion_cliente,))

            # SUBIDA DE CAMBIOS A LA BASE DE DATOS

            cliente_eliminar.commit()

            # MENSAJE DE EXITO

            print("Eliminacion de cliente comoleta.")
    
    # MANEJO DE ERRORES
    
    except ValueError:
        print("Error de digitacion, volver a registrar.")
    except sqlite3.Error as error:
        print(f"Error en la base datos: {error}")

