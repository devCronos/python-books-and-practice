class Enemy:
    life = 3

    def atack(self):
        print('ew!! :(')
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print('boom dead')
        else:
            print(str(self.life) + " life left")

enemy1=Enemy()
enemy1.atack()
enemy1.checkLife()
enemy1.atack()
enemy1.checkLife()
enemy1.atack()
enemy1.checkLife()
