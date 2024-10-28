class Horse:
    def __init__(self, x_distance, sound, y_distance):
        self.x_distance = 0 # пройденный путь.
        self.sound = 'Frrr' #звук, который издаёт лошадь
    def run(self, dx):
        self.dx = dx
        self.x_distance += self.dx

class Eagle: # класс описывающий орла
    def __init__(self,x_distance, sound, y_distance):
        self.y_distance = 0 # высота полёта
        self.sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл
        super().__init__(x_distance, sound, y_distance)
    def fly(self, dy):
        self.dy = dy
        self.y_distance += self.dy

class Pegasus (Horse, Eagle):# класс описывающий пегаса
    def __init__(self, x_distance, sound, y_distance):
        super().__init__(x_distance, sound, y_distance)

    def move(self, dx, dy): #где dx и dy изменения дистанции
        self.run(dx)
        self.fly(dy)
    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice (self):
        print(self.sound)

p1 = Pegasus(0,0)

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()






