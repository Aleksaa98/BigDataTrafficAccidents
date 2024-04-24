# Importing common modules to create a public interface
from .data_loading import load_data_from_mongo
from .processing import process_data
from .visualization import visualize_data

# Initialization message (for debugging purposes)
print("Package 'src' initialized")

import logging
logging.basicConfig(level=logging.INFO)