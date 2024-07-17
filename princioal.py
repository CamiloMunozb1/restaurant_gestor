from restaurant.funciones.mesas import gestor_mesa
from restaurant.funciones.eliminar_mesa import eliminar_mesa
from restaurant.funciones.clientes import gestion_clientes

while True:
    print("""
          Bienvenido al gestor de tu restaurante:
          1. Agregar una nueva mesa.
          2. Eliminar mesa
          3. Registro de clientes.
          4. Gestor de reservas. 
          5. Salir
          """)
    try:
        usuario = int(input("Ingrese una opcion: "))
        if usuario == 1:
            gestor_mesa()
        elif usuario == 2:
            eliminar_mesa()
        elif usuario == 3:
           gestion_clientes()
        elif usuario == 4:
            print("Proxima funcionalidad.")
        elif usuario == 5:
            print("Hasta luego, gracias por gestionar tus reservas.")
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")