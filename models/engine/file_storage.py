import json
import os
"""
module that serializes instances to a JSON
file and deserializes JSON file to instances
"""


class FileStorage:
    """
    serializesinstance to json file
    deserealizes json file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        "returns the dict __objects"
        return self.__objects

    def new(self, obj):
        """
        creates a key for the __objects dictionary
        using the object's class name and id, and
        then adds the object to the dictionary
        using that key
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        # update the __object dictionary with values
        self.__objects[key] = obj

    def save(self):
        "serializes __objects to the JSON file"

        obj_dict = {
                    key: value.to_dict() for key,
                    value in self.__objects.items()
                    }
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        else it does none
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    mod_name = "models." + class_name
                    obj_class = eval(mod_name)[class_name]
                    self.__objects[key] = obj_class(**value)
