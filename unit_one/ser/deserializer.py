import pickle
import json
import yaml
from yaml.loader import SafeLoader

def from_pickle(pkl_file):
    with open(pkl_file, 'rb') as f1:
        obj1 = pickle.load(f1)
        return(obj1)
    print(obj1)
    f1.close()

# my_obj = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
my_file_1 = 'test_data/test-2.pickle'
from_pickle(my_file_1)

def from_json(json_file):
    with open(json_file, 'rt') as f2:
        obj2 = json.load(f2)
        return(obj2)
    print(obj2)
    f2.close()

#  my_obj = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
my_file_2 = 'test_data/test-2.json'
from_json(my_file_2)

def from_yaml(yaml_file):
    with open(yaml_file, 'rb') as f3:
        obj3 = yaml.load(f3, Loader = SafeLoader)
        return(obj3)
    print(obj3)
    f3.close()

#  my_obj = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
my_file_3 = 'test_data/test-2.yaml'
from_yaml(my_file_3)