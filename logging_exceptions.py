import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='output.log')

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.exception('Exception occurred')
