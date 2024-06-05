from OpenGL.GL import * # type: ignore
from OpenGL.GLUT import * # type: ignore
from OpenGL.GLU import * # type: ignore
import sys
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

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 1, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

        
        
def createRuangan():
    # SAMPING KANAN
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)

    # Face 1
    glVertex3f(2, 0, -2)
    glVertex3f(2, 0, 2)
    glVertex3f(2, 2, 2)
    glVertex3f(2, 2, -2)

    # Face 2
    glVertex3f(2.2, 0, -2)
    glVertex(2.2, 0, 2)
    glVertex3f(2.2, 2, 2)
    glVertex3f(2.2, 2, -2)

    # Connect the faces
    glVertex3f(2, 0, -2)
    glVertex3f(2.2, 0, -2)
    glVertex3f(2.2, 2, -2)
    glVertex3f(2, 2, -2)

    glVertex3f(2, 0, 2)
    glVertex3f(2.2, 0, 2)
    glVertex3f(2.2, 2, 2)
    glVertex3f(2, 2, 2)

    glVertex3f(2, 0, -2)
    glVertex3f(2, 0, 2)
    glVertex3f(2.2, 0, 2)
    glVertex3f(2.2, 0, -2)

    glVertex3f(2, 2, -2)
    glVertex3f(2, 2, 2)
    glVertex3f(2.2, 2, 2)
    glVertex3f(2.2, 2, -2)
    
    glEnd()

    # DINDING BAWAH
    glBegin(GL_QUAD_STRIP)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-2, 0, -2)
    glVertex3f(2, 0, -2)
    glVertex3f(-2, 0, 2)
    glVertex3f(2, 0, 2)
    glEnd()

    # SAMPING KIRI
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)
    
    glVertex3f(-2, 0, -2)
    glVertex3f(-2, 0, 2)
    glVertex3f(-2, 2, 2)
    glVertex3f(-2, 2, -2)
    
     # Face 2
    glVertex3f(-2.2, 0, -2)
    glVertex3f(-2.2, 0, 2)
    glVertex3f(-2.2, 2, 2)
    glVertex3f(-2.2, 2, -2)
    
    # Connect the faces
    glVertex3f(-2, 0, -2)
    glVertex3f(-2.2, 0, -2)
    glVertex3f(-2.2, 2, -2)
    glVertex3f(-2, 2, -2)

    glVertex3f(-2, 0, 2)
    glVertex3f(-2.2, 0, 2)
    glVertex3f(-2.2, 2, 2)
    glVertex3f(-2, 2, 2)

    glVertex3f(-2, 0, -2)
    glVertex3f(-2, 0, 2)
    glVertex3f(-2.2, 0, 2)
    glVertex3f(-2.2, 0, -2)

    glVertex3f(-2, 2, -2)
    glVertex3f(-2, 2, 2)
    glVertex3f(-2.2, 2, 2)
    glVertex3f(-2.2, 2, -2)
    
    glEnd()

    # BELAKANG
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.6, 0.6)
    glVertex3f(-2.2, 0, -2)
    glVertex3f(2.2, 0, -2)
    glVertex3f(2.2, 2, -2)
    glVertex3f(-2.2, 2, -2)
    
    glVertex3f(-2.2, 0, -2.2)
    glVertex3f(2.2, 0, -2.2)
    glVertex3f(2.2, 2, -2.2)
    glVertex3f(-2.2, 2, -2.2)
    
    glVertex3f(-2.2, 0, -2)
    glVertex3f(-2.2, 0, -2.2)
    glVertex3f(-2.2, 2, -2.2)
    glVertex3f(-2.2, 2, -2)
    
    glVertex3f(2.2, 0, -2)
    glVertex3f(2.2, 0, -2.2)
    glVertex3f(2.2, 2, -2.2)
    glVertex3f(2.2, 2, -2)
    
    glVertex3f(2.2, 2, -2)
    glVertex3f(2.2, 2, -2.2)
    glVertex3f(-2.2, 2, -2.2)
    glVertex3f(-2.2, 2, -2)
    
    glVertex3f(2.2, 0, -2)
    glVertex3f(2.2, 0, -2.2)
    glVertex3f(-2.2, 0, -2.2)
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
    
    glBegin(GL_QUADS)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(-1.98,1.1,0.1)
    glVertex3f(-1.98,1.1,0.4)
    glVertex3f(-1.98,1.4,0.4)
    glVertex3f(-1.98,1.4,0.1)
    glEnd()
    
