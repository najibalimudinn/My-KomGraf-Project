import py5
import primitif.utility

width, height = 1700, 900
anim = 0
times = 15
xo, yo = primitif.utility.convert_to_cartesian(0,0, 1700, 900, 25)
baltrans = {
    'vertical': 0,
    'degree': 0,
    'scale': .5,
    'verdir': 1,
    'rotadir': 1,
    'scadir': 1,
    'maxdegree': 0,
    'floating': False,
    'blowing': False
}
balloon_positions = [
    (xo + 200, yo + 200),
    (xo, yo + 150),
    (xo - 200, yo + 200),
    (xo - 400, yo + 150),
    (xo - 600, yo + 200)
]
cloud_positions = [
    (xo + 300, yo - 250, 50),
    (xo - 500, yo - 300, 60),
    (xo - 10, yo - 330, 40),
    (xo + 600, yo - 390, 60),
    (xo - 900, yo - 350, 40)
]
clotrans = {
    'clotrlt': [0 for _ in cloud_positions],
    'clotdir': [1 for _ in cloud_positions],
    'speed': 2,
}
direction = 1
balloons = []
clouds = []
helium = None
blowing_balloon = None