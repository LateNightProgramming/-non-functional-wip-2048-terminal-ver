import random as r

global row1
global row2
global row3
global row4
row1 = [0,0,0,0]
row2 = [0,0,0,0]
row3 = [0,0,0,0]
row4 = [0,0,0,0]
global control
control = ""
global points
points = 0
def main():
    def printfunc():
        print(row1)
        print(row2)
        print(row3)
        print(row4)
        
    def newblock():
        starter = False
        while starter == False:
            rowchoice = r.randint(1,4)
            if rowchoice == 1:
                slotchoice = r.randint(0,3)
                if row1[slotchoice] == 0:
                    row1[slotchoice] += 2
                    starter = True
            elif rowchoice == 2:
                slotchoice = r.randint(0,3)
                if row2[slotchoice] == 0:
                    row2[slotchoice] += 2
                    starter = True
            elif rowchoice == 3:
                slotchoice = r.randint(0,3)
                if row3[slotchoice] == 0:
                    row3[slotchoice] += 2
                    starter = True
                
            
                
    def inputfunc():
        global control
        global row1
        global row2
        global row3
        global row4
        control = ""
        while control != 'left' and control != 'right' and control != 'up' and control != 'down':
            control = input("please input which direction").lower()
            if control != 'left' and control != 'right' and control != 'up' and control != 'down':
                print("bruh")
            elif control == "left":
                selector = 3
                selector2 = 3
                selector3 = 3
                selector4 = 3
                for x in range(4):
                    if row1[selector] > 0:
                        addvar = row1[selector]
                        if selector != 0:
                            row1[selector] = 0
                            if row1[selector - 1] == 0 or row1[selector - 1] == addvar:
                                row1[selector - 1] += addvar
                                selector -= 1
                    else:
                        selector -= 1
                        
                    if row2[selector2] > 0:
                        addvar2 = row2[selector2]
                        if selector2 != 0:
                            row2[selector2] = 0
                            if row2[selector2 - 1] == 0 or row2[selector2 - 1] == addvar2:
                                row2[selector2 - 1] += addvar2
                                selector2 -= 1
                    else:
                        selector2 -= 1

                    if row3[selector3] > 0:
                        addvar3 = row3[selector3]
                        if selector3 != 0:
                            row3[selector3] = 0
                            if row3[selector3 - 1] == 0 or row3[selector3 - 1] == addvar3:
                                row3[selector3 - 1] += addvar3
                                selector3 -= 1
                    else:
                        selector3 -= 1

                    if row4[selector4] > 0:
                        addvar4 = row4[selector4]
                        if selector4 != 0:
                            row4[selector4] = 0
                            if row4[selector4 - 1] == 0 or row4[selector4 - 1] == addvar4:
                                row4[selector4 - 1] += addvar4
                                selector4 -= 1
                    else:
                        selector4 -= 1
                main()
            elif control == "right":
                selector = 0
                selector2 = 0
                selector3 = 0
                selector4 = 0
                for x in range(4):
                    if row1[selector] > 0:
                        addvar = row1[selector]
                        if selector != 3:
                            row1[selector] = 0
                            if row1[selector + 1] == 0 or row1[selector + 1] == addvar:
                                row1[selector + 1] += addvar
                                selector += 1
                    else:
                        selector += 1

                    if row2[selector2] > 0:
                        addvar2 = row2[selector2]
                        if selector2 != 3:
                            row2[selector2] = 0
                            if row2[selector2 + 1] == 0 or row2[selector2 + 1] == addvar2:
                                row2[selector2 + 1] += addvar2
                                selector2 += 1
                    else:
                        selector2 += 1

                    if row3[selector3] > 0:
                        addvar3 = row3[selector3]
                        if selector3 != 3:
                            row3[selector3] = 0
                            if row3[selector3 + 1] == 0 or row3[selector3 + 1] == addvar3:
                                row3[selector3 + 1] += addvar3
                                selector3 += 1
                    else:
                        selector3 += 1
                        
                    if row4[selector4] > 0:
                        addvar4 = row4[selector4]
                        if selector4 != 3:
                            row4[selector4] = 0
                            if row4[selector4 + 1] == 0 or row4[selector4 + 1] == addvar4:
                                row4[selector4 + 1] += addvar4
                                selector4 += 1
                    else:
                        selector4 += 1
            elif control == "up":
                selector = 0
                for x in range(4):
                    for x in range(4):
                        if row2[selector] > 0:
                            if row1[selector] == 0 or row1[selector] == row2[selector]:
                                row1[selector] += row2[selector]
                                row2[selector] = 0
                        if row3[selector] > 0:
                            if row2[selector] == 0 or row2[selector] == row3[selector]:
                                row2[selector] += row3[selector]
                                row3[selector] = 0
                        if row4[selector] > 0:
                            if row3[selector] == 0 or row3[selector] == row4[selector]:
                                row3[selector] += row4[selector]
                                row4[selector] = 0
                    selector+=1
            elif control == "down":
                selector = 0
                for x in range(4):
                    for x in range(4):
                        if row1[selector] > 0:
                            if row2[selector] == 0 or row2[selector] == row1[selector]:
                                row2[selector] += row1[selector]
                                row1[selector] = 0
                        if row2[selector] > 0:
                            if row3[selector] == 0 or row3[selector] == row2[selector]:
                                row3[selector] += row2[selector]
                                row2[selector] = 0
                        if row3[selector] > 0:
                            if row4[selector] == 0 or row4[selector] == row3[selector]:
                                row4[selector] += row3[selector]
                                row3[selector] = 0
                    selector+=1
                        
    printfunc()
    inputfunc()
    newblock()
    main()
def setup():
    global row1
    global row2
    global row3
    global row4
    v1 = False
    for x in range(2):
        startchoice = r.randint(1,4)
        if startchoice == 1:
            while v1 == False:
                blockstart = r.randint(0,3)
                if row1[blockstart] == 0:
                    row1[blockstart] += r.choice([2,4])
                    v1 = True
        v1 = False
        if startchoice == 2:
            while v1 == False:
                blockstart = r.randint(0,3)
                if row2[blockstart] == 0:
                    row2[blockstart] += r.choice([2,4])
                    v1 = True
        v1 = False
        if startchoice == 3:
            while v1 == False:
                blockstart = r.randint(0,3)
                if row3[blockstart] == 0:
                    row3[blockstart] += r.choice([2,4])
                    v1 = True
        v1 = False
        if startchoice == 4:
            blockstart = r.randint(0,3)
            row4[blockstart] += r.choice([2,4])
setup()
main()
