import sys
import cv2

# 마스크 영상은 항상 그레이스케일 영상
# 마스크 영상을 이용한 영상 합성
src = cv2.imread('./ch02/airplane.bmp', cv2.IMREAD_COLOR)
mask = cv2.imread('./ch02/mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
dst = cv2.imread('./ch02/field.bmp', cv2.IMREAD_COLOR)

if src is None or mask is None or dst is None:
    print('Image load failed!')
    sys.exit()

cv2.copyTo(src, mask, dst)  # src : 입력영상
                            # mask : 마스크 영상, cv2.CV_8U, 0이 아닌 픽셀에 대해서만 복사 연산을 수행
                            # dst : 출력영상
                            # src, mask, dst는 모두 크기가 같아야함
                            # src와 dst는 같은 타입이어야 하고, mask는 그레이스케일 타입의 이진영상
# dst[mask > 0] = src[mask > 0]

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()

# 알파 채널을 마스크 영상으로 이용
src = cv2.imread('./ch02/cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

if src is None or logo is None:
    print('Image load failed!')
    sys.exit()

mask = logo[:, :, 3]    # mask는 알파 채널로 만든 마스크 영상
logo = logo[:, :, :-1]  # logo는 b, g, r 3채널로 구성된 컬러 영상
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]  # logo, mask와 같은 크기의 부분 영상 추출

cv2.copyTo(logo, mask, crop)
#crop[mask > 0] = logo[mask > 0]

cv2.imshow('src', src)
cv2.imshow('logo', logo)
cv2.imshow('mask', mask)
cv2.waitKey()
cv2.destroyAllWindows()
