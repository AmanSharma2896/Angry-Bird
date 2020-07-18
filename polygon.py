import pygame
import pymunk as pm
from pymunk import Vec2d
import math

class Polygon():
    def __init__(self,pos,length,height,space,mass = 5.0):
        
        moment = 1000
        body = pm.Body(mass,moment)
        body.position = Vec2d(pos)        # Defining the gravity in this position
        
        shape = pm.Poly.create_box(body ,(length,height))
        
        shape.color = (0,0,255)
        shape.friction = 0.5
        shape.collision_type = 2          # TO detect the collision of wood
        space.add(body,shape)
        self.body = body
        self.shape = shape
        
        wood = pygame.image.load("wood.png").convert_alpha()
        wood2 = pygame.image.load("wood2.png").convert_alpha()
        
        rect = pygame.Rect(251,357,86,22)           # To extract the beam from combination of images
        self.beam_image = wood.subsurface(rect).copy()
         
        rect = pygame.Rect(16,252,22,84)
        self.column_image = wood2.subsurface(rect).copy()

    
    def to_pygame(self,p):
        return int(p.x), int(-p.y + 600) # It will convert pymunk into pygame co-ordinate
                                         # Here p is body position created from pymunk module
        
            
         
    def draw_poly(self,element,screen):
        poly = self.shape
        ps = poly.get_vertices()            # ps is list of vertices of polygon
        ps.append(ps[0])
        ps = map(self.to_pygame,ps)      #  We have to call to_pygame function to every element of ps
        ps = list(ps)
        color = (255,0,0)
        pygame.draw.lines(screen,color,False,ps)
        
        if element == "beams":
            p = poly.body.position
            p = Vec2d (self.to_pygame(p))
            
            angle_degrees = math.degrees(poly.body.angle) + 180     # to rotate the beam according to our needs
            
            # rotation of beam
            
            rotated_logo_img = pygame.transform.rotate(self.beam_image,angle_degrees)
            
            offset = Vec2d(rotated_logo_img.get_size()) / 2. # We have divides by 2 beceuse if we take another number then there will be displacement in position of beam and our beam will not be according to our column
            
            p = p - offset
            
            np = p               # New position after rotation
            
            screen.blit(rotated_logo_img, (np.x, np.y))
            
        if element == 'columns':
            p = poly.body.position
            p = Vec2d (self.to_pygame(p))
            
            angle_degrees = math.degrees(poly.body.angle) + 180     # to rotate the beam according to our needs
            
            # rotation of beam
            
            rotated_logo_img = pygame.transform.rotate(self.column_image,angle_degrees)
            
            offset = Vec2d(rotated_logo_img.get_size()) / 2. # We have divides by 2 beceuse if we take another number then there will be displacement in position of beam and our beam will not be according to our column
            
            p = p - offset   
            
            np = p               # New position after rotation
            
            screen.blit(rotated_logo_img,(np.x, np.y))
            
            
             
        
