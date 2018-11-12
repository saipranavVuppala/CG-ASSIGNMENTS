def setup():
    global viewport;
    size(800,600,P3D)
    background(255)

def draw():
    translate(mouseX-50,mouseY-50)
    fill(mouseX%255,mouseY%255,30)
    noStroke()
    ellipse(250,100,60,60)
    
def keyPressed():
    if(key=='c'):
        background(255)
