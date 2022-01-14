import colorgram

rgb_colors = []
colors = colorgram.extract("hirst_spot_painting.jpeg", 30)
for color in colors:
    r = color.rbg.r
    g = color.rbg.g
    b = color.rbg.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
