from decimal import Decimal

from .logic import CalculadorImpuestos
from ..models import Orden


class OrdenBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._usuario = None
        self._items = []
        self._libro = None
        self._cantidad = 1
        self._direccion = ""

    def con_usuario(self, usuario):
        self._usuario = usuario
        return self

    def con_productos(self, productos):
        self._items = list(productos) if productos is not None else []
        # Compatibilidad con el modelo actual (Orden requiere un `libro`):
        # tomamos el primero como referencia del detalle.
        self._libro = self._items[0] if self._items else None
        self._cantidad = 1
        return self

    def con_libro(self, libro):
        self._libro = libro
        self._items = []
        return self

    def con_cantidad(self, cantidad):
        self._cantidad = cantidad
        return self

    def para_envio(self, direccion):
        self._direccion = direccion
        return self

    def build(self) -> Orden:
        if not self._items and not self._libro:
            raise ValueError("Datos insuficientes para crear la orden.")

        if self._items:
            subtotal = sum(Decimal(str(p.precio)) for p in self._items)
            total = Decimal(str(CalculadorImpuestos.obtener_total_con_iva(subtotal)))
        else:
            total_unitario = CalculadorImpuestos.obtener_total_con_iva(self._libro.precio)
            total = Decimal(str(total_unitario)) * self._cantidad

        orden = Orden.objects.create(
            usuario=self._usuario,
            libro=self._libro,
            total=total,
            direccion_envio=self._direccion,
        )
        self.reset()
        return orden
