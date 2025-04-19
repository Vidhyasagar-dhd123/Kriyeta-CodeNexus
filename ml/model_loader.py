import pickle

def load_model(path):
    with open(path,"r") as file:
        model = pickle.load(file)
    return model
