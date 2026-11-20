#a Import Libraries
import cv2, numpy as np, matplotlib.pyplot as plt

img = cv2.cvtColor(cv2.imread("Red Marigold.jpg"), cv2.COLOR_BGR2RGB)
print("Dimensions:", img.shape)

#b and c Original & Resize
res = cv2.resize(img, (300, 300))
plt.subplot(1, 2, 1); plt.imshow(img); plt.title("Original")
plt.subplot(1, 2, 2); plt.imshow(res); plt.title("Resized (300x300)")
plt.show()

# 1(d) Grayscale & 1(e) Black & White
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
plt.subplot(1, 2, 1); plt.imshow(gray, cmap="gray"); plt.title("Grayscale")
plt.subplot(1, 2, 2); plt.imshow(bw, cmap="gray"); plt.title("Black & White")
plt.show()

#f Image Profile
plt.plot(gray[450]); plt.title("Profile (Row 450)")
plt.show()

#g RGB Planes & 1(h) Merge RGB
r, g, b = cv2.split(img)
merged = cv2.merge((r, g, b))
plt.subplot(2, 2, 1); plt.imshow(r, cmap="gray"); plt.title("R Plane")
plt.subplot(2, 2, 2); plt.imshow(g, cmap="gray"); plt.title("G Plane")
plt.subplot(2, 2, 3); plt.imshow(b, cmap="gray"); plt.title("B Plane")
plt.subplot(2, 2, 4); plt.imshow(merged); plt.title("Merged RGB")
plt.show()

#i Write 2D Data
data = np.zeros((300, 300), dtype=np.uint8)
data[50:250, 50:250] = 255
cv2.imwrite("output.png", data)
plt.imshow(data, cmap="gray"); plt.title("2D Data")
plt.show()