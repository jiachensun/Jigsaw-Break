# coding: utf-8

import uiautomator2 as u2

import cv2
import numpy as np

# 连接设备
d = u2.connect()

# 截屏
image = d.screenshot()
image.save("D:\\sunjiachen\\code_workspace\\python\\test\\1.png")

# 加载原图
img = cv2.imread("D:\\sunjiachen\\code_workspace\\python\\test\\1.png")
emptyImage = np.zeros(img.shape, np.uint8)
imgth,imgtw = emptyImage.shape[:2]
emptyImage2 = img.copy()

# 加载滑块图片
template = cv2.imread("D:\\sunjiachen\\code_workspace\\python\\test\\2.png")
template1 = np.zeros(template.shape, np.uint8)
template2 = template.copy()
template3 = cv2.resize(template2, (150, 150), )
th,tw = template3.shape[:2]

# 图形比对
result = cv2.matchTemplate(emptyImage2, template3, cv2.TM_SQDIFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
rectStart = min_loc

print(rectStart[0])

# 结束
cv2.waitKey(0)
cv2.destroyAllWindows()

# 移动滑块
loc = 0;
loc1 = imgtw/4;
print(loc1)
if rectStart[0] < loc1 :
    loc = 25;
elif loc1 < rectStart[0] < loc1*2 :
    loc = 45;
elif loc1*2 < rectStart[0] < loc1*3 :
    loc = 75;
else :
    loc = 100;
    
moveX = rectStart[0] + loc;
d.touch.down(33, 960 + 60) # 模拟按下
d.swipe(33, 960 + 60, moveX, 1040) # 模拟滑动
d.touch.up(moveX, 1040)  # 模拟抬起




