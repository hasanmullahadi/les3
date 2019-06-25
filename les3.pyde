# see :
#  https://processing.org/reference/ellipseMode_.html
g_x =400
g_y =400
g_vx = 5
g_vy = 5
g_dia = 50



def setup():
    size(800,600)
    
    
def draw():
    global g_x,g_y,g_vx,g_vy,g_dia
    ellipseMode(CORNER)
    g_x +=g_vx
    g_y +=g_vy    

    background(0)
    if g_x+g_dia>=width or g_x<=0:
        g_vx *= -1
    if g_y+g_dia >= height or g_y<=0:
        g_vy *= -1
    

    ellipse(g_x,g_y,g_dia,g_dia)
