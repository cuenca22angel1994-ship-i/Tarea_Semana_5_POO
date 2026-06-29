# Importar clases necesarias
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def main():
    # Crear instancia del restaurante
    mi_restaurante = Restaurante(nombre="Sazón Manaba")

    # Crear objetos de Producto
    producto1 = Producto(
        codigo="P001",
        nombre="Arroz Marinero",
        categoria="Plato Principal",
        precio=5.00,
        disponible=True
    )

    producto2 = Producto(
        codigo="B001",
        nombre="Jugo de Maracuyá",
        categoria="Bebida",
        precio=2.00,
        disponible=True
    )

    # Crear objetos de Cliente 
    cliente1 = Cliente(
        id_cliente="C001",
        nombre="Marixa López",
        telefono="0975654390",
        correo="marix@manaba.com"
    )

    cliente2 = Cliente(
        id_cliente="C002",
        nombre="Jhon Velez",
        telefono="0999433428"
    )

    # Agregar objetos a la gestión del restaurante
    mi_restaurante.agregar_producto(producto1)
    mi_restaurante.agregar_producto(producto2)
    mi_restaurante.agregar_cliente(cliente1)
    mi_restaurante.agregar_cliente(cliente2)

    # Mostrar toda la información registrada
    print(f"=== Sistema de Gestión: {mi_restaurante.nombre} ===")
    mi_restaurante.mostrar_productos()
    mi_restaurante.mostrar_clientes()


# Ejecutar solo si este archivo es el principal
if __name__ == "__main__":
    main()