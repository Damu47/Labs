import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread("Red Marigold.jpg", 0)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(img, kernel, iterations=2)
dilated = cv2.dilate(img, kernel, iterations=2)

plt.subplot(1, 3, 1); plt.imshow(img, cmap="gray"); plt.title("Original")
plt.subplot(1, 3, 2); plt.imshow(eroded, cmap="gray"); plt.title("Erosion")
plt.subplot(1, 3, 3); plt.imshow(dilated, cmap="gray"); plt.title("Dilation")
plt.show()

import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.imread("#1output.png", 0)
kernel = np.ones((5, 5), np.uint8)
eroded = cv2.erode(img, kernel, iterations=4)
dilated = cv2.dilate(img, kernel, iterations=4)

plt.subplot(1, 3, 1); plt.imshow(img, cmap="gray"); plt.title("Original")
plt.subplot(1, 3, 2); plt.imshow(eroded, cmap="gray"); plt.title("Erosion (Shrunk)")
plt.subplot(1, 3, 3); plt.imshow(dilated, cmap="gray"); plt.title("Dilation (Expanded)")
plt.show()