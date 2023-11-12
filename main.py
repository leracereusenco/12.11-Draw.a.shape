import ast
import turtle

varInput = ''
verify = False
database = {}


def getAllRecords():
    global database
    with open('db.txt') as data: #with open - cu ajutorul celuilalt file
        f = data.read()
        database = ast.literal_eval(f)


def getInput():
    global varInput
    varInput = input('enter shape\n') #input


def verifyShape(shape):
    global verify
    if shape in database.keys():
        print('Shape found')
        verify = True
        return verify
    else:
        print('Not found')
        verify = False
        return verify


def drawTriangle():
    laturi = database.get(varInput)
    for i in range(3):
        turtle.forward(100)
        turtle.right(360/3)
    turtle.Screen().exitonclick()


def drawSquare():
    laturi = database.get(varInput)
    for i in range(4):
        turtle.forward(100)
        turtle.right(360/4)
    turtle.Screen().exitonclick()


def printShape(isTrue):
    global varInput
    if isTrue:
        if varInput == 'Triangle':
            drawTriangle()
        elif varInput == 'Square':
            drawSquare()
        else:
            print('Finish')
    else:
        print('Shape not found')


if __name__ == '__main__':
    getAllRecords()
    getInput()
    verifyShape(varInput)
    printShape(verify)


