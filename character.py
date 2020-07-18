import pymunk as pm
from pymunk import Vec2d                                           # To define gravity vertor in space

class Bird():
    def __init__(self,distance,angle,x,y,space):
        self.life = 20                                             # To define over all life of a Bird
        mass = 5                                                   # Mass/ weight of the bird keep it low other wise it will accordingly follow the laws of physics
        radius = 12
        inertia = pm.moment_for_circle(mass, 0, radius,(0,0))      #  We have taken inner radius as 0 to depict a solid body
        body = pm.Body(mass,inertia)                               #  Creating a body for bird which will follow laws of physics
        
        body.position = x,y                                        #  To check position of body
        
        power = distance * 53                                      #  Movement of the bird
        
        impulse = power * Vec2d(1,0)
        
        angle = -angle                                             #  To give oposite direction
        
        body.apply_impulse_at_local_point(impulse.rotated(angle))  #  Add the local impulse to the body as if applied from body loacal point
        
        shape = pm.Circle(body, radius , (0,0))
        shape.elasticity = 0.95                                    #  For bird to bounce
        self.friction = 1
        
        shape.collision_type = 0                                   #  there will be three type of collision bird, pigs and wood
        
        space.add(body,shape)
        self.body = body
        self.shape = shape
        

class Pig():
    def __init__(self,x,y,space):
        self.life = 20                                            
        mass = 5                                                   
        radius = 14
        
        inertia = pm.moment_for_circle(mass, 0, radius,(0,0))
        body = pm.Body(mass,inertia)
        body.position = x, y
        
        shape = pm.Circle(body, radius , (0,0))
        shape.elasticity = 0.95                                    
        self.friction = 1
        shape.collision_type = 1
        
        space.add(body,shape)
        self.body = body
        self.shape = shape