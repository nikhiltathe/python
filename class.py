class Enemy:
    life = 3

    def __init__(self, x):
        self.life = x

    def attack(self):
        print("Ahh")
        self.life -=1

    def checkLife(self):
       if self.life<0:
           print("Dead !")
       else:
           print("Life left", self.life)


E1 = Enemy(0)
E2 = Enemy(3)

E1.attack()
E1.checkLife()
E1.attack()
E1.checkLife()
E1.attack()
E1.checkLife()
E1.attack()
E1.checkLife()

E2.checkLife()
E2.attack()

