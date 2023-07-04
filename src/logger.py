# any execution that happens we should be able to log all those information, execution in some flles
# so we can track in cse of some errors

import logging 
import os 
from datetime import datetime

# log file naming convention
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# os.get working directory
logs_path = os.path.join(os.getcwd() ,'logs', LOG_FILE)
os.makedirs(logs_path,exist_ok=True) 
# means that even if theres a folder, keep on appedning the files in it

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
filename= LOG_FILE_PATH,
format = "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s" , 
level = logging.INFO,

)
#logging.info('Logging has started')

# if __name__ == " __main__" :
#     logging.info('Logging has started')