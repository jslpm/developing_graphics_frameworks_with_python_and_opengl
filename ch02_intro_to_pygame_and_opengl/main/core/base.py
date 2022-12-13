import pygame
import sys

from core.input import Input

class Base(object):
    
    def __init__(self, screenSize=[512, 512]):
        # Initialize all pygame modules
        pygame.init()
        # Indicate rendering details
        displayFlags = pygame.DOUBLEBUF | pygame.OPENGL
        # Initialize buffers to perform antialiasing
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
        pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
        # Use a core OpenGL profile for cross-platform compatibility
        pygame.display.gl_set_attribute(
            pygame.GL_CONTEXT_PROFILE_MASK,
            pygame.GL_CONTEXT_PROFILE_CORE
        )
        # Create and display the window
        self.screen = pygame.display.set_mode(screenSize, displayFlags)
        # Set the text that appers in the title bar of the window
        pygame.display.set_caption('Graphics Window')

        # Determine if main loop is active
        self.running = True
        # Manage time-related data and operations
        self.clock = pygame.time.Clock()

        # Manage user input
        self.input = Input()
    
    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):

        ## Startup ##
        self.initialize()

        ## Main loop ##
        while self.running:

            ## Process input ##
            self.input.update()
            if self.input.quit:
                self.running = False

            ## Update ##
            self.update()

            ## Render ##
            # Display image on screen
            pygame.display.flip()

            # pause if necessary to archieve 60 FPS
            self.clock.tick(60)
        
        ## Shutdown ##
        pygame.quit()
        sys.exit()
