import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagen_01.jpg', 0)

# Histograma con:
# (images, channels, mask, histSize, ranges, hist=..., accumulate=...)
# Arreglo de una dimención: .flatten()
histo = cv2.calcHist([img], [0], None, [256], [0,256]).flatten()


cv2.imshow('Imagen', img)

# Mostrar el histograma
fig = plt.figure()
plt.bar(range(len(histo)), histo)
plt.show()

cv2.waitKey()