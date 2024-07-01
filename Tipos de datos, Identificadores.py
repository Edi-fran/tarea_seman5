class ListaDeTareas:
    def __init__(self):
        """
        Constructor para la clase ListaDeTareas.
        Inicializa una lista vacía para almacenar las tareas.
        """
        self.tareas = []

    def agregar_tarea(self, tarea, prioridad, tiempo_estimado):
        """
        Método para agregar una nueva tarea a la lista.
        :param tarea: Descripción de la tarea (str)
        :param prioridad: Prioridad de la tarea (int)
        :param tiempo_estimado: Tiempo estimado para completar la tarea (float)
        """
        # Validación de los tipos de datos
        if isinstance(prioridad, int) and isinstance(tiempo_estimado, float) and isinstance(tarea, str):
            self.tareas.append({'tarea': tarea, 'prioridad': prioridad, 'tiempo': tiempo_estimado})
            print("Tarea agregada exitosamente.")
        else:
            print("Error: Tipos de datos incorrectos.")

    def ver_tareas(self):
        """
        Método para imprimir todas las tareas en la lista con sus detalles.
        """
        if not self.tareas:
            print("No hay tareas pendientes.")
        else:
            print("Tareas pendientes:")
            for item in self.tareas:
                print(f"- {item['tarea']} (Prioridad: {item['prioridad']}, Tiempo Est.: {item['tiempo']} horas)")

# Creación de una instancia de ListaDeTareas
lista_de_tareas = ListaDeTareas()

# Interfaz de usuario en la consola
while True:
    accion = input("¿Quieres agregar una tarea o ver las tareas? (agregar/ver/salir): ")
    if accion.lower() == "agregar":
        tarea = input("Ingresa la nueva tarea: ")
        prioridad = int(input("Ingresa la prioridad de la tarea (1-5, donde 5 es máxima prioridad): "))
        tiempo_estimado = float(input("Ingresa el tiempo estimado para completar la tarea (en horas): "))
        lista_de_tareas.agregar_tarea(tarea, prioridad, tiempo_estimado)
    elif accion.lower() == "ver":
        lista_de_tareas.ver_tareas()
    elif accion.lower() == "salir":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no reconocida. Por favor, elige 'agregar', 'ver' o 'salir'.")

