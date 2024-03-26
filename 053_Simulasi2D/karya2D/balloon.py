import primitif.transformasi
import primitif.basic
import primitif.utility
import primitif.line
import numpy as np

class Balloon:
    def __init__(self, xc, yc, r):
        self.xc = xc
        self.yc = yc
        self.rx = r
        self.ry = int(r*1.2)
        self.a = int(r*0.2)
        self.parts = [
            self.ellips(),
            *self.triangle(),
            self.rope()
        ]
        self.tms = [np.identity(3) for _ in self.parts]

    def ellips(self):
        return primitif.basic.ellips(self.xc, self.yc, self.rx, self.ry)

    def triangle(self):
        triangle1 = primitif.basic.segitiga_siku(self.xc, self.yc + self.ry + self.a, self.a, -self.a)
        triangle2 = primitif.basic.segitiga_siku(self.xc, self.yc + self.ry + self.a, -self.a, -self.a)
        return triangle1, triangle2
    
    def rope(self):
        return primitif.line.line_bresenham(self.xc, self.yc + self.ry + self.a, self.xc, self.yc + self.ry + self.a + self.ry*2)
    
    def translate(self, tx, ty):
        self.xc += tx
        self.yc += ty
        for i in range(len(self.parts)):
            self.tms[i] = primitif.transformasi.translate2D(tx, ty, self.tms[i])
    
    def rotate(self, degree):
        for i in range(len(self.parts)):
            self.tms[i] = primitif.transformasi.rotate2D(degree, self.xc, self.yc, self.tms[i])
    
    def scale(self, sx, sy):
        for i in range(len(self.parts)):
            self.tms[i] = primitif.transformasi.scale2D(sx, sy, self.xc, self.yc, self.tms[i])
    
    def update(self):
        for i in range(len(self.parts)):
            self.parts[i] = primitif.transformasi.transformPoints2D(self.parts[i], self.tms[i])

    def draw(self):
        for part in self.parts:
            primitif.basic.draw_bentuk(part)