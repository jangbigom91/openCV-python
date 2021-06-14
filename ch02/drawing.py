import numpy as np
import cv2

img = np.full((400, 400, 3), 255, np.uint8)

# 직선 그리기
# cv2.line(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
# img : 그림을 그릴 영상, pt1, pt2 : 직선의 시작점과 끝점 color : 선 색상 또는 밝기
# thickness : 선 두께, 기본값은 1 lineType : 선타입, 기본값은 cv2.LINE_8 shift : 그리기 좌표 값의 축소 비율, 기본값은 0
cv2.line(img, (50, 50), (200, 50), (0, 0, 255), 5)
cv2.line(img, (50, 60), (150, 160), (0, 0, 128))

# 사각형 그리기
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220), (180, 280), (0, 128, 0), -1)

# 원 그리기
cv2.circle(img, (300, 100), 30, (255, 255, 0), -1, cv2.LINE_AA)
cv2.circle(img, (300, 100), 60, (255, 0, 0), 3, cv2.LINE_AA)

# 다각형 그리기
pts = np.array([[250, 200], [300, 200], [350, 300], [250, 300]])
cv2.polylines(img, [pts], True, (255, 0, 255), 2)

text = 'Hello? OpenCV ' + cv2.__version__
# 문자열 출력
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
            (0, 0, 255), 1, cv2.LINE_AA)

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()

