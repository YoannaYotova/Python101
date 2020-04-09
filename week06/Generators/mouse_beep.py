def mouse_pos():
    import pyautogui

    yield pyautogui.position()

import os

def beep():
    duration = 0.2
    freq = 400
    # os.system('spd-say "yoanna is super cool"')
    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
    return ()


def main(): 
    mouse = mouse_pos()
    beep()
    print(next(mouse.x))


if __name__ == '__main__':
    main()

