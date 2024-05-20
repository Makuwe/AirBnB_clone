#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def _init_(self):
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        self.updated_at = datetime.utcnow()
        
    def to_dict(self):
        
        inst_dict = self._dict_.copy()
        inst_dict["_class"] = self.class.name_
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        
        return inst_dict
    
    def _str_(self):
        
        class_name = self._class.name_
        return "[{}] ({}) {}".format(class_name, self.id, self._dict_)

if _name_ == "_main_":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 24
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model-json)
    print("JSON of my model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]).(my_model_json[key])

            print('--')
            my_new_model = Basemodel(**my_model_json)
            print(my_new_model.id)
            print(my_new_model)
            print(type(my_new_model.created_at))

            print("--")
            print(my_model is my_new_model)


                                                                                                                                   15,0-1        Top
