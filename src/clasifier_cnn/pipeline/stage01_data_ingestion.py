
from clasifier_cnn.components.data_ingestion import DataIngestion
from clasifier_cnn.config.configuration import ConfigurationManager

class DataIngwationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_zip_file()
        data_ingestion.unzip_file()

    