
#  Description: Walking around a house adventure game!

class Room:

    def __init__(self,name,north,east,south,west,up,down):
        self.where = name
        self.n = north
        self.e = east
        self.s = south
        self.w = west
        self.u = up
        self.d = down

        
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
        print()
                      

def createRoom(roomData):

    room = Room(roomData[0],roomData[1],roomData[2],roomData[3],roomData[4],roomData[5],roomData[6])

    return room

def look():

    print("You are currently in the " + str(current.where))

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

    global floorPlan    # make the variable "floorPlan" a global variable
    
    room1 = ["Living Room","Dining Room",None,None,None,"Upper Hall",None]
    room2 = ["Dining Room",None,None,"Living Room","Kitchen",None,None]
    room3 = ["Kitchen",None,"Dining Room",None,None,None,None]
    room4 = ["Upper Hall","Bathroom","Small Bedroom","Master Bedroom",None,None,"Living Room"]
    room5 = ["Bathroom",None,None,"Upper Hall",None,None,None]
    room6 = ["Small Bedroom",None,None,None,"Upper Hall",None,None]
    room7 = ["Master Bedroom","Upper Hall",None,None,None,None,None]

    floorPlan = [createRoom(room1),createRoom(room2),createRoom(room3),createRoom(room4),createRoom(room5),createRoom(room6),createRoom(room7)]

def main():

    global current      # make the variable "current" a global variable
    
    loadMap()
    
    displayAllRooms()

    # TEST CODE:  walk around the house
    
    current = floorPlan[0]      # start in the living room
    look()                      # Living Room
    
    current = move("south")     # can't move this direction
    current = move("west")      # can't move this direction
    current = move("north")     # Dining Room
    current = move("south")     # Living Room
    current = move("up")        # Upper Hall
    look()                      # Upper Hall
    current = move("east")      # Small Bedroom
    current = move("east")      # can't move this direction
    current = move("west")      # Upper Hall
    current = move("south")     # Master Bedroom
    current = move("north")     # Upper Hall
    current = move("north")     # Bathroom
    current = move("south")     # Upper Hall
    look()                      # Upper Hall
    current = move("west")      # can't move this direction
    look()                      # still in the Upper Hall
    current = move("down")      # Living Room
    current = move("north")     # Dining Room
    current = move("west")      # Kitchen
    current = move("north")     # can't move this direction

main()
        
