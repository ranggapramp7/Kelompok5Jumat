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