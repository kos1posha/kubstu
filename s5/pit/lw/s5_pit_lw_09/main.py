from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from glew import glewInit


frag_color = [160.0, 32.0, 240.0]
bfrag_color = [173.0, 255.0, 47.0]

cntLine = 100
mode = 2

vsPath = 'shaders\\vertex.shader'
fsPath1 = 'shaders\\fragment.shader'
fsPath2 = 'shaders\\fragment_row.shader'
fsPath3 = 'shaders\\fragment_columns.shader'

w, h = 800, 800
program = None
attrib_vertex = None
unif_matr = None
unif_color = None
unif_color_back = None
unif_cntLine = None


def check_openGL_error():
    errCode = glGetError()
    if errCode != GL_NO_ERROR:
        print('OpenGl error! -', gluErrorString(errCode))


def load_file(path):
    with open(path, 'r') as fs:
        fsS = fs.read()
        print(fsS)
        return fsS


def init_shader():
    global program, unif_matr, attrib_vertex, unif_color, unif_color_back, unif_cntLine

    f = load_file(vsPath)
    vsSource = f.encode()

    vShader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vShader, [vsSource])
    glCompileShader(vShader)

    if not mode:
        f = load_file(fsPath1)
    elif mode == 1:
        f = load_file(fsPath2)
    else:
        f = load_file(fsPath3)

    fsSource = f.encode()

    fShader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fShader, [fsSource])
    glCompileShader(fShader)

    program = glCreateProgram()
    glAttachShader(program, vShader)
    glAttachShader(program, fShader)
    glLinkProgram(program)

    link_ok = glGetProgramiv(program, GL_LINK_STATUS)
    if not link_ok:
        print('error attach shaders')
        return

    attr_name = 'coord'
    attrib_vertex = glGetAttribLocation(program, attr_name)
    if attrib_vertex == -1:
        print('could not bind attrib', attr_name)
        return

    unif_color = 'color_front'
    unif_color = glGetUniformLocation(program, unif_color)
    if unif_color == -1:
        print('could not bind uniform', unif_color)
        return

    if mode:
        cb = 'color_back'
        unif_color_back = glGetUniformLocation(program, cb)
        if unif_color_back == -1:
            print('could not bind uniform', cb)
            return

        cnt = 'cnt'
        unif_cntLine = glGetUniformLocation(program, cnt)
        if unif_cntLine == -1:
            print('could not bind uniform', cnt)
            return

    check_openGL_error()


def free_shader():
    glUseProgram(0)
    glDeleteProgram(program)


def resize_window(width, height):
    glViewport(0, 0, width, height)


def render():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glUseProgram(program)

    cf = [frag_color[0] / 255.0, frag_color[1] / 255.0, frag_color[2] / 255.0, 1.0]
    glUniform4fv(unif_color, 1, cf)

    if mode:
        cb = [bfrag_color[0] / 255.0, bfrag_color[1] / 255.0, bfrag_color[2] / 255.0, 1.0]
        glUniform4fv(unif_color_back, 1, cb)
        glUniform1i(unif_cntLine, cntLine)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-0.5, 0.5)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.5, 0.5)
    glEnd()

    glFlush()
    glUseProgram(0)
    check_openGL_error()
    glutSwapBuffers()


def main():
    global program
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DEPTH | GLUT_RGBA | GLUT_ALPHA | GLUT_DOUBLE)
    glutInitWindowSize(w, h)
    glutCreateWindow('Shaders')
    glClearColor(0, 0, 0, 0)

    glew_status = glewInit()
    init_shader()

    glutReshapeFunc(resize_window)
    glutDisplayFunc(render)
    glutMainLoop()

    free_shader()


if __name__ == '__main__':
    main()
