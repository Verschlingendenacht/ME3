from src.soporte import Lista

#========= ColaSolicitudes.py ==========
class ColaSolicitudes:
    """
    Clase Queue.
    Implementa una cola (FIFO) basada en una lista simple.
    Utilizada para gestionar solicitudes normales en orden de llegada.
    """
    def __init__(self):
        self.list = Lista()

    def enqueue(self, data):
        """
        Inserta un elemento al final de la cola.
        Representa el ingreso de solicitudes normales en el orden en que
        los estudiantes las envían.
        """
        self.list.addLast(data)

    def dequeue(self):
        """
        Elimina y retorna el primer elemento de la cola.
        Simula la atención de la solicitud más antigua registrada,
        cumpliendo el principio FIFO.
        """
        return self.list.removeFirst()

    def estaVacio(self):
        return self.list.isEmpty()
    
    def mostrar(self):
        """
        Muestra el contenido actual de la cola utilizando
        el método showAll() de la clase Lista.
        """
        print("Contenido de la cola:")
        self.list.showAll()


