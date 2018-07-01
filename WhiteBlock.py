import  pyautogui as pag
import  cv2
pag.FAILSAFE = True
screenWidth, screenHeight = pag.size()
print(screenWidth, screenHeight)
y = 670
pointx = (620, 720, 820, 920)
i = 0
while(True):
    for x in pointx:
        if(pag.pixelMatchesColor(x, y, (1,1,1))):
            #pag.moveTo(x, y)
            pag.click(x,y)
