from random import random

from OpenGL.GL import *
from OpenGL.GLUT import *
from PySide6.QtCore import Qt
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtWidgets import QWidget

from ui import Ui_Form


class MyOpenGLWidget(QOpenGLWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vertex = None
        self.fragment = None
        self.program = None
        self.point_data = [[0, 0.5, 0], [-0.5, -0.5, 0], [0.5, -0.5, 0]]
        self.point_color = [[1, 1, 0], [0, 1, 1], [1, 0, 1]]
        self.rotate = {'x': 0, 'y': 0, 'z': 0}

    def initializeGL(self):
        glutInit()
        glClearColor(0.2, 0.2, 0.2, 1)
        self.vertex = self.create_shader(GL_VERTEX_SHADER, self.read_file('vertex_shader1'))
        self.fragment = self.create_shader(GL_FRAGMENT_SHADER, self.read_file('vertex_shader2'))
        self.program = glCreateProgram()
        glAttachShader(self.program, self.vertex)
        glAttachShader(self.program, self.fragment)
        glLinkProgram(self.program)
        glUseProgram(self.program)

    @property
    def scale_x(self):
        try: return float(self.parent().scale_x_input.text())
        except: return float(1.0)

    @property
    def scale_y(self):
        try: return float(self.parent().scale_y_input.text())
        except: return float(1.0)

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        glVertexPointer(3, GL_FLOAT, 0, self.point_data)
        glColorPointer(3, GL_FLOAT, 0, self.point_color)
        glPushMatrix()
        glScalef(self.scale_x, self.scale_y, 0)
        glRotatef(self.rotate['x'], 1, 0, 0)
        glRotatef(self.rotate['y'], 0, 1, 0)
        glRotatef(self.rotate['z'], 0, 0, 1)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glPopMatrix()
        glDisableClientState(GL_VERTEX_ARRAY)
        glDisableClientState(GL_COLOR_ARRAY)

    def special(self, key):
        angle = 10
        if key == int(Qt.Key.Key_Up):
            self.rotate['x'] += angle
        if key == int(Qt.Key.Key_Down):
            self.rotate['x'] -= angle
        if key == int(Qt.Key.Key_Left):
            self.rotate['y'] += angle
        if key == int(Qt.Key.Key_Right):
            self.rotate['y'] -= angle
        if key == Qt.Key.Key_End:
            self.point_color = [[random(), random(), random()], [random(), random(), random()], [random(), random(), random()]]

    def create_shader(self, shader_type, source):
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)
        return shader

    def read_file(self, path):
        with open(path) as file:
            text = file.read()
        return text


class MainWindow(Ui_Form, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Shaders!')
        self.setGeometry(50, 50, 300, 300)
        self.opengl_widget = MyOpenGLWidget(self)
        self.layout().addWidget(self.opengl_widget)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.scale_x_input.textChanged.connect(lambda: self.opengl_widget.update())
        self.scale_y_input.textChanged.connect(lambda: self.opengl_widget.update())

    def keyPressEvent(self, event):
        self.opengl_widget.special(event.key())
        self.opengl_widget.update()
