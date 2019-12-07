# Guitar Scale name.

korScale = ['도', '도#', '레', '레#', '미', '파', '파#', '솔', '솔#', '라', '라#', '시']
enScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
standardTunning = [4, 9, 2, 7, 11, 4]

def makeHandShape(handLoc):
    '''
    '''
    high = 0
    low = 36
    # Real scale of Hand Shape.
    handShape = []

    for loc in handLoc:
        if loc > high:
            high = loc
        if loc < low and loc != -1:
            low = loc
    
    for _ in range(low, high + 1):
        handShape.append([0, 0, 0, 0, 0, 0])

    for i in range(0, 6):
        if handLoc[i] != -1:
            handShape[handLoc[i] - low][i] = 1
    return high, low, handShape

def makeHandShapeList(high, low, handLocList):
    '''
    Make Hand shape with given max-min list.
    Elemental of hand location list is not high-low lengt
    '''
    length = high - low + 1

    for i in range(0, len(handLocList)):
        if len(handLocList[i]) != length:
            for _ in range(0, length - len(handLocList[i])):
                handLocList[i].append([0, 0, 0, 0, 0])

    return handLocList

def showCodeName(codeName, tail="_", end=""):
    cn = codeName

    while len(cn) < 6:
        cn = cn + tail

    if len(cn) == 8:
        print(cn, end=end)
    elif len(cn) == 7:
        print("[" + cn, end=end)
    else:
        print("[" + cn + "]", end=end)

def showCode(handLoc, finger=1):
    '''
    Show code with hand location input.
    '''
    high, low, handShape = makeHandShape(handLoc)
    
    if finger == 1:
        # Type 1
        f = "O"
    elif finger == 2:
        # Type 2
        f = "○"
    else:
        print("Finger type error.")

    for j in range(low - low, high + 1 - low):
        if j < 10:
            print(str(j) + " ", end="")
        else :
            print(str(j), end="")

        for i in range(0, 6):
            if handShape[j][i] == 1:
                print(f, end="")
                continue
            # If not scaled..
            if j == low - low:
                if i == 0:
                    print("┌", end="")
                elif i == 5:
                    print("┐", end="")
                else:
                    print("┬", end="")

            elif j == high - low:
                if i == 0:
                    print("└", end="")
                elif i == 5:
                    print("┘", end="")
                else:
                    print("┴", end="")
            else:
                print("│", end="")
        print("")

def showCodeWithName(codeName, handLoc, tail="-", finger=1, end=""):
    showCodeName(codeName, tail=tail, end=end)
    showCode(handLoc, finger=finger)
    print("")


