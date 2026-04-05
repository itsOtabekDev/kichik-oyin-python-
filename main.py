
class Dori:
    def __init__(self, x, y, kuchi):
        self.x = x
        self.y = y
        self.kuchi = kuchi
aspirin = Dori(2,2,20)
hudud = [
    ["*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*"],
    ["*","*","*","*","*","*","*","*"]
]

def print_hudud():
    for i in hudud:
        print(i)

class player():
    def __init__(self, x, y, health, qurollar=[]):
        self.x = x
        self.y = y
        self.health = health
        self.qurollar = qurollar
    def go(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if 0 <= new_x < len(hudud[0]) and 0 <= new_y < len(hudud):
            hudud[self.y][self.x] = "*"
            self.x = new_x
            self.y = new_y
            if self.x == aspirin.x and self.y == aspirin.y:
                self.health += aspirin.kuchi
                print(f"aspirin dorisi qabul qilindi va soglik {self.health} boldi")
            hudud[self.y][self.x] = "P"


player1 = player(0,0,100)
hudud[player1.y][player1.x] = "P"
hudud[aspirin.y][aspirin.x] = "D"
print_hudud()
while True:
    x = int(input("onga yoki chapkga yuring (-1,1,0): "))
    y = int(input("tepaga yoki pastga yuring (-1,1,0): "))
    if player1.y == 6 and player1.x == 6:
        print("finish")
        break
    player1.go(x,y)
    print_hudud()