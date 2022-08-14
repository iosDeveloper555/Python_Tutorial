import cv2
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
resorces_path = "/Users/apple/Documents/Python/PyCharm_Project/Python_Scripting/Resources/Images/"

img = cv2.imread(resorces_path + "ocr.jpeg")


# get gray scal of image
def get_Gray_Scale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# remove_noise
def remove_noise(image):
    return cv2.medianBlur(image, 5)


# Threshold
def Thresholding(image):
    return cv2.threshold(image, 0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]


# Get text from image
def ocr_core(image):
    text = pytesseract.image_to_string(image)
    return text


img = get_Gray_Scale(img)
img = Thresholding(img)
img = remove_noise(img)

print(ocr_core(img))
#print("Test from image =", ocr_code(img))
''' 
cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('grayscale.jpg',img)
'''