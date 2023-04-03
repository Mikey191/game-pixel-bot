from key_mouse_func import *
from move_func import *

#ищет связку цветов в таргете для функции target_on
def detectid_color(alower, aupper, str):
    print('func detectid_color')
    lower = np.array(alower)
    upper = np.array(aupper)
    kernel = np.ones((5,5), np.uint8)

    frame = np.array(ImageGrab.grab(bbox=(195,45,300,85)))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)
    #res = cv2.bitwise_and(frame, frame, mask = mask)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_OPEN, kernel)
    edge = cv2.Canny(closing, 100, 150)
    contours, h = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse=True)
    #cv2.imshow(str, frame)
    flag = False
    try:
        if len(contours):
            p = cv2.drawContours(frame, [contours[0]], -1, (255, 0, 0), 1)
            if p[0][0][0] > 0:
                flag = True
        else:
            flag = False
    except ValueError:
        flag = False
    return flag

#есть ли выделинный таргет
def target_on():
    print('func target_on')
    # Зеленый
    lower_green = np.array([45, 255, 50])
    upper_green = np.array([62, 255, 255])
    # Желтый
    lower_yellow = np.array([29, 79, 156])
    upper_yellow = np.array([32, 255, 255])
    # красный
    lower_red = np.array([0, 0, 165])
    upper_red = np.array([2, 255, 255])
    try:
        print('детектим цвет в функции combat первый раз')
        flag_green = detectid_color(lower_green, upper_green, 'green')
        print('combat: G', flag_green)
        flag_yellow = detectid_color(lower_yellow, upper_yellow, 'yellow')
        print('combat: Y', flag_yellow)
        flag_red = detectid_color(lower_red, upper_red, 'red')
        print('combat: R', flag_red)
        if (flag_green & flag_yellow) or (flag_green & flag_red):
            flag = True
        else:
            flag = False
        return flag
    except ValueError:
        return False

#функция определения расстояния до цели что бы подойти ближе, если не достают скилы
def detect_range_target():#переделать с использованием аддона Range Display
    frame = np.array(ImageGrab.grab(bbox=(350, 555, 450, 585)))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #желтый текст для дистанции
    lower = np.array([20, 148, 149])
    upper = np.array([30, 255, 255])
    mask = cv2.inRange(hsv, lower, upper)
    #считываем текст из окошка
    temp_text = pytesseract.image_to_string(mask)
    if len(temp_text):
        temp_text_array = temp_text.split('-')
        try:
            distence_first_num = float(temp_text_array[0])
            distence_second_num = float(temp_text_array[1])
            print('distence_first_num =', distence_first_num,'\ndistence_second_num =', distence_second_num )
            if distence_first_num >= 30.0:
                step_up()
        except ValueError:
            print('считал текст с ошибкой')
    else:
        print('не смог считать!')

#функция следование мыши за таргетом
def follow_target_mouse():
    flag = False #флажек показывающий, рандомное значение или настоящее
    # Желтый
    lower = np.array([29, 79, 200])
    upper = np.array([30, 255, 255])
    kernel = np.ones((5, 5), np.uint8)
    # vertex = np.array([[165,170], [600, 170], [600, 420], [165, 420]])
    vertex = np.array([[340, 300], [460, 300], [460, 385], [340, 385]])
    cv2.namedWindow('temp_frame', cv2.WINDOW_NORMAL)
    temp_frame = np.array(ImageGrab.grab(bbox=(340, 300, 460, 385)))
    cv2.imshow('temp_frame', temp_frame)
    frame = np.array(ImageGrab.grab(bbox=(0, 30, 800, 630)))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.bilateralFilter(frame, 9, 75, 75)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # поиск по цвету
    hsv_mask = cv2.inRange(hsv, lower, upper)
    mask = vertex_mask(hsv_mask, [vertex])
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    # cv2.drawContours(image=frame, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
    if len(contours) >= 5:
        x_finish_line = contours[0][0][0][0]
        y_finish_line = contours[0][0][0][1]
        # temp_list = (x_finish_line, y_finish_line)
        # follow_mouse_to_cor_target(x_finish_line + 5, y_finish_line + 30)
        print('Координаты со смещением: \nx =', x_finish_line, '\ny =', y_finish_line)
        flag = True
        return x_finish_line, y_finish_line, flag
    else:
        #рандомные значения из круга вокруг
        x_finish_line = random.randint(360, 440)
        y_finish_line = random.randint(285, 340)
        flag = False
        print('Координаты с рандома: \nx =', x_finish_line, '\ny =', y_finish_line)
        return x_finish_line, y_finish_line, flag
    cv2.imshow('mask', mask)

def battle_end():
    flag = target_on()
    return flag