def showCodeHo(codeList, level=5, finger=1):
    '''
    Show hand location with given list 'codeList' with 'level' number.
    ARGV:
        codeList : want to show Code form.
        level : want to show how many code form with horizontally.
    RAISE:
        nothing.
    RETURN:
        nothing.
    '''
    if finger == 1:
        # Type 1
        f = "O"
    elif finger == 2:
        # Type 2
        f = "○"
    else:
        print("Finger type error.")

    lowList = []
    handShapeList = []

    for handLoc in codeList:
        _, low, handShape = makeHandShape(handLoc)
        lowList.append(low)
        handShapeList.append(handShape)

    printList = []
    
    for i in range(0, len(lowList)):
        # Change hand shape and high-low data to printing list.
        tempData = []
        for j in range(0, len(handShapeList[i])):
            tempRow = []
            if lowList[i] + j < 10:
                tempRow.append(str(lowList[i] + j) + " ")
            else:
                tempRow.append(str(lowList[i] + j))
            tempRow += handShapeList[i][j]
            tempData.append(tempRow)
        printList.append(tempData)
    
    for i in range(0, int(len(printList) / level) + 1):
        if i != int(len(printList) / level):
            # Get Max row for index 0  to level - 1.
            maxRow = 0
            for pl in printList[0 + i * level : (i + 1) * level -1]:
                if maxRow < len(pl):
                    maxRow = len(pl)
            for l in range(0, maxRow):
                for j in range(0, level):
                    if l == 0:
                        print(printList[j + i*level][l][0], end="")
                        for k in range(1, 7):
                            if printList[j + i*level][l][k] == 1:
                                print(f, end="")
                            else:
                                if k == 1:
                                    print("┌", end="")
                                elif k == 6:
                                    print("┐", end="")
                                else:
                                    print("┬", end="")
                    elif l == len(printList[j + i*level]) - 1 or l == maxRow - 1:
                        try:
                            print(printList[j + i*level][l][0], end="")
                        except:
                            print("  ", end="")
                        for k in range(1, 7):
                            try:
                                if printList[j + i*level][l][k] == 1:
                                    print(f, end="")
                                else:
                                    if k == 1:
                                        print("└", end="")
                                    elif k == 6:
                                        print("┘", end="")
                                    else:
                                        print("┴", end="")
                            except:
                                print(" ", end="")
                    else:
                        try:
                            print(printList[j + i*level][l][0], end="")
                        except:
                            print("  ", end="")
                        for k in range(1, 7):
                            try:
                                if printList[j + i*level][l][k] == 1:
                                    print(f, end="")
                                else:
                                    print("│", end="")
                            except:
                                print(" ", end="")
                    print(" ", end="") # For space with horizon-code.
                print("")   # For next line.
    else:
        if len(printList) % level != 0:
            # Get Max row for index 0  to level - 1.
            maxRow = 0
            length = len(printList[i * level:]) # Length of i * level to end.

            for pl in printList[i * level:]:
                if maxRow < len(pl):
                    maxRow = len(pl)
            for l in range(0, maxRow):
                for j in range(0, length):
                    if l == 0:
                        print(printList[j + i*level][l][0], end="")
                        for k in range(1, 7):
                            if printList[j + i*level][l][k] == 1:
                                print(f, end="")
                            else:
                                if k == 1:
                                    print("┌", end="")
                                elif k == 6:
                                    print("┐", end="")
                                else:
                                    print("┬", end="")
                    elif l == len(printList[j + i*level]) - 1 or l == maxRow - 1:
                        try:
                            print(printList[j + i*level][l][0], end="")
                        except:
                            print("  ", end="")
                        for k in range(1, 7):
                            try:
                                if printList[j + i*level][l][k] == 1:
                                    print(f, end="")
                                else:
                                    if k == 1:
                                        print("└", end="")
                                    elif k == 6:
                                        print("┘", end="")
                                    else:
                                        print("┴", end="")
                            except:
                                print(" ", end="")
                    else:
                        try:
                            print(printList[j + i*level][l][0], end="")
                        except:
                            print("  ", end="")
                        for k in range(1, 7):
                            try:
                                if printList[j + i*level][l][k] == 1:
                                    print(f, end="")
                                else:
                                    print("│", end="")
                            except:
                                print(" ", end="")
                    print(" ", end="") # For space with horizon-code.
                print("")   # For next line.

