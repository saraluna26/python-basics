class TaskNotFoundError(Exception):
    pass

class Task:
    ALLOWED_STATUSES = ["TODO", "In progress", "Completed"]

    def __init__ (self, id, description, status):
        self.id = id
        self._description = description  
        self._status = status

    def tasks_to_dicc(self):
        return { 
            'id': self.id,
            'description': self._description,
            'status': self._status
        }

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if not isinstance(description, str) or len(description) < 3:
            raise ValueError ("La descripción debe tener al menos 3 caracteres y una cadena. Enteros no son validos")


    @property
    def status(self):
        return self._status
    
    @status.setter
    def status (self, status):
        if not isinstance(status, str) or status not in self.ALLOWED_STATUSES:
            raise ValueError ("Status only can be: TODO, In progress and Completed")