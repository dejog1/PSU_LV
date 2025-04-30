import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.transform import resize
from skimage import color
from tensorflow.keras import models
import numpy as np

filename = 'test.png'

# Ucitaj sliku
img_original = mpimg.imread(filename)  
if img_original.ndim == 3:
    img = color.rgb2gray(img_original)
else:
    img = img_original  # već siva slika

# Promijeni veličinu na 28x28 i prikaži sliku
img = resize(img, (28, 28), anti_aliasing=True)
plt.imshow(img, cmap='gray')
plt.axis('off')
plt.title('Ulazna slika')
plt.show()

# Pripremi sliku - ulaz u mrežu
img = img.reshape(1, 28, 28, 1).astype('float32')

# TODO: učitaj izgrađenu mrežu
model = models.load_model('best_model.h5')

# TODO: napravi predikciju
predictions = model.predict(img)
predicted_class = np.argmax(predictions)

# TODO: ispiši rezultat u terminal
print(f"Predviđena znamenka: {predicted_class}")
print(f"Distribucija vjerojatnosti po klasama: {predictions}")
