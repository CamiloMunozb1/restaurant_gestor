
# USO DE ARQUITECTURA EN CAPAS PARA EL USO DE LAS FUNCIONALIDADES

from restaurant.funciones.mesas import gestor_mesa
from restaurant.funciones.eliminar_mesa import eliminar_mesa
from restaurant.funciones.clientes import gestion_clientes
from restaurant.funciones.eliminar_cliente import eliminar_cliente
from restaurant.funciones.reservas import gestor_reservas


while True:

    # MENU PARA EL USUARIO

    print("""
          Bienvenido al gestor de tu restaurante:
          1. Agregar una nueva mesa.
          2. Eliminar mesa
          3. Registro de clientes.
          4. Eliminar cliente.
          5. Gestor de reservas. 
          6. Salir
          """)
    try:

        # INGRESO DEL USUARIO

        usuario = int(input("Ingrese una opcion: "))

        # OPCIONES PARA EL USUARIO

        if usuario == 1:
            gestor_mesa()
        elif usuario == 2:
            eliminar_mesa()
        elif usuario == 3:
           gestion_clientes()
        elif usuario == 4:
            eliminar_cliente()
        elif usuario == 5:
            gestor_reservas()
        
        # SALIDA DEL PROGRAMA

        elif usuario == 6:
            print("Hasta luego, gracias por gestionar tus reservas.")
            break
    
    # MANEJO DE ERRORES
    
    except ValueError:
        print("Error de digitacion, vuelve a intentar.")