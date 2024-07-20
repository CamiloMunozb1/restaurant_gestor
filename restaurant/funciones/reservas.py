
# USO DEL MODULO "SQLITE3" PARA MANEJO DE LA BASE DE DATOS

import sqlite3


# USO DE UNA FUNCION PARA USARLA EN EL CODIGO PRINCIPAL

def gestor_reservas():

    # CONEXION A LA BASE DE DATOS

    with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as reservas_gestor:
        try:

            # USO DEL CURSOR PARA REALIZAR LAS CONSULTAS

            consulta_cursor = reservas_gestor.cursor()

            # INGRESO DE ENTRADAS DEL USUARIO PARA INDICAR LA INFORMACION DE LA RESERVA

            nombre_cliente = str(input("Ingrese el nombre del cliente: "))
            numero_mesa = int(input("Ingrese el numero de la mesa: "))
            fecha_reserva = str(input("Ingrese una fecha de reserva (DD/MM/YY): "))
            hora_reserva = str(input("Ingresa la hora de la reserva: "))
            
            # CONSULTA HACIA LA BASE DE DATOS PARA SELECCIONAR LA CLAVE FORANEA DE LA TABLA "GESTION_CLIENTE"

            consulta_cursor.execute("SELECT Cliente_ID FROM Gestion_cliente WHERE Nombre_cliente = ?", (nombre_cliente,))

            # USO DE "fetchone" PARA DEVOLVER UNA SOLA FILA DE RESULTADOS DE UNA CONSULTA SQL.

            cliente = consulta_cursor.fetchone()
            if cliente:

                # SE RASTREA EL ID DESDE EL COMIENZO DE LA TABLA

                cliente_id = cliente[0]

            else:

                # MENSAJE SI NO SE ENCUENTRA EL CLIENTE SE RETORNA

                print("Cliente no encontrado.")
                return
            

            # CONSULTA HACIA LA BASE DE DATOS PARA SELECCIONAR LA CLAVE FORANEA DE LA TABLA "GESTION_MESA"

            consulta_cursor.execute("SELECT Mesa_ID FROM Gestion_mesa WHERE Numero_mesa = ?", (numero_mesa,))

            #  USO DE "fetchone" PARA DEVOLVER UNA SOLA FILA DE RESULTADOS DE UNA CONSULTA SQL.
            mesa = consulta_cursor.fetchone()
            if mesa:

                # SE RESTREA EL ID DESDE EL COMIENZO DE LA TABLA 

                mesa_id = mesa[0]

            else:

                # MENSAJE SI NO SE ENCUENTRA LA MESA 
                print("Mesa no encontrada.")
                return
            

            #  INGRESO DE ENTRADAS DEL USUARIO Y LAS CLAVES FORANEAS PARA INDICAR LA INFORMACION HACIA "GESTION_RESERVAS"

            consulta_cursor.execute("INSERT INTO Gestion_reservas (Hora_reserva, Fecha_reserva,  Cliente_ID,  Mesa_ID) VALUES (?, ?, ?, ?)",(hora_reserva, fecha_reserva, cliente_id, mesa_id))

            # SUBIR LOS CAMBIOS A LA BASE DE DATOS

            reservas_gestor.commit()

            # MENSAJE DE EXITO

            print("Reserva gestionada con éxito.")
        

        # MANEJO DE ERRORES
        
        except ValueError:
            print("Error de digitación, vuélvalo a intentar.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")




