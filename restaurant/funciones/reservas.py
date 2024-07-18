import sqlite3

def gestor_reservas():
    with sqlite3.connect("C:/Users/POWER/gestor_restaurante.db") as reservas_gestor:
        consulta_cursor = reservas_gestor.cursor()
        fecha_reserva = str(input("Ingrese una fehca de reserva (DD/MM/YY): "))
        hora_reserva = str(input("Ingresa la hora de la reserva: "))
        