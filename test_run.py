from clasifier_cnn.pipeline.stage01_data_ingestion import DataIngwationPipeline
from clasifier_cnn import logger

STAGE_NAME = "Fzrst stage: data ingestion"

try:
    logger.info(f"Trying to copy data set: This is the {STAGE_NAME} stay tuned and relax")
    pipeline = DataIngwationPipeline()
    pipeline.main()
    logger.info(f"succefuly unziped the file and you are done with {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e