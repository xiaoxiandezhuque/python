from colorsys import rgb_to_hsv
from com.pc.Bead import Bead

colors = dict((
    ((189, 28, 41), Bead.red),
    ((226, 164, 54), Bead.yellow),
    ((95, 183, 48), Bead.green),
    ((107, 186, 41), Bead.green),
    ((135, 225, 66), Bead.green),
    ((27, 134, 195), Bead.bule),
    ((114, 32, 170), Bead.purple),
    ((219, 172, 239), Bead.purple),
    ((239, 239, 239), Bead.other),

    ((168, 126, 106), Bead.gray),))

# ((196, 2, 51), "RED"),
# ((255, 165, 0), "ORANGE"),
# ((255, 205, 0), "YELLOW"),
# ((0, 128, 0), "GREEN"),
# ((0, 0, 255), "BLUE"),
# ((127, 0, 255), "VIOLET"),
# ((0, 0, 0), "BLACK"),
# ((255, 255, 255), "WHITE"),))

def to_hsv(color):
    """ converts color tuples to floats and then to hsv """
    return rgb_to_hsv(*[x / 255.0 for x in color])  # rgb_to_hsv wants floats!


def color_dist(c1, c2):
    """ returns the squared euklidian distance between two color vectors in hsv space """
    return sum((a - b) ** 2 for a, b in zip(to_hsv(c1), to_hsv(c2)))


def min_color_diff(color_to_match, colors):
    """ returns the `(distance, color_name)` with the minimal distance to `colors`"""
    return min(  # overal best is the best match to any color:
        (color_dist(color_to_match, test), colors[test])  # (distance to `test` color, color name)
        for test in colors)


def get_color(color):
    return min_color_diff(color, colors)[1]

# color_to_match = (203, 41, 52)
# print(min_color_diff(color_to_match, colors)[1])
