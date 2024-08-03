import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np
import os

def generate_random_color():
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def draw_2d_shapes():
    fig, ax = plt.subplots()
    shapes = ['circle', 'square', 'triangle']
    for _ in range(random.randint(1, 5)):
        shape = random.choice(shapes)
        color = generate_random_color()
        if shape == 'circle':
            circle = plt.Circle((random.uniform(0.1, 0.9), random.uniform(0.1, 0.9)), 0.1, color=color)
            ax.add_artist(circle)
        elif shape == 'square':
            square = plt.Rectangle((random.uniform(0.1, 0.8), random.uniform(0.1, 0.8)), 0.2, 0.2, color=color)
            ax.add_artist(square)
        elif shape == 'triangle':
            triangle = plt.Polygon(np.random.rand(3, 2), color=color)
            ax.add_artist(triangle)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.axis('off')
    plt.savefig("2d_shapes.png")
    plt.show()

def draw_3d_shapes():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    shapes = ['cube', 'pyramid', 'sphere']
    for _ in range(random.randint(1, 3)):
        shape = random.choice(shapes)
        color = generate_random_color()
        if shape == 'cube':
            r = [0, 1]
            X, Y = np.meshgrid(r, r)
            ax.plot_surface(X, Y, np.zeros((2, 2)), color=color)
            ax.plot_surface(X, Y, np.ones((2, 2)), color=color)
            ax.plot_surface(X, np.zeros((2, 2)), Y, color=color)
            ax.plot_surface(X, np.ones((2, 2)), Y, color=color)
            ax.plot_surface(np.zeros((2, 2)), X, Y, color=color)
            ax.plot_surface(np.ones((2, 2)), X, Y, color=color)
        elif shape == 'pyramid':
            vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0.5, 0.5, 1]])
            faces = [[vertices[j] for j in [0, 1, 4]], [vertices[j] for j in [1, 2, 4]],
                     [vertices[j] for j in [2, 3, 4]], [vertices[j] for j in [3, 0, 4]],
                     [vertices[j] for j in [0, 1, 2, 3]]]
            ax.add_collection3d(Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='r', alpha=.25))
        elif shape == 'sphere':
            u, v = np.mgrid[0:2*np.pi:20j, 0:np.pi:10j]
            x = np.cos(u)*np.sin(v)
            y = np.sin(u)*np.sin(v)
            z = np.cos(v)
            ax.plot_surface(x, y, z, color=color)
    plt.savefig("3d_shapes.png")
    plt.show()

def main():
    shape_type = random.choice(['2D', '3D'])
    if shape_type == '2D':
        draw_2d_shapes()
    else:
        draw_3d_shapes()

if __name__ == "__main__":
    main()