def showCodeWithNameHo(codeName, codeList, tail="_", level=5, finger=1, end=""):
    '''
    Show hand location with given list 'codeList' with 'level' number.
    ARGV:
        codeList : want to show Code form.
        level : want to show how many code form with horizontally.
    RAISE:
        nothing.
    RETURN:
        nothing.
    '''
    if finger == 1:
        # Type 1
        f = "O"
    elif finger == 2:
        # Type 2
        f = "○"
    else:
        print("Finger type error.")

    lowList = []
    handShapeList = []

    for handLoc in codeList:
        _, low, handShape = makeHandShape(handLoc)
        lowList.append(low)
        handShapeList.append(handShape)

    printList = []
    
    for i in range(0, len(lowList)):
        # Change hand shape and high-low data to printing list.
        tempData = []
        for j in range(0, len(handShapeList[i])):
            tempRow = []
            if lowList[i] + j < 10:
                tempRow.append(str(lowList[i] + j) + " ")
            else:
                tempRow.append(str(lowList[i] + j))
            tempRow += handShapeList[i][j]
            tempData.append(tempRow)
        printList.append(tempData)
    
    for i in range(0, int(len(printList) / level) + 1):
        if i != int(len(printList) / level):
            # Get Max row for index 0  to level - 1.
            maxRow = 0

            for j in range(0, level):
                showCodeName(codeName[j + i * level], tail=tail, end=end)
                print(" ", end=end)
            print("")

            for pl in printList[0 + i * level : (i + 1) * level -1]:
                if maxRow < len(pl):
                    maxRow = len(pl)

            for l in range(0, maxRow):
                for j in range(0, level):
                    if l == 0:
                        print(printList[j + i*level][l][0], end="")
                        for k in range(1, 7):
                            if printList[j + i*level][l][k] == 1:
                                print(f, end="")
                            else:
                                if k == 1:
                                    print("┌", end="")
                                elif k == 6:
                                    print("┐", end="")
                                else:
                                    print("┬", end="")

                    elif l == len(printList[j + i*level]) - 1 or l == maxRow - 1:
                        try:
                            print(printList[j + i*level][l][0], end="")
                        except:
                            print("  ", end="")
                        for k in range(1, 7):
                            try:
                                if printList[j + i*level][l][k] == 1:
                                    print(f, end="")
                                else:
                                    if k == 1:
                                        print("└", end="")
                                    elif k == 6:
                                        print("┘", end="")
                                    else:
                                        print("┴", end="")
                            except:
                                print(" ", end="")
                    else:
                        try:
                            print(printList[j + i*level][l][0], end="")
                        except:
                            print("  ", end="")
                        for k in range(1, 7):
                            try:
                                if printList[j + i*level][l][k] == 1:
                                    print(f, end="")
                                else:
                                    print("│", end="")
                            except:
                                print(" ", end="")
                    print(" ", end="") # For space with horizon-code.
                print("")   # For next line.
    else:
        if len(printList) % level != 0:
            # Get Max row for index 0  to level - 1.
            maxRow = 0
            length = len(printList[i * level:]) # Length of i * level to end.

            for j in range(0, length):
                showCodeName(codeName[j + i * level], tail=tail, end=end)
                print(" ", end=end)
            print("")

            for pl in printList[i * level:]:
                if maxRow < len(pl):
                    maxRow = len(pl)
            for l in range(0, maxRow):
                for j in range(0, length):
                    if l == 0:
                        print(printList[j + i*level][l][0], end="")
                        for k in range(1, 7):
                            if printList[j + i*level][l][k] == 1:
                                print(f, end="")
                            else:
                                if k == 1:
                                    print("┌", end="")
                                elif k == 6:
                                    print("┐", end="")
                                else:
                                    print("┬", end="")
                    elif l == len(printList[j + i*level]) - 1 or l == maxRow - 1:
                        try:
                            print(printList[j + i*level][l][0], end="")
                        except:
                            print("  ", end="")
                        for k in range(1, 7):
                            try:
                                if printList[j + i*level][l][k] == 1:
                                    print(f, end="")
                                else:
                                    if k == 1:
                                        print("└", end="")
                                    elif k == 6:
                                        print("┘", end="")
                                    else:
                                        print("┴", end="")
                            except:
                                print(" ", end="")
                    else:
                        try:
                            print(printList[j + i*level][l][0], end="")
                        except:
                            print("  ", end="")
                        for k in range(1, 7):
                            try:
                                if printList[j + i*level][l][k] == 1:
                                    print(f, end="")
                                else:
                                    print("│", end="")
                            except:
                                print(" ", end="")
                    print(" ", end="") # For space with horizon-code.
                print("")   # For next line.

def getScaleName(handLoc):
    '''
    Return english scale of give hand location.
    '''
    _, _, handShape = makeHandShape(handLoc)
    # Standard Tunning.
    tScale = [4, 9, 2, 7, 11, 4]
    scale = []
    for i in range(0, 6):
        if handLoc[i] != -1:
            scale.append((tScale[i] + handLoc[i]) % len(enScale))
        else:
            scale.append("X")

    nameScale = []
    for i in scale:
        try:
            nameScale.append(enScale[i])
        except:
            nameScale.append("X")
    return nameScale

def changeScaleLang(kor=None, en=None):
    '''
    Change scale language to Korean <-> English.
    ARGV:
        kor : korean scale.
        en : english scale.
    RAISE:
        nothing:
    RETURN:
        k to e scale or e to k scale.
        if input is wrong, return empty list.
    '''
    ret = []
    if kor != None:
        for k in kor:
            try:
                ret.append(enScale[korScale.index(k)])
            except:
                ret.append("X")
    elif en != None:
        for e in en:
            try:
                ret.append(korScale[enScale.index(e)])
            except:
                ret.append("X")
    return ret

