#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 18:45:05 2021

@author: Priyabrata Sahoo
"""
import numpy as np
from tensorflow import keras
from keras.models import load_model
from keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image


class ricegrains:
    def __init__(self,filename):
        self.filename =filename

# This functions helps to upload the image on the ui front and helps to convert the image to required format so that the image could be predicted
    def predictionricegrains(self):
        # load model
        model = load_model('model_name.h5',compile=False)

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict_proba(test_image)
        print(result)

        classes = ['good rice grains', 'bad rice grains']

        label_name = {classes[i]: result[i] for i in range(len(result))}

# if result is having value greater that .8 then it will predict good rice grains or else it will predict bad rice grains
        if result[0][0] >=.8:
            Prediction = 'Good Rice Grains'
            return [{"image": Prediction}]
        else:
            Prediction = 'Bad Rice Grains'
            return [{"image": Prediction}]


