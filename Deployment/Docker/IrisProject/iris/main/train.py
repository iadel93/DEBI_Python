from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import sys
sys.path.append('../..')
from iris.utils.data_utils import load_data, stratified_split
from iris.utils.model_utils import ClfSwitcher, format_params, save_model

import logging
from iris.utils.config import get_default

logger = logging.getLogger(__name__)

C = get_default('models', 'regression_C')
MAX_DEPTH = get_default('models', 'tree_max_depth')
MIN_SAMPLES_LEAF = get_default('models', 'tree_min_samples_leaf')
SCORING = get_default('design', 'scoring')
NUM_FOLDS = get_default('design', 'cv')
N_SAMPLES = get_default('design', 'n_samples')

def main():
    data_df = load_data()
    train_df, test_df = stratified_split(
        data=data_df, target='species', n_samples=N_SAMPLES)

    # compile the modelling pipeline for CV using sklearn
    steps = [('scaler', StandardScaler()), ('clf', ClfSwitcher())]
    pipeline = Pipeline(steps)
    parameters = [format_params(LogisticRegression(),
                                C=C),
                  format_params(DecisionTreeClassifier(),
                                max_depth=MAX_DEPTH,
                                min_samples_leaf=MIN_SAMPLES_LEAF),
                  format_params(LinearDiscriminantAnalysis())]

    gscv = GridSearchCV(pipeline, parameters, cv=NUM_FOLDS, scoring=SCORING)

    logger.info('Training model')
    gscv.fit(train_df.iloc[:, :4], train_df['species'])

    # print results
    logger.info('best model: {}'.format(gscv.best_estimator_))
    logger.info('best params: {}'.format(gscv.best_params_))
    logger.info('best score: {}'.format(gscv.best_score_))
    accuracy = gscv.score(
        test_df.iloc[:, :4], test_df['species'])
    logger.info('Test set accuracy: {}'.format(accuracy))

    save_model(gscv)


if __name__ == '__main__':
    main()
