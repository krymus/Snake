from tensorflow import keras
from keras.layers import Dense
from keras.models import Sequential
import numpy as np

model = Sequential([
    Dense(400, activation='relu'),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(4, activation='softmax')  
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

file_path = "game_netALG/statesALG.txt"
batch_size = 10000 
episode = 1

with open(file_path, 'r') as file:
    X_batch = np.array([])
    Y_batch = np.array([])

    for line in file:
        x = np.array([float(value)/8.0 for value in line[:400]])
        y = int(line[401])

        X_batch = np.append(X_batch, x)
        Y_batch = np.append(Y_batch, y)

        if len(Y_batch) >= batch_size:
            Y_batch = keras.utils.to_categorical(Y_batch, num_classes=4)
            X_batch = X_batch.reshape(-1, 400)
            model.fit(X_batch, Y_batch, epochs=10)
            X_batch = np.array([])
            Y_batch = np.array([])
            print("Training episode " + str(episode) + " completed")
            episode += 1

# Train on the remaining data (if any)
if len(X_batch) > 0:
    Y_batch = keras.utils.to_categorical(Y_batch, num_classes=4)
    X_batch = X_batch.reshape(-1, 400)
    model.fit(X_batch, Y_batch, epochs=10)

print("Training completed.")
model.save('game_netALG/NNALG.keras')

    
    