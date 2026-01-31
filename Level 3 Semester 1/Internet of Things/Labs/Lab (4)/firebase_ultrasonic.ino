#include <WiFi.h>                  // Library to connect ESP32 to Wi-Fi
#include <Firebase_ESP_Client.h>   // Library for Firebase functions
#include "addons/TokenHelper.h"    // Helper for Firebase authentication
#include "addons/RTDBHelper.h"     // Helper for Firebase Realtime Database

// ===========================
// 👇 STUDENTS MUST CHANGE THESE VALUES 
// ===========================

// Wi-Fi credentials
#define WIFI_SSID "rahmabadar"        //  Replace with your own Wi-Fi network name
#define WIFI_PASSWORD "rahma@011"     //  Replace with your own Wi-Fi password

// Firebase credentials
#define API_KEY "AIzaSyALtMaCgDbtjnjoag8zCuQ7PzgEg5014SY"     //  Replace with your Firebase project's API Key
#define DATABASE_URL "https://ultrasonic-esp32-8490b-default-rtdb.firebaseio.com/"  //  Replace with your Firebase Realtime Database URL
#define USER_EMAIL "rahma@gmail.com"     //  Replace with the email used in Firebase Authentication
#define USER_PASSWORD "rahmaa123456"     //  Replace with the password for the above email

// ===========================
//  END OF STUDENT-EDITABLE SECTION 
// ===========================


// Pin Definitions
#define TRIG_PIN 32    
#define ECHO_PIN 33    
#define LED_PIN 13     

// Firebase Objects
FirebaseData fbdo;       
FirebaseAuth auth;       
FirebaseConfig config;   

// Variables for distance measurement
long duration;           
float distance;          

void setup() {
  Serial.begin(115200); // Start serial communication for debugging

  // Initialize pins
  pinMode(TRIG_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);

  // Connect to Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }
  Serial.println("\nConnected to Wi-Fi!");

  // Configure Firebase
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;

  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;

  // Initialize Firebase connection
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true); // Auto-reconnect Wi-Fi if disconnected

  Serial.println("Firebase initialized!");
}

void loop() {
  // Measure distance using ultrasonic sensor
  digitalWrite(TRIG_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN, LOW);

  duration = pulseIn(ECHO_PIN, HIGH);       
  distance = duration * 0.034 / 2;          // Convert time to distance in cm

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println("Cm");

  // Send distance to Firebase
  if (Firebase.RTDB.setFloat(&fbdo, "/distance", distance)) {
    Serial.println("Distance updated in Firebase");
  } else {
    Serial.print("Failed to send distance: ");
    Serial.println(fbdo.errorReason());
  }

  // Control LED based on distance
  if (distance < 10) {
    digitalWrite(LED_PIN, HIGH);             // Turn LED ON if object is closer than 10 cm
    Firebase.RTDB.setString(&fbdo, "/led", "ON");
  } else {
    digitalWrite(LED_PIN, LOW);              // Turn LED OFF otherwise
    Firebase.RTDB.setString(&fbdo, "/led", "OFF");
  }

  delay(2000); // Wait 2 seconds before next measurement
}
