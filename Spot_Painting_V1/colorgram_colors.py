import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('Spot_Painting_V1\img.jpg', 6)

my_list = []

for i in range(len(colors)):
    rgb = colors[i].rgb
    my_list.append((rgb.r, rgb.g, rgb.b))

print(my_list)