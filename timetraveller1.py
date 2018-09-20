#https://github.com/gingij4/TileTraveller.git

# We start of assuming you can travel in any direction.
# If the player is touching a border we eliminate the direction of that border
# If the player is touching a wall we eliminite the direction of that wall
# There are walls on every edge in row 1
# There are walls to the north and east of (2, 2), south of (2, 3) and west of (3, 2)
# We output the valid directions
# The user inputs a direction, if it is invalid he is prompted again to enter a direction
# Once the user inputs a valid direction he is moved
# If he has not reached (3, 1) return to the start.
# Once he reaches (3, 1) we output "Victory!" and end the program.

# n = x + 0, y + 1
# s = x + 0, y - 1
# e = x + 1, y + 0
# w = x - 1, y + 0

 
x, y = 1, 1

while not (x == 3 and y == 1):
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
    

    #output available directions
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
    
    # get input, move player
    direction = ""
    while True:
        direction = input("Direction: ").upper()
        if direction == "N" and n:
            y += 1
            break
        elif direction == "E" and e:
            x += 1
            break
        elif direction == "S" and s:
            y -= 1
            break
        elif direction == "W" and w:
            x -= 1
            break
        print("Not a valid direction!")

print("Victory!")