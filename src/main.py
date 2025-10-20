# =====================================================
# Proyecto: Sistema de Gestión de Solicitudes de Tutorías
# Curso: Estructuras de Datos 
#
# Autores: 
#   Julián Felipe Vélez Medina 
#   Luz Natalia Ríos Serna
#   Juan Pablo Salazar Ceballos
#   Nilzon Alejandro Gómez Maya
# =====================================================


from GestorTutorias import GestorTutorias
from Solicitud import Solicitud

def main():
    gestor = GestorTutorias()

    # 1️⃣ Cargar desde archivo CSV
    gestor.cargar_desde_archivo("src/recursos/entradas.csv")

    # 2️⃣ Registrar nuevas solicitudes manualmente
    gestor.registrar_solicitud(Solicitud("Laura Gómez", "Cálculo I", "2025-10-25", "normal", 2))
    gestor.registrar_solicitud(Solicitud("Carlos Ruiz", "Programación II", "2025-10-20", "urgente", 1))

    # 3️⃣ Mostrar estado actual
    print("\n=== COLA DE SOLICITUDES ===")
    gestor.cola_normal.mostrar()
    print("\n=== PILA DE URGENCIAS ===")
    gestor.pila_urgente.mostrar()

    # 4️⃣ Procesar solicitudes
    gestor.procesar_solicitud()
    gestor.procesar_solicitud()

    # 5️⃣ Buscar solicitudes
    gestor.buscar_solicitud("Cálculo")

    # 6️⃣ Eliminar una solicitud
    gestor.eliminar_solicitud("Laura Gómez")

    # 7️⃣ Ordenar estructuras
    gestor.ordenar_solicitudes()

    # 8️⃣ Guardar resultados
    gestor.guardar_resultados("src/recursos/atendidas.txt")

if __name__ == "__main__":
    main()
