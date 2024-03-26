import primitif.transformasi
import primitif.basic
import primitif.utility
import primitif.line

class Cloud:
    def __init__(self, xc, yc, r):
        self.xc = xc
        self.yc = yc
        self.r = r
    
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