import numpy as np
import cv2

background_img = np.full((500,400,3),255,dtype=np.uint8)

rect = {
    'width': 40,
    'height': 60,
    'space' : 10,
    'data' : []
}
#init location
x = 30
y = 10

nX = x
nY = y
count = 0
for row in range(7):
    for col in range(7):
        if count == 45:
            break
        rect['data'].append([nX,nY])
        count+=1
        nX += rect['space'] + rect['width']
    nX = x
    nY += rect['space'] + rect['height']
    
# Choose a font
font = cv2.FONT_HERSHEY_SIMPLEX

count = 0
for data in rect['data']:
    count +=1
    cv2.rectangle(background_img, (data[0], data[1]), (data[0]+rect['width'], data[1]+rect['height']), (0, 0, 0), 2)
    center_x = int((data[0]+rect['width'])) - int(rect['width']/2) - 10
    center_y = int((data[1]+rect['height'])) - int(rect['height']/2) + 10
    if count >= 10:
        center_x -= 11
    cv2.putText(background_img,str(count),(center_x,center_y), font, 1,(0,0,0),2,cv2.LINE_AA)
    
cv2.imwrite('../data/background_lotto.jpg',background_img)
