import math
import numpy
import numpy as np
from moderngl_window.opengl.vao import VAO

def load_quad_2D(program):
    size = 1.0

    positions = []

    positions.append([-size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0])
    positions.append([size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0])
    positions.append([size / 2.0, size / 2.0])

    positions = numpy.array(positions, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "2f", ["in_position"])

    return vao.instance(program)


def load_cube(program):
    size = 1.0

    positions = []
    # Front face
    positions.append([size / 2.0, size / 2.0, size / 2.0])
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    positions.append([size / 2.0, size / 2.0, size / 2.0])
    # Back face
    positions.append([size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0, -size / 2.0])
    positions.append([size / 2.0, size / 2.0, -size / 2.0])
    positions.append([size / 2.0, -size / 2.0, -size / 2.0])
    # Top face
    positions.append([size / 2.0, size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    positions.append([size / 2.0, size / 2.0, size / 2.0])
    positions.append([size / 2.0, size / 2.0, -size / 2.0])
    # Bottom face
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    # Left face
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    positions.append([-size / 2.0, size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([-size / 2.0, -size / 2.0, size / 2.0])
    positions.append([-size / 2.0, size / 2.0, size / 2.0])
    # Right face
    positions.append([size / 2.0, size / 2.0, -size / 2.0])
    positions.append([size / 2.0, size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0, size / 2.0])
    positions.append([size / 2.0, -size / 2.0, -size / 2.0])
    positions.append([size / 2.0, size / 2.0, -size / 2.0])

    normals = generate_normals(positions)

    positions = numpy.array(positions, dtype=numpy.float32).flatten()
    normals = numpy.array(normals, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "3f", ["in_position"])
    vao.buffer(normals, "3f", ["in_normal"])
    return vao.instance(program)

def load_cylinder(program, radius=0.5, height=1.0, segments=36):
    positions = []

    # top circle
    yBottom = -height / 2.0
    yTop = yBottom + height
    for i in range(segments):

        theta = 2.0 * np.pi * i / segments
        x0 = radius * np.cos(theta)
        y0 = radius * np.sin(theta)
        theta = 2.0 * np.pi * (i + 1) / segments
        x1 = radius * np.cos(theta)
        y1 = radius * np.sin(theta)

        # botom circle
        positions.append([x0, yBottom, y0])
        positions.append([0, yBottom, 0])
        positions.append([x1, yBottom, y1])

        # top circle
        positions.append([x0, yTop, y0])
        positions.append([x1, yTop, y1])
        positions.append([0, yTop, 0])

        # side
        positions.append([x0, yBottom, y0])
        positions.append([x1, yBottom, y1])
        positions.append([x1, yTop, y1])
        positions.append([x1, yTop, y1])
        positions.append([x0, yTop, y0])
        positions.append([x0, yBottom, y0])
    

    normals = generate_normals(positions)
    
    positions = numpy.array(positions, dtype=numpy.float32).flatten()
    normals = numpy.array(normals, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "3f", ["in_position"])
    vao.buffer(normals, "3f", ["in_normal"])
    return vao.instance(program)


def load_sphere(program, radius=0.5, stacks=18, slices=36):
    t_positions = []
    t_normals = []
    for i in range(stacks + 1):
        phi = np.pi * i / stacks
        for j in range(slices + 1):
            theta = 2.0 * np.pi * j / slices
            x = radius * np.sin(phi) * np.cos(theta)
            y = radius * np.sin(phi) * np.sin(theta)
            z = radius * np.cos(phi)
            t_positions.append((x, y, z))
            t_normals.append((x / radius, y / radius, z / radius))
    
    positions = []
    normals = []
    for i in range(stacks):
        for j in range(slices):
            first = i * (slices + 1) + j
            second = first + slices + 1

            indicate = (first, second, first + 1)
            positions.append([t_positions[indicate[0]], t_positions[indicate[1]], t_positions[indicate[2]]])
            normals.append([t_normals[indicate[0]], t_normals[indicate[1]], t_normals[indicate[2]]])

            indicate = (second, second + 1, first + 1)
            positions.append([t_positions[indicate[0]], t_positions[indicate[1]], t_positions[indicate[2]]])
            normals.append([t_normals[indicate[0]], t_normals[indicate[1]], t_normals[indicate[2]]])
    
    positions = numpy.array(positions, dtype=numpy.float32).flatten()
    normals = numpy.array(normals, dtype=numpy.float32).flatten()

    vao = VAO()
    vao.buffer(positions, "3f", ["in_position"])
    vao.buffer(normals, "3f", ["in_normal"])
    return vao.instance(program)


def generate_normals(positions):
    N = len(positions)
    normals = []
    for i in range(0, N, 3):
        p0 = numpy.array(positions[i + 0])
        p1 = numpy.array(positions[i + 1])
        p2 = numpy.array(positions[i + 2])
        cross = numpy.cross(p1 - p0, p2 - p0)
        norm = cross / numpy.linalg.norm(cross)
        for v in range(3):
            normals.append(list(norm))
    return normals