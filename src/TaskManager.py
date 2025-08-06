class TaskManager:

    def __init__ (self, tasks_lst):
        self.tasks = tasks_lst
  
    def add_task(self, task):
        self.tasks.append(task)
        return self.tasks

    def complete_task(self, task):
        for tarea in self.tasks:
            if task.id == tarea.id:
                tarea.status = "Completed"

    def remove_task():
        pass

    def get_pending_task():
        pass

    def get_completed_task():
        pass
