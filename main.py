from OpenGL.GL import * # type: ignore
from OpenGL.GLUT import * # type: ignore
from OpenGL.GLU import * # type: ignore
import sys
from PIL import Image
import numpy as np

from pyopengl.OpenGL.GL.exceptional import glVertex

# Camera control variables
camera_pos = [0.0, 5, 4.0]
camera_front = [0.0, 0.0, -1.0]
camera_up = [0.0, 1.0, 0.0]
yaw = -90.0
pitch = 0.0
last_x, last_y = 400, 100
first_mouse = True

move_speed = 0.05
sensitivity = .5
path = [
    "texture/meja.jpg", 
    "texture/dinding.jpg",
    "texture/floor.jpg",
    "texture/carpet.jpg",
    "texture/jam.png",
    "texture/keyboard.jpg",
    "texture/desktop.png",
    "texture/meja2.jpg",
    "texture/black.jpg",
    "texture/backpack.jfif"
    ]

textures = []

def load_texture(image_path):
    image = Image.open(image_path)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    img_data = np.array(image.convert("RGBA"))
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_data.shape[1], img_data.shape[0], 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    return texture_id

def init_textures(texture_paths):
    global textures
    textures = [load_texture(path) for path in texture_paths]


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
     # Set up lighting
    light_pos = [1.0, 1.0, 1.0, 1.0]
    light_ambient = [0.5, 0.5, 0.5, 1.0]
    light_diffuse = [0.5, 0.5, 0.5, 1.0]
    light_specular = [1.0, 1.0, 1.0, 1.0]

    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
    
    

        
        
def createRuangan():
    # SAMPING KANAN
    glBindTexture(GL_TEXTURE_2D, textures[1])
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)

    # Face 1
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2, 0, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2, 2, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2, 2, -2)
    

    # Face 2
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex(2.2, 0, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.2, 2, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2.2, 2, -2)

    # Connect the faces
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2, 0, -2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.2, 0, -2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.2, 2, -2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2, 2, -2)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(2, 0, 2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.2, 0, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.2, 2, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2, 2, 2)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2, 0, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.2, 0, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2.2, 0, -2)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(2, 2, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2, 2, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.2, 2, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2.2, 2, -2)
    
    glEnd()

    # DINDING BAWAH
    glBindTexture(GL_TEXTURE_2D, textures[2])

    glBegin(GL_QUAD_STRIP)
    glColor3f(0.8, 0.8, 0.8)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2, 0, -2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2, 0, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2, 0, 2)
    glEnd()

    glBindTexture(GL_TEXTURE_2D, textures[1])

    # SAMPING KIRI
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2, 0, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2, 2, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2, 2, -2)
    
     # Face 2
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.2, 0, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.2, 2, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.2, 2, -2)
    
    # Connect the faces
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.2, 0, -2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.2, 2, -2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2, 2, -2)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2, 0, 2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.2, 0, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.2, 2, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2, 2, 2)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2, 0, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.2, 0, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.2, 0, -2)

    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2, 2, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2, 2, 2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.2, 2, 2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.2, 2, -2)
    
    glEnd()

    # BELAKANG
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.6, 0.6)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.2, 0, -2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.2, 2, -2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.2, 2, -2)
    
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.2, 0, -2.2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.2, 0, -2.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.2, 2, -2.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.2, 2, -2.2)
    
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2.2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2.2, 0, -2.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.2, 2, -2.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.2, 2, -2)
    
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.2, 0, -2.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(2.2, 2, -2.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(2.2, 2, -2)
    
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.2, 2, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.2, 2, -2.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.2, 2, -2.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.2, 2, -2)
    
    glTexCoord2f(0.0, 0.0)
    glVertex3f(2.2, 0, -2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(2.2, 0, -2.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2.2, 0, -2.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2.2, 0, -2)
    
    glEnd()
    
def gambarJam():

    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 0.0)
    glVertex3f(-1.99,1,0)
    glVertex3f(-1.99,1,0.5)
    glVertex3f(-1.99,1.5,0.5)
    glVertex3f(-1.99,1.5,0)
    glEnd()
    
    glBindTexture(GL_TEXTURE_2D, textures[4])
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.98,1.05,0.05)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.98,1.05,0.45)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.98,1.45,0.45)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.98,1.45,0.05)
    glEnd()
    
