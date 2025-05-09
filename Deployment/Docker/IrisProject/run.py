import importlib
import sys
import logging
from iris.utils.config import get_default

# Create a logger
logging.basicConfig(level=get_default('logger','level'),
                    format=get_default('logger','format'),
                    handlers=[logging.FileHandler(get_default('logger','filename')), logging.StreamHandler()])

logging.info('Beginning process {}'.format(sys.argv[1]))

module = importlib.import_module('iris.main.' + sys.argv[1])
main = getattr(module, 'main')
main()