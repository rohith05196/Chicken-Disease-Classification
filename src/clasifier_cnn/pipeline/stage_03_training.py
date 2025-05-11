from clasifier_cnn.config.configuration import ConfigurationManager
from clasifier_cnn.components.prepare_callbacks import PrepareCallbacks
from clasifier_cnn.components.training import Training
from clasifier_cnn import logger


STAGE_NAME = "Training"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
       config = ConfigurationManager()
       prepare_callbacks_config = config.get_prepare_callbacks_config()
       prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
       callback_list = prepare_callbacks.get_checkpoint_callbacks()

       training_config = config.get_training_config()
       training = Training(config =training_config )
       training.get_base_model()
       training.train_valid_generator()
       training.train(
            callback_list=callback_list
        )
       
if __name__ == '__main__':

    STAGE_NAME = "Third Stage"

    try:
        
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    
    except Exception as e:
        logger.exception(e)
        raise e