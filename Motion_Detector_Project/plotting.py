#Executes motion_detector, which runs until quitted
#Then imports the finished df here
from bokeh.plotting import figure, show, output_file
from motion_detector import df

from bokeh.plotting import figure

p = figure(x_axis_type='datetime', height= 100, width=500, title = "Motion Graph", sizing_mode= "scale_both")

q=p.quad(left = df["Start"],right = df["End"], bottom = 0,top = 1, color = "green")
output_file("Graph.html")
show(p)