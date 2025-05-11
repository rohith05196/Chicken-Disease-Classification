from clasifier_cnn.config.configuration import TraningConfig
from pathlib import Path
import tensorflow as tf
from tensorflow.keras.optimizers import Adam

class Training:
    def __init__(self, config:TraningConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path, compile = False
        )

    def train_valid_generator(self):

        data_generator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.20
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = "biliniear"
        )

        valid_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        self.valid_generator = valid_generator.flow_from_directory(
            directory = self.config.training_data,
            subset = "validation",
            shuffle = False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = 40,
                horizontal_flip = True,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                shear_range = 0.2,
                zoom_range = 0.2,
                **data_generator_kwargs
            )
        else:
            train_datagenerator = valid_generator

        self.train_datagenerator = train_datagenerator.flow_from_directory(
            directory = self.config.training_data,
            subset = "training",
            shuffle = True,
            **dataflow_kwargs
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_datagenerator.samples // self.train_datagenerator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
        
        self.model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy'],
        run_eagerly = True
        )
        
        self.model.fit(
            self.train_datagenerator,
            epochs = self.config.params_epoch,
            steps_per_epoch =  self.steps_per_epoch,
            validation_steps =  self.validation_steps,
            validation_data = self.valid_generator,
            callbacks = callback_list
        )

        self.save_model(
            path = self.config.training_model_path,
            model = self.model
        )