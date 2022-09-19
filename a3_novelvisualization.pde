String [] uniquewords; 
PFont font;
// Assigning color values
color red = color(198, 60, 60); 
color maroon = color(157, 94, 92);
color cream = color(242,242, 242); 

void setup(){
  size(700,600); 
  background(0);
  uniquewords = loadStrings("uniquewords.txt");
  font = createFont("Trattatello", 36);
  textFont(font);
  //This font looks kind of old timey, and Dracula is a pretty old book
  textAlign(LEFT);
}

void draw(){
  // black background
  background(0);
  
  int word_x = 15; 
  int word_y = 40;
  int word_size = 0;
  
  // looping through the words and adding to screen if they fit
  for(int i = 0; i < uniquewords.length; i++){
    // some padding to height so words don't go over edge, since this font is a bit tall
    while(word_y <= height - 20){
      int index = (int)(random(uniquewords.length));
      word_size = uniquewords[index].length();
      determineColor(word_size);
      // if word goes above length then new line started, other wise filling in until width surpassed
      if(word_x + textWidth(uniquewords[index]) + 5 < width){
        text(uniquewords[index], word_x, word_y);  
      } else {
        word_x = 15;
        word_y += 50;
        if(word_y < height - 20){
          text(uniquewords[index], word_x, word_y);
        }
      }
      word_x += textWidth(uniquewords[index]); 
      word_x += 10;
    }
  }
  noLoop(); 
}

// mouse press triggers another random set of words appearing on screen
void mousePressed(){
  loop();
}

void determineColor(int word_size) {
  // smaller words are the brightest red color in order to not overwhelm the eye, the longer words are in more neutral colors
  // that will make up most of the screen.
  if(word_size <= 5){
    fill(red);
  } else if(word_size > 5 && word_size <= 10 ){
    fill(maroon);
  } else {
    fill(cream);
  }
}
