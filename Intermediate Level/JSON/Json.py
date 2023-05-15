#######################################################
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSO
person_json2 = json.dumps(person, indent=4, sort_keys=True)
print(person_json2) 

with open('person.json', 'w') as f:
    json.dump(person, f, indent=4) # you can also specify indent etc...


#Encoding

def encode_complex(z):
    if isinstance(z, complex):
        # just the key of the class name is important, the value can be arbitrary.
        return {z.__class__.__name__: True, "real":z.real, "imag":z.imag}
    else:
        raise TypeError(f"Object of type '{z.__class__.__name__}' is not JSON serializable")

z = 5 + 9j
zJSON = json.dumps(z, default=encode_complex)
print(zJSON)

from json import JSONEncoder
class ComplexEncoder(JSONEncoder):
    
    def default(self, o):
        if isinstance(z, complex):
            return {z.__class__.__name__: True, "real":z.real, "imag":z.imag}
        # Let the base class default method handle other objects or raise a TypeError
        return JSONEncoder.default(self, o)
    
z = 5 + 9j
zJson = ComplexEncoder().encode(z)
print(zJSON)

##########################################
# Decoding

# Possible but decoded as a dictionary
z = json.loads(zJSON)
print(type(z))
print(z)

def decode_complex(dct):
    if complex.__name__ in dct:
        return complex(dct["real"], dct["imag"])
    return dct

# Now the object is of type complex after decoding
z = json.loads(zJSON, object_hook=decode_complex)
print(type(z))
print(z)

##########################################

class User:
    # Custom class with all instance variables given in the __init__()
    def __init__(self, name, age, active, balance, friends):
        self.name = name
        self.age = age
        self.active = active
        self.balance = balance
        self.friends = friends
        
class Player:
    # Other custom class
    def __init__(self, name, nickname, level):
        self.name = name
        self.nickname = nickname
        self.level = level
          
            
def encode_obj(obj):
    """
    Takes in a custom object and returns a dictionary representation of the object.
    This dict representation also includes the object's module and class names.
    """
  
    #  Populate the dictionary with object meta data 
    obj_dict = {
      "__class__": obj.__class__.__name__,
      "__module__": obj.__module__
    }
  
    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)
  
    return obj_dict


def decode_dct(dct):
    """
    Takes in a dict and returns a custom object associated with the dict.
    It makes use of the "__module__" and "__class__" metadata in the dictionary
    to know which object type to create.
    """
    if "__class__" in dct:
        # Pop ensures we remove metadata from the dict to leave only the instance arguments
        class_name = dct.pop("__class__")
        
        # Get the module name from the dict and import it
        module_name = dct.pop("__module__")
        
        # We use the built in __import__ function since the module name is not yet known at runtime
        module = __import__(module_name)
        
        # Get the class from the module
        class_ = getattr(module,class_name)

        # Use dictionary unpacking to initialize the object
        # Note: This only works if all __init__() arguments of the class are exactly the dict keys
        obj = class_(**dct)
    else:
        obj = dct
    return obj

# User class works with our encoding and decoding methods
user = User(name = "John",age = 28, friends = ["Jane", "Tom"], balance = 20.70, active = True)

userJSON = json.dumps(user,default=encode_obj,indent=4, sort_keys=True)
print(userJSON)

user_decoded = json.loads(userJSON, object_hook=decode_dct)
print(type(user_decoded))

# Player class also works with our custom encoding and decoding
player = Player('Max', 'max1234', 5)
playerJSON = json.dumps(player,default=encode_obj,indent=4, sort_keys=True)
print(playerJSON)

player_decoded = json.loads(playerJSON, object_hook=decode_dct)
print(type(player_decoded))