from clasifier_cnn.config.configuration import ConfigurationManager
from clasifier_cnn.components.prepare_callbacks import PrepareCallbacks
from clasifier_cnn.components.training import Training


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