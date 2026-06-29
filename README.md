# Tarea_Semana_5_POO #
Aplicación de identificadores y tipos de datos en un proyecto Python modular
Alumno: Angel Rafael Cuenca Tamayo

*** Clases Principales ***

## `Producto`
Representa un plato, bebida o artículo disponible en el restaurante.
- **Atributos**: `codigo`, `nombre`, `categoria`, `precio`, `disponible`
- **Métodos**: `__init__`, `__str__`

## `Cliente`
Representa una persona registrada en el sistema.
- **Atributos**: `id_cliente`, `nombre`, `telefono`, `correo`, `activo`
- **Métodos**: `__init__`, `__str__`

## `Restaurante`
Clase de servicio que administra las listas de productos y clientes.
- **Atributos**: `nombre`, `lista_productos`, `lista_clientes`
- **Métodos**: `agregar_producto`, `mostrar_productos`, `agregar_cliente`, `mostrar_clientes`
---
***Características y Requisitos Cumplidos***
- ✅ Uso de convenciones de nombres: `PascalCase` para clases, `snake_case` para el resto
- ✅ Tipos de datos adecuados: `str`, `float`, `bool`
- ✅ Anotaciones de tipo para mayor claridad
- ✅ Uso de listas para almacenar múltiples objetos
- ✅ Método especial `__str__` para representar objetos como texto
- ✅ Importaciones correctas entre módulos
- ✅ Código comentado y organizado
- ✅ Estructura modular para facilitar futuras ampliaciones

