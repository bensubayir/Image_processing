import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('smile.jpg')


laplacian = cv2.Laplacian(image, cv2.CV_64F)
sharpened_image = np.uint8(np.clip(image - 0.7 * laplacian, 0, 255))

plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Orijinal Görüntü')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Keskinleştirilmiş Görüntü')
plt.imshow(cv2.cvtColor(sharpened_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()
