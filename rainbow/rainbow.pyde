def setup():
    size(800,800);
    background(255);
    noFill();
    
def draw():
    strokeWeight(random(3,10));
    stroke(random(255),random(255),random(255));
    rainbow_size=random(600,750);
    ellipse(800,800,rainbow_size,rainbow_size);
