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