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

    def estaVacio(self):
        return self.head is None

    def agregarPrimero(self, data):
        """
        Inserta un nuevo nodo al inicio de la lista.
        Utilizado por la pila (Stack) para aplicar el comportamiento LIFO
        en el registro de solicitudes urgentes o cancelaciones.
        """
        new_node = Nodo(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            new_node.setNext(self.head)
            self.head = new_node
        self.size += 1

    def agregarUltimo(self, data):
        """
        Inserta un nuevo nodo al final de la lista.
        Utilizado por la cola (Queue) para aplicar el comportamiento FIFO
        en el registro de solicitudes normales.
        """
        new_node = Nodo(data)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.setNext(new_node)
            self.tail = new_node
        self.size += 1

    def eliminarPrimero(self):
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

    def eliminarPorAtributo(self, attr, value):
        """
        Elimina el primer nodo cuyo objeto interno tenga un atributo 'attr'
        igual al valor 'value'.

        Este método es fundamental para el sistema, ya que permite
        eliminar solicitudes específicas de la cola cuando un estudiante cancela
        su tutoría. La búsqueda por atributo (tipo 'estudiante') asegura que el
        sistema pueda ubicar y retirar dinámicamente una solicitud sin conocer su
        posición exacta, cumpliendo el requerimiento de incluir
        procedimientos de búsqueda y eliminación por valor de atributo :emoji con gafas:.
        """
        if self.isEmpty():
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