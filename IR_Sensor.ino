int IRSensor =2; //connect IR sensor OUT PIN to Arduino PIn 2
int LED =13; //connect LED pin to Arduino Pin 13



void setup()
{

   pinMode(IRSensor,INPUT); //IRSensor is INPUT
   pinMode(LED,OUTPUT); // LED is OUTPUT
}

void loop()
{
  int statusSensor = digitalRead(IRSensor);//Read ir Sensor

  if (statusSensor == 1)
   {
     digitalWrite(LED,LOW); //LED LOW
   }

   else
   {
     digitalWrite(LED,HIGH); //LED HIGH
   }
}
//END 
