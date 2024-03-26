import py5
import primitif.line
import primitif.basic
import primitif.utility
import primitif.transformasi
import karya2D.balloon
import karya2D.cloud
import karya2D.heliumtube

width, height = 1700, 900
xo, yo = primitif.utility.convert_to_cartesian(0,0, width, height, 25)

def setup():
    py5.size(1700, 900)

def draw():
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

    tube = karya2D.heliumtube.HeliumTube(xo + 600, yo + 300)

    blow_balloon = karya2D.balloon.Balloon(xo + 510, yo + 183, 30)
    blow_balloon.rotate(270)
    blow_balloon.update()
    primitif.basic.draw_bentuk(blow_balloon.parts[0])

    for balloon in balloons:
        balloon.draw()
    for cloud in clouds:
        cloud.draw()
    tube.draw()

py5.run_sketch()

