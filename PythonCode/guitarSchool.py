import sys
import threading
import time
import signal
import random
import timerInput

def giveScaleNameQuestion(diff):
    # diff = difficulty. ( 1, 2, 3, 4 )
    kor = ['도', '도#', '레b', '레', '레#', '미b', '미', '파', '파#', '솔b', '솔', '솔#', '라b', '라', '라#', '시b', '시']
    en = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']
    
    errKor = ['도b', '미#', '파b', '시#']
    errEn = ['Cb', 'E#', 'Fb', 'B#']

    if diff == 1:
        idx = random.randrange(0, len(kor))
        ke = random.randrange(0, 2)
        if ke == 0:
            print(kor[idx] + "을/를 영어로 바꾸면?")
            return en[idx]
        else :
            print(en[idx] + "을/를 한글로 바꾸면?")
            return kor[idx]

while(True):
    print("듣고싶은 강의의 숫자를 입력하세요. ")
    print("1. ABC to 도레미")
    print("2. Code 보기")

    num = timerInput.timerInput(10)
    try:
        num = int(num)
    except:
        print("숫자만 입력 하세요.")
        continue

    a = giveScaleNameQuestion(1)
    answer = timerInput.timerInput(10)
    print(a)
    print(answer)

