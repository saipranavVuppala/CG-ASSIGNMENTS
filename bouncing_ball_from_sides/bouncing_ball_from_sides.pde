float circleX = 50;
float circleY = 0;

float xSpeed = 1;
float ySpeed = 1;

void draw() {
  background(200);

  ellipse(circleX, circleY, 20, 20);

  circleX = circleX + xSpeed;
  circleY = circleY + ySpeed;

  if (circleX < 0 || circleX > width) {
    xSpeed = xSpeed * -1;
  }

  if (circleY < 0 || circleY > height) {
    ySpeed = ySpeed * -1;
  }
}
