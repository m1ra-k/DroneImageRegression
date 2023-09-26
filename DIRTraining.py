from tensorflow import keras
from keras import layers
import pickle


def train_model(screenshot_images, screenshot_labels, data_range, model_name):
    # split data into training , test based off of range
    training_images = screenshot_images[0:data_range]
    training_labels = screenshot_labels[0:data_range]
    testing_images = screenshot_images[2832:]
    testing_labels = screenshot_labels[2832:]

    # model set up
    model = keras.Sequential([
        # allows model to learn complex patterns
        layers.Conv2D(32, (3, 3), activation="relu", input_shape=(200, 200, 3)),
        # calculates the largest value in batch
        layers.MaxPooling2D(2, 2),
        layers.MaxPooling2D(2, 2),
        # reshapes
        layers.Flatten(),
        layers.Dense(64, activation="relu"),
        # we are expecting one single output/prediction of suggest angle
        layers.Dense(1)
    ])

    # generates model according to parameters
    model.compile(optimizer="adam", loss="mean_squared_error", metrics=["mae"])

    # saving the history throughout each epoch
    history = model.fit(training_images, training_labels, epochs=20, validation_data=(testing_images, testing_labels))
    # uses pickle to save history to accessible file for future reference
    with open(model_name + ".history", "wb") as history_file:
        pickle.dump(history, history_file)

    # converts MAEs from each epoch into list form so that it may be visualized later on
    model_test_maes = history.history['val_mae']

    # evaluates the finalized model on the testing images/labels reporting its effectiveness
    loss, accuracy = model.evaluate(testing_images, testing_labels)
    print(f"Loss: {loss}")
    print(f"Accuracy: {accuracy}")

    # saves the model according to name
    model.save(model_name + ".model")

    return model_test_maes
