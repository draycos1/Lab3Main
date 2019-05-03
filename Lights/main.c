#include <msp430.h>
#include "ws2812.h"
#include "stdint.h"


void gradualFill(u_int n, u_char r, u_char g, u_char b);
u_char r;
u_char b;
u_char g;
uint8_t color [3];
u_char changecolor;
u_char recieved;
int i=0;
int newcolor;
int main(void) {
	newcolor=0;
    WDTCTL = WDTPW + WDTHOLD;  // Stop WDT
    if (CALBC1_16MHZ==0xFF)    // If calibration constant erased
    {
        while(1);              // do not load, trap CPU!!
    }

    // configure clock to 16 MHz
    BCSCTL1 = CALBC1_16MHZ;    // DCO = 16 MHz
    DCOCTL = CALDCO_16MHZ;

    // initialize LED strip
    initStrip();  // ***** HAVE YOU SET YOUR NUM_LEDS DEFINE IN WS2812.H? ******


    // set strip color red
    //fillStrip(color[0], color[1], color[2]);

    // show the strip
    showStrip();
    clearStrip();
    // gradually fill for ever and ever
   // fillStrip(0x35,0x35,0x35);
    while (1) {
       // gradualFill(NUM_LEDS, 0x00, 0xFF, 0x00);  // green
       // gradualFill(NUM_LEDS, 0x00, 0x00, 0xFF);  // blue
       // gradualFill(NUM_LEDS, 0xFF, 0x00, 0xFF);  // magenta
       // gradualFill(NUM_LEDS, 0xFF, 0xFF, 0x00);  // yellow
       // gradualFill(NUM_LEDS, 0x00, 0xFF, 0xFF);  // cyan
       // gradualFill(NUM_LEDS, 0xFF, 0x00, 0x00);  // red
    	if(newcolor==1){
    	fillStrip(color[0], color[1], color[2]);
    	newcolor=0;
    	}

     }
}

void gradualFill(u_int n, u_char r, u_char g, u_char b){
    int i;
    for (i = 0; i < n; i++){        // n is number of LEDs
        setLEDColor(i, r, g, b);
        showStrip();
        _delay_cycles(1000000);       // lazy delay
    }
}

#pragma vector=USCIAB0RX_VECTOR
__interrupt void USCI0RX_ISR(void)
{
	if(i>2){
		i=0;
	}
	if(i==2){
		newcolor=1;
	}
	color[i]=UCA0RXBUF;
	i++;

//	if(UCA0RXBUF=='o'){
//		changecolor=1;
//	}
//	if(UCA0RXBUF=='r'){
//			changecolor=2;
//		}
	//recieved=UCA0RXBUF;
	//changecolor=1;
   //for(i=0; i<3; i++){
   //   color[i]=UCA0RXBUF; //store in the values into the color array
   //}
}


