from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from iris.config import model_configs
import pickle
import os
import logging

# Set up logging
os.makedirs("./logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
file_handler = logging.FileHandler("./logs/train_model.log")
stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

def run():
    """Main function to train the model."""
    # Load the Iris dataset
    data = load_iris()
    X = data.data
    y = data.target
    logger.info(f"Loaded dataset with {X.shape[0]} samples and {X.shape[1]} features.")
    logger.info(f"Feature names: {data.feature_names}")

    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=model_configs.test_size, random_state=model_configs.random_state)

    # Create and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=model_configs.random_state)
    logger.info("Training the model...")

    model.fit(X_train, y_train)
    logger.info("Model training completed.")

    # Evaluate the model
    accuracy = model.score(X_test, y_test)
    logger.info(f"Model accuracy: {accuracy:.2f}")

    # Save the trained model
    os.makedirs(os.path.dirname(model_configs.model_path), exist_ok=True)
    with open(model_configs.model_path, "wb") as f:
        pickle.dump(model, f)
    logger.info(f"Model saved to {model_configs.model_path}")


if __name__ == "__main__":
    run()

