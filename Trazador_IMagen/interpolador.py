import cv2

def main():
    image = cv2.imread("mano1.png",1)
    image2 = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
    #ret, image3 = cv2.threshold(image2, 110, 255, cv2.THRESH_TRIANGLE)
    image3 = cv2.adaptiveThreshold(image2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,5,2)
    median = cv2.medianBlur(image3,3)
    cv2.imwrite("imagen.png",median)

if __name__ == '__main__':
    main()
