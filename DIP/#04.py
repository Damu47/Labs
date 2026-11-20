import cv2, matplotlib.pyplot as plt

img1 = cv2.cvtColor(cv2.imread("Red Marigold.jpg"), cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(cv2.imread("Sunflower.jpg"), cv2.COLOR_BGR2RGB)
img2_res = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# 4(a) Bitwise AND
plt.subplot(1, 3, 1); plt.imshow(img1); plt.title("Marigold")
plt.subplot(1, 3, 2); plt.imshow(img2_res); plt.title("Sunflower")
plt.subplot(1, 3, 3); plt.imshow(cv2.bitwise_and(img1, img2_res)); plt.title("Bitwise AND")
plt.show()

# 4(b) Bitwise OR
plt.subplot(1, 3, 1); plt.imshow(img1); plt.title("Marigold")
plt.subplot(1, 3, 2); plt.imshow(img2_res); plt.title("Sunflower")
plt.subplot(1, 3, 3); plt.imshow(cv2.bitwise_or(img1, img2_res)); plt.title("Bitwise OR")
plt.show()

# 4(c) Bitwise NOT
plt.subplot(1, 2, 1); plt.imshow(img2); plt.title("Sunflower")
plt.subplot(1, 2, 2); plt.imshow(cv2.bitwise_not(img2)); plt.title("Bitwise NOT")
plt.show()