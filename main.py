from time import sleep
import win32api, win32con

def exep(func):
    def wrap(*args, **kwargs):
        try: func()
        except: raise
        else: return 200
    return wrap

def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    sleep(.002)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
    return 200

def key_click(key):
    if win32api.GetKeyState(key) != 0:
        return 1
    else: return 0
    
@exep
def main():
    # thread = win32api.GetCurrentThread()
    # print(thread)
    # print(win32api.GetKeyboardLayout(thread))
    # print(win32api.GetKeyboardLayoutList())
    # print(win32api.GetKeyboardLayoutName())
    # print(win32api.GetKeyboardState())
    # print(win32api.GetKeyState(0x41))
    
    '''
    a = win32api.GetKeyState(0x41)
    print(a)
    if a:
        print(200)
    '''
    
    duration = .002
    
    while True:    
        sleep(duration)
        print(key_click(0x4A))
        
        if key_click(0x4A):
            while True:
                click()
                if key_click: break
    
if __name__ == "__main__":
    print("OK")
    main()
    