def gambar_meja():
    #alas atas
    glBindTexture(GL_TEXTURE_2D, textures[7])
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1,1,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1,1,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1,1,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1,1,-2)
    glEnd()
    
    #alas bawah
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1,.9,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1,.9,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1,.9,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1,.9,-2)
    glEnd()
    
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1,1,-1.2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1,1,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1,.9,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1,.9,-1.2)
    glEnd()
    
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1,1,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1,1,-2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1,.9,-2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1,.9,-2)
    glEnd()
    
    #cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1,1,-1.2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1,1,-2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1,.9,-2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1,.9,-1.2)
    glEnd()
    
     #cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1,1,-1.2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1,1,-2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1,.8,-2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1,.8,-1.2)
    glEnd()
    
   
    
    #bagian kaki kanan
    #cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(1,1,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1,1,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1,0,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(1,0,-2)
    glEnd()
    
    #bagian kaki kiri
    #cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1,1,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1,1,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1,0,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1,0,-2)
    glEnd()
     # cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.2, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.9,1,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.9,1,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.9,0,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.9,0,-2)
    glEnd()
    
     # cover belakng
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1,1,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.9,1,-2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.9,0,-2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1,0,-2)
    glEnd()
    
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1,1,-1.2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.9,1,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.9,0,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1,0,-1.2)
    glEnd()
    
    #cover bawah
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1,0,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.9,0,-2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.9,0,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1,0,-1.2)
    glEnd()
    
    
    
    #laci kanan
    #conver kanan
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.2, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.5,1,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.5,1,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.5,0,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.5,0,-2)
    glEnd()
    
    #conver bawah
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.5,0.11,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1,0.11,-2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1,0.11,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.5,0.11,-1.2)
    glEnd()
    
     
    #conver belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.5,0.11,-1.99)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1,0.11,-1.99)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1,1,-1.99)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.5,1,-1.99)
    glEnd()
    
    #conver depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.5,0.01,-1.2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1,0.01,-1.2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1,.9,-1.2)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.5,.9,-1.2)
    glEnd()
    
     #conver depan lagi
    glBegin(GL_QUADS)
    glColor3f(0.33, 0.25, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.55,0.05,-1.19)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.95,0.05,-1.19)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.95,.85,-1.19)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.55,.85,-1.19)
    glEnd()
    
    glBindTexture(GL_TEXTURE_2D, textures[ 1])
    glPushMatrix()
    glColor3f(1, 1, 1)  
    glTranslatef(.6, .45, -1.19)
    glutSolidSphere(0.02, 32, 32)
    glPopMatrix()
    
    
