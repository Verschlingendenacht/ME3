from ColaSolicitudes import ColaSolicitudes
from PilaSolicitudes import PilaSolicitudes
from Solicitud import Solicitud
from soporte.List import List
from soporte.Node import Node

class GestorTutorias:
    """
    Coordina las operaciones entre la cola y la pila, actuando como el
    controlador principal del sistema de gestión de tutorías.
    """

    def __init__(self):
        self.cola_normal = ColaSolicitudes()
        self.pila_urgente = PilaSolicitudes()
        self.atendidas = []  # Para registrar las solicitudes procesadas

    # ------------------------------------------------------------
    # 1. Cargar solicitudes desde archivo
    # ------------------------------------------------------------
    def cargar_desde_archivo(self, archivo):
        """
        Carga solicitudes desde un archivo CSV.
        
        Args:
            archivo (str): Ruta al archivo CSV con formato:
                estudiante,materia,fecha,tipo,prioridad
        """
        import csv
        with open(archivo, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                if len(row) == 5:
                    estudiante, materia, fecha, tipo, prioridad = row
                    try:
                        solicitud = Solicitud(estudiante, materia, fecha, tipo, int(prioridad))
                        self.registrar_solicitud(solicitud)
                    except ValueError as e:
                        print(f"Error al procesar fila: {row}")
                        print(f"Error: {e}")

    # ------------------------------------------------------------
    # 2. Registrar una solicitud (normal o urgente)
    # ------------------------------------------------------------
    def registrar_solicitud(self, solicitud):
        """
        Determina si la solicitud va a la cola o a la pila según su tipo.
        """
        if solicitud.tipo.lower() == "urgente":
            self.pila_urgente.push(solicitud)
        else:
            self.cola_normal.enqueue(solicitud)
        print(f"📥 Solicitud registrada: {solicitud}")

    # ------------------------------------------------------------
    # 3. Procesar una solicitud (atender)
    # ------------------------------------------------------------
    def procesar_solicitud(self):
        """
        Atiende una solicitud. Si hay urgentes, se atienden primero (pila).
        Si no hay urgentes, se atiende la primera solicitud normal (cola).
        """
        solicitud = None
        if not self.pila_urgente.isEmpty():
            solicitud = self.pila_urgente.pop()
            print(f"🚨 Se atendió solicitud urgente: {solicitud}")
        elif not self.cola_normal.isEmpty():
            solicitud = self.cola_normal.dequeue()
            print(f"🎓 Se atendió solicitud normal: {solicitud}")
        else:
            print("⛔ No hay solicitudes pendientes.")
            return None

        if solicitud:
            self.atendidas.append(solicitud)
        return solicitud

    # ------------------------------------------------------------
    # 4. Buscar solicitud por nombre o materia
    # ------------------------------------------------------------
    def buscar_solicitud(self, criterio):
        """
        Busca una solicitud por nombre o materia en ambas estructuras.
        """
        print(f"🔍 Buscando solicitudes que coincidan con '{criterio}'...")
        encontrados = []

        # Buscar en la cola
        actual = self.cola_normal.data.head
        while actual:
            s = actual.getData()
            if criterio.lower() in s.estudiante.lower() or criterio.lower() in s.materia.lower():
                encontrados.append(s)
            actual = actual.getNext()

        # Buscar en la pila
        actual = self.pila_urgente.data.head
        while actual:
            s = actual.getData()
            if criterio.lower() in s.estudiante.lower() or criterio.lower() in s.materia.lower():
                encontrados.append(s)
            actual = actual.getNext()

        if encontrados:
            print("✅ Resultados encontrados:")
            for s in encontrados:
                print("  ", s)
        else:
            print("⚠️ No se encontraron coincidencias.")
        return encontrados

    # ------------------------------------------------------------
    # 5. Eliminar solicitud por nombre
    # ------------------------------------------------------------
    def eliminar_solicitud(self, nombre):
        """
        Elimina una solicitud por nombre, ya sea normal o urgente.
        """
        eliminado = False
        eliminado |= self.cola_normal.data.eliminarPorAtributo("estudiante", nombre)
        eliminado |= self.pila_urgente.data.eliminarPorAtributo("estudiante", nombre)

        if eliminado:
            print(f"🗑️ Solicitud de '{nombre}' eliminada correctamente.")
        else:
            print(f"⚠️ No se encontró ninguna solicitud de '{nombre}'.")
        return eliminado

    # ------------------------------------------------------------
    # 6. Ordenar solicitudes
    # ------------------------------------------------------------
    def ordenar_solicitudes(self):
        """
        Ordena la cola por prioridad ascendente (1 = más urgente)
        y la pila por prioridad ascendente (1 = más urgente).
        """
        # --- Ordenar cola (menor prioridad = más urgente)
        if self.cola_normal.isEmpty():
            print("⚠️ No hay solicitudes normales para ordenar.")
        else:
            self._ordenar_lista_por_prioridad(self.cola_normal.data)
            print("📋 Cola ordenada por prioridad.")

        # --- Ordenar pila (también menor número = más urgente)
        if self.pila_urgente.isEmpty():
            print("⚠️ No hay solicitudes urgentes para ordenar.")
        else:
            self._ordenar_lista_por_prioridad(self.pila_urgente.data)
            print("🚨 Pila ordenada por prioridad.")

    def _ordenar_lista_por_prioridad(self, lista):
        """
        Método auxiliar de ordenamiento por inserción sobre una lista enlazada.
        """
        if lista.isEmpty() or lista.head.getNext() is None:
            return

        sorted_list = List()
        current = lista.head
        while current:
            data = current.getData()
            new_node = Node(data)

            # Inserción ordenada (prioridad menor primero)
            if sorted_list.isEmpty() or data.prioridad < sorted_list.head.getData().prioridad:
                new_node.setNext(sorted_list.head)
                sorted_list.head = new_node
                if sorted_list.tail is None:
                    sorted_list.tail = new_node
            else:
                temp = sorted_list.head
                while temp.getNext() and temp.getNext().getData().prioridad <= data.prioridad:
                    temp = temp.getNext()
                new_node.setNext(temp.getNext())
                temp.setNext(new_node)
                if new_node.getNext() is None:
                    sorted_list.tail = new_node
            sorted_list.size += 1
            current = current.getNext()

        lista.head = sorted_list.head
        lista.tail = sorted_list.tail
        lista.size = sorted_list.size

    # ------------------------------------------------------------
    # 7. Guardar resultados en archivo
    # ------------------------------------------------------------
    def guardar_resultados(self, ruta):
        """
        Genera un archivo de texto con las solicitudes atendidas.
        """
        with open(ruta, "w", encoding="utf-8") as file:
            for s in self.atendidas:
                file.write(f"{s.estudiante},{s.materia},{s.fecha},{s.tipo},{s.prioridad}\n")
        print(f"📝 Resultados guardados en '{ruta}'.")
