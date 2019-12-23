import cv2
import sys

file_name = sys.argv[1]
I  = cv2.imread(file_name)


print(I.shape)
