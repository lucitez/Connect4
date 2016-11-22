float ang, ang2;
float x, y;
float x2,y2,x3,y3,x4,y4,x5,y5,x6,y6;

void setup() {
  background(0);
  size(600, 600);
}

void draw() {
  //background(0);
  //fill(0,2);
  //noStroke();
  //rect(0,0,width,height);
  x5=(sin(ang)*300+width/2);
  y5=(cos(ang)*300+height/2);
  x6=(sin(ang2)*300+width/2);
  y6=(cos(ang2)*300+height/2);
  x=(sin(ang)*200+width/2);
  y=(cos(ang)*200+height/2);
  x2=(sin(ang2)*200+width/2);
  y2=(cos(ang2)*200+height/2);
  x3=(sin(ang)*100+width/2);
  y3=(cos(ang)*100+height/2);
  x4=(sin(ang2)*100+width/2);
  y4=(cos(ang2)*100+height/2);
  stroke(255,10);
  line(x, y, x2,y2);
  line(x3, y3, x4,y4);
  //line(x5,y5,x6,y6);
  
  //line(x, y, random(x),random(y));
  ang+=random(100);
  ang2+=random(-100,100);
}

