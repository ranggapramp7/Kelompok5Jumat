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