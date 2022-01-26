#include <Metro.h> 

const int pin13 = 13;     // pin 13 outputs 1hz signal
const int pin12 = 12;     // pin 12 outputs 10hz signal
const int PPS_in = 4;    // pin 4 inputs PPS signal


//changes the frequency's high and low states
boolean state_1hz = true;
boolean state_10hz = true;


Metro delay_1hz = Metro(500); //1hz with 50% duty cycle
Metro delay_10hz = Metro(50); //10hz with 50% duty cycle



void setup(){

  //set inputs and outputs
  pinMode(pin13 , OUTPUT);
  pinMode(pin12 , OUTPUT);
  pinMode(PPS_in, INPUT);
}


void loop(){


  //1hz signal
  if(delay_1hz.check()){
    state_1hz = !state_1hz;
    digitalWrite(pin13, state_1hz);
  }

  //10hz signal
  if(delay_10hz.check()){
    state_10hz = !state_10hz;
    digitalWrite(pin12, state_10hz);
  }
  
}
