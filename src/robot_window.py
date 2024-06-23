import moderngl
from pyrr import Matrix44, Vector3

import numpy as np

import models
from base_window import BaseWindow

class RobotWindow(BaseWindow):

    def __init__(self, **kwargs):
        super(RobotWindow, self).__init__(**kwargs)

    def load_models(self):
       self.cube = models.load_cube(self.program)

    def init_shaders_variables(self):
        self.unicode_color = self.program["color"]
        self.unicode_mvp = self.program["mvp"]

    def render(self, time: float, frame_time: float):
        self.ctx.clear(0.1, 0.2, 0.3, 0.0)
        self.ctx.enable(moderngl.DEPTH_TEST | moderngl.CULL_FACE)

        self.projection = Matrix44.perspective_projection(45.0, self.aspect_ratio, 0.1, 1000.0)
        self.view = Matrix44.look_at(
            (5.0, 5.0, -15.0),
            (0.0, 2.0, 0.0),
            (0.0, 1.0, 0.0),
        )

        COLOR_HEAD = (1, 1, 1)
        COLOR_BODY = (1, 1, 1)
        COLOR_ARM = (0, 0, 0)
        COLOR_LEG = (0, 0, 0)

        # head
        self.draw(self.cube,
                  position=(0, 5, 0),
                  scale=(1.5, 1.5, 1.5),
                  color=COLOR_HEAD)
         # body
        self.draw(self.cube,
                  position=(0, 2, 0),
                  scale=(2, 4, 2),
                  color=COLOR_BODY)
        # arm left
        self.draw(self.cube,
                  position=(2.5, 4, 0),
                  rotation=(0, 45, 0),
                  scale=(0.75, 2.5, 0.75),
                  color=COLOR_ARM)
        # arm right
        self.draw(self.cube,
                  position=(-2.5, 4, 0),
                  rotation=(0, -45, 0),
                  scale=(0.75, 2.5, 0.75),
                  color=COLOR_ARM)
        # leg left
        self.draw(self.cube,
                  position=(2, -2, 0),
                  rotation=(0, -30, 0),
                  scale=(1, 3, 1),
                  color=COLOR_LEG)
        # leg right
        self.draw(self.cube,
                  position=(-2, -2, 0),
                  rotation=(0, 30, 0),
                  scale=(1, 3, 1),
                  color=COLOR_LEG)

    def draw(self, obj: moderngl.VertexArray, position=(0,0,0), rotation=(0,0,0), scale=(1,1,1), color=(1,0,0)):
        m_translation = Matrix44.from_translation(position)
        m_rotation = Matrix44.from_eulers((np.radians(rotation[0]), np.radians(rotation[1]), np.radians(rotation[2])))
        m_scale = Matrix44.from_scale(scale)
        model = m_translation * m_rotation * m_scale
        self.unicode_mvp.write((self.projection * self.view * model).astype('f4'))
        self.unicode_color.value = color
        obj.render(moderngl.TRIANGLES)