def drawLaptop():
    #bodybawah
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.01,-1.8)
    glVertex3f(.2,1.01,-1.8)
    glVertex3f(.2,1.01,-1.5)
    glVertex3f(-.2,1.01,-1.5)
    glEnd()
    
     #bodyatas
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.019,-1.8)
    glVertex3f(.2,1.019,-1.8)
    glVertex3f(.2,1.019,-1.5)
    glVertex3f(-.2,1.019,-1.5)
    glEnd()
    #keyboard
    glBindTexture(GL_TEXTURE_2D, textures[5])

    glBegin(GL_QUADS)
    glColor3f(1, 1, 1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.18,1.02,-1.78)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.18,1.02,-1.78)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.18,1.02,-1.6)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.18,1.02,-1.6)
    glEnd()
    
     #bodysamping kanan
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(.2,1.01,-1.8)
    glVertex3f(.2,1.01,-1.5)
    glVertex3f(.2,1.019,-1.5)
    glVertex3f(.2,1.019,-1.8)
    glEnd()
    
     #bodysamping kiri
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.01,-1.8)
    glVertex3f(-.2,1.01,-1.5)
    glVertex3f(-.2,1.019,-1.5)
    glVertex3f(-.2,1.019,-1.8)
    glEnd()
    
    
     #bodysamping kiri
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.01,-1.5)
    glVertex3f(.2,1.01,-1.5)
    glVertex3f(.2,1.019,-1.5)
    glVertex3f(-.2,1.019,-1.5)
    glEnd()
    
    #layar
    #Depan
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.01,-1.8)
    glVertex3f(.2,1.01,-1.8)
    glVertex3f(.2,1.4,-1.85)
    glVertex3f(-.2,1.4,-1.85)
    glEnd()
    #belakang
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.01,-1.805)
    glVertex3f(.2,1.01,-1.805)
    glVertex3f(.2,1.4,-1.855)
    glVertex3f(-.2,1.4,-1.855)
    glEnd()
    #samping kanan
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(.2,1.01,-1.805)
    glVertex3f(.2,1.01,-1.8)
    glVertex3f(.2,1.4,-1.855)
    glVertex3f(.2,1.4,-1.85)
    glEnd()
    #samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.01,-1.805)
    glVertex3f(-.2,1.01,-1.8)
    glVertex3f(-.2,1.4,-1.855)
    glVertex3f(-.2,1.4,-1.85)
    glEnd()
     #samping atas
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.4,-1.85)
    glVertex3f(.2,1.4,-1.85)
    glVertex3f(.2,1.4,-1.855)
    glVertex3f(-.2,1.4,-1.855)
    glEnd()
    
    
    glBindTexture(GL_TEXTURE_2D, textures[6])
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.18,1.05,-1.805)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.18,1.05,-1.805)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.18,1.38,-1.845)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.18,1.38,-1.845)
    glEnd()
    
def drawKarpet():
    glBindTexture(GL_TEXTURE_2D, textures[3])

    glBegin(GL_QUADS)
    # glColor3f(0.5, 0.7, .2)
    glColor3f(.5, .5, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.2,.01,-2)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.2,.01,-2)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.2,.01,-0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.2,.01,0)
    glEnd()
    
