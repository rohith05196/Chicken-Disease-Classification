import numpy as np 
from tensorflow.keras.models import load_model 
from tensorflow.keras.preprocessing import image
import os 


class PredictionPipeline:
    def __init__(self, input_file):
        self.input_file = input_file

    def predict(self):

        model = load_model("artifacts/training/model.h5")

        input_image = self.input_file
        image_input = image.load_img(input_image, target_size = (224,224))
        image_input = image.img_to_array(image_input)
        image_input = np.expand_dims(image_input, axis=0)
        output_predict = np.argmax(model.predict(image_input), axis=1)

        if output_predict[0] == 1:
            return [{"image" : "Healthy"}]
        else:
            return [{"image" : "Cocidiosis"}]
