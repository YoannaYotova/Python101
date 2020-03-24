import json
import xml.etree.ElementTree as ET 

class WithSetAttributes:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)

class WithEqualDictionary:
    def dictionary_with_attributes(self):
        lst = list(self.__dict__.keys())

        dictionary = {}

        for attr in lst:
            if isinstance(self.__dict__[attr], (str, int, list, tuple, dict,float)):
                dictionary[attr] = self.__dict__[attr]

            else:
                new_name = self.__dict__[attr].__class__.__name__

                dictionary[attr] = {'type': new_name,'dict': self.__dict__[attr].__dict__}

        return dictionary

class WithEqualAttributes(WithEqualDictionary):
    def __eq__(self, other):
        lst1 = list(self.__dict__.keys())
        lst2 = list(other.__dict__.keys())

        dictionary1 =self.dictionary_with_attributes()
        dictionary2 =other.dictionary_with_attributes()

        return dictionary1 == dictionary2



class Jsonable(WithEqualDictionary):
    def to_json(self, indent=4):
        name = self.__class__.__name__
        
        dictionary = self.dictionary_with_attributes()

        return json.dumps({'type': name, 'dict': dictionary}, indent = indent)

    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)

        class_name = data['type']

        if class_name != cls.__name__:
            raise ValueError('Wrong type.')

        attributes = data['dict']

        return cls(**attributes)


class Xmlable:
    def to_xml(self):
        


