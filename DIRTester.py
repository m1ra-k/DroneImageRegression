from tensorflow import keras
from keras import datasets, layers, models
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import os

while True:
    filepath = str(input("Enter the path of the image you would like to test. "))
    if os.path.isfile(filepath):
        break
    else:
        print("Image not found. Try again.")

# load model to test on a picture (must resize to 200, 200 in image editor - fix to do this programatically)
model = models.load_model("angle_prediction_model_80p.model")

img = cv.resize(cv.imread(filepath), (200, 200))
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img, cmap=plt.cm.binary)

prediction = model.predict(np.array([img]) / 255)

print("predicted angle: ", prediction)

plt.show()
