import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


def function(a, b, x):
    return a * x + b


x = np.random.randint(10, 200, 30)
ratio = 8
intercept = 50
y = function(ratio, intercept, x)

x = np.array(x, dtype=float)
y = np.array(y, dtype=float)
l0 = tf.keras.layers.Dense(1, input_shape=[1])
model = tf.keras.Sequential([l0])
model.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss="mse")
history = model.fit(x, y, epochs=500)

plt.xlabel("Epoch Numbers")
plt.ylabel("Loss Magnitude")
plt.plot(history.history["loss"])
plt.show()

print(model.predict([100]))


