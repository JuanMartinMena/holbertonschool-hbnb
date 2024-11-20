from abc import ABC, abstractmethod

# Clase abstracta Repository que define las operaciones CRUD y búsqueda
class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        """Agrega un objeto al repositorio"""
        pass

    @abstractmethod
    def get(self, obj_id):
        """Obtiene un objeto por su ID"""
        pass

    @abstractmethod
    def get_all(self):
        """Obtiene todos los objetos del repositorio"""
        pass

    @abstractmethod
    def update(self, obj_id, data):
        """Actualiza un objeto con el ID proporcionado"""
        pass

    @abstractmethod
    def delete(self, obj_id):
        """Elimina un objeto por su ID"""
        pass

    @abstractmethod
    def get_by_attribute(self, attr_name, attr_value):
        """Obtiene un objeto buscando por un atributo y su valor"""
        pass


# Implementación de Repository utilizando almacenamiento en memoria
class InMemoryRepository(Repository):
    def __init__(self):
        """Inicializa el repositorio en memoria con un diccionario"""
        self._storage = {}

    def add(self, obj):
        """Agrega un objeto al almacenamiento en memoria"""
        self._storage[obj.id] = obj

    def get(self, obj_id):
        """Obtiene un objeto por su ID del almacenamiento en memoria"""
        return self._storage.get(obj_id)

    def get_all(self):
        """Obtiene todos los objetos almacenados"""
        return list(self._storage.values())

    def update(self, obj_id, data):
        """Actualiza un objeto existente en el almacenamiento"""
        obj = self.get(obj_id)
        if obj:
            obj.update(data)

    def delete(self, obj_id):
        """Elimina un objeto del almacenamiento en memoria"""
        if obj_id in self._storage:
            del self._storage[obj_id]

    def get_by_attribute(self, attr_name, attr_value):
        """Busca un objeto por un atributo específico"""
        return next((obj for obj in self._storage.values() if getattr(obj, attr_name) == attr_value), None)
