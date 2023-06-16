
from imageai.Prediction import ImagePrediction
import os

execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath("model.h5")
prediction.loadModel()


predictions, percentage_probabilities = prediction.predictImage("car.jpeg", result_count=12)
for index in range(len(predictions)):
    print("-----------"+str(predictions[index]) , " : " , str(percentage_probabilities[index])+"-------")