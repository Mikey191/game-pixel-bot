import mouse
from ctype_keyboard import PressKey, ReleaseKey, W, A, S, D, Q, E, Space, TAB, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, Esc, F1
import random
import time
import numpy as np

def start_window():
    t = random.random()
    print('до старта бота %.f2 секунд' %t)
    mouse.move(400, 300, absolute=True, duration=t)
    mouse.click(button='left')

def mouse_target(x_line_mob, y_line_mob):
    ReleaseKey(W)
    if x_line_mob <= 300:
        mouse.move(x_line_mob - 25, y_line_mob + 30, absolute=True, duration=0.2)
    elif x_line_mob >= 500:
        mouse.move(x_line_mob + 25, y_line_mob + 30, absolute=True, duration=0.2)
    else:
        mouse.move(x_line_mob, y_line_mob + 25, absolute=True, duration=0.2)
    mouse.press(button='right')
    time.sleep(0.1)
    mouse.release(button='right')
    mouse.move(400, 300, absolute=True, duration=0.2)

def click_but(key, t):
    PressKey(key)
    time.sleep(t)
    ReleaseKey(key)

def attack():
    print('func attak')
    t1 = random.uniform(0.1, 0.3)
    t2 = random.uniform(1.0, 2.0)
    PressKey(ONE)
    time.sleep(t1)
    ReleaseKey(ONE)
    time.sleep(t2)

def chek_buffs_mage():
    print('1')

def turn_180():
    print('func turn_pers_180')
    lst = [A, D]
    t1 = random.uniform(0.4, 0.6)
    ad = random.choice(lst)
    PressKey(ad)
    time.sleep(t1)
    ReleaseKey(ad)

def turn_right_top():
    t = random.uniform(0.15, 0.25)
    print('A', t)
    PressKey(D)
    time.sleep(t)
    ReleaseKey(D)

def turn_right_bot():
    t = random.uniform(0.4, 0.6)
    print('A', t)
    PressKey(D)
    time.sleep(t)
    ReleaseKey(D)

def turn_left_top():
    t = random.uniform(0.15, 0.25)
    print('D', t)
    PressKey(A)
    time.sleep(t)
    ReleaseKey(A)

def turn_left_bot():
    t = random.uniform(0.4, 0.6)
    print('D', t)
    PressKey(A)
    time.sleep(t)
    ReleaseKey(A)

def search_mob_right():
    print('func: search_mob_right(key_mouse_func)')
    t2 = random.uniform(0.2, 0.4)
    PressKey(W)
    PressKey(D)
    time.sleep(t2)
    ReleaseKey(D)

def search_mob_left():
    print('func: search_mob_left(key_mouse_func)')
    t2 = random.uniform(0.2, 0.4)
    PressKey(W)
    PressKey(A)
    time.sleep(t2)
    ReleaseKey(A)

def step_up():
    t = random.uniform(0.3, 0.6)
    PressKey(W)
    time.sleep(t)
    ReleaseKey(W)

def looting_start(dir):
    t = random.random()
    mouse.move(400, 320, absolute=True, duration=t)
    if dir == 'left-top':
        mouse.move(-30, 0, absolute=False, duration=0.1)
    elif dir == 'right-top':
        mouse.move(30, 0, absolute=False, duration=0.1)
    elif dir == 'right-bot':
        mouse.move(30, 0, absolute=False, duration=0.1)
    elif dir == 'left-bot':
        mouse.move(-30, 0, absolute=False, duration=0.1)

def looting_finish():
    mouse.press(button='right')
    time.sleep(0.3)
    mouse.release(button='right')
    time.sleep(0.5)
    PressKey(F1)
    time.sleep(0.4)
    ReleaseKey(F1)
    PressKey(Esc)
    time.sleep(0.2)
    ReleaseKey(F1)

def follow_mouse_to_cor_target(x, y):
    t = random.uniform(0.1, 0.3)
    t2 = random.uniform(0.5, 0.9)
    mouse.move(x, y, absolute=True, duration=t)
    time.sleep(t2)

def turn_pers_180():
    print('func turn_pers_180')
    lst = [A, D]
    t1 = random.uniform(0.8, 1.1)
    t2 = random.uniform(1.5, 1.8)
    ad = random.choice(lst)
    PressKey(ad)
    time.sleep(t1)
    ReleaseKey(ad)
    PressKey(W)
    time.sleep(t2)
    ReleaseKey(W)

def chek_circle_around_pers(x_mouse, y_mouse):
    # flag = False
    x_start = 400
    y_start = 350
    x_finish = 440
    y_finish = 295
    r_circle = np.sqrt((x_start - x_finish)**2 + (y_start - y_finish)**2)
    r_mouse_point = np.sqrt((x_start - x_mouse)**2 + (y_start - y_mouse)**2)
    if r_circle >= r_mouse_point:
        flag = True
    else:
        flag = False

    return flag