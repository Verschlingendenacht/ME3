#pa las urgencias

from soporte.List import List
from soporte.Node import Node

class PilaSolicitudes:
    """
    Implementa una pila (LIFO) basada en una lista simple enlazada.
    Utilizada para manejar solicitudes urgentes dentro del sistema de tutorías.
    """
    def __init__(self):
        self.data = List()

    def size(self):
        return self.data.size

    def isEmpty(self):
        """
        Verifica si la pila está vacía.
        """
        return self.data.isEmpty()

    def push(self, data):
        """
        Inserta un nuevo elemento en la parte superior de la pila.
        Utiliza addFirst() de la lista para garantizar el comportamiento LIFO.
        """
        self.data.addFirst(data)

    def pop(self):
        """
        Elimina y retorna el elemento ubicado en la parte superior de la pila.
        Simula el procesamiento de la solicitud más reciente (LIFO).
        """
        if self.isEmpty():
            print("La pila está vacía.")
            return None
        return self.data.removeFirst()
    
    def top(self):
        if self.isEmpty():
            return None
        return self.data.first().getData()
        
    def eliminarPorAtributo(self, attr, value):
        """
        Elimina una solicitud de la pila cuyo atributo coincide con el valor especificado.
        """
        eliminado = self.data.eliminarPorAtributo(attr, value)
        if eliminado:
            print(f"Elemento con {attr} = '{value}' eliminado correctamente.")
        else:
            print(f"No se encontró elemento con {attr} = '{value}'.")
        return eliminado
    
    def mostrar(self):
        """
        Muestra todos los elementos de la pila utilizando
        el método showAll() de la clase List.
        """
        print("Contenido de la pila:")
        self.data.mostrar()




"""
    def removeFirst(self):
        if not self.isEmpty():
            temp = Node()
            temp = self.head
            self.head = temp.getNext()
            temp.setNext(None)
            self.size -= 1
        else:
            return None
        
    def removeLast(self):
        if self.size == 1:
            self.removeFirst
        elif self.size>1:
            temp = Node()
            temp = self.tail
            anterior = Node()
            anterior = self.head

            while(anterior.getNext()!=self.tail):
                anterior = anterior.getNext()
            anterior.setNext(None)
            self.tail = anterior
            self.size -= 1
            return temp.getData()
        else:
            return None

"""
