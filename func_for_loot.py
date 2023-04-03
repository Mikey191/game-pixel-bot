from key_mouse_func import *
from move_func import *

def loot_for():
    list_dots_around_player = ([345, 370], [349, 335], [366, 314], [401, 310], [435, 316], [445, 342], [454, 368])
    for point in list_dots_around_player:
        t = random.uniform(0.05, 0.2)
        t2 = random.uniform(0.03, 0.1)
        mouse.move(point[0], point[1], True, t)
        mouse.click('right')
        time.sleep(t2)

def clear_target():
    t1 = random.uniform(0.05, 0.9)
    t2 = random.uniform(0.04, 0.5)
    PressKey(F1)
    time.sleep(t1)
    ReleaseKey(F1)
    PressKey(Esc)
    time.sleep(t2)
    ReleaseKey(Esc)