def drawKursi():
    #dudukan
    #atas
    glBindTexture(GL_TEXTURE_2D, textures[0])
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.2,.6,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.6,-1.4)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.6,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.2,.6,-1)
    glEnd()
    #bawah
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.2,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.4)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.55,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.2,.55,-1)
    glEnd()
    #cover samping kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.2,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.6,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.2,.6,-1.4)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .1)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.2,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,.6,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.2,.6,-1.4)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.2,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.4)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.6,-1.4)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.2,.6,-1.4)
    glEnd()
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.2,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.6,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.2,.6,-1)
    glEnd()
    
    
    #kaki
    #depan kanan
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.4)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.0,-1.4)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,.0,-1.4)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1.36)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.36)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.0,-1.36)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,.0,-1.36)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.16,.55,-1.36)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.16,.0,-1.36)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,.0,-1.4)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.2,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.36)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.0,-1.36)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.2,.0,-1.4)
    glEnd()
    
    #kaki
    #depan kiri
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1.4)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,.0,-1.4)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,.0,-1.4)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1.36)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1.36)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,.0,-1.36)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,.0,-1.36)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.16,.55,-1.36)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.16,.0,-1.36)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,.0,-1.4)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.2,.55,-1.4)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1.36)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,.0,-1.36)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.2,.0,-1.4)
    glEnd()
    
    #kaki
    #belakang kiri
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1.04)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,.0,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,.0,-1.04)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,.0,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,.0,-1)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.16,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.16,.0,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,.0,-1)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.2,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,.0,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.2,.0,-1)
    glEnd()
    
    #kaki
    #belakang kanan
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1.04)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.0,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,.0,-1.04)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.0,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,.0,-1)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.16,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.16,.0,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,.0,-1)
    glEnd()
    #cover samping kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.2,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,.0,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.2,.0,-1)
    glEnd()
    
    
    #leher kanan
    #cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.2,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,1.2,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.2,1.2,-1)
    glEnd()
    #cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.16,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.16,1.2,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,1.2,-1)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,1.2,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,1.2,-1)
    glEnd()
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.55,-1.04)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,1.2,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,1.2,-1.04)
    glEnd()
    #cover atas
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.16,.1,-1.04)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.2,.1,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.2,1.2,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.16,1.2,-1)
    glEnd()
    
    #leher kiri
    #cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.2,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,1.2,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.2,1.2,-1)
    glEnd()
    #cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.16,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.16,1.2,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,1.2,-1)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,1.2,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,1.2,-1)
    glEnd()
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.55,-1.04)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.55,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,1.2,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,1.2,-1.04)
    glEnd()
    #cover atas
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.16,.1,-1.04)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.2,.1,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.2,1.2,-1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.16,1.2,-1)
    glEnd()
    
    
    #senderan
    #cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.23,1.2,-1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.23,1.2,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.23,1,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.23,1,-1.07)
    glEnd()
    #cover kanan
    #cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.23,1.2,-1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.23,1.2,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.23,1,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.23,1,-1.07)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.23,1.2,-1.04)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.23,1.2,-1.04)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.23,1,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.23,1,-1.04)
    glEnd()
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(.23,1.2,-1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-.23,1.2,-1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-.23,1,-1.07)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(.23,1,-1.07)
    glEnd()
    #cover atas
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.23,1.2,-1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.23,1.2,-1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.23,1.2,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.23,1.2,-1.04)
    glEnd()
    #cover bawah
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-.23,1,-1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(.23,1,-1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(.23,1,-1.04)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-.23,1,-1.04)
    glEnd()
    
