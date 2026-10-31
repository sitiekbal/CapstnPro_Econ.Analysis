import pickle

with open("trend_model.pkl", "rb") as file:
    model = pickle.load(file)

print("Model loaded successfully!")

