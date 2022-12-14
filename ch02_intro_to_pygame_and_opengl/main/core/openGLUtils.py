from OpenGL.GL import *

# Static methods to load and compile OpenGL shaders
# and link to create programs
class OpenGLUtils(object):

    @staticmethod
    def initializeShader(shaderCode, shaderType):
        # Specify required OpenGL/GLSL version
        shaderCode = '#version 130\n' + shaderCode

        # Create empty shader object and return reference value
        shaderRef = glCreateShader(shaderType)

        # Store the source code in the shader
        glShaderSource(shaderRef, shaderCode)

        # Compiles source code previously stored in the
        # shader object
        glCompileShader(shaderRef)

        # queries wheter shader compile was successful
        compileSuccess = glGetShaderiv(shaderRef, GL_COMPILE_STATUS)

        if not compileSuccess:
            # Retrieve error message
            errorMessage = glGetShaderInfoLog(shaderRef)

            # Free memory uset to store shader program
            glDeleteShader(shaderRef)

            # Convert byte string to character string
            errorMessage = '\n' + errorMessage.decode('utf-8')

            # Raise exception: halt program and print error message
            raise Exception(errorMessage)

        # Compilation was succesfull; return shder reference value
        return shaderRef

    @staticmethod
    def initializeProgram(vertexShaderCode, fragmentShaderCode):
        vertexShaderRef = OpenGLUtils.initializeShader(
            vertexShaderCode, GL_VERTEX_SHADER
        )
        fragmentShaderRef = OpenGLUtils.initializeShader(
            fragmentShaderCode, GL_FRAGMENT_SHADER
        )

        # Create empty program object and store reference to it
        programRef = glCreateProgram()

        # Attach previously compiled shader program
        glAttachShader(programRef, vertexShaderRef)
        glAttachShader(programRef, fragmentShaderRef)

        # Link vertex shader to fragment shader
        glLinkProgram(programRef)

        # Queries whether program link was successful
        linkSuccess = glGetProgramiv(programRef, GL_LINK_STATUS)

        if not linkSuccess:
            # Retrieve error message
            errorMessage = glGetProgramInfoLog(programRef)

            # Free memory used to store program
            glDeleteProgram(programRef)

            # Convert byte string to character string
            errorMessage = '\n' + errorMessage.decode('utf-8')

            # Raise excepton: halt application and print error message
            raise Exception(errorMessage)

        # Linking was successful; return program reference value
        return programRef

    @staticmethod
    def printSystemInfo():
        print("\tVendor: " + glGetString(GL_VENDOR).decode('utf-8'))
        print("\tRenderer: " + glGetString(GL_RENDER).decode('utf-8'))
        print("\tOpenGL version supported: " + glGetString(GL_VERSION).decode('utf-8'))
        print("\tGLSL version supported: " + glGetString(GL_SHADING_LANGUAGE_VERSION).decode('utf-8'))

