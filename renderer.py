import os

import constants
import subprocess


class Renderer:

    def __init__(self, input_file):
        self.input_file = input_file
        self.path_of_image = 'data/image.png'
        self.command = os.path.normpath(constants.BLENDER_EXE + ' ' + self.input_file)

    def render(self):
        subprocess.check_output(f'{self.command} --background --python render_script.py')
