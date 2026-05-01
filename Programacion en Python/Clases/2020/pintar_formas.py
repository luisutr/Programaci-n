from matplotlib import pyplot as plt
import numpy as np


class Circle():
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def plot(self,  ax = None,  show = True):
        alpha = np.linspace(0, 2 * np.pi, 1000)
        self.x = self.center[0] + self.radius * np.cos(alpha)
        self.y = self.center[1] + self.radius * np.sin(alpha)
        if not ax:
            fig = plt.figure()
            ax = fig.add_subplot(111)
        # plot circle
        ax.plot(self.x, self.y, 'r-', label='Circle')
        ax.axis('equal')
        ax.grid(ls='--', lw=0.6)
        ax.legend()
        if not show:
            return ax
        plt.show()


class Triangle():
    def __init__(self, vertices):
        # (3, 2) Array of triangle vertices
        self.v = np.array(vertices)

    def plot(self, ax = None,  show = True):
        if not ax:
            fig = plt.figure()
            ax = fig.add_subplot(111)
        # plot triangle
        ax.plot(np.hstack((self.v[:, 0], self.v[0, 0])),
                np.hstack((self.v[:, 1], self.v[0, 1])),
                'k-', label='Triangle')
        ax.axis('equal')
        ax.grid(ls='--', lw=0.6)
        ax.legend()
        if not show:
            return ax
        plt.show()


    def intrianglecircle(self, radius=None):
        if radius is None:
            self.radius = 0.05 * self.inradius()
        else:
            self.radius = radius
        # random number [0, 1]
        r1, r2 = np.random.random(), np.random.random()
        # x-coordinate
        px = (1-np.sqrt(r1))*self.v[0][0]+(np.sqrt(r1)*(1-r2)) * \
            self.v[1][0]+(np.sqrt(r1)*r2)*self.v[2][0]
        # y-coordinate
        py = (1-np.sqrt(r1))*self.v[0][1]+(np.sqrt(r1)*(1-r2)) * \
              self.v[1][1]+(np.sqrt(r1)*r2)*self.v[2][1]
        # center circle
        self.center = np.array([px, py])
        return Circle(self.center, self.radius)

    def plotintrianglecircle(self):
        c = Circle(self.center, self.radius)
        ax = self.plot(show = False)
        c.plot(ax)


# Graficar círculo + triángulo
vertices = [[2, 1.5], [4.5, 4], [6, 2]]
t = Triangle(vertices)
t.intrianglecircle(1)
t.plotintrianglecircle()

# Graficar triángulo por separado
t.plot()

#Graficar un círculo por separado
c = Circle((0, 0), 0.5)
c.plot()