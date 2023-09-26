# https://www.kaggle.com/code/gcdatkin/age-prediction-from-images-cnn-regression/notebook
import cv2 as cv
import numpy as np
from pathlib import Path
import os.path
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from PIL import Image
import tensorflow as tf
import csv
import glob
from tensorflow import keras
from tensorflow.keras import datasets, layers, models

# # to get the screenshots (images)
# image_labels = []
# screenshot_images = []

# # to get the angle (image labels)
# screenshot_labels = []
# i = 0
# with open('/home/ama9tk/Desktop/Regression/all_screenshot_labels.csv', mode = 'r', newline='') as file:
#     reader = csv.reader(file)

#     for row in reader:
#         image_labels.append('/home/ama9tk/Desktop/Regression/Data/Screenshots/' + row[1] + ".png")
#         screenshot_labels.append(row[0])

# image_paths = [os.path.join('/home/ama9tk/Desktop/Regression/Data/Screenshots', screenshot) for screenshot in os.listdir('/home/ama9tk/Desktop/Regression/Data/Screenshots')]
# # i want to sort it in the order it appears in the folder
# image_paths = sorted(image_paths, key=lambda x: image_labels.index(x))
# print(len(image_paths))

# i = 0
# for image_path in image_paths:
#     print(image_path)
#     screenshot_image = tf.io.read_file(image_path)
#     screenshot_image = tf.image.decode_image(screenshot_image, channels=3)
#     screenshot_image = tf.image.resize(screenshot_image, (200, 200))
#     screenshot_images.append(screenshot_image)
        
# screenshot_images = np.array(screenshot_images)
# # converts to categorical label to numerical form
# screenshot_labels = LabelEncoder().fit_transform(screenshot_labels)

# # loading and preprocessing dataset = done

def train_model(range, model_name):
    # split data into training , test based off of range
    training_images = screenshot_images[0:range]
    training_labels = screenshot_labels[0:range]
    testing_images = screenshot_images[2832:]
    testing_labels = screenshot_labels[2832:]

    # model set up
    model = keras.Sequential([
        # allows model to learn complex patterns
        layers.Conv2D(32, (3, 3), activation = "relu", input_shape = (200, 200, 3)),
        # calculates the largest value in batch
        layers.MaxPooling2D(2, 2),
        layers.MaxPooling2D(2, 2),
        # reshapes 
        layers.Flatten(),
        layers.Dense(64, activation = "relu"),
        # we are expecting one single output/prediction of suggest angle
        layers.Dense(1)
    ])

    # generates model according to parameters
    model.compile(optimizer = "adam", loss = "mean_squared_error", metrics = ["mae"])

    # saving the history throughout each epoch
    history = model.fit(training_images, training_labels, epochs = 20, validation_data = (testing_images, testing_labels))
    # converts MAEs from each epoch into list form so that it may be visualized later on
    model_test_maes = history.history['val_mae']

    # evaluates the finalized model on the testing images/labels reporting its effectiveness
    loss, accuracy = model.evaluate(testing_images, testing_labels)
    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}")

    # saves the model according to name
    model.save(model_name + ".model")

    return model_test_maes

# generate plot for comparison of models after models are created
# test_maes = []
# test_maes.append(train_model(567, "angle_prediction_model_16p"))
# test_maes.append(train_model(1133, "angle_prediction_model_32p"))
# test_maes.append(train_model(1699, "angle_prediction_model_48p"))
# test_maes.append(train_model(2265, "angle_prediction_model_64p"))
# test_maes.append(train_model(2832, "angle_prediction_model_80p"))

# for i in test_maes[0]:
#     print("test accuracies 0: " + str(i))

# epochs = range(1, 20 + 1)

# plt.plot(epochs, test_maes[0], label='Model 0')
# plt.plot(epochs, test_maes[1], label='Model 1')
# plt.plot(epochs, test_maes[2], label='Model 2')
# plt.plot(epochs, test_maes[3], label='Model 3')
# plt.plot(epochs, test_maes[4], label='Model 4')
# plt.xlabel('Epochs')
# plt.ylabel('MAE')
# plt.title('Validation/Test MAE vs. Number of Epochs')
# plt.legend()
# plt.show()

