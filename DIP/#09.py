import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread("Red Marigold.jpg", 0)
r, c = img.shape

fshift = np.fft.fftshift(np.fft.fft2(img))
mask = np.zeros((r, c), np.uint8)
mask[r//2-30:r//2+30, c//2-30:c//2+30] = 1

low = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * mask)))
high = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * (1 - mask))))

plt.subplot(1, 3, 1); plt.imshow(img, cmap="gray"); plt.title("Original")
plt.subplot(1, 3, 2); plt.imshow(low, cmap="gray"); plt.title("Low Pass")
plt.subplot(1, 3, 3); plt.imshow(high, cmap="gray"); plt.title("High Pass")
plt.show()