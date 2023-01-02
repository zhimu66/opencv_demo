# -*- coding:utf-8 -*-
import numpy as np
import cv2


def white_word():
    """黑底白字"""
    file = 'imgs/黑底白字.png'
    img = cv2.imread(file)

    kernel0 = np.zeros((15, 15), np.uint8)
    kernel1 = np.ones((5, 5), np.uint8)

    # 腐蚀
    print("黑底白字_0_腐蚀------>白边线 下移")
    erode0 = cv2.erode(img, kernel0, iterations=1)
    cv2.imwrite("imgs/黑底白字_0_腐蚀.png", erode0)

    print("黑底白字_1_腐蚀-------> 变瘦")
    erode1 = cv2.erode(img, kernel1, iterations=1)
    cv2.imwrite("imgs/黑底白字_1_腐蚀.png", erode1)

    # 膨胀
    print("黑底白字_0_膨胀------>下移")
    dilate0 = cv2.dilate(img, kernel0, iterations=1)
    cv2.imwrite("imgs/黑底白字_0_膨胀.png", dilate0)

    print("黑底白字_1_膨胀-------> 变胖")
    dilate1 = cv2.dilate(img, kernel1, iterations=1)
    cv2.imwrite("imgs/黑底白字_1_膨胀.png", dilate1)


def black_word():
    """白底黑字"""
    file = 'imgs/白底黑字.png'
    img = cv2.imread(file)

    kernel0 = np.zeros((15, 15), np.uint8)
    kernel1 = np.ones((5, 5), np.uint8)

    # 腐蚀
    print("白底黑字_0_腐蚀------>下移")
    erode0 = cv2.erode(img, kernel0, iterations=1)
    cv2.imwrite("imgs/白底黑字_0_腐蚀.png", erode0)

    print("白底黑字_1_腐蚀-------> 字变胖")
    erode1 = cv2.erode(img, kernel1, iterations=1)
    cv2.imwrite("imgs/白底黑字_1_腐蚀.png", erode1)

    # 膨胀
    print("白底黑字_0_膨胀------>黑边线 下移")
    dilate0 = cv2.dilate(img, kernel0, iterations=1)
    cv2.imwrite("imgs/白底黑字_0_膨胀.png", dilate0)

    print("白底黑字_1_膨胀-------> 字变瘦")
    dilate1 = cv2.dilate(img, kernel1, iterations=1)
    cv2.imwrite("imgs/白底黑字_1_膨胀.png", dilate1)



# def fun():
#     file = 'imgs/黑底白字.png'
#     img = cv2.imread(file)
#     ret, fg = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV)
#     cv2.imwrite('imgs/白底黑字.png', fg)





if __name__ == "__main__":
    # fun()
    # white_word()
    black_word()
