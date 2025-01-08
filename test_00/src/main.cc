#include <wiringPi.h>
#include <stdio.h>

#define ledPin 0 // define the led pin number

int main(void)
{
	printf("Program is starting ... \n");

	wiringPiSetup(); // Initialize wiringPi.
	
	pinMode(ledPin, OUTPUT);
	printf("Using pin%d\n",ledPin);

	printf("\n test_00");
	for(int i = 0; i<10; ++i)
	{
		digitalWrite(ledPin, HIGH);
		printf("led turned on >>>\n");
		delay(1000);

		digitalWrite(ledPin, LOW);
		printf("led turned off <<<\n");
		delay(1000);
	}
	printf("\n");

	return 0;
}