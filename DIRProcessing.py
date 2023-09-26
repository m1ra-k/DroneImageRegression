import numpy as np
import os.path
from sklearn.preprocessing import LabelEncoder
import tensorflow as tf
import csv


def preprocess_images_labels():
    # to get the screenshots (images)
    image_labels = []
    screenshot_images = []

    # to get the angle (image labels)
    screenshot_labels = []
    i = 0
    with open('/home/ama9tk/Desktop/Regression/all_screenshot_labels.csv', mode = 'r', newline='') as file:
        reader = csv.reader(file)

        for row in reader:
            image_labels.append('/home/ama9tk/Desktop/Regression/Data/Screenshots/' + row[1] + ".png")
            screenshot_labels.append(row[0])

    image_paths = [os.path.join('/home/ama9tk/Desktop/Regression/Data/Screenshots', screenshot) for screenshot in os.listdir('/home/ama9tk/Desktop/Regression/Data/Screenshots')]
    # i want to sort it in the order it appears in the folder
    image_paths = sorted(image_paths, key=lambda x: image_labels.index(x))
    print(len(image_paths))

    for image_path in image_paths:
        print(image_path)
        screenshot_image = tf.io.read_file(image_path)
        screenshot_image = tf.image.decode_image(screenshot_image, channels=3)
        screenshot_image = tf.image.resize(screenshot_image, (200, 200))
        screenshot_images.append(screenshot_image)

    processed_screenshot_images = np.array(screenshot_images)
    # converts to categorical label to numerical form
    processed_screenshot_labels = LabelEncoder().fit_transform(screenshot_labels)
    return processed_screenshot_images, processed_screenshot_labels


