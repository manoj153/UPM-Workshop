#include <wiringPi.h>

int main()
{
 wiringPiSetupGpio(); //Broadcom pin system
 pinMode(23, OUTPUT); //initialize pin as output
 pinMode(24, INPUT); //initialize pin as output


 while(1)
{
	if (digitalRead(24)) // Button not presses gives 1
        {
                   digitalWrite(23, LOW);     // Regular LED off
        }
	else
   	{
		digitalWrite(23, HIGH);
		delay(25);
 	}


}

}




