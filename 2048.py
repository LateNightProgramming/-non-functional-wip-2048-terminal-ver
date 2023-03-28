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
    def inputfunc():
        global control
        global row1
        global row2
        global row3
        global row4
        control = ""
        while control != 'left' and control != 'right' and control != 'up' and control != 'down':
            control = input("please input which direction")
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
                    if row2[selector] > 0:
                        if row1[selector] == 0 or row1[selector] == row2[selector]:
                            row1[selector] += row2[selector]
                            row2[selector] = 0
                    selector+=1
                        
                main()
    printfunc()
    inputfunc()
def setup():
    global row1
    global row2
    global row3
    global row4
    for x in range(2):
        startchoice = r.randint(1,4)
        if startchoice == 1:
            blockstart = r.randint(0,3)
            row1[blockstart] += 2
        elif startchoice == 2:
            blockstart = r.randint(0,3)
            row2[blockstart] += 2
        elif startchoice == 3:
            blockstart = r.randint(0,3)
            row3[blockstart] += 2
        else:
            blockstart = r.randint(0,3)
            row4[blockstart] += 2
setup()
main()
