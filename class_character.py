from func_for_battle import *
from func_for_search import *
from func_for_loot import *
from move_func import *

class Character:
    # path_coord = [[28.99, 21.66]] #ЯЛ
    # path_coord = [[38.79, 38.50]] #ТБ
    path_coord = [[56.17, 45.28]] #ТДС
    # path_coord = [[28.79, 38.61]] #ДПЛ

    #конструктор __init__ формирует полный список координат из файла (csv)

    #перемещение по точка с добавлением координат в список в классе
    def p2p(self, path_coord):
        s_start = 0
        s_change = 0
        stop_flag = False
        # дойти до нужной точки используя координаты из массива
        for i in range(len(path_coord)):
            # s_1 = move_start_point(path_coord)
            while stop_flag != True:
                s_start, stop_flag = move_p2p(path_coord, s_start, s_change, stop_flag)
                # stop_flag = move_p2p(path_coord, s_start, s_change, stop_flag)
                if cv2.waitKey(30) == ord('g'):
                    cv2.destroyAllWindows()
                    break
            # path_coord.pop(0) #раскоментить, когда добавляешь большой список точек
            stop_flag = False

    def search_target(self, flag_battle):
        flag_battle = battle_end()
        while not flag_battle:
            detectid_mobs(self.path_coord)
            flag_battle = battle_end()
        return flag_battle

    @staticmethod
    def battle(flag_battle):
        flag_battle = battle_end()
        click_but(SEVEN, 0.1)
        while flag_battle:
            detect_range_target()
            attack()
            flag_battle = battle_end()
        return flag_battle

    @staticmethod
    def loot(flag_battle):
        loot_for()
        clear_target()
        flag_battle = battle_end()
        return flag_battle