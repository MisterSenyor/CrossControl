import pyautogui, keyboard, socket

pyautogui.FAILSAFE = False

def handle_command(src, dst, msg):
    try:
        msg = msg.decode('utf-8')
        device_type = msg[0]
        mode = msg[1]
        if device_type == "M":
            # position in format xxxx yyyy (for example 05000400 for x=500, y=400)
            x = int(msg[2:6])
            y = int(msg[6:10])
            pos = (x, y)

            if mode == 'M':
                pyautogui.moveTo(pos)
            elif mode == 'L':
                pyautogui.click(pos, button='left')
            elif mode == 'R':
                pyautogui.click(pos, button='right')
            elif mode == 'D':
                pyautogui.dragTo(pos)

        elif device_type == "K":
            data = msg[2:]
            if mode == 'W':
                keyboard.write(data)
            elif mode == 'P':
                keyboard.press_and_release(data)
    except Exception as e:
        print(f"RAN INTO EXCEPTION: {e}")