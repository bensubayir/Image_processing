#doğrusal kontrast germe
import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('kahve.jpg', cv2.IMREAD_GRAYSCALE)

normalized_img = image.astype('float32') / 255.0

min_value = 0.1
max_value = 0.9


contrast_stretched = np.clip((normalized_img - min_value) / (max_value - min_value), 0, 1)
contrast_stretched = (contrast_stretched * 255).astype('uint8')

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Orijinal Görüntü')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Doğrusal Kontrast Germe')
plt.imshow(contrast_stretched, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

