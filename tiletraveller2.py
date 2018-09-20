#https://github.com/gingij4/TileTraveller.git

""" 
1.
It was easier to implement the second version, but that may just be because I had already implemented it before.
2.
It is defenitely way easier to read the second version. You don't need to comprehend the entire program to understand what it does.
3.
This version is much more malliable. If i wanted to it would be easy to add a second player.
Functions are very important when it comes to scalability.
"""

def getDirections(x, y):
    ''' Returns the directions one could travel in from x, y according to the diagram '''
    n = True
    s = True
    e = True
    w = True

    #check borders
    if y == 3:
        n = False
    elif y == 1:
        s = False
    if x == 1:
        w = False
    elif x == 3:
        e = False

    #check walls
    if y == 1:
        e = False
        w = False
    elif x == 2 and y == 2:
        n = False
        e = False
    elif x == 3 and y == 2:
        w = False
    elif x == 2 and y == 3:
        s = False
    return n, e, s, w

def printAvailableDirections(x, y):
    ''' Prints the directions one could travel in from x, y '''
    n, e, s, w = getDirections(x, y)
    print("You can travel:", end=" ")
    if n:
        print("(N)orth", end="")
        if e or w or s:
            print(" or", end=" ")
    if e:
        print("(E)ast", end="")
        if w or s:
            print(" or", end=" ")
    if s:   
        print("(S)outh", end="")
        if w:
            print(" or", end=" ")
    if w:
        print("(W)est", end="")
    print(".")

def getValidInput(x, y):
    ''' Returns a user inputted direction that one could travel in from x, y '''
    n, e, s, w = getDirections(x, y)
    while True:
        direction = input("Direction: ").upper()
        if direction == "N" and n:
            break
        elif direction == "E" and e:
            break
        elif direction == "S" and s:
            break
        elif direction == "W" and w:
            break
        print("Not a valid direction!")
    return direction

def movePlayer(x, y, direction):
    ''' Returns the moved x, y coordinates according to the direction '''
    if direction == "N":
        y += 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y -= 1
    elif direction == "W":
        x -= 1
    return x, y


x, y = 1, 1
while not (x == 3 and y == 1):
    printAvailableDirections(x, y)
    direction = getValidInput(x, y)
    x, y = movePlayer(x, y, direction)
print("Victory!")