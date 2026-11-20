#a AND
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("Red Marigold.jpg")
img2 = cv2.imread("Sunflower.jpg")

if img1 is None:
    print("Red Marigold.jpg not found")
elif img2 is None:
    print("Sunflower.jpg not found")
else:
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    result = cv2.bitwise_and(img1, img2_resized)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title("Image 1: Red Marigold")
    plt.axis("on")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(img2_resized, cv2.COLOR_BGR2RGB))
    plt.title("Image 2: Sunflower (Resized)")
    plt.axis("on")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("4(a) Bitwise AND")
    plt.axis("on")

    plt.tight_layout()
    plt.show()

#b OR
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("Red Marigold.jpg")
img2 = cv2.imread("Sunflower.jpg")

if img1 is None:
    print("Red Marigold.jpg not found")
elif img2 is None:
    print("Sunflower.jpg not found")
else:
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    result = cv2.bitwise_or(img1, img2_resized)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title("Image 1: Red Marigold")
    plt.axis("on")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(img2_resized, cv2.COLOR_BGR2RGB))
    plt.title("Image 2: Sunflower (Resized)")
    plt.axis("on")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("4(b) Bitwise OR")
    plt.axis("on")

    plt.tight_layout()
    plt.show()

#c NOT
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Sunflower.jpg")

if img is None:
    print("Sunflower.jpg not found")
else:
    result = cv2.bitwise_not(img)

    plt.figure(figsize=(9, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original: Sunflower (408x728)")
    plt.axis("on")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("4(c) Bitwise NOT")
    plt.axis("on")

    plt.tight_layout()
    plt.show()

