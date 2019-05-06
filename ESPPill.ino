#include <WiFi.h>
#include "Adafruit_MQTT.h" 
#include "Adafruit_MQTT_Client.h" 
/************************* WiFi Access Point *********************************/ 
#define WLAN_SSID       "HunterLAB2" 
#define WLAN_PASS       "" 
#define MQTT_SERVER      "192.168.1.212" // static ip address
#define MQTT_PORT         1883                    
#define MQTT_USERNAME    "" 
#define MQTT_PASSWORD         "" 
/************ Global State ******************/ 
WiFiClient client; 
Adafruit_MQTT_Client mqtt(&client, MQTT_SERVER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD); 
/****************************** Feeds ***************************************/ 
Adafruit_MQTT_Publish button = Adafruit_MQTT_Publish(&mqtt, MQTT_USERNAME "button"); 
Adafruit_MQTT_Subscribe lock= Adafruit_MQTT_Subscribe(&mqtt, MQTT_USERNAME "Doorp"); 
/*************************** Sketch Code ************************************/

const int GPIO2=2;

void MQTT_connect(); 
void setup() { 
  pinMode(GPIO2,OUTPUT);
int lockstate=1;
 Serial.begin(9600); 
 delay(10); 
 Serial.println(F("RPi-ESP-MQTT")); 
 Serial.println();
 Serial.println(); 
 Serial.print("Connecting to "); 
 Serial.println(WLAN_SSID); 
 WiFi.begin(WLAN_SSID, WLAN_PASS); 
 while (WiFi.status() != WL_CONNECTED) { 
   delay(500); 
   Serial.print("."); 
 } 
 Serial.println(); 
 Serial.println("WiFi connected"); 
 Serial.println("IP address: "); Serial.println(WiFi.localIP()); 
 mqtt.subscribe(&lock); 
} 
uint32_t x=0; 
void loop() { 
   
 MQTT_connect(); 
 Adafruit_MQTT_Subscribe *subscription; 
 while ((subscription = mqtt.readSubscription())) { 
   if (subscription == &lock) { 
     char *message = (char *)lock.lastread; 
    Serial.write(message);
    Serial.write(strcmp(message,"Locked"));
 
    if (strcmp(message,"Locked")){
     
      Serial.write("this is locked ");
       digitalWrite(GPIO2,LOW);
    }
     if (strcmp(message,"Unlocked")){
     
      Serial.write("this is unlocked ");
       digitalWrite(GPIO2,HIGH);
    }
   }
 } 

 } 

void MQTT_connect() { 
 int8_t ret; 
 // Stop if already connected. 
 if (mqtt.connected()) { 
   return; 
 } 
 Serial.print("Connecting to MQTT... "); 
 uint8_t retries = 3; 
 while ((ret = mqtt.connect()) != 0) { // connect will return 0 for connected 
      Serial.println(mqtt.connectErrorString(ret)); 
      Serial.println("Retrying MQTT connection in 5 seconds..."); 
      mqtt.disconnect(); 
      delay(5000);  // wait 5 seconds 
      retries--; 
      if (retries == 0) { 
        // basically die and wait for WDT to reset me 
        while (1); 
      } 
 } 
 Serial.println("MQTT Connected!"); 
} 
