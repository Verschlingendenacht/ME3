#pa las urgencias

from src.soporte import Lista

class PilaSolicitudes:
    """
    Implementa una pila (LIFO) basada en una lista simple enlazada.
    Utilizada para manejar solicitudes urgentes dentro del sistema de tutorías.
    """
    def __init__(self):
        self.list = Lista()

    def estaVacio(self):
        """
        Verifica si la pila está vacía.
        """
        return self.list.estaVacio()

    def push(self, data):
        """
        Inserta un nuevo elemento en la parte superior de la pila.
        Utiliza addFirst() de la lista para garantizar el comportamiento LIFO.
        """
        self.list.agregarPrimero(data)

    def pop(self):
        """
        Elimina y retorna el elemento ubicado en la parte superior de la pila.
        Simula el procesamiento de la solicitud más reciente (LIFO).
        """
        if self.estaVacio():
            print("La pila está vacía.")
            return None
        return self.list.eliminarPrimero()

    def mostrar(self):
        """
        Muestra todos los elementos de la pila utilizando
        el método showAll() de la clase List.
        """
        print("Contenido de la pila:")
        self.list.mostrar()

    def eliminarPorAtributo(self, attr, value):
        """
        Elimina una solicitud de la pila cuyo atributo coincide con el valor especificado.
        """
        eliminado = self.list.eliminarPorAtributo(attr, value)
        if eliminado:
            print(f"Elemento con {attr} = '{value}' eliminado correctamente.")
        else:
            print(f"No se encontró elemento con {attr} = '{value}'.")
        return eliminado


#nos falta eliminar por nombre y ordenar por prioridad