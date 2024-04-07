
def empty():
    return Optional(None)


def of(value):
    return Optional(value)


class Optional:
    """Representa un valor que bien puede estar presente, o no estar, y que se puedan
    realizar operaciones sobre este sin tener que estar llenando el código de ifs."""

    def __init__(self, value):
        """Crea el Optional con el valor asociado. No debería ser usado. Usar las funciones of y empty"""
        self.value = value

    def is_present(self):
        """Determina si el valor está presente, o no"""
        return self.value is not None

    def is_empty(self):
        """Determina si el Optional está vacío (empty)"""
        return self.value is None

    def get(self):
        """Obtiene el valor del Optional, si está presente. Sino, lanza una ValueError."""
        if self.is_empty():
            raise ValueError("Optional is empty")
        return self.value

    def map(self, mapfn):
        """Crea un nuevo Optional con el valor de haber aplicar la mapfn al valor de este optional.
        Si el Optional está vacío, simplemente devuelve un Optional Vacío."""
        if self.is_empty():
            return empty()
        return of(mapfn(self.value))

    def flatmap(self, mapfn):
        """Similar a map, pero pensado para el caso que la mapfn devuelve un Optional. Si se usara map en ese caso,
        se tendría como resultado un Optional de un Optional, lo cual puede ser muy molesto para trabajar. En este
        caso, si el Optional tiene valor, se devuelve directamente el resultado de aplicar la mapfn, teniendo
        directamente ese Optional."""
        if self.is_empty():
            return empty()
        return mapfn(self.value)

    def or_else(self, default_value):
        """Devuelve el valor de este optional si es que hay, y sino devuelve el valor default."""
        return self.value if self.is_present() else default_value

    def if_present(self, applyfn):
        """Si el valor se encuentra presente, aplica la función sobre el valor. Si el Optional está vacio, no se
        hace nada"""
        if self.is_present():
            applyfn(self.value)

    def __repr__(self):
        if self.is_empty():
            return "Empty"
        else:
            return "Optional[" + repr(self.value) + "]"
