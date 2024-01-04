import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('dolar.jpg')


noise_density = 0.02

rows, cols, channels = image.shape
noise = np.zeros((rows, cols, channels), dtype=np.uint8)

cv2.randu(noise, 0, 255)
salt = (noise > 255 * (1 - noise_density))
pepper = (noise < 255 * noise_density)

noisy_image = np.copy(image)
noisy_image[salt] = 255
noisy_image[pepper] = 0

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Orijinal Görüntü')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Salt and Pepper Gürültülü Görüntü')
plt.imshow(cv2.cvtColor(noisy_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()
