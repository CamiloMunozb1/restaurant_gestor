import sqlite3

def eliminar_mesa():
    with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as eliminacion_mesa:
        try:
            consulta_cursor = eliminacion_mesa.cursor()
            mesa_eliminar = int(input("Ingrese el numero de la mesa: "))
            consulta_cursor.execute("DELETE FROM Gestion_mesa WHERE Numero_mesa = ? ", (mesa_eliminar,))
            eliminacion_mesa.commit()
            print("Mesa eliminada")
        except ValueError:
            print("Error de digitacion, volver a intentarlo.")
        except sqlite3.Error as error:
            print(f"Error en la base: {error}")