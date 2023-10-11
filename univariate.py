from numpy import array
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Conv1D
from keras.layers import MaxPooling1D


def split_sequence(sequence,  n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps
        if end_ix > len(sequence) - 1:
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)


raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
n_steps = 3
X, y = split_sequence(raw_seq, n_steps)
n_features = 1
X = X.reshape(X.shape[0], X.shape[1], n_features)
# for i in range(len(X)):
#     print(X[i], y[i])

# defined model
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=2, activation='relu',
          input_shape=(n_steps, n_features)))
model.add(MaxPooling1D(pool_size=2))
model.add(Flatten())
model.add(Dense(50, activation='relu'))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')
# fit model
model.fit(X, y, epochs=1000, verbose=0)
# demonstrate
x_input = array([70, 80, 90])
x_input = x_input.reshape(1, n_steps, n_features)
yhat = model.predict(x_input, verbose=0)
print(yhat)
