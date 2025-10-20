# ========= Solicitud.py ==========

class Solicitud:
    """
    Clase Solicitud.
    Representa una solicitud de tutoría académica registrada por un estudiante.
    Puede ser normal (almacenada en la cola) o urgente (almacenada en la pila).
    """

    def __init__(self, estudiante, materia, fecha, tipo="normal", prioridad=1):
        """
        Constructor de la solicitud.
        Parámetros:
            estudiante (str): nombre del estudiante que realiza la solicitud.
            materia (str): asignatura o tema para el cual se solicita tutoría.
            fecha (str): fecha o turno propuesto para la tutoría.
            tipo (str): tipo de solicitud ('normal' o 'urgente').
            prioridad (int): valor numérico que indica el nivel de urgencia (1=normal, 2=alta, etc.)
        """
        self.estudiante = estudiante
        self.materia = materia
        self.fecha = fecha
        self.tipo = tipo
        self.prioridad = prioridad

    def __str__(self):
        """
        Devuelve una representación legible de la solicitud.
        Permite que al imprimir la cola o la pila se muestre información significativa.
        """
        return f"[{self.tipo.upper()}] {self.estudiante} - {self.materia} - {self.fecha} (Prioridad: {self.prioridad})"
