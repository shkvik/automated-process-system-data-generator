from keras.layers import Input, Dense, LSTM, Dropout, concatenate
from keras.models import Model, Sequential
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd


# Загрузка и предварительная обработка данных
data1 = pd.read_csv("./dataset/train/trainX/trainX_0.csv", delimiter=",")
data2 = pd.read_csv("./dataset/train/trainX/trainX_0.csv", delimiter=",")
data3 = pd.read_csv("./dataset/train/trainY/trainY_0.csv", delimiter=",")


X_train1 = np.array(data1.values)
X_train2 = np.array(data1.values)
Y_train  = np.array(data3.values)

X_train1 = X_train1.transpose()
X_train2 = X_train2.transpose()
Y_train = Y_train.transpose()


scaler1 = MinMaxScaler(feature_range=(0, 1))
scaler2 = MinMaxScaler(feature_range=(0, 1))

data1 = scaler1.fit_transform(data1)
data2 = scaler2.fit_transform(data2)


timesteps = 800
num_features1 = 1
num_features2 = 1
num_outputs = 800

# Определение модели
input1 = Input(shape=(timesteps, num_features1))
lstm1 = LSTM(64, activation='relu', return_sequences=True)(input1)
dropout1 = Dropout(0.2)(lstm1)
lstm2 = LSTM(32, activation='relu', return_sequences=False)(dropout1)

input2 = Input(shape=(timesteps, num_features2))
lstm3 = LSTM(64, activation='relu', return_sequences=True)(input2)
dropout2 = Dropout(0.2)(lstm3)
lstm4 = LSTM(32, activation='relu', return_sequences=False)(dropout2)


merged = concatenate([lstm2, lstm4])
output = Dense(num_outputs)(merged)

model = Model(inputs=[input1, input2], outputs=output)

# Компиляция модели
model.compile(optimizer='adam', loss='mse')

model.save('./test2.h5')


# Обучение модели
history = model.fit([X_train1, X_train2], Y_train, epochs=50, batch_size=64, validation_split=0.1)
                    


# # Получение предсказаний
# predictions = model.predict([X_test1, X_test2])

# # Оценка результатов
# mse = np.mean(np.power(scaler.inverse_transform(predictions) - scaler.inverse_transform(y_test), 2), axis=1)
# anomalies = np.where(mse > threshold)[0]



# timesteps = 10
# input_dim = 1

# # Создаем модель нейронной сети LSTM
# model = Sequential()
# model.add(LSTM(128, input_shape=(timesteps, input_dim)))
# model.add(Dense(1, activation='sigmoid'))

# # Компилируем модель
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# # Генерируем синтетические данные для обучения
# import numpy as np
# timesteps = 10
# input_dim = 1
# x_train = np.random.randn(1000, timesteps, input_dim)
# Y_train = np.random.randint(2, size=(1000, 1))

# # Обучаем модель на данных
# model.fit(x_train, Y_train, epochs=10, batch_size=32)