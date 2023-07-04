# all the code related to reading the data from any source like from cloud, big data team etc, very important file 
# next step will data transformation

import os 
import sys 
#from pathlib import Path
#sys.path.append(str(Path(__file__).parent.parent))

from src.exception import CustomException # we made this custom exception in the exception file 
from src.logger import logging 

import pandas as pd 
from sklearn.model_selection import train_test_split 
from dataclasses import dataclass 

# we make a decorator, inside a class to define the class we use init, but if we use this dataclass we'd be able ot directly define our class variable

@dataclass
class DataIngestionConfig : #in the DI component, any i/p that is req we'll give through this component
    train_data_path : str= os.path.join('artifact','train.csv') # the DI component will save the files in this path, the o/p will be saved in this folder
    test_data_path : str= os.path.join('artifact','test.csv')
    raw_data_path : str= os.path.join('artifact','data.csv')

    # this is the input that we're giving and later on the data ingestion will save the train.csv in this path
    # these 3 are the inputs given to the data ingestion component

class DataIngestion :
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # as soon as we execute this, the 3 values from dataingetionconfig will be used here in thi class as input

    def initiate_data_ingestion(self) : # if the data is stored in some databases, the we write the code to read the data, we can create a mongodb client or myql client in utils function
        logging.info('Entered the data ingestion method or component')
        try :
            df = pd.read_csv('notebook\Data\StudentsPerformance.csv') # read the data, can change it according to the source of the data like sql, mongoDB etc
            logging.info('Read the dataset as dataframe') # create a log so it's easy to understand where the error is

            # we know the path or training data (artifacts folder writen above), so now we actually create thoe folders 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok= True) # we combine the directory path name so we use os.path.dirname

            df.to_csv(self.ingestion_config.train_data_path, index = False, header = True)
            logging.info('Train test split initiated')

            train_set, test_set = train_test_split(df, test_size=  0.2, random_state=42 )

            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header = True) 
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header = True) 
            logging.info('Ingestion of the data is completed')
            # here we've done the split we just save the data in the respective files

            return(
                    self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path



            )

        except Exception as e :
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