def renderTas():
    glBindTexture(GL_TEXTURE_2D, textures[9])
    
    # Bagian belakang tas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.93, 1.5, -1.15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.93, 0.9, -1.15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.93, 0.9, -0.85)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.93, 1.5, -0.85)
    glEnd()
    
    # Bagian depan tas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.8, 1.4, -1.15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.8, 0.9, -1.15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.8, 0.9, -0.85)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.8, 1.4, -0.85)
    glEnd()
    
    # Bagian bawah tas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.93, 0.9, -1.15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.8, 0.9, -1.15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.8, 0.9, -0.85)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.93, 0.9, -0.85)
    glEnd()
    
    # Bagian atas tas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.5, -1.15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.8, 1.4, -1.15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.8, 1.4, -0.85)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.5, -0.85)
    glEnd()
    
    # Bagian atas tas 2
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.5, -1.15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.93, 1.5, -1.15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.93, 1.5, -0.85)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.5, -0.85)
    glEnd()
    
    # Samping kiri tas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.5, -0.85)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.8, 1.4, -0.85)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.8, 0.9, -0.85)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 0.9, -0.85)
    glEnd()
    
    # Samping kiri tas2
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.5, -0.85)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.93, 1.5, -0.85)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.93, 0.9, -0.85)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 0.9, -0.85)
    glEnd()
    
    # Samping kanan tas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.5, -1.15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.8, 1.4, -1.15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.8, 0.9, -1.15)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 0.9, -1.15)
    glEnd()
    
    # Samping kanan tas 2
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.5, -1.15)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.93, 1.5, -1.15)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.93, 0.9, -1.15)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 0.9, -1.15)
    glEnd()
    
    # Tali tas kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.5, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.8, 1.4, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.8, 0.9, -0.95)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.5, -0.95)
    glEnd()
    
    # Tali tas kanan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.5, -1.05)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.8, 1.4, -1.05)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.8, 0.9, -1.1)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.5, -1.1)
    glEnd()
    
    #Pegangan 
    #Pegangan atas - cover atas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.57, -1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.57, -1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.92, 1.57, -.93)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.57, -.93)
    glEnd()
    
    #Pegangan atas - cover bawah
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.56, -1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.56, -1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.92, 1.56, -.93)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.56, -.93)
    glEnd()
    
    #Pegangan atas - cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.92, 1.56, -1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.57, -1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.92, 1.57, -.93)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.92, 1.56, -.93)
    glEnd()
    
    #Pegangan atas - cover depan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.56, -1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.9, 1.57, -1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.9, 1.57, -.93)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.56, -.93)
    glEnd()
    
    #Pegangan atas - cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.56, -1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.9, 1.57, -1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.93, 1.57, -1.07)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.93, 1.56, -1.07)
    glEnd()
    
    #Pegangan atas - cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.56, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.9, 1.57, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.93, 1.57, -.93)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.93, 1.56, -.93)
    glEnd()
    
    #Pegangan kanan - cover depan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.57, -1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.9, 1.5, -1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.9, 1.5, -1.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.57, -1.05)
    glEnd()
    
    
     #Pegangan kanan - cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.92, 1.57, -1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.5, -1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.92, 1.5, -1.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.92, 1.57, -1.05)
    glEnd()
    
    #Pegangan kanan - cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.92, 1.57, -1.07)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.5, -1.07)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.9, 1.5, -1.07)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.57, -1.07)
    glEnd()
    
    #Pegangan kanan - cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.92, 1.57, -1.05)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.5, -1.05)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.9, 1.5, -1.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.57, -1.05)
    glEnd()
    
     #Pegangan kiri - cover depan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.9, 1.57, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.9, 1.5, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.9, 1.5, -.95)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.57, -.95)
    glEnd()
    
     #Pegangan kiri - cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.92, 1.57, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.5, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.92, 1.5, -.95)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.92, 1.57, -.95)
    glEnd()
    
        #Pegangan kanan - cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.92, 1.57, -.95)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.5, -.95)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.9, 1.5, -.95)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.57, -.95)
    glEnd()
    
    #Pegangan kanan - cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.92, 1.57, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.92, 1.5, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.9, 1.5, -.93)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.9, 1.57, -.93)
    glEnd()
    
     #Tali belakang - Kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.95, 1, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.95, 1.45, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95, 1.45, -.97)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95, 1, -.97)
    glEnd()
    
    
     #Tali belakang - Kiri depan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.945, 1, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.945, 1.45, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.945, 1.45, -.97)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.945, 1, -.97)
    glEnd()
    
     #Tali belakang - Kiri atas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.93, 1.5, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.945, 1.45, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.945, 1.45, -.97)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.93, 1.5, -.97)
    glEnd()
    
    #Tali belakang - Kiri atas 2
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.935, 1.5, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.95, 1.45, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95, 1.45, -.97)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.935, 1.5, -.97)
    glEnd()
    
    #Tali belakang - Kiri cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.945, 1, -.93)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.945, 1.45, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95, 1.45, -.93)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95, 1, -.93)
    glEnd()
    
    #Tali belakang - Kiri cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.93, 1, -.97)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.93, 1, -.93)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95, 1, -.93)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95, 1, -.97)
    glEnd()
    
    
    #---
    
       #Tali belakang - Kanan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.95, 1, -1.01)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.95, 1.45, -1.01)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95, 1.45, -1.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95, 1, -1.05)
    glEnd()
    
    
     #Tali belakang - Kanan depan
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.945, 1, -1.01)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.945, 1.45, -1.01)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.945, 1.45, -1.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.945, 1, -1.05)
    glEnd()
    
     #Tali belakang - Kanan atas
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.93, 1.5, -1.01)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.945, 1.45,-1.01)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.945, 1.45, -1.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.93, 1.5, -1.05)
    glEnd()
    
    #Tali belakang - Kanan atas 2
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.935, 1.5, -1.01)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.95, 1.45, -1.01)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95, 1.45, -1.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.935, 1.5, -1.05)
    glEnd()
    
    #Tali belakang - Kanan cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.945, 1, -1.01)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.945, 1.45,-1.01)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95, 1.45,-1.05)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95, 1, -1.05)
    glEnd()
    
    #Tali belakang - Kanan cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.93, 1, -1.05)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.93, 1, -1.01)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95, 1, -1.01)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95, 1, -1.05)
    glEnd()
    
    
    
    
