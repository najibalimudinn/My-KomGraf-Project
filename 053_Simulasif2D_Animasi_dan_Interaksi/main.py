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
import numpy as np

def setup():
    py5.size(config.width, config.height)

def draw():
    py5.background(0)
    # py5.fill(0)
    text = 'Press LEFT/RIGHT to rotate the balloon\nPress F to make the balloon floating'
    py5.text(text, 10, 10, 10)

    balloons = [karya2D.balloon.Balloon(x, y, 50) for x, y in config.balloon_positions]
    clouds = [karya2D.cloud.Cloud(x, y, r) for x, y, r in config.cloud_positions]
    helium = karya2D.heliumtube.HeliumTube(config.xo + 600, config.yo + 300)
    blowing_balloon = karya2D.balloon.Balloon(config.xo + 490, config.yo + 183, 50)

    for idx, balloon in enumerate(balloons):
        balloon.translate(0, (-1)**(idx+1) * config.baltrans['vertical'])
        balloon.rotate(config.baltrans['degree'])
        balloon.update()
        balloon.draw()

    for idx, cloud in enumerate(clouds):
        cloud.translate(config.clotrans['clotrlt'][idx], 0)
        cloud.update()
        cloud.draw()

        if cloud.xc > 1.08*py5.width:
            config.clotrans['clotrlt'][idx] -= 1.15*py5.width
        elif cloud.xc < -.08*py5.width:
            config.clotrans['clotrlt'][idx] += 1.15*py5.width

    helium.draw()
    blowing_balloon.scale(config.baltrans['scale'], config.baltrans['scale'])
    blowing_balloon.rotate_rubber(270)
    blowing_balloon.update()
    primitif.basic.draw_bentuk(blowing_balloon.parts[0], [255, 0, 0, 255])

    update_baltrans()
    update_clotrans()
    if config.baltrans['floating']:
        floating_balloons()

def update_baltrans():
    config.baltrans['scale'] += .02*config.baltrans['scadir']
    if config.baltrans['scale'] >= 1 or config.baltrans['scale'] <= .5:
        config.baltrans['scadir'] *= -1

    if config.baltrans['rotadir'] == 1 and config.baltrans['degree'] < config.baltrans['maxdegree']:
        config.baltrans['degree'] += 4 if config.baltrans['maxdegree'] == 30 else 2
    elif config.baltrans['rotadir'] == -1 and config.baltrans['degree'] > config.baltrans['maxdegree']:
        config.baltrans['degree'] -= 4 if config.baltrans['maxdegree'] == -30 else 2

def update_clotrans():
    config.clotrans['speed'] = 3 if config.baltrans['maxdegree'] == 30 or config.baltrans['maxdegree'] == -30 else 2
    for idx in range(len(config.clotrans['clotdir'])):
        if config.baltrans['degree'] != 0:
            config.clotrans['clotrlt'][idx] += config.clotrans['speed']*config.clotrans['clotdir'][idx]

        config.clotrans['clotdir'][idx] = -1 if config.baltrans['degree'] < 0 else 1 if config.baltrans['degree'] > 0 else 0

def floating_balloons():
    config.baltrans['vertical'] += config.baltrans['verdir']
    if config.baltrans['vertical'] >= 50 or config.baltrans['vertical'] <= 0:
        config.baltrans['verdir'] *= -1

def key_pressed():
    if py5.key_code == py5.LEFT:
        config.baltrans['rotadir'] = -1
        if config.baltrans['maxdegree'] > -30:
            config.baltrans['maxdegree'] -= 15
    elif py5.key_code == py5.RIGHT:
        config.baltrans['rotadir'] = 1
        if config.baltrans['maxdegree'] < 30:
            config.baltrans['maxdegree'] += 15
    elif py5.key == 'F' or py5.key == 'f':
        config.baltrans['floating'] = not config.baltrans['floating']

py5.run_sketch()