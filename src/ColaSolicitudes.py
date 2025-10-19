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
        self.list.agregarUltimo(data)

    def dequeue(self):
        """
        Elimina y retorna el primer elemento de la cola.
        Simula la atención de la solicitud más antigua registrada,
        cumpliendo el principio FIFO.
        """
        return self.list.eliminarPrimero()

    def estaVacio(self):
        return self.list.estaVacio()
    
    def mostrar(self):
        """
        Muestra el contenido actual de la cola utilizando
        el método mostrar() de la clase Lista.
        """
        print("Contenido de la cola:")
        self.list.mostrar()


