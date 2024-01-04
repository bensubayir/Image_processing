import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('smile.jpg')

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

red_component = image_rgb[:, :, 0]
green_component = image_rgb[:, :, 1]
blue_component = image_rgb[:, :, 2]


plt.figure(figsize=(10, 4))

plt.subplot(1, 4, 1)
plt.title('Orijinal Görüntü')
plt.imshow(image_rgb)
plt.axis('off')

plt.subplot(1, 4, 2)
plt.title('Kırmızı Bileşen')
plt.imshow(red_component, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 3)
plt.title('Yeşil Bileşen')
plt.imshow(green_component, cmap='gray')
plt.axis('off')

plt.subplot(1, 4, 4)
plt.title('Mavi Bileşen')
plt.imshow(blue_component, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
