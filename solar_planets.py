import cv2

img=cv2.imread('solar-system.jpg')


cv2.putText(img,
            'Sun',
            (20,100),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )


cv2.putText(img,
            'Mercury',
            (50,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )


cv2.putText(img,
            'Venus',
            (180,250),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )


cv2.putText(img,
            'Earth',
            (280,150),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )


cv2.putText(img,
            'Mars',
            (370,200),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )

        
cv2.putText(img,
            'Jupiter',
            (500,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )


cv2.putText(img,
            'Saturn',
            (700,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )


cv2.putText(img,
            'Uranus',
            (950,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )


cv2.putText(img,
            'Neptune',
            (1100,300),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=1,
            color=(255,255,255)
            )

cv2.imshow('output',img)
cv2.waitKey(0)
cv2.imwrite('Solar_systemwithname.jpg',img)