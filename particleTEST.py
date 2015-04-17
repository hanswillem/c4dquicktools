#Still unfinished!
import c4d

class Particle(object):
    def __init__(self, obj, x, y, z):
        self.obj = obj
        self.x = x
        self.y = y
        self.z = z
        self.loc = c4d.Vector(self.x, self.y, self.z)
        self.vel = c4d.Vector(0, 0, 0)
        self.acc = c4d.Vector(0, 0, 0)
    def show(self):
        self.obj[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = self.loc.x
        self.obj[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = self.loc.y
        self.obj[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = self.loc.z
    def update(self):
        self.vel += self.acc
        self.loc += self.vel
        self.acc *= 0
    def applyForce(self, f):
        self.acc += f
    def bounce(self):
        if self.loc.y < 0:
            self.loc.y = 0
            self.vel.y *= -1

obj = op.GetObject()
p = Particle(obj, 0, 500, 0)

def main():
    g = c4d.Vector(0, -25, 0)
    p.applyForce(g)
    p.update()
    p.bounce()
    p.show()
