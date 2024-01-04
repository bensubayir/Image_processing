import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('smile.jpg')


blurred_image = cv2.GaussianBlur(image, (5, 5), 0)


plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Orijinal Görüntü')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Gaussian Blur Uygulanmış Görüntü')
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.tight_layout()
plt.show()

