import cv2, matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("Red Marigold.jpg"), cv2.COLOR_BGR2RGB)
gray = cv2.imread("Red Marigold.jpg", 0)

# 2(a) Negative Image
neg = 255 - img
plt.subplot(1, 2, 1); plt.imshow(img); plt.title("Original")
plt.subplot(1, 2, 2); plt.imshow(neg); plt.title("Negative")
plt.show()

# 2(b) Flip Image
h, v, b = cv2.flip(img, 1), cv2.flip(img, 0), cv2.flip(img, -1)
plt.subplot(2, 2, 1); plt.imshow(img); plt.title("Original")
plt.subplot(2, 2, 2); plt.imshow(h); plt.title("Horizontal Flip")
plt.subplot(2, 2, 3); plt.imshow(v); plt.title("Vertical Flip")
plt.subplot(2, 2, 4); plt.imshow(b); plt.title("Both Flips")
plt.show()

# 2(c) Thresholding
_, th = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
plt.subplot(1, 2, 1); plt.imshow(gray, cmap="gray"); plt.title("Grayscale")
plt.subplot(1, 2, 2); plt.imshow(th, cmap="gray"); plt.title("Thresholded")
plt.show()

# 2(d) Contrast Stretching
low = cv2.normalize(gray, None, 90, 150, cv2.NORM_MINMAX)
stretched = cv2.normalize(low, None, 0, 255, cv2.NORM_MINMAX)
plt.subplot(1, 2, 1); plt.imshow(low, cmap="gray", vmin=0, vmax=255); plt.title("Low Contrast")
plt.subplot(1, 2, 2); plt.imshow(stretched, cmap="gray", vmin=0, vmax=255); plt.title("Contrast Stretched")
plt.show()