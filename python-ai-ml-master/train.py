import tensorflow as tf
import numpy as np

# np.set_printoptions(suppress=True)
# DATA_START=-10
# DATA_END=10
# DATA_STEP=0.5
EPOCHS=50000
# MODEL_FILE_PATH="models/"
MODEL_NAME="models/quadratic.model"
x = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,100,200,100000,500002,1233,3112,-1,-3,-6,-7,-10,-20,-23,-12,24,-30,-1000,-2000,-3000,-100,-200,-300,-400,-500], dtype=float)
# x = np.arange(start=-10, stop=10, step=DATA_STEP,dtype=float) + np.arange(start=-200, stop=-100, step=DATA_STEP,dtype=float) + np.arange(start=100, stop=150, step=DATA_STEP,dtype=float)

# y = x*3+3         #lineer
y= np.power(x,2)          #quadratic

def data_debug():
    # x = np.arange(start=-10, stop=10, step=DATA_STEP,dtype=float) + np.arange(start=-200, stop=-100, step=DATA_STEP,dtype=float) + np.arange(start=100, stop=150, step=DATA_STEP,dtype=float)
    # x=np.concatenate(np.arange(start=-10, stop=10, step=DATA_STEP,dtype=float),np.arange(start=-200, stop=-100, step=DATA_STEP,dtype=float))
    print(x)
    print("-------  --- -----")
    print(y)


def main():
    neural_network_model = tf.keras.Sequential([tf.keras.layers.Dense(units=1,input_shape=[1])])
    neural_network_model.compile(optimizer='adam',loss='mse')
    neural_network_model.fit(x,y,epochs=EPOCHS)
    neural_network_model.save(MODEL_NAME)

if __name__ == '__main__':
    # main()
    data_debug()