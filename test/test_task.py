from Task import Task

class TestTask:
    def setup_method(self):
        self.task1 = Task(1, "Example task", "TODO")
        self.task2 = Task(1, "Example task", "In progress")
        self.task3 = Task(1, "Example task", "Task to do")
        print (self.task1.description)

    def test_first_status(self):
        assert self.task1.status != "Completed"
        assert self.task2.status != "Completed"
    
    def test_validate_status(self):
        assert self.task1.status in Task.ALLOWED_STATUSES
        assert self.task3.status not in self.task1.ALLOWED_STATUSES