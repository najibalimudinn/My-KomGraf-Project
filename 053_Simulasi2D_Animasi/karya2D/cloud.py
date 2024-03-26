import primitif.transformasi
import primitif.basic
import primitif.utility
import primitif.line
import numpy as np

class Cloud:
    def __init__(self, xc, yc, r):
        self.xc = xc
        self.yc = yc
        self.r = r
        self.parts = [
            self.center_circle(),
            self.left_circle(),
            self.right_circle(),
            self.rightest_circle()
        ]
        self.tms = [np.identity(3) for _ in self.parts]
    
    def center_circle(self):
        return primitif.basic.lingkaran(self.xc, self.yc, self.r)
    
    def left_circle(self):
        return primitif.basic.lingkaran(self.xc - self.r, self.yc, int(self.r*0.6))
    
    def right_circle(self):
        return primitif.basic.lingkaran(self.xc + self.r, self.yc, int(self.r*0.8))
    
    def rightest_circle(self):
        return primitif.basic.lingkaran(self.xc + int(self.r*1.8), self.yc, int(self.r*0.5))
    
    def draw(self):
        primitif.basic.draw_bentuk(self.left_circle())
        primitif.basic.draw_bentuk(self.rightest_circle())
        primitif.basic.draw_bentuk(self.right_circle())
        primitif.basic.draw_bentuk(self.center_circle())
    
    def translate(self, tx, ty):
        self.xc += tx
        self.yc += ty
        for i in range(len(self.parts)):
            self.tms[i] = primitif.transformasi.translate2D(tx, ty, self.tms[i])
    
    def update(self):
        for i in range(len(self.parts)):
            self.parts[i] = primitif.transformasi.transformPoints2D(self.parts[i], self.tms[i])