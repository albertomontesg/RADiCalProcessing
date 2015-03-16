#include <FreqCounter.h>

unsigned long frq;
int time = 200; // miliseconds

void setup()
{
  Serial.begin(9600);  // start serial for output 
}
void loop() { 
 // wait if any serial is going on
  FreqCounter::f_comp=10;   // Cal Value / Calibrate with professional Freq Counter
  FreqCounter::start(time);  // 500 ms Gate Time
  while (FreqCounter::f_ready == 0) 
  frq = FreqCounter::f_freq;
  frq = frq*1000/time;
  Serial.println(frq);
  delay(20);
}

