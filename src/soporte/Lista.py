from src.soporte import Nodo

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
        self.size = 0

    def size(self):
        return self.size

    def isEmpty(self):
        return self.head is None
    
    def setSize(self, s):
        self.size == s

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
        n = Nodo(data)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.setNext(self.head)
            self.head = n
        self.size += 1

    def addLast(self, data):
        """
        Inserta un nuevo nodo al final de la lista.
        Utilizado por la cola (Queue) para aplicar el comportamiento FIFO
        en el registro de solicitudes normales.
        """
        n = Nodo(data)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            self.tail.setNext(n)
            self.tail = n
        self.size += 1

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
        self.size -= 1
        if self.size == 0:
            self.tail = None
        return data
    
    def removeLast(self):
        if self.size==1:
            self.removeFirst()
        elif self.size >1:
            temp = Nodo()
            temp = self.tail
            anterior = Nodo()
            anterior = self.head
            while(anterior.getNext()!=self.tail):
                anterior = anterior.getNext()
            anterior.setNext(None)
            self.tail = anterior
            self.size -= 1
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
        if self.estaVacio():
            return False
        current = self.head
        prev = None
        while current is not None:
            # Verifica si el atributo coincide (ej: solicitud.estudiante == "Julian Vélez")
            if getattr(current.getData(), attr) == value:
                if prev is None:
                    self.head = current.getNext()
                else:
                    prev.setNext(current.getNext())
                if current == self.tail:
                    self.tail = prev
                self.size -= 1
                return True
            prev = current
            current = current.getNext()
        return False

    def mostrar(self):
        """Muestra todos los elementos de la lista sin usar estructuras nativas."""
        current = self.head
        if current is None:
            print(" (vacía)")
        while current is not None:
            print(current.getData())
            current = current.getNext()