from typing import List
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Clase de servicio que gestiona productos y clientes del restaurante"""

    def __init__(self, nombre: str):
        self.nombre: str = nombre
        # Listas para almacenar objetos de cada modelo
        self.lista_productos: List[Producto] = []
        self.lista_clientes: List[Cliente] = []

    # Métodos para gestionar productos
    def agregar_producto(self, producto: Producto) -> None:
        """Agrega un nuevo producto a la lista"""
        self.lista_productos.append(producto)

    def mostrar_productos(self) -> None:
        """Muestra todos los productos registrados"""
        print("\n--- Menú de Productos ---")
        if not self.lista_productos:
            print("No hay productos registrados.")
            return
        for prod in self.lista_productos:
            print(prod)

    # Métodos para gestionar clientes
    def agregar_cliente(self, cliente: Cliente) -> None:
        """Agrega un nuevo cliente a la lista"""
        self.lista_clientes.append(cliente)

    def mostrar_clientes(self) -> None:
        """Muestra todos los clientes registrados"""
        print("\n--- Lista de Clientes ---")
        if not self.lista_clientes:
            print("No hay clientes registrados.")
            return
        for cli in self.lista_clientes:
            print(cli)