import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception('Exception occurred')
