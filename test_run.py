from clasifier_cnn.pipeline.stage01_data_ingestion import DataIngwationPipeline
from clasifier_cnn import logger
from clasifier_cnn.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from clasifier_cnn.pipeline.stage_03_training import TrainingPipeline


STAGE_NAME = "First stage: data ingestion"

try:
    logger.info(f"Trying to copy data set: This is the {STAGE_NAME} stay tuned and relax")
    pipeline = DataIngwationPipeline()
    pipeline.main()
    logger.info(f"succefuly unziped the file and you are done with {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Second stage: Model Creation"

try:
    logger.info(f"Trying to copy data set: This is the {STAGE_NAME} stay tuned and relax")
    pipeline = PrepareBaseModelPipeline()
    pipeline.main()
    logger.info(f"succefuly unziped the file and you are done with {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Third stage: Model Training"

try:
    logger.info(f"Trying to train the model: This is the {STAGE_NAME} stay tuned and relax")
    pipeline = TrainingPipeline()
    pipeline.main()
    logger.info(f"succefuly finished training {STAGE_NAME}")

except Exception as e:
    logger.exception(e)
    raise e
