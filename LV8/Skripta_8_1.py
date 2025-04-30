from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import os

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# 1) Izgradnja potpuno konvolucijske mreže (bez Dense slojeva)
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),

    layers.Conv2D(128, (3, 3), activation='relu'),

    layers.Conv2D(10, (1, 1), activation='softmax'),
    layers.GlobalAveragePooling2D() 
])

# 2) Kompajliranje modela
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 3) Callbacks
log_dir = "logs/" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
tensorboard_cb = callbacks.TensorBoard(log_dir=log_dir, histogram_freq=1)

checkpoint_cb = callbacks.ModelCheckpoint("best_model.h5", save_best_only=True, monitor="val_accuracy", mode="max")

# 4) Treniranje modela s 10% podataka za validaciju
history = model.fit(x_train_s, y_train_s,
                    validation_split=0.1,
                    epochs=10,
                    batch_size=128,
                    callbacks=[tensorboard_cb, checkpoint_cb])

# 5) Učitavanje najboljeg modela
best_model = keras.models.load_model("best_model.h5")

# 6) Evaluacija modela
train_preds = best_model.predict(x_train_s)
test_preds = best_model.predict(x_test_s)

train_acc = accuracy_score(np.argmax(y_train_s, axis=1), np.argmax(train_preds, axis=1))
test_acc = accuracy_score(np.argmax(y_test_s, axis=1), np.argmax(test_preds, axis=1))

print(f"Točnost na skupu za učenje: {train_acc:.4f}")
print(f"Točnost na skupu za testiranje: {test_acc:.4f}")

# 7) Matrica zabune
def prikazi_matricu_zabune(y_true, y_pred, naziv_skupa):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title(f"Matrica zabune - {naziv_skupa}")
    plt.xlabel("Predviđeno")
    plt.ylabel("Stvarno")
    plt.show()

prikazi_matricu_zabune(np.argmax(y_train_s, axis=1), np.argmax(train_preds, axis=1), "Trening")
prikazi_matricu_zabune(np.argmax(y_test_s, axis=1), np.argmax(test_preds, axis=1), "Test")
