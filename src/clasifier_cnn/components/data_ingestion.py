import os
import urllib.request as request
import zipfile
from clasifier_cnn import logger
from clasifier_cnn.entity.config_entity import DataIngestionConfig
from clasifier_cnn.utils.common_func import get_size
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
        
    def download_zip_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url = self.config.source_url,
                filename=self.config.local_data_file
            )
            logger.info(f"succesfully downloaded the zip {filename} with following info \n{header}")
        else:
            logger.info(f"The file already exists and the size is {get_size(Path(self.config.local_data_file))}")

    def unzip_file(self):
        os.makedirs(self.config.unzip_dir, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file:
            zip_file.extractall(self.config.unzip_dir)

            
