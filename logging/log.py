import logging
from datetime import datetime
import os, sys

LOG_DIR = 'mushroom_log'
current_time_stamp = f'{datetime.now().strftime(%d-%m-%Y_%H%M%S)}'
log_file_name = f'log_{current_time_stamp}.log'
os.makedirs(LOG_DIR, exist_ok= True)
log_file_path = os.path.join(LOG_DIR, log_file_name)

logging.basicConfig(
    filename=log_file_path, 
    filemode='w',
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s ",
    level=logging.INFO)