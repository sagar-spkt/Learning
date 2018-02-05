from PyOpenGL.line import LineDDA, LineBres
# from PyOpenGL.curve import Circle, Ellipse


if __name__ == '__main__':
    xa, ya, xb, yb = tuple(map(int, input('Enter 2 end points: ').strip().split()))
    # lineDDA = LineDDA(xa, ya, xb, yb)
    # lineDDA.draw()
    lineBres = LineBres(xa, ya, xb, yb)
    lineBres.draw()
    # x_center, y_center, radius = tuple(map(int, input('Enter center and radius: ').strip().split()))
    # circle = Circle(x_center, y_center, radius)
    # circle.draw()
    # rad_x, rad_y, x_center, y_center = tuple(map(int, input('Enter ellipse param: ').strip().split()))
    # ellipse = Ellipse(rad_x, rad_y, x_center, y_center)
    # ellipse.draw()
