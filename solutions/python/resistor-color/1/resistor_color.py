def color_code(color):
    for i,ind in enumerate(colors()):
        if color == ind:
            return i

def colors():
    return ["black", 
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"]