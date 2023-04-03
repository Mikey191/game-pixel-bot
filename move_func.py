import cv2
import numpy as np
from PIL import ImageGrab
import pytesseract
import random
import time
from ctype_keyboard import PressKey, ReleaseKey, W, A, S, D, Q, E, Space, TAB, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, Esc

#маска для поиска для функции follow_target
def vertex_mask(screen, vertex):
    temp_mask = np.zeros_like(screen)
    cv2.fillPoly(temp_mask, vertex, 255)
    mask = cv2.bitwise_and(screen, temp_mask)
    return mask

#функция прохода до нужной точки
def move_p2p(path_coord, s_1, s_2, stop_flag):
    print('+++++++++++++++++++++')
    x_finish = path_coord[0][0]
    y_finish = path_coord[0][1]
    print('x_finish =', x_finish)
    print('y_finish =', y_finish)
    # окно для считывания координат
    window_cord = np.array(ImageGrab.grab(bbox=(340, 32, 500, 65)))
    print('окно считалось')
    cv2.imshow('w_c', window_cord)
    temp_text = pytesseract.image_to_string(window_cord)
    print('перевел в текст: ', temp_text)
    # элемент рандома
    # t1 = random.uniform(0.5, 1.5)
    t2 = random.uniform(0.1, 0.2)
    t3 = random.uniform(0.1, 0.2)
    try:
        temp_text_array = temp_text.split(',')
        x_start = float(temp_text_array[0])
        print('x_start =', x_start)
        y_start = float(temp_text_array[1])
        print('y_start =', y_start)
        # находим кратчайший путь между точками
        s_2 = np.sqrt((x_start - x_finish) ** 2 + (y_start - y_finish) ** 2)
        print('путь s_1 =', s_1)
        print('путь s_2 =', s_2)
        if s_2 < 1.032:
            print('stop')
            ReleaseKey(W)
            ReleaseKey(A)
            ReleaseKey(S)
            ReleaseKey(D)
            stop_flag = True
        elif s_2 < s_1:
            print('s_2 < s_1, press W')
            PressKey(W)
        elif s_2 == s_1:
            print('s_1 == s_2, press Q or E 0.7 sec')
            ReleaseKey(W)
            PressKey(S)
            time.sleep(0.2)
            ReleaseKey(S)
            PressKey(Q)
            time.sleep(t2)
            ReleaseKey(Q)
        elif s_2 > s_1:
            print('s_2 > s_1, press D+W')
            ReleaseKey(W)
            PressKey(Q)
            PressKey(A)
            time.sleep(t3)
            ReleaseKey(A)
            ReleaseKey(Q)
        else:
            pass
        s_1 = s_2
    except ValueError:
        pass
    return s_1, stop_flag