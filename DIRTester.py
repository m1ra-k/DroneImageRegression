from keras import models
import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np
import os
import csv

filepath = ""
actual = 0.0

while True:
    model = str(input("Enter the name of the model you would like to test. "))
    if os.path.exists(model):
        break
    else:
        print("Model", "'" + model + "'", "not found. Try again.")

# load model to test on a picture
model = models.load_model(model)

while True:
    filepath = str(input("Enter the path of the image you would like to test. If you would like to exit, press *. "))
    if os.path.isfile(filepath):

        # resizing
        img = cv.resize(cv.imread(filepath), (200, 200))
        img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

        plt.imshow(img, cmap=plt.cm.binary)

        prediction = model.predict(np.array([img]) / 255)

        with open("all_screenshot_labels.csv", "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            for row in csv_reader:
                extracted_name_png = row[1] + ".png"
                if os.path.basename(filepath) == extracted_name_png:
                    actual = row[0]
                    break

        print("predicted angle: ", prediction[0])
        print("actual angle: ", actual)

        print("Close the plot to check another image.")
        plt.show()
    elif filepath == "*":
        break
    else:
        print("Image", "'" + filepath + "'", "not found. Try again.")
