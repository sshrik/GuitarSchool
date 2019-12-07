import codeFile
import showCode
import timerProgress

def getCodeMainScale(code):
    '''
    extract code scale.
    '''
    exScale = []
    scode = codeFile.searchCodeWithName(code)
    # scode is all hand location of give code "code".
    for handLoc in scode:
        scale = showCode.getScaleName(handLoc)
        if len(scale) == 0:
            return exScale
        for s in scale:
            if s not in exScale:
                exScale.append(s)
    if "X" in exScale:
        del exScale[exScale.index("X")]
    return exScale

def listCombination(list1):
    ret = []
    if len(list1) > 1:
        retV = listCombination(list1[1:])
        baseList = list1[0]
        for l1 in list1[0]:
            for _retV in retV:
                tempList = []
                tempList.append(l1)
                ret.append(tempList + _retV)
        return ret
    else:
        for l1 in list1[0]:
            tempList = []
            tempList.append(l1)
            ret.append(tempList)
        return ret

def listCompare(list1, list2):
    ret = 0
    non = 0
    for l in list1:
        if l != -1:
            non += 1
            if l in list2:
                ret += 1

    return ret / non

def codeGenerate(exScale, startB=0, endB=-1):
    '''
    Code generator with scale "exScale".
    exScale : scale list which consist code.
    startB : start limit fingerboard, deafult 0.
    endB : end fingerboard, default start board + 5; or does not set.
    '''
    if endB == -1:
        endB=startB+5

    base = showCode.standardTunning
    possibleLoc = []
    for _ in range(0, 6):
        possibleLoc.append([-1])

    # Search all scale location canddiate.
    for st in range(0, 6):
        for fi in range(startB, endB+1):
            if showCode.enScale[(base[st] + fi) % len(showCode.enScale)] in exScale:
                possibleLoc[st].append(fi)
                
    return listCombination(possibleLoc)

def getBase(list1):
    '''
    Get base code form. [-1, -1, -1, 2, 3, 2] to [-1, -1, -1, 0, 1, 0]
    If code form set with -1, return empty.
    '''
    # Appropriate large number setting to small.
    small = 100
    ret = []
    
    for l in list1:
        if l != -1 and l < small:
            small = l
    
    if small == 100:
        return list1

    for l in list1:
        if l != -1:
            ret.append(l - small)
        else:
            ret.append(-1)

    return ret

def getCodeFormSim(list1, list2, X=1):
    '''
    Get base form of two hand location list1, 2 and get simmilarity of 2 hand form.
    if X with setting -1, except does not ringing string. ( Default do not except )
    '''
    bList1 = getBase(list1)
    bList2 = getBase(list2)
    
    if len(bList1) == 0 or len(bList2) == 0:
        print("Error from get base.")
        return 1

    simmil = 0

    if X == -1:
        for i in range(0, len(list1)):
            if bList1[i] != -1 and bList2[i] != -1:
                simmil += (bList[i] - bList2[i]) ** 2
    else :
        for i in range(0, len(list1)):
            simmil += (bList1[i] - bList2[i]) ** 2
    
    return simmil

def codeAvailable(codeForm, mainScale, man=80, simLim=2):
    '''
    Check if given "codeForm" can be real code form.
    1. Need more "man"% code scale ratio.
    or
    2. Need max sim with exist codes more than "sim"%.
    '''
    exScale = showCode.getScaleName(codeForm)
    scaleSim = listCompare(exScale, mainScale) # Get how many scale`s sound in exScale is in mainScale.
    codeName, handLoc = codeFile.readFile()
    simMin = ( 5 ** 2 )* 6 # 5칸 떨어진 것이 6줄.
    i = 0
    index = i

    for h in handLoc:
        sim = getCodeFormSim(codeForm, h)
        if simMin > sim:
            simMin = sim
            index = i
        i += 1
    if simMin < simLim :
        if scaleSim * 100 > man :
            return 0, handLoc[index], codeName[index]
        else :
            return 1, handLoc[index], codeName[index]
    else :
        if scaleSim * 100 > man :
            return 3, handLoc[index], codeName[index]
        else :
            return 4, handLoc[index], codeName[index]
    
if __name__ == "__main__":
    print("Code generater manager.")
    code = input("Input code : ")
    exScale = getCodeMainScale(code)
    locCand = codeGenerate(exScale, startB=0, endB=20)

    codeForm = codeFile.searchCodeWithName(code)    
    showCode.showCodeHo(codeForm)

    locAns = []
    locSim = []
    locSimCode = []
    
    p = timerProgress.Progress(len(locCand))

    p.showProgressTimer()
    for c in locCand:
        ret, code, name = codeAvailable(c, exScale)
        p.addProgress()
        if ret == 0:
            locAns.append(c)
            locSim.append(name)
            locSimCode.append(code)
    p.timerJoin()
    showCode.showCodeHo(locAns)
