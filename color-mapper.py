from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import colorsys
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
imgfull = Image.open(askopenfilename())
imgfull.thumbnail((400, 400))

img = np.asarray(imgfull)

plotcolors = []
hues = []
saturations = []
values = []

for row in img:
    for pixel in row:
        red = pixel[0]/255
        green = pixel[1]/255
        blue = pixel[2]/255
        # plotcolors.append([red,green,blue])
        hsv = colorsys.rgb_to_hsv(red, green, blue)
        hues.append(hsv[0]*np.pi*2)
        saturations.append(hsv[1])
        values.append(hsv[2])
        plotcolors.append(colorsys.hsv_to_rgb(hsv[0],hsv[1],0.5))


fig = plt.figure()
ax = fig.add_subplot(projection='polar')
c = ax.scatter(hues, saturations, c=plotcolors, edgecolors='none', alpha=0.2)

plt.show()