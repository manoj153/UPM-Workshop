#include <wiringPi.h>
int main()
{

 wiringPiSetupGpio(); //Broadcom pin system
 pinMode(23, OUTPUT); //initialize pin as output

 while(1)
{
digitalWrite(23, LOW);
delay(500);
digitalWrite(23, HIGH);
delay(500);
}

}
