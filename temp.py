import logging
import sys

# Configure logger
logging.basicConfig(
    filename='app.log',  # Output file
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # Set the console log level
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)
logging.getLogger().addHandler(console_handler)

# Add exception handling to log uncaught exceptions
def log_uncaught_exceptions(exc_type, exc_value, exc_traceback):
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, exc_traceback)
        return
    logging.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))

# Redirect uncaught exceptions to the logger
sys.excepthook = log_uncaught_exceptions

# Example usage
logging.info("Application started.")

# assert 1 == 2

# x = None
# y = x + 10

print("ok-----")

# raise ValueError("An example error!")  # This will be logged

import time

x = None
y = 1 + x

print("Start")

for i in range(10):
    print(f'step {i}')
    time.sleep(10)  # Pause for 5 seconds

print("End")