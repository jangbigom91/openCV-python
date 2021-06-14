import sys
import cv2


# 카메라 열기
cap = cv2.VideoCapture(0)  # 기본 카메라 장치 열기

if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

# 카메라 프레임 처리
while True:
    ret, frame = cap.read() # 카메라로부터 프레임을 정상적으로 받아오면 ret에는 True, frame에는 해당 프레임이 저장됨

    if not ret:
        break

    inversed = ~frame  # 현재 프레임 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27: # 일정 시간(e.g. 10ms) 기다린 후 다음 프레임 처리, 만약 ESC키를 누르면 while 루프 종료
        break

cap.release() # 사용한 자원해제
cv2.destroyAllWindows()
