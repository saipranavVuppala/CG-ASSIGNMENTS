import random;
r=0;
backr=0;
backG=0;
backB=0;

def setup():
    global backR;
    global backG;
    global backB;
    size(700,500);
    backR=noise(0,100);    #use random or noise
    backG=noise(0,100);
    backB=noise(0,100);
    frameRate(900);
    
    backgroud=(backR,backG,backB);
    rectMode(CENTER);
    
    noStroke();
    smooth();
    
def draw():
    global r;
    fill(backR,backG,backB,50);
    rect(width/2,height/2,width,height);
    
    #fill(mouseX%255,mouseY%255,80);
    fill(random.randint(0,255),random.randint(0,255),random.randint(0,255));
    translate(mouseX,mouseY);
    rotate(r)
    rect(0,0,100,100);
    r+=1;
