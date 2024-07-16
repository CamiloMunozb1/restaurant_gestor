from restaurant.funciones.mesas import gestor_mesa

while True:
    print("""
          Bienvenido al gestor de tu restaurante:
          1. Agregar una nueva mesa.
          2. Registro de clientes.
          3. Gestor de reservas. 
          4. Salir
          """)
    try:
        usuario = int(input("Ingrese una opcion: "))
        if usuario == 1:
            gestor_mesa()
        elif usuario == 2:
            print("Proxima funcionalidad.")
        elif usuario == 3:
            print("Proxima funcionalidad.")
        elif usuario == 4:
            print("Hasta luego, gracias por gestionar tus reservas.")
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")