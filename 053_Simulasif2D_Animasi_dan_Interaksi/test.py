import py5
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasi
import karya2D.balloon
import karya2D.cloud
import karya2D.heliumtube
import config
import math

color = [255, 0, 0, 255]

def setup():
    py5.size(config.width, config.height)

def draw():
    py5.background(255)

    persegi = primitif.basic.persegi(100, 100, 200)
    # primitif.basic.fill_scanline(persegi, color)
    primitif.basic.draw_bentuk(persegi, color)

py5.run_sketch()