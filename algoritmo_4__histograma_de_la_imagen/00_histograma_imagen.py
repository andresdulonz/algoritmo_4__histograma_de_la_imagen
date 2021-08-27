import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagen_01.jpg', 0)

# Normalización del histograma por su tamaño
[M, N] = img.shape[0:2]

# Características del histograma: images, channels, mask, histSize, ranges, hist=..., accumulate=...)
# Arreglo de una dimención: .flatten()
#hist = cv2.calcHist([img], [0], None, [256], [0,256]).flatten()/(M*N)
# Separación en quitiles
hist = cv2.calcHist([img], [0], None, [5], [0,256]).flatten()/(M*N)

cv2.imshow('Imagen', img)

# Mostrar el histograma
fig = plt.figure()
plt.bar(range(len(hist)), hist)
plt.show()

cv2.waitKey()