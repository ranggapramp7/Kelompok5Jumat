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