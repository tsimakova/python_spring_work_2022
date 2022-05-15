import pickle
import json
import yaml

def to_pickle(obj, pkl_file):
    with open(pkl_file, 'wb') as f1:
        pickle.dump(obj, f1)
    f1.close()

my_obj = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
my_file = 'test_data/test-2.pickle'
to_pickle(my_obj, my_file)

def to_json(obj, json_file):
    with open(json_file, 'wt') as f2:
        json.dump(obj, f2, indent = 4)
    f2.close()

my_obj = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
my_file = 'test_data/test-2.json'
to_json(my_obj, my_file)


def to_yaml(obj, yaml_file):
    with open(yaml_file, 'wt') as f3:
        yaml.dump(obj, f3)
    f3.close()


my_obj = [True, 'If the implementation is hard to explain, it\'s a bad idea.', {'age': 27}]
my_file = 'test_data/test-2.yaml'
to_yaml(my_obj, my_file)