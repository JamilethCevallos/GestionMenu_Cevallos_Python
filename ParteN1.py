# Diccionario que representa el menú del restaurante
# Cada clave es el nombre de un plato, y el valor es otro diccionario con precio e ingredientes
menu_restaurante = {
    'tigrillo': {
        'precio': 4.0,
        'ingredientes': ('verde', 'queso', 'leche', 'huevos', 'cebolla', 'sal', 'mantequilla')
    },
    'arroz moro': {
        'precio': 3.0,
        'ingredientes': ('arroz', 'lenteja', 'aceite', 'ajo', 'achiote', 'cebolla', 'mantequilla')
    },
    'corviche': {
        'precio': 1.0,
        'ingredientes': ('verde', 'corvina', 'maní molido', 'cebolla', 'achiote', 'cilantro', 'sal', 'aceite')
    },
    'encebollado': {
        'precio': 2.5,
        'ingredientes': ('pescado', 'yuca', 'cebolla colorada', 'tomate', 'limon', 'cilantro')
    },
    'guatita': {
        'precio': 3.5,
        'ingredientes': ('arroz', 'mondongo', 'cilantro', 'ajo machacado', 'cebolla blanca', 'maní')
    },
    'ceviche de camaron': {
        'precio': 7.0,
        'ingredientes': ('camaron', 'tomate', 'cebolla colorada', 'limon', 'cilantro')
    },
    'bolón mixto': {
        'precio': 5.5,
        'ingredientes': ('verde', 'chancho', 'queso', 'mantequilla', 'aceite', 'tocino', 'sal')
    }
}

# Definimos una función que recibe un menú y muestra sus platos con detalles
def mostrar_menu(menu):
    print("\nMENU DEL RESTAURANTE")  # Encabezado del menú
    
    # Recorremos todos los platos del menú
    for nom_plato, precio in menu.items():
        # Mostramos el nombre del plato, con la primera letra en mayúscula
        print(f"\nPlato: {nom_plato.title()}")
        
        # Mostramos el precio del plato
        print(f"Precio: ${precio['precio']}")
        
        # Mostramos los ingredientes del plato, separados por comas
        print(f"Ingredientes: {', '.join(precio['ingredientes'])}")

# Llamamos a la función para mostrar el menú al usuario
mostrar_menu(menu_restaurante)
