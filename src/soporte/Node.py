# ========= Nodo.py ==========
class Node:
    """
    Clase Nodo.
    Representa una unidad básica de una lista enlazada simple.
    Contiene un dato (data) y una referencia al siguiente nodo (next).
    Utilizada por las estructuras List, PilaSolicitudes y ColaSolicitudes.
    """

    def __init__(self, data=None):
        """
        Constructor del nodo.
        Inicializa el dato almacenado y la referencia al siguiente nodo.
        """
        self.data = data
        self.next = None

    def getData(self):
        """
        Retorna el dato almacenado en el nodo.
        """
        return self.data

    def setData(self, data):
        """
        Actualiza el dato almacenado en el nodo.
        """
        self.data = data

    def getNext(self):
        """
        Retorna la referencia al siguiente nodo en la lista.
        """
        return self.next

    def setNext(self, next_node):
        """
        Asigna la referencia al siguiente nodo.
        """
        self.next = next_node

