import primitif.transformasi
import primitif.basic
import primitif.utility
import primitif.line

class HeliumTube:
    def __init__(self, xc, yc):
        self.rx = 25
        self.ry = 100
        self.xc = xc
        self.yc = yc
        self.r = 55
        self.aa = 20
    
    def top_side(self):
        return primitif.line.line_bresenham(self.xc - self.rx, self.yc - self.ry, self.xc + self.rx, self.yc - self.ry)
        
    def bottom_side(self):
        return primitif.line.line_bresenham(self.xc - self.rx, self.yc + self.ry, self.xc + self.rx, self.yc + self.ry)
        
    def left_side(self):
        return primitif.line.line_bresenham(self.xc - self.rx - self.r, self.yc - self.ry + self.r, self.xc - self.rx - self.r, self.yc + self.ry - self.r)
        
    def right_side(self):
        return primitif.line.line_bresenham(self.xc + self.rx + self.r, self.yc - self.ry + self.r, self.xc + self.rx + self.r, self.yc + self.ry - self.r)
    
    def left_top(self):
        return primitif.basic.lingkaran(self.xc - self.rx, self.yc - self.ry + self.r, self.r, 'II')
    
    def right_top(self):
        return primitif.basic.lingkaran(self.xc + self.rx, self.yc - self.ry + self.r, self.r, 'I')
    
    def left_bottom(self):
        return primitif.basic.lingkaran(self.xc - self.rx, self.yc + self.ry - self.r, self.r, 'III')
    
    def right_bottom(self):
        return primitif.basic.lingkaran(self.xc + self.rx, self.yc + self.ry - self.r, self.r, 'IV')
    
    def right_handle(self):
        return primitif.basic.trapesium_siku(self.xc, self.yc - self.ry, self.aa, 2*self.aa, -2*self.aa)
    
    def left_handle(self):
        return primitif.basic.trapesium_siku(self.xc, self.yc - self.ry, -self.aa, -2*self.aa, -2*self.aa)
    
    def pipe(self):
        return primitif.basic.trapesium_siku(self.xc - 3*self.aa, self.yc - self.ry - self.aa, int(1.5*self.aa), int(1.68*self.aa), int(0.3*self.aa))

    def draw(self):
        primitif.basic.draw_bentuk(self.top_side())
        primitif.basic.draw_bentuk(self.bottom_side())
        primitif.basic.draw_bentuk(self.left_side())
        primitif.basic.draw_bentuk(self.right_side())
        primitif.basic.draw_bentuk(self.left_top())
        primitif.basic.draw_bentuk(self.right_top())
        primitif.basic.draw_bentuk(self.left_bottom())
        primitif.basic.draw_bentuk(self.right_bottom())
        primitif.basic.draw_bentuk(self.right_handle())
        primitif.basic.draw_bentuk(self.left_handle())
        primitif.basic.draw_bentuk(self.pipe())