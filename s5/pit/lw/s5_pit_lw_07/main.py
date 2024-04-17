import math

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image


textBg, texCarBody, texCarWindow = None, None, None
w, h, l = 0, 0, 0
car_x, car_y, car_angle = 0, 0, 0
speed = 10
rotate_x, rotate_y, rotate_z = 0, 0, 0
flags = [False, False, False, False, False]
cam_dist, ang_hor, ang_vert = 15, 20, 40


def load_texture(file_path):
    image = Image.open(file_path)
    image_data = image.convert('RGBA').tobytes()
    texture_id = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)

    return texture_id


def load_textures():
    global textBg, texCarBody, texCarWindow
    textBg = load_texture('assets\\road.bmp')
    texCarBody = load_texture('assets\\car.bmp')
    texCarWindow = load_texture('assets\\window.bmp')


def init():
    global rotate_x, rotate_y, rotate_z, car_x, car_y
    rotate_x = 0
    rotate_y = 0
    rotate_z = 0
    car_x = -450
    car_y = 100
    glClearColor(0.3, 0.5, 0.5, 1.0)
    glLoadIdentity()
    load_textures()
    glLightModelf(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
    glEnable(GL_NORMALIZE)


def draw_road():
    glBindTexture(GL_TEXTURE_2D, textBg)
    glEnable(GL_TEXTURE_2D)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-500.0, 0.0, 0.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-500.0, 0.0, 320.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(520.0, 0.0, 320.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(520.0, 0.0, 0.0)
    glEnd()
    glDisable(GL_TEXTURE_2D)


def draw_lamps():
    glColor3f(0.3, 0.1, 0.4)
    glPushMatrix()
    glTranslatef(10.0, 10.0, 10.0)
    glutSolidCube(20)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(10.0, 10.0, 300.0)
    glutSolidCube(20)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(300.0, 10.0, 10.0)
    glutSolidCube(20)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(300.0, 10.0, 300.0)
    glutSolidCube(20)
    glPopMatrix()
    glColor3f(1, 1, 1)
    glColor3f(1, 0.76, 0.678)
    glPushMatrix()
    glTranslatef(10.0, 25.0, 10.0)
    glutSolidCube(30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(10.0, 25.0, 300.0)
    glutSolidCube(30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(300.0, 25.0, 10.0)
    glutSolidCube(30)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(300.0, 25.0, 300.0)
    glutSolidCube(30)
    glPopMatrix()
    glColor3f(1, 1, 1)


def draw_car():
    r = 7
    w1 = 80
    l1 = 60
    glPushMatrix()
    glTranslatef(car_x, 0, car_y)
    glRotatef(car_angle, 0, 1, 0)
    glTranslatef(-car_x, 0, -car_y)
    glColor3f(0.0, 0.0, 0.0)
    glPushMatrix()
    glTranslatef(car_x + r, r + 1, car_y + l1)
    glutSolidTorus(3, r, 54, 54)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(car_x + w1 - r, r + 1, car_y + l1)
    glutSolidTorus(3, r, 54, 54)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(car_x + r, r + 1, car_y)
    glutSolidTorus(3, r, 54, 54)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(car_x + w1 - r, r + 1, car_y)
    glutSolidTorus(3, r, 54, 54)
    glPopMatrix()
    glBindTexture(GL_TEXTURE_2D, texCarBody)
    glEnable(GL_TEXTURE_2D)
    d = 12
    glColor3f(0.40, 0.35, 0.35)
    glBegin(GL_QUAD_STRIP)
    glVertex3f(car_x, 40.0, car_y)
    glTexCoord2f(0, 0)
    glVertex3f(car_x + w1, 40.0, car_y)
    glTexCoord2f(1, 0)
    glVertex3f(car_x, 40.0, car_y + l1)
    glTexCoord2f(0, 1)
    glVertex3f(car_x + w1, 40.0, car_y + l1)
    glTexCoord2f(1, 1)
    glVertex3f(car_x, d, car_y + l1)
    glTexCoord2f(0, 0)
    glVertex3f(car_x + w1, d, car_y + l1)
    glTexCoord2f(1, 0)
    glVertex3f(car_x, d, car_y)
    glTexCoord2f(1, 1)
    glVertex3f(car_x + w1, d, car_y)
    glTexCoord2f(0, 1)
    glVertex3f(car_x, 40.0, car_y)
    glTexCoord2f(0, 0)
    glVertex3f(car_x + w1, 40.0, car_y)
    glTexCoord2f(1, 0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f(car_x, 40.0, car_y)
    glTexCoord2f(0, 1)
    glVertex3f(car_x, 40.0, car_y + l1)
    glTexCoord2f(1, 1)
    glVertex3f(car_x, d, car_y + l1)
    glTexCoord2f(1, 0)
    glVertex3f(car_x, d, car_y)
    glTexCoord2f(0, 0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f(car_x + w1, 40.0, car_y)
    glTexCoord2f(0, 1)
    glVertex3f(car_x + w1, 40.0, car_y + l1)
    glTexCoord2f(1, 1)
    glVertex3f(car_x + w1, d, car_y + l1)
    glTexCoord2f(1, 0)
    glVertex3f(car_x + w1, d, car_y)
    glTexCoord2f(0, 0)
    glEnd()
    glBegin(GL_QUAD_STRIP)
    glVertex3f(car_x + w1 - 30, 70.0, car_y)
    glTexCoord2f(0, 0)
    glVertex3f(car_x + w1, 70.0, car_y)
    glTexCoord2f(1, 0)
    glVertex3f(car_x + w1 - 30, 70.0, car_y + l1)
    glTexCoord2f(1, 1)
    glVertex3f(car_x + w1, 70.0, car_y + l1)
    glTexCoord2f(0, 1)
    glVertex3f(car_x + w1 - 30, 40.0, car_y + l1)
    glTexCoord2f(0, 0)
    glVertex3f(car_x + w1, 40.0, car_y + l1)
    glTexCoord2f(1, 0)
    glVertex3f(car_x + w1 - 30, 40.0, car_y)
    glTexCoord2f(0, 1)
    glVertex3f(car_x + w1, 40.0, car_y)
    glTexCoord2f(1, 1)
    glVertex3f(car_x + w1 - 30, 70.0, car_y)
    glTexCoord2f(1, 0)
    glVertex3f(car_x + w1, 70.0, car_y)
    glTexCoord2f(0, 0)
    glEnd()
    glBegin(GL_QUADS)
    glVertex3f(car_x + w1 - 30, 70.0, car_y)
    glTexCoord2f(0, 0)
    glVertex3f(car_x + w1 - 30, 70.0, car_y + l1)
    glTexCoord2f(1, 0)
    glVertex3f(car_x + w1 - 30, 40.0, car_y + l1)
    glTexCoord2f(1, 1)
    glVertex3f(car_x + w1 - 30, 40.0, car_y)
    glTexCoord2f(0, 1)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glBindTexture(GL_TEXTURE_2D, texCarWindow)
    glEnable(GL_TEXTURE_2D)
    glColor3f(0.55, 0.9, 0.9)
    glBegin(GL_QUADS)
    glVertex3f(car_x + w1, 70.0, car_y)
    glTexCoord2f(0, 0)
    glVertex3f(car_x + w1, 70.0, car_y + l1)
    glTexCoord2f(1, 0)
    glVertex3f(car_x + w1, 40.0, car_y + l1)
    glTexCoord2f(1, 1)
    glVertex3f(car_x + w1, 40.0, car_y)
    glTexCoord2f(0, 1)
    glEnd()
    glDisable(GL_TEXTURE_2D)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(car_x, 0, car_y)
    glRotatef(car_angle, 0, 1, 0)
    glTranslatef(-car_x, 0, -car_y)
    glPushMatrix()
    glColor3f(0.7, 0.7, 0.2)
    glTranslatef(car_x + w1 + 5, 35, car_y + 10)
    glutSolidSphere(5, 48, 48)
    glPopMatrix()
    glPushMatrix()
    glColor3f(0.7, 0.7, 0.2)
    glTranslatef(car_x + w1 + 5, 35, car_y + l1 - 10)
    glutSolidSphere(5, 48, 48)
    glPopMatrix()
    glPopMatrix()
    glColor3f(1, 1, 1)


def add_lights():
    glPushMatrix()
    glLoadIdentity()
    light_pos0 = [0, 0, 0, 1.0]
    dif = [1, 0.76, 0.978, 1.0]
    dif_p = [0.7, 0.7, 0.2, 1.0]
    sp1 = [0, 0, -1]
    coff1 = [180]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos0)
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, sp1)
    glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF, coff1)
    light_pos = [300.0, 20.0, 10.0, 1.0]
    light_pos1 = [10.0, 20.0, 10.0, 1.0]
    light_pos2 = [10.0, 20.0, 300.0, 1.0]
    light_pos3 = [300.0, 20.0, 300.0, 1.0]
    glLightfv(GL_LIGHT1, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT1, GL_DIFFUSE, dif)
    glLightfv(GL_LIGHT2, GL_POSITION, light_pos1)
    glLightfv(GL_LIGHT2, GL_DIFFUSE, dif)
    glLightfv(GL_LIGHT3, GL_POSITION, light_pos2)
    glLightfv(GL_LIGHT3, GL_DIFFUSE, dif)
    glLightfv(GL_LIGHT4, GL_POSITION, light_pos3)
    glLightfv(GL_LIGHT4, GL_DIFFUSE, dif)
    light_pos_p = [0, 0, 0, 1]
    sp = [-0.45, 0.15, -1]
    coff = [45.0]
    se = [15.0]
    glPushMatrix()
    glTranslatef(car_x, 0, car_y)
    glRotatef(car_angle, 0, 0, 1)
    glTranslatef(-car_x, 0, -car_y)
    glPushMatrix()
    glTranslatef(car_x, 25, car_y + 7)
    glLightfv(GL_LIGHT5, GL_POSITION, light_pos_p)
    glLightfv(GL_LIGHT5, GL_SPOT_DIRECTION, sp)
    glLightfv(GL_LIGHT5, GL_SPOT_CUTOFF, coff)
    glLightfv(GL_LIGHT5, GL_SPOT_EXPONENT, se)
    glLightfv(GL_LIGHT5, GL_DIFFUSE, dif_p)
    glPopMatrix()
    glPushMatrix()
    glTranslatef(car_x, 25, car_y + l - 7)
    glLightfv(GL_LIGHT6, GL_POSITION, light_pos_p)
    glLightfv(GL_LIGHT6, GL_SPOT_DIRECTION, sp)
    glLightfv(GL_LIGHT6, GL_SPOT_CUTOFF, coff)
    glLightfv(GL_LIGHT6, GL_SPOT_EXPONENT, se)
    glLightfv(GL_LIGHT6, GL_DIFFUSE, dif_p)
    glPopMatrix()
    glPopMatrix()
    glPopMatrix()


def display():
    global rotate_x, rotate_y, rotate_z, car_x, car_y
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(360.0, 360.0, 360.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
    glRotatef(rotate_x, 1.0, 0.0, 0.0)
    glRotatef(rotate_y, 0.0, 1.0, 0.0)
    glRotatef(rotate_z, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    if flags[0]:
        glEnable(GL_LIGHT1)
    if flags[1]:
        glEnable(GL_LIGHT2)
    if flags[2]:
        glEnable(GL_LIGHT3)
    if flags[3]:
        glEnable(GL_LIGHT4)
    if flags[4]:
        glEnable(GL_LIGHT5)
        glEnable(GL_LIGHT6)
    add_lights()
    draw_road()
    draw_lamps()
    draw_car()
    glDisable(GL_LIGHT0)
    glDisable(GL_LIGHT1)
    glDisable(GL_LIGHT2)
    glDisable(GL_LIGHT3)
    glDisable(GL_LIGHT4)
    glDisable(GL_LIGHT5)
    glDisable(GL_LIGHT6)
    glDisable(GL_LIGHTING)
    glDisable(GL_DEPTH_TEST)
    glFlush()
    glutSwapBuffers()


def camera_move():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, float(w) / h, 1.0, 1000.0)
    glMatrixMode(GL_MODELVIEW)


def reshape(width, height):
    global w, h
    w = width
    h = height
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(65.0, w / h, 1.0, 1000.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    camera_move()


def keyboard(key, x, y):
    global rotate_x, rotate_y, rotate_z
    if key == b'w':
        rotate_x -= 5
    elif key == b's':
        rotate_x += 5
    elif key == b'a':
        rotate_y -= 5
    elif key == b'd':
        rotate_y += 5
    elif key == b'q':
        rotate_z -= 5
    elif key == b'e':
        rotate_z += 5
    if key == b'1':
        flags[0] = not flags[0]
    elif key == b'2':
        flags[1] = not flags[1]
    elif key == b'3':
        flags[2] = not flags[2]
    elif key == b'4':
        flags[3] = not flags[3]
    elif key == b'5':
        flags[4] = not flags[4]
    glutPostRedisplay()


def special(key, x, y):
    global car_x, car_y, car_angle, rotate_x, rotate_y, rotate_z, speed
    if key == GLUT_KEY_UP:
        car_x += math.cos(-car_angle / 180 * math.pi) * speed
        car_y += math.sin(-car_angle / 180 * math.pi) * speed
        speed += 0.6
    elif key == GLUT_KEY_DOWN:
        car_x -= math.cos(-car_angle / 180 * math.pi) * speed
        car_y -= math.sin(-car_angle / 180 * math.pi) * speed
        speed += 0.3
    else:
        speed = 10
    if key == GLUT_KEY_LEFT:
        car_angle += 10
    elif key == GLUT_KEY_RIGHT:
        car_angle -= 10
    elif key == GLUT_KEY_F1:
        flags[0] = not flags[0]
    elif key == GLUT_KEY_F2:
        flags[1] = not flags[1]
    elif key == GLUT_KEY_F3:
        flags[2] = not flags[2]
    elif key == GLUT_KEY_F4:
        flags[3] = not flags[3]
    elif key == GLUT_KEY_F5:
        flags[4] = not flags[4]
    glutPostRedisplay()


def main():
    global w, h
    glutInit(sys.argv)
    glutInitWindowPosition(50, 50)
    glutInitWindowSize(800, 600)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA)
    glutCreateWindow('Vroom vroom')
    init()
    glEnable(GL_COLOR_MATERIAL)
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(special)
    glutMainLoop()


if __name__ == "__main__":
    main()
