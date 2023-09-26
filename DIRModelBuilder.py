import DIRLabelling as dirLabelling
import DIRProcessing as dirProcessing
import DIRTraining as dirTraining
import matplotlib.pyplot as plt
from keras import datasets, layers, models
import os
import pickle


while True:
    choice_build_model = str(input("Would you like to build new models (ENTER 0) or view the previously existing ones (ENTER 1)? "))
    if choice_build_model == "0" or choice_build_model == "1":
        break
    else:
        print("You did not pick a valid option. Try again.")

test_maes = []

if choice_build_model == "0":
    print("You chose to build new models.")

    dirLabelling.create_labels()
    processed_screenshot_images, processed_screenshot_labels = dirProcessing.preprocess_images_labels()

    # generate plot for comparison of models after models are created
    test_maes = [dirTraining.train_model(processed_screenshot_images, processed_screenshot_labels, 567, "angle_prediction_model_16p", ),
                 dirTraining.train_model(processed_screenshot_images, processed_screenshot_labels, 1133, "angle_prediction_model_32p"),
                 dirTraining.train_model(processed_screenshot_images, processed_screenshot_labels, 1699, "angle_prediction_model_48p"),
                 dirTraining.train_model(processed_screenshot_images, processed_screenshot_labels, 2265, "angle_prediction_model_64p"),
                 dirTraining.train_model(processed_screenshot_images, processed_screenshot_labels, 2832, "angle_prediction_model_80p")]


elif choice_build_model == "1":
    print("You chose to view the previously existing models.")

    existing_models = True

    if os.path.isfile("/home/ama9tk/DroneImageRegression/angle_prediction_model_16p.model"):
        print("However, there are no existing models. Try building some first.")
        existing_models = False

    if existing_models:
        model_names = ["angle_prediction_model_16p",
                       "angle_prediction_model_32p",
                       "angle_prediction_model_48p",
                       "angle_prediction_model_64p",
                       "angle_prediction_model_80p"]

        for i in range(5):
            with open(model_names[i] + ".history", "rb") as history_file:
                test_maes[i] = pickle.load(history_file)

# for i in test_maes[0]:
#     print("test accuracies 0: " + str(i))

epochs = range(1, 20 + 1)

plt.plot(epochs, test_maes[0], label='Model 0')
plt.plot(epochs, test_maes[1], label='Model 1')
plt.plot(epochs, test_maes[2], label='Model 2')
plt.plot(epochs, test_maes[3], label='Model 3')
plt.plot(epochs, test_maes[4], label='Model 4')
plt.xlabel('Epochs')
plt.ylabel('MAE')
plt.title('Validation/Test MAE vs. Number of Epochs')
plt.legend()
plt.show()
