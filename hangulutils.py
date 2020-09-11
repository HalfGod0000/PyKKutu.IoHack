import keyboard
import random
import time

try:
    import pyautogui as pag
except:
    print("pyautogui 모듈을 다운로드하세요!")
try:
    import keyboard
except:
    print("keyboard 모듈을 다운로드하세요!")

print("""
이건 끄투리오 서버용 핵입니다
이것을 끄투코리아 서버에서 사용은 불가합니다
만약 당신이 단어라는 입력창이 뜨지 않은 상태에서 f키를 누르면 입력창으로 이동합니다
편리한 기능이죠
당신이 backspace키를 누르게 되면 입력창이 뜨고 첫 글자를 쓰면 문장을 자동으로 쳐줍니다
이제 사용하세요!!
""")



f = open('kkutuword.txt', mode='rt')
f
result = [line.strip() for line in f.readlines()]
while True:
    if keyboard.is_pressed('backspace'):
        if keyboard.is_pressed('f'):
            pag.leftClick(1424, 897)
        word = input('단어: ')
        for i in result:
            a = random.choice(result)

            if a.startswith(word) and not a.endswith(']') and not a.endswith('}'):
                pag.leftClick(840, 975)
                time.sleep(0.01)
                keyboard.write(a)
                print(a)
                if a.endswith(")"):
                    pag.press('backspace')
                    pag.press('backspace')
                    pag.press('backspace')
                    pag.press('backspace')
                    pag.press('backspace')
                    pag.press('backspace')
                if keyboard.is_pressed('f'):
                    pag.press('backspace')
                    pag.leftClick(1424, 897)
                break
    if keyboard.is_pressed('f'):
        pag.press('backspace')
        pag.leftClick(1424, 897)
    if keyboard.is_pressed('h'):
        pag.leftClick(790, 37)
        pag.leftClick(1040, 18)
