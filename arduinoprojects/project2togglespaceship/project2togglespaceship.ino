int switchState = 0;
int lightState = 0;

void setup(){
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(2, INPUT);
}

void loop(){
  if (switchState == 1 && digitalRead(2) == 0){  
    lightState = (lightState + 1)%2;
  }
  
  switchState = digitalRead(2);

  if(lightState == LOW){
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
    digitalWrite(5, LOW);
  }
  else {
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
    digitalWrite(5, HIGH);
    delay(80);
    digitalWrite(4, HIGH);
    digitalWrite(5, LOW);
    delay(80);
  }
}
