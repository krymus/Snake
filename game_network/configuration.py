import sys
from tensorflow import keras
from keras.layers import Dense, Flatten
from keras.models import Sequential
import numpy as np

def readStates():
    file = open("states.txt")
    X = np.array([])
    Y = np.array([])

    for line in file:
        x = np.array([])
        for i in range(400):
            x = np.append(x, float(line[i])/8.0)
        y = int(line[401])
        X = np.append(X,x)
        Y = np.append(Y,y)
    
    Y = keras.utils.to_categorical(Y, num_classes=4)
    X = X.reshape(-1, 400)
        
    return X, Y

Xtrain, Ytrain = readStates()   


#sys.exit()

model = Sequential([
Dense(400, activation='relu'),
Dense(128, activation='relu'),
Dense(128, activation='relu'),
Dense(64, activation='relu'),
Dense(4, activation='softmax')  # Output layer with 4 nodes for directions (up, down, left, right)
])


model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(Xtrain, Ytrain, epochs=3)



model.save('NN.keras')




    
    