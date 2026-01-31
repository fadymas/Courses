#include <ESP8266WiFi.h>                              // Include the WiFi library
#include <PubSubClient.h>                             // Include the MQTT library

const char* ssid = "iotlab";                          // WiFi SSID
const char* password = "hostiotlab";                  // WiFi Password

const char* broker = "192.168.137.1";                 // MQTT broker address
const int port = 1883;                                // MQTT broker port
const char* topic = "home/led";                       // MQTT topic name

WiFiClient espClient;                                 // Create an object of the WiFiClient class
PubSubClient client(espClient);                       // Create an MQTT client instance

// Callback function to handle incoming MQTT messages
void on_message(char* topic, byte* message, unsigned int length) {
  Serial.print("Message received: ");                 // A message prefix

  for (int i = 0; i < length; i++)                    // Loop through the message bytes
    Serial.print((char)message[i]);                   // Print each character to the Serial Monitor

  Serial.println();                                   // Move to a new line after printing the message
}

void setup() {
  Serial.begin(115200);                               // Initialize serial communication at baudrate of 115200
  
  WiFi.begin(ssid, password);                         // Attempt to connect to the Wi-Fi network
  while (WiFi.status() != WL_CONNECTED) {             // Wait until the NodeMCU is successfully connected
    delay(1000);                                      // Wait 1 second before rechecking Wi-Fi connection status
    Serial.println("Connecting to WiFi...");          // A message indicating an attempt to connect to Wi-Fi
  }
  Serial.println("Connected to WiFi.");               // A message indicating a successful connection

  client.setServer(broker, port);                     // Connect to the MQTT broker
  client.setCallback(on_message);                     // Set callback function for incoming messages

  client.connect("NodeMCU_Subscriber");               // Connect to MQTT broker with the name "NodeMCU_Subscriber"
  Serial.println("Connected to MQTT broker.");        // Successful connection to MQTT broker
  
  client.subscribe(topic);                            // Subscribe to the specified topic
}

void loop() {
  client.loop();                                      // Start MQTT client loop to receive messages
}
