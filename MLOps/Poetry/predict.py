import pickle


sample_input = [[5.1, 3.5, 1.4, 0.2]]  # Example input for prediction

# Load the model
with open("models/model.pkl", "rb") as f:
    model = pickle.load(f)

# Make a prediction
predictions = model.predict(sample_input)
print(f"Predicted class: {predictions[0]}")