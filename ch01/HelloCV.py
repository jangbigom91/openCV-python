import cv2
import sys

print('Hello, OpenCV', cv2.__version__)

img = cv2.imread('./ch01/cat.bmp')

if img is None:
    print('Image load failed!')
    sys.exit()

cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # cv2.WINDOW_NORMAL -> 사이즈 조정 가능
cv2.imshow('image', img)
# cv2.imwrite('catzz.png', img)  # imwrite -> 영상파일 저장(catzz.png로 img를 저장한다는 뜻)
# cv2.waitKey(3000)   # () 안에 시간을 주면 자동으로 꺼진다
while True:
    if cv2.waitKey() == 27:  # 주요 특수키 코드 : 27(ESC), 13(ENTER), 9(TAB)
        break                # 이미지가 나오고 특수키를 누르면 이미지창이 꺼짐
                             # 이미지가 나오고 27로 설정되었으면 ESC키 누를 시 이미지창 꺼짐

cv2.destroyAllWindows()
