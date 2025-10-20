from soporte.Node import Node

# ======== Lista.py ==========
class List:
    """
    Clase List.
    Implementa una lista enlazada simple que permite agregar, recorrer y eliminar nodos.
    Esta estructura sirve como base para construir las pilas y colas del sistema.
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, s):
        self._size = s

    def isEmpty(self):
        return self.head is None

    def first(self):
        return self.head
    
    def last(self):
        return self.tail

    def addFirst(self, data):
        """
        Inserta un nuevo nodo al inicio de la lista.
        Utilizado por la pila (Stack) para aplicar el comportamiento LIFO
        en el registro de solicitudes urgentes.
        """
        n = Node(data)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.setNext(self.head)
            self.head = n
        self._size += 1

    def addLast(self, data):
        """
        Inserta un nuevo nodo al final de la lista.
        Utilizado por la cola (Queue) para aplicar el comportamiento FIFO
        en el registro de solicitudes normales.
        """
        n = Node(data)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            self.tail.setNext(n)
            self.tail = n
        self._size += 1

    def removeFirst(self):
        """
        Elimina y retorna el primer nodo de la lista.
        Permite extraer elementos de pilas o colas respetando
        el orden correspondiente (LIFO o FIFO).
        """
        if self.isEmpty():
            raise Exception("Lista vacía")
        data = self.head.getData()
        self.head = self.head.getNext()
        self._size -= 1
        if self._size == 0:
            self.tail = None
        return data
    
    def removeLast(self):
        if self._size == 1:
            return self.removeFirst()
        elif self._size > 1:
            anterior = self.head
            while anterior.getNext() is not self.tail:
                anterior = anterior.getNext()
            temp = self.tail
            anterior.setNext(None)
            self.tail = anterior
            self._size -= 1
            return temp.getData()
        else:
            return None


    def eliminarPorAtributo(self, attr, value):
        """
        Elimina el primer nodo cuyo objeto interno tenga un atributo 'attr'
        igual al valor 'value'.

        Este método es fundamental para el sistema, ya que permite
        eliminar solicitudes específicas de la cola (por ejemplo, si el programa tuviese dicha extension, facilitar la cancelacion de tutorias).
        La búsqueda por atributo (tipo 'estudiante') asegura que el
        sistema pueda ubicar y retirar dinámicamente una solicitud sin conocer su
        posición exacta, cumpliendo el requerimiento de incluir
        procedimientos de búsqueda y eliminación por valor de atributo :emoji con gafas:.
        """
        if self.isEmpty():
            return False
        current = self.head
        prev = None
        while current is not None:
            if getattr(current.getData(), attr) == value:
                if prev is None:
                    self.head = current.getNext()
                else:
                    prev.setNext(current.getNext())
                if current == self.tail:
                    self.tail = prev
                self._size -= 1
                return True
            prev = current
            current = current.getNext()
        return False

    def mostrar(self):
        """Muestra todos los elementos de la lista sin usar estructuras nativas."""
        current = self.head
        if current is None:
            print(" (vacía)")
            return
        while current is not None:
            print(current.getData())
            current = current.getNext()