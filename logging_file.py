import logging

# Configure logging to a file
logging.basicConfig(filename='my_log.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Log messages
logging.info('Logging to a file')
