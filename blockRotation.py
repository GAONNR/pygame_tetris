### shape I
shapeI = [[], [], [], []]
shapeI[0] = [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]]
shapeI[1] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 1, 1, 1]]
shapeI[2] = shapeI[0]
shapeI[3] = shapeI[1]

### shape J
shapeJ = [[], [], [], []]
shapeJ[0] = [[0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0]]
shapeJ[3] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 1, 1, 0],
             [0, 0, 1, 0]]
shapeJ[2] = [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]]
shapeJ[1] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 0, 0, 0],
             [1, 1, 1, 0]]

### shape L
shapeL = [[], [], [], []]
shapeL[0] = [[0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 0]]
shapeL[3] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 1, 0],
             [1, 1, 1, 0]]
shapeL[2] = [[0, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]]
shapeL[1] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 1, 1, 0],
             [1, 0, 0, 0]]

### shape O
shapeO = [[], [], [], []]
shapeO[0] = [[0, 0, 0, 0],
              [0, 0, 0, 0],
              [1, 1, 0, 0],
              [1, 1, 0, 0]]
shapeO[1] = shapeO[0]
shapeO[2] = shapeO[0]
shapeO[3] = shapeO[0]

### shape S
shapeS = [[], [], [], []]
shapeS[0] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 1, 1, 0],
             [1, 1, 0, 0]]
shapeS[1] = [[0, 0, 0, 0],
             [1, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 0, 0]]
shapeS[2] = shapeS[0]
shapeS[3] = shapeS[1]

### shape T
shapeT = [[], [], [], []]
shapeT[0] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 1, 1, 0],
             [0, 1, 0, 0]]
shapeT[1] = [[0, 0, 0, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 0, 0]]
shapeT[2] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 1, 0, 0],
             [1, 1, 1, 0]]
shapeT[3] = [[0, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 0, 0]]

### shape Z
shapeZ = [[], [], [], []]
shapeZ[0] = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 1, 1, 0]]
shapeZ[1] = [[0, 0, 0, 0],
             [0, 1, 0, 0],
             [1, 1, 0, 0],
             [1, 0, 0, 0]]
shapeZ[2] = shapeZ[0]
shapeZ[3] = shapeZ[1]

def rotateBlock(chara, idx):
    if chara == 'I':
        return shapeI[idx]
    elif chara == 'J':
        return shapeJ[idx]
    elif chara == 'L':
        return shapeL[idx]
    elif chara == 'O':
        return shapeO[idx]
    elif chara == 'S':
        return shapeS[idx]
    elif chara == 'T':
        return shapeT[idx]
    else:
        return shapeZ[idx]
