#a Negative Image
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Red Marigold.jpg")
negative = 255 - img

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis("on")

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(negative, cv2.COLOR_BGR2RGB))
plt.title("Negative Image")
plt.axis("on")

plt.tight_layout()
plt.show()

#b Flip Image
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Red Marigold.jpg")
h = cv2.flip(img, 1)
v = cv2.flip(img, 0)
b = cv2.flip(img, -1)

plt.figure(figsize=(9, 8))

plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("on")

plt.subplot(2, 2, 2)
plt.imshow(cv2.cvtColor(h, cv2.COLOR_BGR2RGB))
plt.title("Horizontal Flip")
plt.axis("on")

plt.subplot(2, 2, 3)
plt.imshow(cv2.cvtColor(v, cv2.COLOR_BGR2RGB))
plt.title("Vertical Flip")
plt.axis("on")

plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(b, cv2.COLOR_BGR2RGB))
plt.title("Both (Horizontal + Vertical)")
plt.axis("on")

plt.tight_layout()
plt.show()

#c Thresholding
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Red Marigold.jpg", 0)
_, th = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Grayscale")
plt.axis("on")

plt.subplot(1, 2, 2)
plt.imshow(th, cmap="gray")
plt.title("Binary Thresholded (Cutoff = 127)")
plt.axis("on")

plt.tight_layout()
plt.show()

#d Contrast Stretching
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Red Marigold.jpg", 0)
low_contrast = cv2.normalize(img, None, 90, 150, cv2.NORM_MINMAX)
stretched = cv2.normalize(low_contrast, None, 0, 255, cv2.NORM_MINMAX)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(low_contrast, cmap="gray", vmin=0, vmax=255)
plt.title("Low-Contrast Input (Range: 90–150)")
plt.axis("on")

plt.subplot(1, 2, 2)
plt.imshow(stretched, cmap="gray", vmin=0, vmax=255)
plt.title("Contrast Stretched Output (Range: 0–255)")
plt.axis("on")

plt.tight_layout()
plt.show()