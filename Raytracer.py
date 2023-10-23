import pygame
from pygame.locals import * 
from rt import Raytracer
from figures import *
from lights import *
from materials import *

width = 512
height = 512

pygame.init()

screen = pygame.display.set_mode((width,height), pygame.DOUBLEBUF | pygame.HWACCEL | pygame.HWSURFACE | pygame.SCALED)
screen.set_alpha(None)

raytracer = Raytracer(screen)

#Se puede usar cualquier formato de imagen.
#hdri-hub.com
raytracer.envMap = pygame.image.load("images/ocean.jpg")
raytracer.rtClearColor(0.25,0.25,0.25)

#Carga de texturas
metalTexture = pygame.image.load("images/metal.jpeg")
build1Texture = pygame.image.load("images/building 1.jpg")
build2Texture = pygame.image.load("images/building 2.jpeg")

#Carga de materiales
metal = Material(texture = metalTexture, spec = 64, ks = 0.1, matType= OPAQUE)
pearl = Material(diffuse=(0.9176, 0.902, 0.7922), spec = 64, ks = 0.1, matType= OPAQUE)
glass = Material(diffuse=(0.9,0.9,0.9), spec = 64, ks = 0.15, ior = 1.5, matType = TRANSPARENT)
glassBuilding = Material(texture = build1Texture, spec = 64, ks = 0.15, ior = 1.5, matType = REFLECTIVE)
concreteBuilding = Material(texture = build2Texture, spec = 64, ks = 0.15, ior = 1.5, matType = OPAQUE)

#Colocacion de figuras
raytracer.scene.append(Ellipsoid(position = (5,5.5,-12), radii = (1.2,0.75,1), material = metal))
raytracer.scene.append(Ellipsoid(position = (-3.5,5.25,-12), radii = (1.35,1,1), material = metal))
raytracer.scene.append(Ellipsoid(position = (-1.75,2.5,-10), radii = (1,0.55,1), material = metal))

raytracer.scene.append(AABB(position = (4.96,4.85,-12), size = (0.5,0.5,0.5), material = pearl))
raytracer.scene.append(AABB(position = (-3.475,4.45,-12), size = (0.6,0.6,0.6), material = pearl))
raytracer.scene.append(AABB(position = (-1.745,2,-10), size = (0.4,0.4,0.4), material = pearl))

raytracer.scene.append(Disk(position = (4.25,5.95,-13), normal = (0,1,2), radius= 1.75, material = glass))
raytracer.scene.append(Disk(position = (-2.5,5.5,-13), normal = (0,1,-1), radius= 1.45, material = glass))
raytracer.scene.append(Disk(position = (-1,2.45,-11), normal = (1,-1,0), radius= 1.25, material = glass))

raytracer.scene.append(Cylinder(position= (0.5, 0.7, -5), radius = 0.3, height=1.4, material = glassBuilding))
raytracer.scene.append(Cylinder(position= (1, 0.48, -3), radius = 0.3, height=0.9, material = glassBuilding))
raytracer.scene.append(Cylinder(position= (0.28, -0.5, -4), radius = 0.3, height=1.35, material = concreteBuilding))
raytracer.scene.append(Cylinder(position= (1.95, 0.75, -5), radius = 0.45, height=1.25, material = concreteBuilding))
raytracer.scene.append(Cylinder(position= (1.98, 0.75, -3), radius = 0.35, height=1.35, material = glassBuilding))

#iluminacion minima del ambiente
raytracer.lights.append(AmbientLight(intensity=0.3))
raytracer.lights.append(DirectionalLight(direction=(1,1,-2), intensity=0.95))
raytracer.lights.append(DirectionalLight(direction=(0,-1.5,-4), intensity=0.5))

#No colocar en la misma ubicacion que ninguna figura
raytracer.lights.append(PointLight(point=(1.5,1,-2), intensity=10, color= (1,1,1)))

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