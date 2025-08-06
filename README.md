# python-basics
## TASK MANAGER GOALS
TaskManager class que permita:
1. Agregar tareas (add_task)
2. Marcar tareas como completadas (complete_task)
3. Eliminar tareas (delete_task)
4. Obtener una lista de tareas pendientes (get_pending_tasks)
5. Obtener una lista de tareas completadas (get_completed_tasks)

6. Agregar tareas con una prioridad (1=alta, 2=media, 3=baja) y obtener las tareas ordenadas por prioridad.
7. Palindromo (ignorando mayúsculas, espacios y signos de puntuación).
8. No es posible anadir dos tareas con el mismo id. 
9. Añade un atributo due_date (fecha límite) que debe ser un objeto datetime.date.
10. Editar descripcion de tarea con validacion. 
11. Agrega un método export_tasks() que escriba las tareas en un JSON.

# Requisitos adicionales:
1. Las tareas deben estar ordenadas por fecha de creación.
2. Si se intenta completar o eliminar una tarea que no existe, debe lanzar una excepción.
3. Las tareas deben mostrarse como diccionarios al obtenerlas.


# Conexion con RESTful API 
 - https://dummyjson.com/todos