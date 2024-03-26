import py5
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasi
import karya2D.balloon
import karya2D.cloud
import karya2D.heliumtube
import config

width, height = 1700, 900
xo, yo = primitif.utility.convert_to_cartesian(0,0, width, height, 25)
balloons = [
    karya2D.balloon.Balloon(xo + 200, yo + 200, 50),
    karya2D.balloon.Balloon(xo, yo + 150, 50),
    karya2D.balloon.Balloon(xo - 200, yo + 200, 50),
    karya2D.balloon.Balloon(xo - 400, yo + 150, 50),
    karya2D.balloon.Balloon(xo - 600, yo + 200, 50)
]

clouds = [
    karya2D.cloud.Cloud(xo + 300, yo - 250, 50),
    karya2D.cloud.Cloud(xo - 500, yo - 300, 60),
    karya2D.cloud.Cloud(xo - 10, yo - 330, 40),
    karya2D.cloud.Cloud(xo + 600, yo - 390, 60)
]

def setup():
    py5.size(1700, 900)
    # py5.loop()
    # primitif.basic.draw_kartesian(py5.width, py5.height, 0)

def draw():
    py5.background(255)

    tube = karya2D.heliumtube.HeliumTube(xo + 600, yo + 300)
    
    # for idx, balloon in enumerate(balloons):
    #     if config.anim <= config.times:
    #         if idx % 2 == 0:
    #             balloon.floating('up')
    #         else:
    #             balloon.floating('down')
    #     elif config.anim <= 2*config.times:
    #         if idx % 2 == 0:
    #             balloon.floating('down')
    #         else:
    #             balloon.floating('up')
    
    if config.anim <= config.times:
        for balloon in balloons:
            balloon.floating()
    
    for balloon in balloons:
        balloon.draw()  
    for cloud in clouds:
        cloud.draw()
    tube.draw()
    
    if config.anim > 2*config.times:
        config.anim = 0
    
    config.anim += 1

py5.run_sketch()

