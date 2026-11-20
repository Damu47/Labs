import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("Red Marigold.jpg"), cv2.COLOR_BGR2RGB)
lp = cv2.filter2D(img, -1, np.ones((5, 5), np.float32) / 25)
hp = cv2.filter2D(img, -1, np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]))

plt.subplot(1, 3, 1); plt.imshow(img); plt.title("Original")
plt.subplot(1, 3, 2); plt.imshow(lp); plt.title("Low Pass")
plt.subplot(1, 3, 3); plt.imshow(hp); plt.title("High Pass")
plt.show()