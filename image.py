import cv2
import os

HCONCAT = os.path.join("./", "hconcat")

L1 = os.listdir("image1/")
L2 = os.listdir("image2/")

for i in range(len(L1)):
    im1 = cv2.imread(os.path.join("image1", L1[i]))
    im2 = cv2.imread(os.path.join("image2", L2[i]))
    image = cv2.hconcat([im1, im2])
    cv2.imwrite(os.path.join(HCONCAT, L1[i]), image)
