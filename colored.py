def color(text, code):
    return f"\x1b[{code}m" + text + "\x1b[37m"
def red(text):
    return color(text, 31)
def green(text):
    return color(text, 32)
def yellow(text):
    return color(text, 33)
def blue(text):
    return color(text, 34)
def magenta(text):
    return color(text, 35)
def cyan(text):
    return color(text, 36)
def white(text):
    return color(text, 37)
def gray(text):
    return color(text, 90)
def bright_red(text):
    return color(text, 91)
def bright_green(text):
    return color(text, 92)
def bright_yellow(text):
    return color(text, 93)
def bright_blue(text):
    return color(text, 94)
def bright_magenta(text):
    return color(text, 95)
def bright_cyan(text):
    return color(text, 96)