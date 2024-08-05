import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.exception import CustomException
from src.logger import logging

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts', 'train.csv')
    test_data_path: str = os.path.join('artifacts', 'test.csv')
    raw_data_path: str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")

        try:
            # Use a relative path or environment variable for better portability
            data_path = 'E:/Projects/mlproject/notebook/data/stud.csv'
            df = pd.read_csv(data_path)
            logging.info("Read the dataset as dataframe.")
            
            # Create directories if they do not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            
            # Save the raw data to file
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            
            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.25, random_state=42)
            
            # Save the train and test sets to files
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info("Ingestion of data is completed")
            
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except FileNotFoundError as e:
            logging.error(f"File not found: {e}")
            raise CustomException(e, sys)
        except pd.errors.ParserError as e:
            logging.error(f"Parsing error: {e}")
            raise CustomException(e, sys)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()
