
from clasifier_cnn.components.data_ingestion import DataIngestion
from clasifier_cnn.config.configuration import ConfigurationManager
from clasifier_cnn import logger

class DataIngwationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_zip_file()
        data_ingestion.unzip_file()

if __name__ == '__main__':

    STAGE_NAME = "First Stage"

    try:
        
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngwationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e