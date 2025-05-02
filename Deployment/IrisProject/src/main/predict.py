from src.utils.model_utils import load_model
from src.utils.data_utils import parse_observation
from src.utils.config import get_default
import logging

logger = logging.getLogger(__name__)
VALUE = get_default('predict', 'value')

def main():
    gscv = load_model()

    new_obs = parse_observation(VALUE)

    prediction = gscv.predict(new_obs)
    logger.info('Predicted class: {}'.format(prediction[0]))


if __name__ == 'main':
    main()