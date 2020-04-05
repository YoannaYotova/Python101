import json
import xml.etree.ElementTree as ET


class WithSetAttributes:
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)


class WithEqualAttributes:
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class Jsonable:
    def to_json(self, indent=4):
        name = self.__class__.__name__

        dictionary = self.__dict__

        for key, value in dictionary.items():
            if not isinstance(value, (str, int, float, list, tuple, dict)):

                if Jsonable in type(value).mro():
                    new_name = value.__class__.__name__

                    dictionary[key] = {'type': new_name, 'dict': value.__dict__}
            elif isinstance(value, list):

                for i in range(len(value)):

                    if not isinstance(value[i], (str, int, float, list, tuple, dict)):

                        if Jsonable in type(value[i]).mro():
                            new_name = value[i].__class__.__name__

                            value[i] = {'type': new_name, 'dict': value[i].__dict__}
            elif isinstance(value, dict):

                for k, v in value.items():
                    if not isinstance(v, (str, int, float, list, tuple, dict)):

                        if Jsonable in type(v).mro():
                            new_name2 = v.__class__.__name__

                            value[k] = {'type': new_name2, 'dict': v.__dict__}

        return json.dumps({'type': name, 'dict': dictionary}, indent=indent)

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
        parts = ['<{}>'.format(self.__class__.__name__)]
        for name, value in self.__dict__.items():
            if not isinstance(value, (str, int, tuple, list, dict, float)):
                parts.append(value.to_xml())
            else:
                parts.append('<{0}>{1}</{0}>'.format(name, value))

        parts.append('</{}>'.format(self.__class__.__name__))

        return ''.join(parts)

    @classmethod
    def from_xml(cls, xml_string):
        root = ET.fromstring(xml_string)

        if root.tag != cls.__name__:
            raise ValueError('Wrong type')
