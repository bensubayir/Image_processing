#Blurring operation with Laplace
import cv2
import numpy as np
from matplotlib import pyplot as plt


image = cv2.imread('kahve.jpg', cv2.IMREAD_GRAYSCALE)


blurred_image = cv2.GaussianBlur(image, (3, 3), 0)


laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)


laplacian_abs = np.uint8(np.absolute(laplacian))

plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.title('Original Image')
plt.imshow(image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.title('Blurred Image (Gaussian)')
plt.imshow(blurred_image, cmap='gray')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.title('Laplacian')
plt.imshow(laplacian_abs, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