def renderHanger():
    glBindTexture(GL_TEXTURE_2D, textures[0])
    #Bagian atas
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2,1.6,-1.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.95,1.6,-1.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95,1.6,-.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2,1.6,-.5)
    glEnd()
    #Bagian bawah
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2,1.5,-1.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.95,1.5,-1.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95,1.5,-.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2,1.5,-.5)
    glEnd()
    #Bagian belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2,1.6,-1.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2,1.5,-1.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-2,1.5,-.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-2,1.6,-.5)
    glEnd()
    #Bagian depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.95,1.6,-1.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-1.95,1.5,-1.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95,1.5,-.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95,1.6,-.5)
    glEnd()
    #Bagian kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2,1.6,-1.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2,1.5,-1.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95,1.5,-1.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95,1.6,-1.5)
    glEnd()
    #Bagian kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-2,1.6,-.5)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(-2,1.5,-.5)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(-1.95,1.5,-.5)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.95,1.6,-.5)
    glEnd()
    
    
    #Hook 1
    z = -.6
    while z > -1.5:
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.95,1.55,z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.95,1.55,z-.01)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.9,1.55,z-.01)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.9,1.55,z)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.95,1.56,z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.95,1.56,z-.01)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.9,1.56,z-.01)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.9,1.56,z)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.95,1.55,z)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.95,1.56,z)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.9,1.56,z)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.9,1.55,z)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.95,1.55,z-.01)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.95,1.56,z-.01)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.9,1.56,z-.01)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.9,1.55,z-.01)
        glEnd()
        
        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        glTexCoord2f(0.0, 0.0)
        glVertex3f(-1.9,1.55,z-.01)
        glTexCoord2f(1.0, 0.0)
        glVertex3f(-1.9,1.56,z-.01)
        glTexCoord2f(1.0, 1.0)
        glVertex3f(-1.9,1.56,z-.01)
        glTexCoord2f(0.0, 1.0)
        glVertex3f(-1.9,1.55,z-.01)
        glEnd()
        z -= .2
        
def draw_cylinder(radius, height, slices):
    quad = gluNewQuadric()
    gluCylinder(quad, radius, radius, height, slices, 1)
    gluDeleteQuadric(quad)        

