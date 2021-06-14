import numpy as np
import cv2

# 트랙바 : 프로그램 동작 중 사용자가 지정한 범위 안의 값을 선택할 수 있는 컨트롤
# OpenCV에서 제공하는(유일한?) 그래픽 사용자 인터페이스

def on_level_change(pos):
    value = pos * 16
    if value >= 255:
        value = 255

    img[:] = value
    cv2.imshow('image', img)


img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')

# cv2.createTrackbar(trackbarName, windowName, value, count, onChange)
# trackbarName : 트랙바 이름, windowName : 트랙바를 생성할 창 이름, value : 트랙바 위치 초기값
# count : 트랙바 최대값, 최소값은 항상 0  # onChange : 트랙바 위치가 변경될 때마다 호출할 콜백 함수이름
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)
   
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

#-*- coding: utf-8 -*-
# R, G, B 트랙바 만들기
import cv2
import numpy as np

def nothing(x):
    pass
img = np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

# trackbar를 생성하여 named window에 등록
cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)
switch = '0:OFF\n1:On'

cv2.createTrackbar(switch, 'image', 1, 1, nothing)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')
    
    if s == 0:
        img[:] = 0 # 모든 행/열 좌표 값을 0으로 변경. 검은색
    else:
        img[:] = [b,g,r] # 모든 행/열 좌표값을 [b,g,r]로 변경

cv2.destroyAllWindows()