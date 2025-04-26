import os
import logging
import sys

logging_string = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" 

log_dir = "run_logs"
log_path = os.path.join(log_dir, "running_log")
os.makedirs(log_dir,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=logging_string,

    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("classifiercnnlogger")