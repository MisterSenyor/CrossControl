import pyautogui, keyboard

pyautogui.FAILSAFE = False

def handle_mouse(src, dst, msg):

    try:
        msg = msg.decode('utf-8')
        mode = msg[0]

        # position in format xxxx yyyy (for example 05000400 for x=500, y=400)
        # position in format xxxx yyyy (for example 05000400 for x=500, y=400)
        x = int(msg[1:5])
        y = int(msg[5:9])
        pos = (x, y)

        if mode == 'M':
            pyautogui.moveTo(pos)
        elif mode == 'L':
            pyautogui.click(pos, button='left')
        elif mode == 'R':
            pyautogui.click(pos, button='right')
    except:
        pass


def handle_keyboard(src, dst, msg):
    try:
        msg = msg.decode('utf-8')
        mode = msg[0]
        data = msg[1:]

        if mode == 'W':
            keyboard.write(data)
        elif mode == 'P':
            keyboard.press_and_release(data)
    except:
        pass
