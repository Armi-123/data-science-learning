import cv2
import numpy as np

image = cv2.imread(r"d:\Unlox\Week_1\Image Manipulation\sample.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

cv2.imshow('Original Image', image)

inverted = 255 - image
cv2.imshow('Inverted Image', inverted)

brightness = 50
bright = np.clip(image + brightness, 0, 255).astype(np.uint8)
cv2.imshow('Brighter Image', bright)

cropped = image[100:300, 200:400]
cv2.imshow('Cropped Image', cropped)

cv2.imwrite('output_inverted.jpg', inverted)
cv2.imwrite('output_bright.jpg', bright)
cv2.imwrite('output_cropped.jpg', cropped)

print("Processing completed successfully! Images saved in output/")

cv2.waitKey(0)
cv2.destroyAllWindows()