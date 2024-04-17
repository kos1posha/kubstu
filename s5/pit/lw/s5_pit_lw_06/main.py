from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


width = 800
height = 600

rotate = {'x': 0, 'y': 0, 'z': 0}
center = {'x': 1.25, 'y': 0.25, 'z': 0.25}

isOrthoProjection = True
rotationMode = 0


def reshape(w, h):
    global width, height
    width = w
    height = h


def display():
    global rotate, center, isOrthoProjection, rotationMode

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    if isOrthoProjection:
        glOrtho(-2.0, 2.0, -2.0, 2.0, -2.0, 2.0)
    else:
        gluPerspective(100.0, width / height, 0.0, 500.0)
        gluLookAt(1.0, 0.5, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    glTranslatef(1.0, 0.0, 0.0)
    if rotationMode == 0:
        glTranslatef(-center['x'], -center['y'], -center['z'])
        glRotatef(rotate['x'], 1.0, 0.0, 0.0)
        glRotatef(rotate['y'], 0.0, 1.0, 0.0)
        glRotatef(rotate['z'], 0.0, 0.0, 1.0)
        glTranslatef(center['x'], center['y'], center['z'])
    elif rotationMode == 1:
        glRotatef(rotate['x'], 1.0, 0.0, 0.0)
        glRotatef(rotate['y'], 0.0, 1.0, 0.0)
        glRotatef(rotate['z'], 0.0, 0.0, 1.0)

    glScalef(1.0, 1.3, 1.0)

    glPushMatrix()
    glColor4f(1.0, 0.8431, 0.3, 1.0)
    if rotationMode == 2:
        glRotatef(rotate['x'], 1.0, 0.0, 0.0)
        glRotatef(rotate['y'], 0.0, 1.0, 0.0)
        glRotatef(rotate['z'], 0.0, 0.0, 1.0)
    glutSolidCube(0.5)
    glPopMatrix()

    glScalef(1.0, 0.5, 1.0)
    glTranslatef(0.5, -0.25, 0.0)

    glPushMatrix()
    glColor4f(0.80, 0.49, 0.19, 1.0)
    if rotationMode == 2:
        glRotatef(rotate['x'], 1.0, 0.0, 0.0)
        glRotatef(rotate['y'], 0.0, 1.0, 0.0)
        glRotatef(rotate['z'], 0.0, 0.0, 1.0)
    glutSolidCube(0.5)
    glPopMatrix()

    glTranslatef(-0.5, 0.25, 0.0)
    glScalef(1.0, 2.0, 1.0)

    glScalef(1.0, 0.7, 1.0)
    glTranslatef(-0.5, -0.110, 0.0)

    glPushMatrix()
    glColor4f(0.75, 0.75, 0.75, 1.0)
    if rotationMode == 2:
        glRotatef(rotate['x'], 1.0, 0.0, 0.0)
        glRotatef(rotate['y'], 0.0, 1.0, 0.0)
        glRotatef(rotate['z'], 0.0, 0.0, 1.0)
    glutSolidCube(0.5)
    glPopMatrix()

    glTranslatef(0.5, 0.105, 0.0)
    glScalef(1.0, 1.4, 1.0)

    glFlush()
    glutSwapBuffers()


def special(key, x, y):
    global rotate, isOrthoProjection, rotationMode

    if key == GLUT_KEY_UP:
        rotate['x'] += 5
    elif key == GLUT_KEY_DOWN:
        rotate['x'] -= 5
    elif key == GLUT_KEY_RIGHT:
        rotate['y'] += 5
    elif key == GLUT_KEY_LEFT:
        rotate['y'] -= 5
    elif key == GLUT_KEY_PAGE_UP:
        rotate['z'] += 5
    elif key == GLUT_KEY_PAGE_DOWN:
        rotate['z'] -= 5
    elif key == GLUT_KEY_F1:
        rotationMode = 0
        rotate['x'] = rotate['y'] = rotate['z'] = 0
    elif key == GLUT_KEY_F2:
        rotationMode = 1
        rotate['x'] = rotate['y'] = rotate['z'] = 0
    elif key == GLUT_KEY_F3:
        rotationMode = 2
        rotate['x'] = rotate['y'] = rotate['z'] = 0
    elif key == GLUT_KEY_F4:
        isOrthoProjection = not isOrthoProjection

    glutPostRedisplay()


def initGL():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.0, 4.0, 10.0, 1.0]
    lightZeroColor = [0.2, 0.9, 0.8, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.5)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.4)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)


def main():
    glutInit()
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(width, height)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutCreateWindow('OpenGL')
    glutReshapeFunc(reshape)
    initGL()
    glutDisplayFunc(display)
    glutSpecialFunc(special)
    glutMainLoop()


if __name__ == "__main__":
    main()
