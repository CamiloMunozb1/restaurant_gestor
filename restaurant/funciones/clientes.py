
# USO DEL MODULO "SQLITE3" PARA MANEJO DE LA BASE DE DATOS

import sqlite3


# USO DE UNA FUNCION PARA USARLA EN EL CODIGO PRINCIPAL

def gestion_clientes():
    try:

        # CONEXION A LA BASE DE DATOS

        with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as ingreso_cliente:

            # USO DEL CURSOR PARA REALIZAR LAS CONSULTAS

            consulta_cursor = ingreso_cliente.cursor()

            # INGRESO DE ENTRADAS DEL USUARIO PARA INDICAR LA INFORMACION DEL CLIENTE 

            informacion_cliente = str(input("Ingrese el nombre del cliente: "))
            numero_telefono = int(input("ingrese el numero telefonico del cliente: "))
            correo_cliente = str(input("Ingrese el correo del cliente: "))

            # CONSULTA HACIA LA BASE DE DATOS QUE INGRESA LOS DATOS DEL CLIENTE

            consulta_cursor.execute("INSERT INTO Gestion_cliente (Nombre_cliente,Numero_cliente,Correo_cliente) VALUES (?,?,?)",(informacion_cliente,numero_telefono,correo_cliente))

            # SUBIDA DE LOS CAMBIOS A LA BASE DE DATOS

            ingreso_cliente.commit()

            # MENSAJE DE EXITO

            print("Informacion del cliente guardada.")
    
    # MENSAJE DE ERROR
    
    except ValueError:
        print("Error de digitacion, intentar nuevamente")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")

