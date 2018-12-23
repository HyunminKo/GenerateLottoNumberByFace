import cv2
import matplotlib.pyplot as plt

def makeLocationsOfBox(rect):
    nX = rect['init_x']
    nY = rect['init_y']
    count = 0
    for row in range(7):
        for col in range(7):
            if count == 45:
                break
            rect['data'].append([nX,nY])
            count+=1
            nX += rect['space'] + rect['width']
        nX = rect['init_x']
        nY += rect['space'] + rect['height']
    return rect

def loadBGImage():
    img = cv2.imread('data/background_lotto.jpg')
    return img

def loadWinningNumberData():
    result = []
    with open('data/WinningNumberByDraw.txt','r') as f:
        for line in f:
            result.append(line.strip('\n').split(' '))
    return result

def fillAreaByIndex(img,rectInfo,rect):
    imgName = rectInfo[0]
    numbers = rectInfo[1].split(',')
    print(numbers)
    for num in numbers:
        x = rect['data'][int(num)-1][0]
        y = rect['data'][int(num)-1][1]
        cv2.rectangle(img, (x, y), (x+rect['width'], y+rect['height']), (0, 0, 0), -1)
    cv2.imwrite('data/train_data/{}.jpg'.format(imgName),img)
    
rect = {
    'width': 40,
    'height': 60,
    'space' : 10,
    'init_x' : 30,
    'init_y' : 10,
    'data' : []
}
makeLocationsOfBox(rect)
result = loadWinningNumberData()
for item in result:
    fillAreaByIndex(loadBGImage(),item,rect)