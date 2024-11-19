class Animal:
    species = "Unknown"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return(f'{self.name} издает звуки')

    def get_info(self):
        return f"Имя: {self.name}, Возраст:{self.age}, Вид:{self.species}"


def introspection_info(obj):
    obj_type = type(obj)

    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]

    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]

    obj_module = getattr(obj, "__module__", None)

    obj_doc = getattr(obj, "__doc__", "нет документации")
    obj_class = getattr(obj, "__class__", None)

    info = {
        "Type": obj_type,
        "Module": obj_module,
        "Attributes": attributes,
        "Methods": methods,
        "Docstring": obj_doc,
        "Class": obj_class
            }
    return info

number_info = introspection_info(42)
print(number_info)

dog = Animal(name="Трезор", age=3)

animal_info = introspection_info(dog)
print(animal_info)