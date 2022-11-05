import Box2D
import pygame
from pygame.locals import *
from Box2D.b2 import (world, polygonShape, circleShape, staticBody, dynamicBody)

# --- constants ---
# Box2D deals with meters, but we want to display pixels,
# so define a conversion factor:
PPM = 20.0  # pixels per meter
TARGET_FPS = 60
TIME_STEP = 1.0 / TARGET_FPS
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# --- pygame setup ---
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Simple pygame example')
clock = pygame.time.Clock()

# --- pybox2d world setup ---
# Create the world
world = world(gravity=(0, 0), doSleep=True)

# And a static body to hold the ground shape
ground_body = world.CreateStaticBody(
    position=(0, 0),
    features=staticBody
)

# Create a couple dynamic bodies
body = world.CreateDynamicBody(
    position=(0, 4),
    shapes=polygonShape(box=(1, 1)),
    #fixtures=polygonShape(box=(1, 1)),

)

body2 = world.CreateDynamicBody(
    position=(0, 6),
    shapes=polygonShape(box=(1, 1)),
)

# This is how to make a joint between two bodies.
# A revolute joint constrains two points on two bodies
# to be the same distance apart. This ensures a
# constant distance between the anchor points.
# If you don't supply a world anchor, the local anchor
# is assumed to be (0, 0).
joint = world.CreateRevoluteJoint(
    bodyA=ground_body,
    bodyB=body,
    anchor=(0, 5),
    collideConnected=False,
)

# This is how to make a joint between a body and the world
# anchor=(0, 0) means the anchor is the center of the object.
joint2 = world.CreateRevoluteJoint(
    bodyA=body,
    bodyB=body2,
    anchor=(0, 0),
    collideConnected=False,
)

# --- main game loop ---
while True:
    # Instruct the world to perform a single step of simulation.
    # It is generally best to keep the time step and iterations fixed.
    world.Step(TIME_STEP, 10, 10)

    # Clear applied body forces. We didn't apply any forces, but you
    # should know about this function.
    world.ClearForces()

    # Now print the position and angle of the body.
    # Note that the body gives its center position and we are
    # converting to a top left corner.
    pos = body.position
    pos2 = body2.position
    angle = body.angle
    angle2 = body2.angle
    print(pos, angle)
    print(pos2, angle2)

    # --- pygame draw ---
    screen.fill((0, 0, 0, 0))
    for body in (ground_body, body, body2):
        for fixture in body.fixtures:
            shape = fixture.shape

            # vertices are stored as relative to body position
            vertices = [(body.transform * v) * PPM for v in shape.vertices]

            # but draw needs them to be absolute
            vertices = [(v[0], SCREEN_HEIGHT - v[1]) for v in vertices]

            pygame.draw.polygon(screen, (255, 255, 255, 0), vertices)
    pygame.display.flip()
    clock.tick(TARGET_FPS)

# --- pygame end ---
pygame.quit()

# --- pybox2d end ---
# It is often useful to release memory back to the operating system
# for debugging purposes.
world = None

# --- end of file ---
