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

from ColaSolicitudes import ColaSolicitudes
from PilaSolicitudes import PilaSolicitudes
from GestorTutorias import GestorTutorias
from Solicitud import Solicitud

def main():
    gestor = GestorTutorias()

    print("\n==== 1️⃣ PRUEBAS: cargar_desde_archivo ====")
    # ✅ Caso exitoso
    gestor.cargar_desde_archivo("src/recursos/entradas.csv")
    # ❌ Caso fallido
    gestor.cargar_desde_archivo("src/recursos/no_existe.csv")

    print("\n==== 2️⃣ PRUEBAS: registrar_solicitud ====")
    # ✅ Caso exitoso
    solicitud_ok = Solicitud("Laura Gómez", "Cálculo I", "2025-10-25", "normal", 2)
    gestor.registrar_solicitud(solicitud_ok)
    # ❌ Caso fallido (tipo inválido)
    solicitud_invalida = Solicitud("Carlos Ruiz", "Física II", "2025-10-25", "express", 1)
    try:
        gestor.registrar_solicitud(solicitud_invalida)
    except Exception as e:
        print("❌ Error detectado:", e)

    print("\n==== 3️⃣ PRUEBAS: procesar_solicitud ====")
    # ✅ Caso exitoso (debería atender 1 solicitud)
    gestor.procesar_solicitud()
    # ❌ Caso fallido (sin solicitudes)
    gestor.cola_normal = ColaSolicitudes()
    gestor.pila_urgente = PilaSolicitudes()
    gestor.procesar_solicitud()

    print("\n==== 4️⃣ PRUEBAS: buscar_solicitud ====")
    # ✅ Caso exitoso
    gestor.buscar_solicitud("Cálculo")
    # ❌ Caso fallido
    gestor.buscar_solicitud("NoExiste")

    print("\n==== 5️⃣ PRUEBAS: eliminar_solicitud ====")
    # ✅ Caso exitoso
    gestor.eliminar_solicitud("Laura Gómez")
    # ❌ Caso fallido
    gestor.eliminar_solicitud("NombreInventado")

    print("\n==== 6️⃣ PRUEBAS: ordenar_solicitudes ====")
    # ✅ Caso exitoso
    gestor.cargar_desde_archivo("src/recursos/entradas.csv")
    gestor.ordenar_solicitudes()
    # ❌ Caso fallido
    gestor.cola_normal = ColaSolicitudes()
    gestor.pila_urgente = PilaSolicitudes()
    gestor.ordenar_solicitudes()

    print("\n==== 7️⃣ PRUEBAS: guardar_resultados ====")
    # ✅ Caso exitoso
    gestor.guardar_resultados("src/recursos/atendidas.txt")
    # ❌ Caso fallido (no hay atendidas)
    gestor.atendidas = []
    gestor.guardar_resultados("src/recursos/vacio.txt")

if __name__ == "__main__":
    main()