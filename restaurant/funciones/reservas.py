
import sqlite3

def gestor_reservas():
    with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as reservas_gestor:
        try:
            consulta_cursor = reservas_gestor.cursor()
            nombre_cliente = str(input("Ingrese el nombre del cliente: "))
            numero_mesa = int(input("Ingrese el numero de la mesa: "))
            fecha_reserva = str(input("Ingrese una fecha de reserva (DD/MM/YY): "))
            hora_reserva = str(input("Ingresa la hora de la reserva: "))
            
            # Obtener Cliente_ID
            consulta_cursor.execute("SELECT Cliente_ID FROM Gestion_cliente WHERE Nombre_cliente = ?", (nombre_cliente,))
            cliente = consulta_cursor.fetchone()
            if cliente:
                cliente_id = cliente[0]
            else:
                print("Cliente no encontrado.")
                return

            # Obtener Mesa_ID
            consulta_cursor.execute("SELECT Mesa_ID FROM Gestion_mesa WHERE Numero_mesa = ?", (numero_mesa,))
            mesa = consulta_cursor.fetchone()
            if mesa:
                mesa_id = mesa[0]
            else:
                print("Mesa no encontrada.")
                return

            # Insertar en Gestion_reservas
            consulta_cursor.execute("INSERT INTO Gestion_reservas (Hora_reserva, Fecha_reserva,  Cliente_ID,  Mesa_ID) VALUES (?, ?, ?, ?)",(hora_reserva, fecha_reserva, cliente_id, mesa_id))
            reservas_gestor.commit()
            print("Reserva gestionada con éxito.")
            
        except ValueError:
            print("Error de digitación, vuélvalo a intentar.")
        except sqlite3.Error as error:
            print(f"Error en la base de datos: {error}")




