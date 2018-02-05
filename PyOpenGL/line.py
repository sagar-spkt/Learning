from OpenGL.GL import *
from .template import Draw
from


def slope(xa, ya, xb, yb):
    return (yb - ya) / (xb - xa)


class LineDDA(Draw):
    def __init__(self, xa, ya, xb, yb):
        self.xa, self.ya, self.xb, self.yb = (xa, ya, xb, yb)

    def __round(self, val):
        return int(val + 0.5)

    def draw_func(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1)
        glBegin(GL_POINTS)
        dx, dy = self.xb - self.xa, self.yb - self.ya
        steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
        x, y, x_inc, y_inc = self.xa, self.ya, dx / steps, dy / steps
        glVertex2d(self.__round(x), self.__round(y))
        for _ in range(steps):
            x += x_inc
            y += y_inc
            glVertex2d(self.__round(x), self.__round(y))
        glEnd()
        glFlush()


class LineBres(Draw):
    def __init__(self, xa, ya, xb, yb):
        self.xa, self.ya, self.xb, self.yb = (xa, ya, xb, yb)

    def draw_func(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1)
        glBegin(GL_POINTS)
        dx, dy = abs(self.xb - self.xa), abs(self.yb - self.ya)
        p = 2 * dy - dx
        two_dy, two_dy_dx = 2 * dy, 2 * (dy - dx)

        # Determine left end point
        x, y, x_end = (self.xb, self.yb, self.xa) if self.xa > self.xb else (self.xa, self.ya, self.xb)
        while x <= x_end:
            glVertex2f(x, y)
            x += 1
            if p < 0:
                p += two_dy
            else:
                y += 1
                p += two_dy_dx
        glEnd()
        glFlush()
