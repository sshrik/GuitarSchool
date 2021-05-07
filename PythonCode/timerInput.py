import time
import select
import sys
import termios, atexit 

# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
# ICANON = Non-canonical mode.
# ~ mean bit flip, like 0001 to 1110
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def timerInput(timer):
    ret = ''
    nowTime = time.time()

    while True:
        if time.time() - nowTime > timer:
            break
        if kbhit():
            _ch = getch()
            if ord(_ch) == ord("\b"):
                sys.stdin.write('\n')
                ret = ret[0:-1]
                putch(ret, flush=True)
            if ord(_ch) == ord("\n"):
                break;
            else:
                ret += _ch
                putch(ret)
    print("\n")
    set_normal_term()
    return ret

def getch(readByte=1):
    return sys.stdin.read(readByte)

def kbhit():
    set_curses_term()
    dr, _, _ = select.select([sys.stdin], [], [], 0)
    # Return if dr is same with empty list.
    return dr != []

def putch(_ch, flush=False):
    if flush:
        sys.stdout.write('\r')
        for _ in range(0, len(_ch)):
            sys.stdout.write(' ')
            sys.stdout.flush()
    sys.stdout.write('\r' + _ch)
    sys.stdout.flush()

atexit.register(set_normal_term)
