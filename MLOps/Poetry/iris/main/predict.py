import pickle
from iris.config import model_configs
from iris.utils.setup_logger import setup_logger
import logging

# Set up logging
logger = logging.getLogger(__name__)
logger = setup_logger(logger)

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
    logger.info(f"Model loaded from {model_configs.model_path}")

    # Make a prediction
    predictions = model.predict(input_data)
    logger.info(f"Input data: {input_data}")
    logger.info(f"Predicted class: {predictions[0]}")

    return predictions[0]

if __name__ == "__main__":
    # Example usage
    input_data = [[5.1, 3.5, 1.4, 0.2]]  # Example input for prediction
    predicted_class = predict(input_data)
    print(f"Predicted class: {predicted_class}")
