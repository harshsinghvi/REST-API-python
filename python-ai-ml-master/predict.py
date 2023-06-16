import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt 
import sys

MODEL_NAME="models/quadratic.model"

# model1 = tf.keras.models.load_model("models/3x+3/mymodel1.h5")
model_trained = tf.keras.models.load_model(MODEL_NAME)
# model_random=tf.keras.models.load_model("models/random.model")

prediction = model_trained.predict([1,2,3,4,5,6,7,1000])  # REMEMBER YOU'RE PASSING A LIST OF THINGS YOU WISH TO PREDICT
print(prediction)


# def graph():
#     DX=0.0001
#     GRAPH_START=int(sys.argv[1])
#     GRAPH_END=int(sys.argv[2])
#     x=np.arange(start=GRAPH_START, stop=GRAPH_END, step=DX)
#     y = x*3+3

#     plt.plot(x, y,) 
#     plt.plot(x, y, label = "linear") 
#     plt.plot(x, model1.predict(x), label = "model1") 
#     plt.plot(x, model_trained(x), label = "model2") 

#     plt.plot(x, model_random.predict(x), label = "random") 



#     # naming the x axis 
#     plt.xlabel('x - axis') 
#     # naming the y axis 
#     plt.ylabel('y - axis') 
    
#     # giving a title to my graph 
#     plt.title('Y=3*x+3') 

#     # show a legend on the plot 
#     plt.legend() 

#     # function to show the plot 
#     plt.show() 