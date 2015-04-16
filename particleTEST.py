# Unfinished script!

import c4d

class Particle(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.loc = c4d.Vector(self.x, self.y, self.z)
        self.vel = c4d.Vector(0, 0, 0)
        self.acc = c4d.Vector(0, 0, 0)
        
    def update(self):
        self.vel += self.acc
        self.loc += self.vel
        self.acc *= 0
    
    def applyForce(self, f):
        self.acc += f

obj = op.GetObject()
p = Particle(0, 0, 0)

def main():
    g = c4d.Vector(0, -1, 0)
    p.applyForce(g)
    p.update()
    obj[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_X] = p.loc.x
    obj[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Y] = p.loc.y
    obj[c4d.ID_BASEOBJECT_REL_POSITION,c4d.VECTOR_Z] = p.loc.z
