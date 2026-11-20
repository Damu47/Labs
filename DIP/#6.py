#a Translation, Rotation and Zoom
import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("Red Marigold.jpg"), cv2.COLOR_BGR2RGB)
h, w = img.shape[:2]

trans = cv2.warpAffine(img, np.float32([[1, 0, 100], [0, 1, 150]]), (w, h))
rot = cv2.warpAffine(img, cv2.getRotationMatrix2D((w//2, h//2), 45, 1), (w, h))
zoom = cv2.resize(img[h//2-150:h//2+150, w//2-150:w//2+150], (w, h))

plt.subplot(2, 2, 1); plt.imshow(img); plt.title("Original")
plt.subplot(2, 2, 2); plt.imshow(trans); plt.title("Translated")
plt.subplot(2, 2, 3); plt.imshow(rot); plt.title("Rotated 45")
plt.subplot(2, 2, 4); plt.imshow(zoom); plt.title("Zoomed")
plt.show()

#b Scaling and Shrinking
import cv2, matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("Red Marigold.jpg"), cv2.COLOR_BGR2RGB)
scaled = cv2.resize(img, None, fx=2, fy=2)
shrunk = cv2.resize(img, None, fx=0.5, fy=0.5)

plt.subplot(1, 3, 1); plt.imshow(img); plt.title("Original")
plt.subplot(1, 3, 2); plt.imshow(scaled); plt.title("Scaled 2x")
plt.subplot(1, 3, 3); plt.imshow(shrunk); plt.title("Shrunk 0.5x")
plt.show()