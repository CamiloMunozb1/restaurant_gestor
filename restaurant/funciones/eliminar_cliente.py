import sqlite3

def eliminar_cliente():
    try:
        with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as cliente_eliminar:
            consulta_cursor = cliente_eliminar.cursor()
            eliminacion_cliente = str(input("Ingrese el nombre del cliente que desea eliminar: "))
            consulta_cursor.execute("DELETE FROM Gestion_cliente WHERE Nombre_cliente = ?", (eliminacion_cliente,))
            cliente_eliminar.commit()
            print("Eliminacion de cliente comoleta.")
    except ValueError:
        print("Error de digitacion, volver a registrar.")
    except sqlite3.Error as error:
        print(f"Error en la base datos: {error}")

