from soporte.List import List

#========= ColaSolicitudes.py ==========
class ColaSolicitudes:
    """
    Clase Queue.
    Implementa una cola (FIFO) basada en una lista simple.
    Utilizada para gestionar solicitudes normales en orden de llegada.
    """
    def __init__(self):
        self.data = List()

    def size(self):
        return self.data.size
    
    def isEmpty(self):
        return self.data.isEmpty()

    def enqueue(self, data):
        """
        Inserta un elemento al final de la cola.
        Representa el ingreso de solicitudes normales en el orden en que
        los estudiantes las envían.
        """
        self.data.addLast(data)

    def dequeue(self):
        """
        Elimina y retorna el primer elemento de la cola.
        Simula la atención de la solicitud más antigua registrada,
        cumpliendo el principio FIFO.
        """
        return self.data.removeFirst()
    
    def mostrar(self):
        """
        Muestra el contenido actual de la cola utilizando
        el método mostrar() de la clase Lista.
        """
        print("Contenido de la cola:")
        self.data.mostrar()
