#  File: Project2.py
#  Description: Adventure game with objects
#  Student's Name: Akiko Barreras
#  Student's UT EID: ab63527
#  Course Name: CS 303E 
#  Unique Number: 50180
#
#  Date Created: 5/1/2020
#  Date Last Modified: 5/2/2020

class Room:

    def __init__(self,name,north,east,south,west,up,down,contents):
        self.where = name
        self.n = north
        self.e = east
        self.s = south
        self.w = west
        self.u = up
        self.d = down
        self.c = contents #Contents is a list

    def displayRoom(self):
        print("Room name: ",self.where)
        if self.n: 
            print("   Room to the north: ",self.n)
        if self.e:
            print("   Room to the east: ",self.e)
        if self.s:
            print("   Room to the south: ", self.s)
        if self.w:
            print("   Room to the west: ",self.w)
        if self.u:
            print("   Room above: ",self.u)
        if self.d:
            print("   Room below: ",self.d)
        if self.c == []:
            print("   Room contents: ","[]")
        else:
            print("   Room contents: ",self.c)
        print()

def createRoom(roomData):

    room = Room(roomData[0],roomData[1],roomData[2],roomData[3],roomData[4],roomData[5],roomData[6],roomData[7])

    return room

def look():

    print("You are currently in the " + str(current.where))
    print("Contents of the room:")
    if current.c != []:
        for i in range(0,len(current.c)):
            print("   " + current.c[i])
    else:
        print("   " + "None")

def getRoom(name):

    for i in range(0,len(floorPlan)):
        if floorPlan[i].where == name:
            room = floorPlan[i]
            break
        else:
            continue
        
    return room
        
def move(direction):

    room = current

    if direction == "north" and current.n:
        room = getRoom(current.n)
        print("You are now in the",room.where)
        
    elif direction == "east" and current.e:
        room = getRoom(current.e)
        print("You are now in the",room.where)
        
    elif direction == "south" and current.s:
        room = getRoom(current.s)
        print("You are now in the",room.where)
        
    elif direction == "west" and current.w:
        room = getRoom(current.w)
        print("You are now in the",room.where)
        
    elif direction == "up" and current.u:
        room = getRoom(current.u)
        print("You are now in the",room.where)
        
    elif direction == "down" and current.d:
        room = getRoom(current.d)
        print("You are now in the",room.where)
        
    else:
        print("You can't move in that direction.")

    return room

def displayAllRooms():
    for i in range(0,len(floorPlan)):
        floorPlan[i].displayRoom()

def loadMap():

    global floorPlan

    house = open("ProjectData.txt","r")

    floorPlan = []

    #Looking at text file line by line
    line = house.readline()
    
    while line != "":

        roomVar = line.split(",")
        objects = []
        
        #Taking out everything after the down room assinment (the objects)
        #And putting it into a list
        while len(roomVar) > 7:
            objects.append(eval(roomVar.pop(7)))

        #removing the \n at the end of the last object
        if objects != []:
            objects[-1] = objects[-1].strip()

        name,north,east,south,west,up,down = [eval(x) for x in roomVar]

        roomList = [name,north,east,south,west,up,down,objects]

        floorPlan.append(createRoom(roomList))

        line = house.readline()

    house.close()

def pickup(item):

    if item in current.c:
        print("You now have the", item)
        #getting the index, removing from contents, appending to inventory
        inventory.append(current.c.pop(current.c.index(item)))
    else:
        print("That item is not in this room.")

def drop(item):
    
    if item in inventory:
        print("You have dropped the", item)
        #getting the index, removing from inventory, appending to contents
        current.c.append(inventory.pop(inventory.index(item)))
    else:
        print("You don't have that item")

def listInventory():

    print("You are currently carrying:")
    if inventory != []:
        for i in range(0,len(inventory)):
            print("   " + inventory[i])
    else:
       print("nothing.") 

def main():

    global current      # make the variable "current" a global variable
    
    loadMap()
    
    displayAllRooms()

    global inventory #List that represents the items the player is carrying

    inventory = []

    current = floorPlan[0]      # start in the living room
    look()
    print()
    
    command = input("Enter a command: ")
    getOrDrop = command.split() #if the user inputs get item or drop item

    while command != "exit":
        if command == "look":
            look()
        elif command == "north":
            current = move("north")
        elif command == "east":
            current = move("east")
        elif command == "south":
            current = move("south")    
        elif command == "west":
            current = move("west")
        elif command == "up":
            current = move("up")
        elif command == "down":
            current = move("down")
        elif command == "inventory":
            listInventory()
        elif getOrDrop[0] == "get":
            pickup(getOrDrop[1])
        elif getOrDrop[0] == "drop":
            drop(getOrDrop[1])
        elif command == "help":
            print(format("look:","13s"),end="")
            print("display the name of the current room and its contents")
            print(format("north:","13s"),end="")
            print("move north")
            print(format("east:","13s"),end="")
            print("move east")
            print(format("south:","13s"),end="")
            print("move south")
            print(format("west:","13s"),end="")
            print("move west")
            print(format("up:","13s"),end="")
            print("move up")
            print(format("down:","13s"),end="")
            print("move down")
            print(format("inventory:","13s"),end="")
            print("list what items you're currently carrying")
            print(format("get <item>:","13s"),end="")
            print("pick up an item currently in the room")
            print(format("drop <item>:","13s"),end="")
            print("drop an item you're currently carrying")
            print(format("help:","13s"),end="")
            print("print this list")
            print(format("exit:","13s"),end="")
            print("quit the game")

        print()
        command = input("Enter a command: ")
        getOrDrop = command.split()

    print("Quitting game")


main()

    

    

    
