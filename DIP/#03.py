import cv2, matplotlib.pyplot as plt

img1 = cv2.cvtColor(cv2.imread("Red Marigold.jpg"), cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread("Sunflower.jpg"), cv2.COLOR_BGR2RGB)
img2_res = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# 3(a) Addition
plt.subplot(1, 3, 1); plt.imshow(img1); plt.title("Marigold")
plt.subplot(1, 3, 2); plt.imshow(img2_res); plt.title("Sunflower")
plt.subplot(1, 3, 3); plt.imshow(cv2.add(img1, img2_res)); plt.title("Addition")
plt.show()

# 3(b) Subtraction
plt.subplot(1, 3, 1); plt.imshow(img1); plt.title("Marigold")
plt.subplot(1, 3, 2); plt.imshow(img2_res); plt.title("Sunflower")
plt.subplot(1, 3, 3); plt.imshow(cv2.subtract(img1, img2_res)); plt.title("Subtraction")
plt.show()

# 3(c) Mean Value
print("Marigold Mean (R, G, B):", cv2.mean(img1)[:3])
print("Sunflower Mean (R, G, B):", cv2.mean(img2)[:3])
plt.subplot(1, 2, 1); plt.imshow(img1); plt.title("Marigold")
plt.subplot(1, 2, 2); plt.imshow(img2); plt.title("Sunflower")
plt.show()