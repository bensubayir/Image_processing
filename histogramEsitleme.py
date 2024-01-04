import cv2
from matplotlib import pyplot as plt


image = cv2.imread('kahve.jpg')
#image = cv2.imread('resim_adı.jpg', 0) gri tonlarda yüklemek için


equalized_image = cv2.equalizeHist(cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))


plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.title('Orijinal Görüntü')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # BGR formatından RGB formatına dönüştürme
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Histogram Eşitlenmiş Görüntü')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()

