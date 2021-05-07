import showCode
fileName = "codeFile"

def saveCode(code, name):
    '''
    code = 6자리 list. 
    '''
    f = open(fileName, 'a')
    f.write(name + "\n")
    codeStr = ""
    for c in code:
        codeStr += str(c) + " "
    f.write(codeStr[0:-1] + '\n')  # Save without last space.
    f.close()

def readCode(code=None, name=None):
    if code != None:
        ret = searchCodeWithCode(code)
    elif name != None:
        ret = searchCodeWithName(name)
    else:
        ret = []
    return ret

def searchCodeWithCode(code):    
    n, c = readFile()
    ret = []
    for i in range(0, len(c)):
        if listCompare(showCode.showScaleName(code), showCode.showScaleName(c)):
            ret.append(c)
    return ret

def searchCodeWithName(name):
    n, c = readFile()
    ret = []
    for i in range(0, len(n)):
        if n[i] == name:
            ret.append(c[i])
    return ret

def listCompare(l1, l2):
    if len(l1) != len(l2):
        return False
    for l in l1:
        if l not in l2:
            return False
    for l in l2:
        if l not in l1:
            return False
    return True

def readFile():
    f = open(fileName, 'r')
    lines = f.readlines()
    code = []
    name = []
    for l in range(0, len(lines)):
        lines[l] = lines[l].replace("\n", "")
        if l % 2 == 0:
            name.append(lines[l])
        else:
            tempCode = []
            for c in lines[l].split(" "):
                tempCode.append(int(c))
            code.append(tempCode)
    f.close()
    return name, code

def resetFile():
    f =  open(fileName, 'w')
    f.close()

def fixCode(codeName, handLoc):
    '''
    Delete same handLoc and sorting with name-list.
    '''
    changedCodeName = []
    changedHandLoc = []
    
    # Delete same code.
    for i in range(0, len(codeName)):
        if handLoc[i] not in changedHandLoc:
            changedCodeName.append(codeName[i])
            changedHandLoc.append(handLoc[i])
    print(changedHandLoc)
    input("")

    # Sort with name order.
    for i in range(0, len(changedCodeName) - 1):
        for j in range(i+1, len(changedCodeName)):
            if changedCodeName[i] > changedCodeName[j]:
                temp = changedCodeName[j]
                changedCodeName[j] = changedCodeName[i]
                changedCodeName[i] = temp

                temp = changedHandLoc[j]
                changedHandLoc[j] = changedHandLoc[i]
                changedHandLoc[i] = temp
    return changedCodeName, changedHandLoc

def saveList(codeName, handLoc, fileName=fileName):
    f = open(fileName, 'a')
    for i in range(0, len(codeName)):
        saveCode(handLoc[i], codeName[i])
    f.close()

def codeHandInput():
    print("Enter N any time if you want to break.")
    code = ""
    handLoc = []
    code = input("Enter Code name : ")
    if code == "N":
        return code, handLoc
    print("Enter Hand location 6 time ( -1 for do not ringing. ): ")
    for i in range(0, 6):
        stringLoc = input(str(i) + " string : ")
        if stringLoc == "N":
            break
        else:
            handLoc.append(stringLoc)
    return code, handLoc

def getAllCodeName():
    '''
    Return all saved code name without duplicate.
    '''
    n, _ =  readFile()
    codeList = []

    # For all code name, choose only 1.
    for name in n:
        if name not in codeList:
            codeList.append(name)

    return codeList

# For managing codeFile file.
if __name__ == "__main__":
    # Excute manager mode if run in script.
    while(True):
        print("Code file manager mode running now.")
        print("Choose menu.")
        print("1. Enter code-add mode.")
        print("2. Enter code-delete mode.")
        print("3. Show all code now.")
        print("4. Search code.")
        print("5. Reset all code.")
        print("6. Check same and sort in code-name order.")
        print("7. Bye.")

        numStr = input("Choose : ")
        try:
            num = int(numStr)
            if num == 1:
                while(True) : 
                    code, handLoc = codeHandInput()
                    if code == "N" or "N" in handLoc:
                        break
                    proceed = input(code + " : " + str(handLoc) + " will be added. Proceed? (y/n)")
                    if proceed == "y":
                       saveCode(handLoc, code) 
            elif num == 2:
                print("Enter code and hand location if you want to delete.")
                code, handLoc = codeHandInput()
                if code == "N" or "N" in handLoc:
                    break
            elif num == 3:
                n, c = readFile()
                showCode.showCodeWithNameHo(n, c)
            elif num == 4:
                n, c = readFile()
                name = []
                codeList = []
                code = input("Input want to find code : ")
                for i in range(0, len(n)):
                    if n[i] == code:
                        name.append(n[i])
                        codeList.append(c[i])
                showCode.showCodeWithNameHo(name, codeList)
            elif num == 5:
                proceed = input("Remove file and cannot be turn back. Proceed? (y/n)")
                if proceed == "y":
                    resetFile()
            elif num == 6:
                proceed = input("Same code will deleted and code will be sorted in name order. Proceed? (y/n)")
                if proceed == "y":
                    n, c = readFile()
                    n, c = fixCode(n, c)
                    resetFile()
                    saveList(n, c)
     
            elif num == 7:
                break
            else:
                print("Please enter only 1 ~ 4 number.")
        except ValueError:
            print("Please enter only integer.")
