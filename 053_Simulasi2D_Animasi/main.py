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

def setup():
    py5.size(config.width, config.height)

def draw():
    py5.background(255)

    balloons = [karya2D.balloon.Balloon(x, y, 50) for x, y in config.balloon_positions]
    clouds = [karya2D.cloud.Cloud(x, y, r) for x, y, r in config.cloud_positions]
    helium = karya2D.heliumtube.HeliumTube(config.xo + 600, config.yo + 300)
    blowing_balloon = karya2D.balloon.Balloon(config.xo + 490, config.yo + 183, 50)

    for idx, balloon in enumerate(balloons):
        balloon.translate(0, (-1)**idx * config.baltrans['vertical'])
        balloon.rotate(config.baltrans['degree'])
        balloon.update()
        balloon.draw()
    
    for idx, cloud in enumerate(clouds):
        if cloud.xc + config.clotrans[idx] > 1.08*py5.width:
            config.clotrans[idx] -= 1.15*py5.width
        cloud.translate(config.clotrans[idx], 0)
        cloud.update()
        cloud.draw()
    
    helium.draw()
    blowing_balloon.scale(config.baltrans['scale'], config.baltrans['scale'])
    blowing_balloon.rotate_rubber(270)
    blowing_balloon.update()
    primitif.basic.draw_bentuk(blowing_balloon.parts[0], [255, 0, 0, 255])

    config.baltrans['vertical'] += config.baltrans['verdir']
    config.baltrans['degree'] += .1*config.baltrans['rotadir']
    config.baltrans['scale'] += .02*config.baltrans['scadir']
    for idx in range(len(config.clotrans)):
        config.clotrans[idx] += 2
    if config.baltrans['vertical'] >= 50 or config.baltrans['vertical'] <= 0:
        config.baltrans['verdir'] *= -1
    if config.baltrans['degree'] >= 15 or config.baltrans['degree'] <= 0:
        config.baltrans['rotadir'] *= -1
    if config.baltrans['scale'] >= 1 or config.baltrans['scale'] <= .5:
        config.baltrans['scadir'] *= -1

py5.run_sketch()