import cv2
import sys

try:
	file_name = sys.argv[1]
	I  = cv2.imread(file_name)
except Exception as ex:
	print(ex)

print(I.shape)