def gambar_meja():
    #alas atas
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glVertex3f(1,1,-2)
    glVertex3f(1,1,-1.2)
    glVertex3f(-1,1,-1.2)
    glVertex3f(-1,1,-2)
    glEnd()
    
    #alas bawah
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glVertex3f(1,.9,-2)
    glVertex3f(1,.9,-1.2)
    glVertex3f(-1,.9,-1.2)
    glVertex3f(-1,.9,-2)
    glEnd()
    
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glVertex3f(1,1,-1.2)
    glVertex3f(-1,1,-1.2)
    glVertex3f(-1,.9,-1.2)
    glVertex3f(1,.9,-1.2)
    glEnd()
    
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glVertex3f(1,1,-2)
    glVertex3f(-1,1,-2)
    glVertex3f(-1,.9,-2)
    glVertex3f(1,.9,-2)
    glEnd()
    
    #cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glVertex3f(1,1,-1.2)
    glVertex3f(1,1,-2)
    glVertex3f(1,.8,-2)
    glVertex3f(1,.8,-1.2)
    glEnd()
    
     #cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glVertex3f(-1,1,-1.2)
    glVertex3f(-1,1,-2)
    glVertex3f(-1,.8,-2)
    glVertex3f(-1,.8,-1.2)
    glEnd()
    
    #bagian kaki kanan
    #cover kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glVertex3f(1,1,-2)
    glVertex3f(1,1,-1.2)
    glVertex3f(1,0,-1.2)
    glVertex3f(1,0,-2)
    glEnd()
    
    #bagian kaki kiri
    #cover kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, 0.0)
    glVertex3f(-1,1,-2)
    glVertex3f(-1,1,-1.2)
    glVertex3f(-1,0,-1.2)
    glVertex3f(-1,0,-2)
    glEnd()
    
    #laci kanan
    #conver kanan
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(.5,1,-2)
    glVertex3f(.5,1,-1.2)
    glVertex3f(.5,0,-1.2)
    glVertex3f(.5,0,-2)
    glEnd()
    
    #conver bawah
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(.5,0.11,-2)
    glVertex3f(1,0.11,-2)
    glVertex3f(1,0.11,-1.2)
    glVertex3f(.5,0.11,-1.2)
    glEnd()
    
     
    #conver belakang
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(.5,0.11,-1.99)
    glVertex3f(1,0.11,-1.99)
    glVertex3f(1,1,-1.99)
    glVertex3f(.5,1,-1.99)
    glEnd()
    
    #conver depan
    glBegin(GL_QUADS)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(.5,0.11,-1.2)
    glVertex3f(1,0.11,-1.2)
    glVertex3f(1,1,-1.2)
    glVertex3f(.5,1,-1.2)
    glEnd()
    
    
def drawLaptop():
    #bodybawah
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.01,-1.8)
    glVertex3f(.2,1.01,-1.8)
    glVertex3f(.2,1.01,-1.5)
    glVertex3f(-.2,1.01,-1.5)
    glEnd()
    
    #layar
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.8, 0.8)
    glVertex3f(-.2,1.01,-1.8)
    glVertex3f(.2,1.01,-1.8)
    glVertex3f(.2,1.4,-1.85)
    glVertex3f(-.2,1.4,-1.85)
    glEnd()
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)
    glVertex3f(-.18,1.07,-1.805)
    glVertex3f(.18,1.07,-1.805)
    glVertex3f(.18,1.39,-1.845)
    glVertex3f(-.18,1.39,-1.845)
    glEnd()
    
def drawKarpet():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.7, .2)
    glVertex3f(-1.2,.01,-2)
    glVertex3f(1.2,.01,-2)
    glVertex3f(1.2,.01,-0)
    glVertex3f(-1.2,.01,0)
    glEnd()
    
def drawKursi():
    #dudukan
    #atas
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .1)
    glVertex3f(-.2,.6,-1.4)
    glVertex3f(.2,.6,-1.4)
    glVertex3f(.2,.6,-1)
    glVertex3f(-.2,.6,-1)
    glEnd()
    #bawah
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .1)
    glVertex3f(-.2,.55,-1.4)
    glVertex3f(.2,.55,-1.4)
    glVertex3f(.2,.55,-1)
    glVertex3f(-.2,.55,-1)
    glEnd()
    #cover samping kanan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .1)
    glVertex3f(.2,.55,-1.4)
    glVertex3f(.2,.55,-1)
    glVertex3f(.2,.6,-1)
    glVertex3f(.2,.6,-1.4)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .1)
    glVertex3f(-.2,.55,-1.4)
    glVertex3f(-.2,.55,-1)
    glVertex3f(-.2,.6,-1)
    glVertex3f(-.2,.6,-1.4)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glVertex3f(-.2,.55,-1.4)
    glVertex3f(.2,.55,-1.4)
    glVertex3f(.2,.6,-1.4)
    glVertex3f(-.2,.6,-1.4)
    glEnd()
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glVertex3f(-.2,.55,-1)
    glVertex3f(.2,.55,-1)
    glVertex3f(.2,.6,-1)
    glVertex3f(-.2,.6,-1)
    glEnd()
    
    
    #kaki
    #depan kanan
    #cover depan
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glVertex3f(.16,.55,-1.4)
    glVertex3f(.2,.55,-1.4)
    glVertex3f(.2,.0,-1.4)
    glVertex3f(.16,.0,-1.4)
    glEnd()
    #cover belakang
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glVertex3f(.16,.55,-1.36)
    glVertex3f(.2,.55,-1.36)
    glVertex3f(.2,.0,-1.36)
    glVertex3f(.16,.0,-1.36)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glVertex3f(.16,.55,-1.4)
    glVertex3f(.16,.55,-1.36)
    glVertex3f(.16,.0,-1.36)
    glVertex3f(.16,.0,-1.4)
    glEnd()
    #cover samping kiri
    glBegin(GL_QUADS)
    glColor3f(0.4, 0.3, .5)
    glVertex3f(.2,.55,-1.4)
    glVertex3f(.2,.55,-1.36)
    glVertex3f(.2,.0,-1.36)
    glVertex3f(.2,.0,-1.4)
    glEnd()

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
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(1000, 800)
    glutCreateWindow(b"3D Sphere with Camera Control")
    init()
    glutDisplayFunc(render)
    glutIdleFunc(render)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse_motion)
    glutMainLoop()

if __name__ == "__main__":
    main()
