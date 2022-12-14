from core.base import Base
from core.openGLUtils import OpenGLUtils
from core.attribute import Attribute
from OpenGL.GL import *

# Render six points in an hexagon arrangement
class Test(Base):

    def initialize(self):
        print('Initialize program...')

        ### Initialize program ###
        vsCode = """
        in vec3 position;
        void main() {
            gl_Position = vec4(position.x, position.y, position.z, 1.0);
        }
        """

        fsCode = """
        out vec4 fragColor;
        void main() {
            fragColor = vec4(1.0, 1.0, 0.0, 1.0);
        }
        """

        self.programRef = OpenGLUtils.initializeProgram(vsCode, fsCode)

        ### Render settigs (optional) ###
        glLineWidth(4)

        ### Set up vertex array object ###
        # vaoRef = glGenVertexArrays(1)
        # glBindVertexArray(vaoRef)

        ### Set up vertex attribute ###
        positionData = [
            [ 0.8,  0.0, 0.0],
            [ 0.4,  0.6, 0.0],
            [-0.4,  0.6, 0.0],
            [-0.8,  0.0, 0.0],
            [-0.4, -0.6, 0.0],
            [ 0.4, -0.6, 0.0]
        ]

        self.vertexCount = len(positionData)
        positionAttribute = Attribute('vec3', positionData)
        positionAttribute.associateVariable(self.programRef, 'position')
    
    def update(self):
        glUseProgram(self.programRef)
        #glDrawArrays(GL_LINE_LOOP, 0, self.vertexCount)
        #glDrawArrays(GL_LINE_STRIP, 0, self.vertexCount)
        #glDrawArrays(GL_LINES, 0, self.vertexCount)
        #glDrawArrays(GL_TRIANGLES, 0, self.vertexCount)
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

# Instantiate this class and run the program
Test().run()