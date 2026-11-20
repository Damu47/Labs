import cv2, matplotlib.pyplot as plt

noisy = cv2.imread("Lenna.png", 0)
gauss = cv2.GaussianBlur(noisy, (5, 5), 0)
median = cv2.medianBlur(noisy, 5)

plt.subplot(1, 3, 1); plt.imshow(noisy, cmap="gray"); plt.title("Noisy Input")
plt.subplot(1, 3, 2); plt.imshow(gauss, cmap="gray"); plt.title("Gaussian (Blurry)")
plt.subplot(1, 3, 3); plt.imshow(median, cmap="gray"); plt.title("Median (Clean)")
plt.show()