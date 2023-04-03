from class_character import *

druid = Character()
start_window()
time.sleep(3)
flag = False
#
while True:
    flag = druid.search_target(flag)
    if flag:
        druid.battle(flag)
        if flag:
            druid.loot(flag)

    if cv2.waitKey(30) == ord('g'):
        cv2.destroyAllWindow()
        break