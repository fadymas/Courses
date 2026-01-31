/*************************************************************
 * WEB SERVER TO CONTROL 2 LEDs (ESP32)
 * ====================================
 * 
 * This program creates a simple web server on ESP32 to control
 * two LEDs connected to GPIO 23 and 22 via a web page.
 * 
 *  Yara Ahmed
 * Date: October 2025
 *************************************************************/

#include "WiFi.h"

#define LED0 23   // LED 1 connected to GPIO 23
#define LED1 22   // LED 2 connected to GPIO 22

// Local Wi-Fi credentials
const char* ssid = "YaraPC";
const char* password = "esp32iot";

// Start the web server on port 80 (HTTP default)
WiFiServer server(80);

// HTML page content
String html = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
<title>ESP32 LED Control</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  body { font-family: Arial; text-align: center; background-color: #f4f4f4; }
  h1, h2 { color: #333; }
  button {
    width: 120px; height: 40px; margin: 10px;
    font-size: 16px; border-radius: 10px; border: none; cursor: pointer;
  }
  .on { background-color: #4CAF50; color: white; }
  .off { background-color: #f44336; color: white; }
</style>
</head>
<body>
  <h1>ESP32 DevKitC LED Control</h1>
  <h2>Control 2 LEDs from Web Page</h2>
  <form>
    <button class="on" name="LED0" value="ON" type="submit">LED0 ON</button>
    <button class="off" name="LED0" value="OFF" type="submit">LED0 OFF</button><br><br>
    <button class="on" name="LED1" value="ON" type="submit">LED1 ON</button>
    <button class="off" name="LED1" value="OFF" type="submit">LED1 OFF</button>
  </form>
</body>
</html>
)rawliteral";

// Function to connect to Wi-Fi
void Connect_WiFi() {
  Serial.print("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
}

// Setup function
void setup() {
  Serial.begin(115200);

  // Configure LED pins as outputs
  pinMode(LED0, OUTPUT);
  pinMode(LED1, OUTPUT);
  digitalWrite(LED0, LOW);
  digitalWrite(LED1, LOW);

  // Connect to Wi-Fi and start server
  Connect_WiFi();
  server.begin();
  Serial.println("Web server started!");
}

// Main loop
void loop() {
  WiFiClient client = server.available(); // Wait for a client to connect
  if (!client) return;

  Serial.println("New client connected.");
  String request = client.readStringUntil('\r');
  client.flush();

  // Check for LED control requests
  if (request.indexOf("LED0=ON") != -1) { digitalWrite(LED0, HIGH); Serial.println("LED0 ON");
  }
  if (request.indexOf("LED0=OFF") != -1) {digitalWrite(LED0, LOW); Serial.println("LED0 OFF");
  }
  if (request.indexOf("LED1=ON") != -1) { digitalWrite(LED1, HIGH);Serial.println("LED1 ON");
  }
  if (request.indexOf("LED1=OFF") != -1) {
    digitalWrite(LED1, LOW);
    Serial.println("LED1 OFF");
  }

  // Send HTML page to client
  client.println("HTTP/1.1 200 OK");
  client.println("Content-type:text/html");
  client.println();
  client.print(html);
  client.println();

  delay(1);
  client.stop();
  Serial.println("Client disconnected.");
}