def renderLampuBelajar():
    glBindTexture(GL_TEXTURE_2D, textures[8])

    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(.8, 1.01, -1.5)
    glRotatef(-90, 1, 0, 0)
    glutSolidCylinder(.1, 0.02, 15, 1)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(.8, 1.01, -1.5)
    glRotatef(-90, 1, 0, 0)
    draw_cylinder(0.015, .3, 10)
    glPopMatrix()
    
    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(.8, 1.3, -1.5)
    glRotatef(-90, 1, 0, 0)
    glRotatef(-35, 0, 1, 0)
    draw_cylinder(0.015, .5, 10)
    glPopMatrix()

    glPushMatrix()
    glColor3f(1, 1, 1)
    glTranslatef(.45, 1.62, -1.54)
    glRotatef(-80, 1, 0, 0)
    glRotatef(45, 0, 1, 0)
    glutSolidCone(0.1, .12, 32, 10)
    glPopMatrix()
    
    glBindTexture(GL_TEXTURE_2D, textures[ 1])
    glPushMatrix()
    glColor3f(1, 1, 1)  
    glTranslatef(.45, 1.62, -1.54)
    glutSolidSphere(0.05, 32, 32)
    glPopMatrix()
    
    glEnable(GL_LIGHT1)
    glLightfv(GL_LIGHT1, GL_POSITION, [0.45, 2, -1.54, 1.0])
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [1.0, 1.0, 0.8, 1.0])
    glLightfv(GL_LIGHT1, GL_SPECULAR, [1.0, 1.0, 0.8, 1.0])
    glLightf(GL_LIGHT1, GL_CONSTANT_ATTENUATION, 1.0)
    glLightf(GL_LIGHT1, GL_LINEAR_ATTENUATION, 0.05)
    glLightf(GL_LIGHT1, GL_QUADRATIC_ATTENUATION, 0.001)


def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    camera_target = [camera_pos[0] + camera_front[0], 
                     camera_pos[1] + camera_front[1], 
                     camera_pos[2] + camera_front[2]]
    gluLookAt(camera_pos[0], camera_pos[1], camera_pos[2], 
              camera_target[0], camera_target[1], camera_target[2], 
              camera_up[0], camera_up[1], camera_up[2])
    
    createRuangan()
    gambarJam()
    gambar_meja()
    drawKarpet()
    drawLaptop()
    drawKursi()
    renderHanger()
    renderTas()
    renderLampuBelajar()
    glutSwapBuffers()


def keyboard(key, x, y):
    global camera_pos
    camera_speed = move_speed
    print(key)
    if key == b'\x1b':  # ESC key
        sys.exit()
    if key == b'w':
        camera_pos[0] += camera_speed * camera_front[0]
        camera_pos[1] += camera_speed * camera_front[1]
        camera_pos[2] += camera_speed * camera_front[2]
    if key == b's':
        camera_pos[0] -= camera_speed * camera_front[0]
        camera_pos[1] -= camera_speed * camera_front[1]
        camera_pos[2] -= camera_speed * camera_front[2]
    if key == b'a':
        camera_pos[0] -= np.cross(camera_front, camera_up)[0] * camera_speed
        camera_pos[1] -= np.cross(camera_front, camera_up)[1] * camera_speed
        camera_pos[2] -= np.cross(camera_front, camera_up)[2] * camera_speed
    if key == b'd':
        camera_pos[0] += np.cross(camera_front, camera_up)[0] * camera_speed
        camera_pos[1] += np.cross(camera_front, camera_up)[1] * camera_speed
        camera_pos[2] += np.cross(camera_front, camera_up)[2] * camera_speed

def mouse_motion(x, y):
    global yaw, pitch, last_x, last_y, first_mouse, camera_front

    if first_mouse:
        last_x, last_y = x, y
        first_mouse = False

    xoffset = x - last_x
    yoffset = last_y - y  # reversed: y ranges bottom to top
    last_x, last_y = x, y

    xoffset *= sensitivity
    yoffset *= sensitivity

    yaw += xoffset
    pitch += yoffset

    # constrain the pitch
    if pitch > 89.0:
        pitch = 89.0
    if pitch < -89.0:
        pitch = -89.0

    front = [0.0, 0.0, 0.0]
    front[0] = np.cos(np.radians(yaw)) * np.cos(np.radians(pitch))
    front[1] = np.sin(np.radians(pitch))
    front[2] = np.sin(np.radians(yaw)) * np.cos(np.radians(pitch))
    camera_front = np.array(front) / np.linalg.norm(front)

def main():
    global path
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutCreateWindow(b"3D Sphere with Camera Control")
    init()
    init_textures(path)
    glutDisplayFunc(render)
    glutIdleFunc(render)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse_motion)
    glutMainLoop()


main()
input()
