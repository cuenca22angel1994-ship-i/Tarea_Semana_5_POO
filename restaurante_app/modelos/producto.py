class Producto:
    """Clase que representa un producto disponible en el restaurante"""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Atributos con tipos de datos adecuados
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria  # Ej: Plato principal, Bebida, Postre
        self.precio: float = precio
        self.disponible: bool = disponible

    def __str__(self) -> str:
        """Representación en texto del producto"""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"[{self.codigo}] {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | {estado}"