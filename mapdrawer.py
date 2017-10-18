# -*- coding: utf-8 -*-
"""
@Haru Fujimura

Hylian Map Maker Program
 """

#Program to Draw a map, Breath of the wild Style

# Get an array of height values
# Get an array of Field Values

# Set the elevation line width (200 m in Z between Lines etc)

#Consider thinking about using matplotlib draw 3d or some other premade drawing tool


#Draw Equi-altitude lines
#Draw Special location Figures(Colour Area blue for water, Colour Area Green for forests, white for snow)
# Draw area names, or make it easy to tell it where to put them (Towns, special locations)s
# get a BotW style font for writing

# as a bonus have it render Area name in small hylian font.
pp.contour(x,y,Z_Array)
xx,yy=np.meshgrid(x,y,sparse=True)
