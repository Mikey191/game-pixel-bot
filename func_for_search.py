from key_mouse_func import *
from move_func import *

#проверяет квадрат в котором находится герой
def chek_square(x_start, y_start):
    try:
        R = 1.032 # находится вручную
        window_cord = np.array(ImageGrab.grab(bbox=(300, 32, 500, 65)))
        # cv2.imshow('c_s', window_cord)
        temp_text = pytesseract.image_to_string(window_cord)
        temp_text_array = temp_text.split(',')
        x_finish = float(temp_text_array[0])
        y_finish = float(temp_text_array[1])
        length = np.sqrt((x_finish - x_start)**2+(y_finish - y_start)**2)
        if length <= R:
            print('В круге.')
            int_flag = 1
        else:
            print('Вышел из круга!!!')
            int_flag = 2
    except ValueError:
        print('Не считал координаты')
        int_flag = 3
    return int_flag

#   функция рисуте линию от перса до моба и возвращает координаты начала и конца линии
def draw_line_to_mob(pointers_array):
    print('func detect(ходим ищем мобов)')
    x_finish = pointers_array[0][0]
    y_finish = pointers_array[0][1]
    flag_square = chek_square(x_finish, y_finish)
    print('detect: int_flag =', flag_square)
    if flag_square == 1:
        kernel = np.ones((5, 5), np.uint8)
        #цвет желтых мобов
        lower = np.array([22, 255, 169])
        upper = np.array([38, 255, 255])
        # цвет красных мобов
        # lower = np.array([1, 100, 100])
        # upper = np.array([10, 255, 255])
        #создаем экран для считывания и преобразовываем
        # vertex = np.array([[360, 365], [175, 150], [615, 150], [435, 365]])
        frame = np.array(ImageGrab.grab(bbox=(0, 30, 800, 630)))
        # frame = np.array(ImageGrab.grab(bbox=(0, 90, 800, 450)))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.bilateralFilter(frame, 9, 75, 75)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        #поиск по цвету
        hsv_mask = cv2.inRange(hsv, lower, upper)
        # vertex = np.array([[400, 300], [0, 200], [800, 200], [400, 300]])
        # vertex = np.array([[330,480],[0,335],[0,150],[800,150],[800,335],[460,480]])
        vertex = np.array([[0, 150], [700, 150], [700, 450], [0, 450]])#вертекс аркан мага
        mask = vertex_mask(hsv_mask, [vertex])
        # res = cv2.bitwise_and(frame, frame, mask=mask)
        opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        contours, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        # contours = sorted(contours, key=cv2.contourArea, reverse=False) # перед персом
        # contours = sorted(contours, key=cv2.contourArea, reverse=True)  # по бокам
        # cv2.drawContours(image=frame, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2, lineType=cv2.LINE_AA)
        x_start_line = 400
        y_start_line = 300
        if len(contours):
            x_finish_line = contours[0][0][0][0]
            # print('x =', contours[0][0][0][0])
            y_finish_line = contours[0][0][0][1]
            # print('y =', contours[0][0][0][1])
            cv2.line(frame, (x_start_line, y_start_line), (x_finish_line, y_finish_line), [255, 0, 255], 1)
        else:
            print('draw_line_to_mob нет линии')
            x_finish_line = 400
            y_finish_line = 300

        cv2.imshow('frame', frame)
        cv2.imshow('mask', mask)
        return x_start_line, y_start_line, x_finish_line, y_finish_line
    elif flag_square == 2:
        s_start = 0
        s_change = 0
        stop_flag = False
        while stop_flag != True:
            s_start, stop_flag = move_p2p(pointers_array, s_start, s_change, stop_flag)
        return 0, 0, 0, 0
    else:
        print('detect: пропуск')
        return 0, 0, 0, 0

#проверяет длину линии
def chek_line(x_start, y_start, x_finish, y_finish):
    length = np.sqrt((x_start - x_finish)**2 + (y_start - y_finish)**2)
    print("chek_line: Длина линии до моба: ", length)
    if length > 1:
        flag = True
    else:
        flag = False
    return flag, length

#функция проверяет угол между прямой и линией до мобстера
def flag_corner(x_1, y_1):
    #проверка на квадрат, где находится моб
    if x_1 < 400 and y_1 < 330:
        turn_left_top()
    elif x_1 > 400 and y_1 < 330:
        turn_right_top()
    elif x_1 > 400 and y_1 > 330:
        turn_right_bot()
    elif x_1 < 400 and y_1 > 330:
        turn_left_bot()

# функция ищет мобов если есть линия до них
def detectid_mobs(pointers_array):
    k = random.randint(0, 1)
    #получаем координаты из функции draw_line_to_mob
    x_start_line, y_start_line, x_finish_line, y_finish_line = draw_line_to_mob(pointers_array)
    #проверяем через функция chek_line
    flag_mob, length = chek_line(x_start_line, y_start_line, x_finish_line, y_finish_line)
    if flag_mob:
        mouse_target(x_finish_line, y_finish_line)
        flag_corner(x_finish_line, y_finish_line)
    else:
        if k == 0:
            search_mob_right()
        else:
            search_mob_left()