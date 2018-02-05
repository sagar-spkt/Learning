from OpenGL.GL import *
from .template import Draw


class Circle(Draw):
    def __init__(self, x_center, y_center, radius):
        self.x_center, self.y_center, self.radius = x_center, y_center, radius

    def draw_func(self):
        def set_points(x_center, y_center, x_org, y_org):
            glVertex2f(x_center + x_org, y_center + y_org)
            glVertex2f(x_center + y_org, y_center + x_org)
            glVertex2f(x_center - y_org, y_center + x_org)
            glVertex2f(x_center - x_org, y_center + y_org)
            glVertex2f(x_center - x_org, y_center - y_org)
            glVertex2f(x_center - y_org, y_center - x_org)
            glVertex2f(x_center + y_org, y_center - x_org)
            glVertex2f(x_center + x_org, y_center - y_org)

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1)
        glBegin(GL_POINTS)
        x, y, p = 0, self.radius, 1 - self.radius
        while x <= y:
            set_points(self.x_center, self.y_center, x, y)
            x += 1
            if p < 0:
                p += 2 * x + 1
            else:
                y -= 1
                p += 2 * (x - y) + 1
        glEnd()
        glFlush()


class Ellipse(Draw):
    def __init__(self, rad_x, rad_y, x_center, y_center):
        self.rad_x, self.rad_y, self.x_center, self.y_center = rad_x, rad_y, x_center, y_center

    def draw_func(self):
        def set_points(x_center, y_center, x_org, y_org):
            glVertex2f(x_center + x_org, y_center + y_org)
            glVertex2f(x_center - x_org, y_center + y_org)
            glVertex2f(x_center - x_org, y_center - y_org)
            glVertex2f(x_center + x_org, y_center - y_org)

        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1)
        glBegin(GL_POINTS)
        x, y = 0, self.rad_y
        rad_x_sq, rad_y_sq = self.rad_x**2, self.rad_y**2
        two_rad_x_sq, two_rad_y_sq = 2*rad_x_sq, 2*rad_y_sq
        px, py = 0, two_rad_x_sq*y
        p = rad_y_sq - rad_x_sq*self.rad_y + 0.25*rad_x_sq
        while px <= py:
            set_points(self.x_center, self.y_center, x, y)
            x += 1
            px += two_rad_y_sq
            if p < 0:
                p += px + rad_y_sq
            else:
                y -= 1
                py -= two_rad_x_sq
                p += px + rad_y_sq - py
        p = rad_y_sq*(x + 0.5)**2 + rad_x_sq*(y-1)**2 - rad_x_sq*rad_y_sq
        while y >= 0:
            set_points(self.x_center, self.y_center, x, y)
            y -= 1
            py -= two_rad_x_sq
            if p > 0:
                p += rad_x_sq - py
            else:
                x += 1
                px += two_rad_y_sq
                p += rad_x_sq - py + px
        glEnd()
        glFlush()
