String[] lines;
// Setups up template.
void setup(){
  surface.setResizable(false);
  lines = loadStrings("wordfrequency.txt");
  int sizeVal = 500;
  surface.setSize(sizeVal, sizeVal);
  stroke(10);
}

void draw(){
  line(width / 2, 0, width / 2, height); // vertical line
  line(0, 0, width, 0); // Top horizontal line
  for (int i = 0; i < lines.length; i++){ // Let's draw our bricks
    String[] line = lines[i].split(":");
    drawBrick(line, i);
  }
  noLoop();
}

void drawBrick(String[] line, int i){
  int brickSize = 10;
  float scaledX = width * (Float.parseFloat(line[1]) - 0) / (width - 0); // Provides normalized X between 0 and 500
  float scaledY = height * (Float.parseFloat(line[0]) - 0) / (height - 0); // Provides normalized Y between 0 and 500
  rect(width / 2 - scaledX, height - scaledY - brickSize * (i + 1), 2 * scaledX, brickSize);
}
