# load model to test on a picture (must resize to 200, 200 in image editor - fix to do this programatically)
model = models.load_model("angle_prediction_model_80p.model")

img = cv.imread("trial27_42.png")
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img, cmap=plt.cm.binary)

prediction = model.predict(np.array([img]) / 255)

print("predicted angle: ", prediction)

plt.show()
