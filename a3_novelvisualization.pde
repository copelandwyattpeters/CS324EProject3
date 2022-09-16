String [] uniquewords; 
PFont font; 
color back = color(95, 69, 17);

void setup(){
  size(700,600); 
  background(back);
  uniquewords = loadStrings("uniquewords.txt");
  font = createFont("SavoyeLetPlain", 42); //font size was chosen to make sure it was visibile 
  textFont(font);//font to emulate the font done in the peacock edition of pride and prejudice
  textAlign(LEFT);
}

void draw(){
  background(back);
  //create colors 
  color sm_wd = color(15, 111, 18); 
  color med_wd = color(245, 237, 220);
  color lrg_wd = color(180,136, 118); 
  
  int x = 10; //x index starts 10 pixels from left 
  int y = 35; //y index starts 42 pixels from top
  int len_word = 0; //length of the word 

  for(int i = 0; i < uniquewords.length; i ++){
    while(y < 600){
      int index = (int)(random(uniquewords.length)); //get a random index
      len_word = uniquewords[index].length();
      //color based on length of string 
      if(len_word <= 6){ //words with 6 or less characters will be green
        fill(sm_wd);
      }
      if(len_word > 6 && len_word <= 9 ){//words with 7-9 characters will be whitesh-tan
        fill(med_wd);
      }
      if(len_word > 9){ // words with 10 or more characters will be tannish-brown
        fill(lrg_wd);
      }
      //check if the word will fit, if not it will go to the next line 
      if(x + (int)textWidth(uniquewords[index]) + 5 > 700){
        x = 10; 
        y += 42; 
        //check if it is on the last line 
        if(y < 560){
          text(uniquewords[index], x, y);
        }
        //if it is the last line it will break out of loop
        else{
          break;
        }
      }
      //if it will fit in the line it will write the next word 5 spaces from the last word 
      else{
        text(uniquewords[index], x, y); 
      }
      //update 
      x += (int)textWidth(uniquewords[index] + 5); 
    }
  }
  noLoop(); 
}

void mousePressed(){
  loop();
}
