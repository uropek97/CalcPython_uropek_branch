from decimal import Decimal

print('Калькулятор.')

def inputOp():
    op = input('Ввод: ')
    opchar = op.split()

    return opchar

def processdata(opchar:list):
    symchar = ['+', '-', '*', '/', '^']

    if len(opchar)!=4:
        return False

    try: 
        Decimal(opchar[0])
    except:
        return False
    
    if opchar[1] not in symchar:
        return False
    
    try:
        Decimal(opchar[2])
    except:
        return False
    
    if opchar[3] != '=':
        return False

    return True

def sendData(opchar:list):
    opchar.pop()
    return opchar

correctOp = False
while not correctOp:
    op = inputOp()
    correctOp = processdata(op)

data = sendData(op)