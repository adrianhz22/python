print("=" * 35)
print("        GESTOR DE TAREAS")
print("=" * 35)

print("\nMENÚ:")
print("  [1] Ver tareas")
print("  [2] Añadir tarea")
print("  [3] Eliminar tarea")
print("=" * 35)

tareas = ["Tender la ropa", "Hacer la comida", "Pasear al perro"]

def mostrar_tareas(tareas):
    print("\nLISTA DE TAREAS")
    print("-" * 35)
    if not tareas:
        print("No hay tareas.")
    else:
        for i, tarea in enumerate(tareas, start=1):
            print(f" {i}. {tarea}")
    print("-" * 35)

def añadir_tarea(tareas):
    print("\nAÑADIR TAREA")
    print("-" * 35)
    tarea_nueva = input("Nueva tarea: ")
    tareas.append(tarea_nueva)
    print("\nTarea añadida correctamente.")
    mostrar_tareas(tareas)

def eliminar_tarea(tareas):
    print("\nELIMINAR TAREA")
    print("-" * 35)
    try:
        mostrar_tareas(tareas)
        tarea_eliminada = int(input("Número de tarea a eliminar: "))
        tareas.pop(tarea_eliminada - 1)
        print("\nTarea eliminada correctamente.")
        mostrar_tareas(tareas)
    except (ValueError, IndexError):
        print("\nOpción no válida.")

while True:
    try:
        opcion = int(input("\nSeleccione una opción: "))
        break
    except ValueError:
        print("Opción no válida, ingrese un número.")

if opcion == 1:
    mostrar_tareas(tareas)
elif opcion == 2:
    añadir_tarea(tareas)
elif opcion == 3:
    eliminar_tarea(tareas)
else:
    print("Opción incorrecta.")