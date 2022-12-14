from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *

# Render single point
class Test(Base):

    def initialize(self):
        print("Initialize program...")

        ### Initialize program ###

        # Vertex shader code
        vsCode = """
        void main() {
            gl_Position = vec4(0.0, 0.0, 0.0, 1.0);
        }
        """

        # Fragment shader code
        fsCode = """
        void main() {
            gl_FragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        # Send code to GPU and compile; store program reference
        self.programRef = OpenGLUtils.initializeProgram(
            vsCode, fsCode
        )

        ### Set up vertex array object
        vaoRef = glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        ### Render settings (optional) ###
        
        # Set point width and height
        glPointSize(10)

    def update(self):
        # Select program to use when rendering
        glUseProgram(self.programRef)

        # Renders geometric objects using selected program
        glDrawArrays(GL_POINTS, 0, 1)


# Instantiate this class and run the program
Test().run()