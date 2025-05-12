import pickle
from iris.config import model_configs

def predict(input_data = model_configs.sample_input):
    """
    Predict the class of the input data using the trained model.

    Args:
        input_data (list): Input data for prediction.

    Returns:
        int: Predicted class.
    """
    # Load the model
    with open(model_configs.model_path, "rb") as f:
        model = pickle.load(f)

    # Make a prediction
    predictions = model.predict(input_data)
    return predictions[0]

if __name__ == "__main__":
    # Example usage
    input_data = [[5.1, 3.5, 1.4, 0.2]]  # Example input for prediction
    predicted_class = predict(input_data)
    print(f"Predicted class: {predicted_class}")
