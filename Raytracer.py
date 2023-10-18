import pygame
from pygame.locals import * 
from rt import Raytracer
from figures import *
from lights import *
from materials import *

width = 256
height = 256

pygame.init()

screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

raytracer = Raytracer(screen)

#Se puede usar cualquier formato de imagen.
#hdri-hub.com
raytracer.envMap = pygame.image.load("images/castle.jpg")
raytracer.rtClearColor(0.25,0.25,0.25)

#Carga de texturas
ballTexture = pygame.image.load("images/Jabulani.jpg")

#Carga de materiales
reflectFlow = Material(texture = ballTexture, spec = 64, ks = 0.1, matType= OPAQUE)
c2 = Material(diffuse=(0.15,0.467,0.7), spec = 64, ks = 0.1, matType= OPAQUE)


#Colocacion de figuras
raytracer.scene.append(Ellipsoid(position = (5,5.5,-12), radii = (1.2,0.75,1), material = reflectFlow))
raytracer.scene.append(Ellipsoid(position = (-3.5,5.25,-12), radii = (1.35,1,1), material = reflectFlow))
raytracer.scene.append(Ellipsoid(position = (-1.75,2.5,-10), radii = (1,0.55,1), material = reflectFlow))

raytracer.scene.append(AABB(position = (4.96,4.85,-12), size = (0.5,0.5,0.5), material = c2))
raytracer.scene.append(AABB(position = (-3.475,4.45,-12), size = (0.6,0.6,0.6), material = c2))
raytracer.scene.append(AABB(position = (-1.745,2,-10), size = (0.4,0.4,0.4), material = c2))

#iluminacion minima del ambiente
raytracer.lights.append(AmbientLight(intensity=0.3))
raytracer.lights.append(DirectionalLight(direction=(1,1,-2), intensity=0.95))

#No colocar en la misma ubicacion que ninguna figura
#raytracer.lights.append(PointLight(point=(0,2,-5), intensity=10, color= (1,1,1)))

raytracer.rtClear()
raytracer.rtRender()

print("\nTiempo de renderizado:", pygame.time.get_ticks() / 1000, "segundos")

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning=False

rect = pygame.Rect(0,0,width,height)
sub = screen.subsurface(rect)
pygame.image.save(sub, "result.jpg")
                
pygame.quit()           