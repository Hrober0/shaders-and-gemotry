from collections import namedtuple
from enum import Enum

import moderngl_window

from base_window import BaseWindow
from robot_window import RobotWindow
from phong_window import PhongWindow
from shapes_window import ShapesWindow

Task = namedtuple('Task', ['window_args', 'window_cls'])

class TaskType(Enum):
    @property
    def window_args(self):
        return self.value.window_args

    @property
    def window_cls(self):
        return self.value.window_cls

    DEFAULT = Task(
        [
            "--shaders_dir_path=./resources/shaders/passthrough",
            "--shader_name=passthrough"
        ],
        BaseWindow
    )
    ROBOT = Task(
        [
            "--shaders_dir_path=./resources/shaders/robot",
            "--shader_name=robot"
        ],
        RobotWindow
    )
    PHONG = Task(
        [
            "--shaders_dir_path=./resources/shaders/phong",
            "--shader_name=phong"
        ],
        PhongWindow
    )
    SHAPES = Task(
        [
            "--shaders_dir_path=./resources/shaders/phong",
            "--shader_name=phong"
        ],
        ShapesWindow
    )


if __name__ == '__main__':
    task = TaskType.SHAPES
    moderngl_window.run_window_config(task.window_cls, args=task.window_args)
