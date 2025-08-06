from Task import Task
from Task import TaskNotFoundError
import pytest


def test_first_status():
    task1 = Task(1, "Example task", "TODO")
    task2 = Task(2, "Example task", "In progress")

    status1 = task1.status
    status2 = task2.status

    assert  status1 != "Completed" 
    assert  status2 != "Completed"

def test_validate_status_raise_value_error():
    task1 = Task(1, "Task1", "TODO")
    with pytest.raises(ValueError) as e_info:
        task1.status = "hi"
    assert str(e_info.value)

def test_validate_status():
    task1 = Task(1, "Task1", "old_status")
    task1.status = "TODO"

    assert task1.status == "TODO"