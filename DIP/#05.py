#a Histogram Calculation
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Sunflower.jpg", 0)

if img is None:
    print("Error: Sunflower.jpg not found")
else:
    hist = cv2.calcHist([img], [0], None, [256], [0, 256])

    plt.figure(figsize=(8, 4))
    plt.plot(hist, color="black")
    plt.title("5(a) Grayscale Histogram (Sunflower.jpg)")
    plt.xlabel("Pixel Intensity (0 = Black, 255 = White)")
    plt.ylabel("Pixel Count (Frequency)")
    plt.xlim([0, 256])
    plt.grid(True, alpha=0.3)
    plt.show()

#b Equalization
import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Sunflower.jpg", 0)

if img is None:
    print("Error: Sunflower.jpg not found")
else:
    equalized = cv2.equalizeHist(img)

    plt.figure(figsize=(9, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap="gray")
    plt.title("Original Grayscale (408x728)")
    plt.axis("on")

    plt.subplot(1, 2, 2)
    plt.imshow(equalized, cmap="gray")
    plt.title("5(b) Histogram Equalized")
    plt.axis("on")

    plt.tight_layout()
    plt.show()