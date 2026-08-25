def value(colors):
    color_code = ["black",
                 "brown",
                 "red",
                 "orange",
                 "yellow",
                 "green",
                 "blue",
                 "violet",
                 "grey",
                 "white"]
    result = ""
    for color in colors:
        for i, ind in enumerate(color_code):
            if color == ind:
                result = result + str(i)
    return int(result[0:2])
