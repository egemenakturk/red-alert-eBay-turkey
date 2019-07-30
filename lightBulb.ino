#include <SoftwareSerial.h>
char receivedChar;
boolean newData = false;
void setup() {
  digitalWrite(6,HIGH);
  pinMode(6, OUTPUT); //green
  pinMode(11,INPUT);//switch
  Serial.begin(9600);
}
  int threeFour = 0 ;
  int fiveSix = 0;

void loop() {
  // listen for the data
  if(digitalRead(11)!=switchInput){
    digitalWrite(6,LOW); 
    switchInput=digitalRead(11); 
  }
  if ( Serial.available() > 0 ) {
    // read a numbers from serial port
    int count = Serial.parseInt();
     // print out the received number
     Serial.print("You have input: ");
     Serial.println(String(count));
    
     blinkLED(count);
     //count=0; 
  }
  
}
void blinkLED(int input){
  if(input==1){ // green
    digitalWrite(6,HIGH);
  }  
  
  
}
