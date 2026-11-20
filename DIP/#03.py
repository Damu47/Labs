#a Addition
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("Red Marigold.jpg")
img2 = cv2.imread("Sunflower.jpg")

if img1 is None:
    print("Red Marigold.jpg not found")
elif img2 is None:
    print("Sunflower.jpg not found")
else:
    print("Original Sunflower Dimensions (H, W, C):", img2.shape)
    img2_resized = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
    result = cv2.add(img1, img2_resized)

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title("Image 1: Red Marigold (735x945)")
    plt.axis("on")

    plt.subplot(1, 3, 2)
    plt.imshow(cv2.cvtColor(img2_resized, cv2.COLOR_BGR2RGB))
    plt.title("Image 2: Sunflower (Resized to 735x945)")
    plt.axis("on")

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title("3(a) Addition (img1 + img2)")
    plt.axis("on")

    plt.tight_layout()
    plt.show()

#b Subtraction
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
    result = cv2.subtract(img1, img2_resized)

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
    plt.title("3(b) Subtraction (img1 - img2)")
    plt.axis("on")

    plt.tight_layout()
    plt.show()

#c Mean Value
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("Red Marigold.jpg")
img2 = cv2.imread("Sunflower.jpg")

if img1 is None or img2 is None:
    print("Error: Check that both Red Marigold.jpg and Sunflower.jpg are in the folder")
else:
    mean1 = cv2.mean(img1)
    mean2 = cv2.mean(img2)
    print(f"Red Marigold Mean (B, G, R): ({mean1[0]:.2f}, {mean1[1]:.2f}, {mean1[2]:.2f})")
    print(f"Sunflower Mean    (B, G, R): ({mean2[0]:.2f}, {mean2[1]:.2f}, {mean2[2]:.2f})")

    plt.figure(figsize=(9, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.title("Red Marigold (735x945)")
    plt.axis("on")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.title("Sunflower (408x728)")
    plt.axis("on")

    plt.tight_layout()
    plt.show()