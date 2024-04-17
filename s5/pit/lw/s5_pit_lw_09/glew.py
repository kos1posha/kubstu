from __future__ import print_function

import collections

from OpenGL.GL import *
from OpenGL.GL.shaders import *
from OpenGL.GLUT import *
from OpenGL.extensions import *
import glfw


GLEW_INITIALIZED = False
GLEW_ERR = 0
GLEW_OK = 1
GLEW_OGL_INFO = None
GL_VERSIONS = 'GL_VERSION'

window = None


def glewInit():
    global GLEW_OK
    global GLEW_INITIALIZED
    global GLEW_OGL_INFO

    GLEW_OGL_INFO = collections.defaultdict(list)
    for name in (GL_VENDOR, GL_RENDERER, GL_VERSION, GL_SHADING_LANGUAGE_VERSION, GL_EXTENSIONS):
        GLEW_OGL_INFO[name] = glGetString(name).decode().split(' ')

    GLEW_OGL_INFO[GL_EXTENSIONS] = list(GLEW_OGL_INFO[GL_EXTENSIONS])

    ogl_version_history = {
        1: [1, 2, 3, 4, 5],
        2: [0, 1],
        3: [0, 1, 2, 3],
        4: [0, 1, 2, 3, 4, 5]
    }

    GLEW_OGL_INFO[GL_VERSIONS] = list()
    this_major = int(GLEW_OGL_INFO[GL_VERSION][0].split('.')[0])
    this_minor = int(GLEW_OGL_INFO[GL_VERSION][0].split('.')[1])

    for major in range(1, this_major + 1):
        for minor in ogl_version_history[major]:
            if major == this_major and minor <= this_minor:
                GLEW_OGL_INFO[GL_VERSIONS].append('GL_VERSION_%d_%d' % (major, minor))
            elif major != this_major:
                GLEW_OGL_INFO[GL_VERSIONS].append('GL_VERSION_%d_%d' % (major, minor))

    GLEW_INITIALIZED = True

    return GLEW_OK


def opengl_init():
    global window
    # Initialize the library
    if not glfw.init():
        print('Failed to initialize GLFW\n', file=sys.stderr)
        return False

    window = glfw.create_window(1024, 768, 'Tutorial 02', None, None)
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    if not window:
        print('Failed to open GLFW window. If you have an Intel GPU, they are not 3.3 compatible. Try the 2.1 version of the tutorials.\n', file=sys.stderr)
        glfw.terminate()
        return False

    glfw.make_context_current(window)
    glewExperimental = True

    if glewInit() != GLEW_OK:
        print('Failed to initialize GLEW\n', file=sys.stderr)
        return False
    return True
