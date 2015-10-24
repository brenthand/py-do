#
#
#
import pickle

FN = "todo.dat"
LIST = []

class TODO:

    def __init__(self, name, task):
        self.name = name
        self.task = task

    def get_name():
        return self.name

    def get_task():
        return self.task

def open_list():
    with open(FN, "rb") as f:
        #LIST = pickle.load(f)
        return pickle.load(f)

def write_list(x):
    with open(FN, "wb") as f:
        pickle.dump(LIST, f)

print("adding item to list")
LIST.append( TODO("test", "task"))
LIST.append(TODO("test2", "task2"))

print("Pickling...")
write_list(LIST)

print("Getting pickled data")
LIST = open_list()

for item in LIST: 
    print(item.name)

#LIST.remove("test")

print("testing remove")

for item in LIST:
    if item.name == "test":
        LIST.remove(item)

for item in LIST: 
    print(item.name)
