class TaskNotFoundError(Exception):
    pass

class Task:
    def __init__ (self, id, description, status):
        self.id = id
        self.description = description  
        self.status = status

    def tasks_to_dicc(self):
        return { 
            "id" = self.id 
            description = "self.description"
            status = "self.status"
        }

    @proprety
    def description(self):
        return self.description
    
    @description.setter
    def description(self, description):
        if not isinstance(description, str) or len(description) < 3:
            raise ValueError ("La descripción debe tener al menos 3 caracteres y una cadena. Enteros no son validos")