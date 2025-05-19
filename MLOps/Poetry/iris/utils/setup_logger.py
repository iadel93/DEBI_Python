import logging
import os

def setup_logger(logger):
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    if not logger.hasHandlers():
        os.makedirs("./logs", exist_ok=True)
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler("./logs/train_model.log")
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)
    return logger