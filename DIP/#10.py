import cv2, matplotlib.pyplot as plt

img = cv2.imread("Red Marigold.jpg", 0)
lap = cv2.Laplacian(img, cv2.CV_64F)
canny = cv2.Canny(img, 100, 200)

plt.subplot(1, 3, 1); plt.imshow(img, cmap="gray"); plt.title("Original")
plt.subplot(1, 3, 2); plt.imshow(lap, cmap="gray"); plt.title("Laplacian")
plt.subplot(1, 3, 3); plt.imshow(canny, cmap="gray"); plt.title("Canny")
plt.show()