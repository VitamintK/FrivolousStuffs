const int switchPin = 2;
const int motorPin = 9;
int switchState = 0;
int motorOn = 0;

void setup(){
  pinMode(motorPin, OUTPUT);
  pinMode(switchPin, INPUT);
}

void loop(){
  if (switchState == 1 && digitalRead(2) == 0){  
    lightState = (lightState + 1)%2;
  }
  
  switchState = digitalRead(2);
  switchState = digitalRead(switchPin);
  if(motorOn == HIGH){
    digitalWrite(motorPin, HIGH);
    delay(50);
  }
  else {
    digitalWrite(motorPin, LOW);
  }
}
