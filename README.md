# DroneImageRegression
Drone Image Regression (DIR) files for Safe Trajectory Simulation research under LESS Lab.

### DIRLabelling.py
* Handles the labelling of images given a CSV of data collected through simulation. 
* Creates a new CSV with the important data extracted: the angle at which the drone turns and the image said angle is correlated to.
### DIRProcessing.py
* Processing the images and labels such that they are readable by the modeling tools.
### DIRTraining.py
* Trains and builds a model using the processed images according to the amount of data 
the user wishes to include.
### DIRModelBuilder.py
* Builds various models with the specifications of the user or loads the models if they already exist.
* Shows a comparison of the models against each other.
### DIRTester.py
* Allows user to continuously test different images on the variety of models created.