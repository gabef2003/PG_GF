import pyautogui as pg



pg.keyDown('ctrl')
pg.keyDown('shift')
pg.keyDown('s')

pg.keyUp('ctrl')
pg.keyUp('shift')
pg.keyUp('s')


pg.typewrite("C:\\Users\\csci\\Desktop\\ test.py",0.3)
pg.hotkey('enter')
