import sqlite3

def gestion_clientes():
    try:
        with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as ingreso_cliente:
            consulta_cursor = ingreso_cliente.cursor()
            informacion_cliente = str(input("Ingrese el nombre del cliente: "))
            numero_telefono = int(input("ingrese el numero telefonico del cliente: "))
            correo_cliente = str(input("Ingrese el correo del cliente: "))
            consulta_cursor.execute("INSERT INTO Gestion_cliente (Nombre_cliente,Numero_cliente,Correo_cliente) VALUES (?,?,?)",(informacion_cliente,numero_telefono,correo_cliente))
            ingreso_cliente.commit()
            print("Informacion del cliente guardada.")
    except ValueError:
        print("Error de digitacion, intentar nuevamente")
    except sqlite3.Error as error:
        print(f"Error en la base de datos: {error}")

