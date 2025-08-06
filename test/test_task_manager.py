from TaskManager import TaskManager
from Task import Task

class TestTaskManager:
    def setup_method(self):
        tasks_lst = []
        self.taskmanager = TaskManager(tasks_lst)

    def test_add_task(self):
        task1 = Task(1, "Task1Des", "TODO")
        input_list_tasks = []
        input_len = len(input_list_tasks) + 1

        output_list_task = self.taskmanager.add_task(task1)

        assert input_len  == len(output_list_task)

    def test_complete_task(self):
        task1 = Task(1, "Task1Des", "TODO")
        self.taskmanager.add_task(task1)

        self.taskmanager.complete_task(task1)

        assert task1.status == "Completed"

    def test_remove_task(self):
        pass



    

