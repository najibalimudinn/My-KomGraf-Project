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
        self.parts = [
            primitif.line.line_bresenham(self.xc - self.rx, self.yc - self.ry, self.xc + self.rx, self.yc - self.ry),  # top_side
            primitif.line.line_bresenham(self.xc - self.rx, self.yc + self.ry, self.xc + self.rx, self.yc + self.ry),  # bottom_side
            primitif.line.line_bresenham(self.xc - self.rx - self.r, self.yc - self.ry + self.r, self.xc - self.rx - self.r, self.yc + self.ry - self.r),  # left_side
            primitif.line.line_bresenham(self.xc + self.rx + self.r, self.yc - self.ry + self.r, self.xc + self.rx + self.r, self.yc + self.ry - self.r),  # right_side
            primitif.basic.lingkaran(self.xc - self.rx, self.yc - self.ry + self.r, self.r, 'II'),  # left_top
            primitif.basic.lingkaran(self.xc + self.rx, self.yc - self.ry + self.r, self.r, 'I'),  # right_top
            primitif.basic.lingkaran(self.xc - self.rx, self.yc + self.ry - self.r, self.r, 'III'),  # left_bottom
            primitif.basic.lingkaran(self.xc + self.rx, self.yc + self.ry - self.r, self.r, 'IV'),  # right_bottom
            primitif.basic.trapesium_siku(self.xc, self.yc - self.ry, self.aa, 2*self.aa, -2*self.aa),  # right_handle
            primitif.basic.trapesium_siku(self.xc, self.yc - self.ry, -self.aa, -2*self.aa, -2*self.aa),  # left_handle
            primitif.basic.trapesium_siku(self.xc - 3*self.aa, self.yc - self.ry - self.aa, int(1.5*self.aa), int(1.68*self.aa), int(0.3*self.aa))  # pipe
        ]

    def draw(self):
        for part in self.parts:
            primitif.basic.draw_bentuk(part)