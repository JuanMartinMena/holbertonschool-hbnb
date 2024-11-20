from abc import ABC, abstractmethod
from datetime import datetime

# Excepciones personalizadas
class EntityNotFoundError(Exception):
    pass

class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        pass


class InMemoryRepository(Repository):
    def __init__(self):
        self._storage = {}

    def add(self, obj):
        self._storage[obj.id] = obj

    def get(self, obj_id):
        return self._storage.get(obj_id)

    def get_all(self):
        return list(self._storage.values())

    def update(self, obj):
        if obj.id in self._storage:
            self._storage[obj.id] = obj
        else:
            raise EntityNotFoundError(f"Object with ID {obj.id} not found")

    def delete(self, obj_id):
        if obj_id in self._storage:
            del self._storage[obj_id]
        else:
            raise EntityNotFoundError(f"Object with ID {obj_id} not found")

    def get_by_attribute(self, attr_name, attr_value):
        return next(
            (obj for obj in self._storage.values() if getattr(obj, attr_name, None) == attr_value),
            None
        )
