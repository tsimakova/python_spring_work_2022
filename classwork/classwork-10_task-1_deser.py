
import pickle

with open("test_data/test.pickle", "rb") as f:
    list_one = pickle.load(f)
    list_two = pickle.load(f)

print(list_one)
print(list_two)