import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('dolar.jpg', cv2.IMREAD_GRAYSCALE)


sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)


plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.title('Orijinal Görüntü')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Sobel X (Dikey Kenarlar)')
plt.imshow(cv2.convertScaleAbs(sobel_x), cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Sobel Y (Yatay Kenarlar)')
plt.imshow(cv2.convertScaleAbs(sobel_y), cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
