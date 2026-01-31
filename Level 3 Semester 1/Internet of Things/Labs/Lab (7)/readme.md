[ESP32 Startup]
       │
       ▼
[Initialize LCD] ──> LCD (Parallel GPIO)
       │
       ▼
[Scan WiFi Networks] ── IEEE 802.11 ──> Nearby Routers (SSID, BSSID, RSSI)
       │
       ▼
[Display Networks] ──> LCD (Parallel GPIO)
       │
       ▼
[Connect WiFi] ── IEEE 802.11 Authentication / Association
       │
       ▼
[DHCP IP Assignment] ── TCP/IP ──> Router (IP, Subnet, Gateway, DNS)
       │
       ▼
[Get WiFi Info] ── Retrieve {SSID, IP, RSSI, MAC, Gateway}
       │
       ▼
[Display WiFi Info] ──> LCD (Parallel GPIO)
       │
       ▼
[Loop Monitor] ──> Reconnect if lost



this is a description of all the flow of the project 

scan_wifi_networks  function

START
   │
   ▼
Activate WiFi (STA_IF)
   │
   ▼
Display "Scanning WiFi..." on LCD
   │
   ▼
Wait 1 second
   │
   ▼
Scan available networks
   │
   ▼
Return networks list
   │
   ▼
END


connect_wifi(ssid, password, timeout)
START
   │
   ▼
Activate WiFi (STA_IF)
   │
   ▼
Is device already connected?
   │
  Yes ─────► Display "Already Connected!" → Return wlan
   │
  No
   │
   ▼
Display "Connecting..." on LCD
   │
   ▼
Connect to SSID
   │
   ▼
Start timer
   │
   ▼
While not connected
   │
   ├─ Timeout reached? → Display "Connection Failed" → Return None
   └─ Else → continue waiting
   │
Connected!
   │
Display "Connected! Getting IP..."
   │
Return wlan
   │
END






get_wifi_info(wlan)

START
   │
   ▼
Is wlan valid and connected?
   │
  No ─────► Return None
   │
  Yes
   │
   ▼
Initialize RSSI
   │
   ▼
Get SSID, IP, Subnet, Gateway, DNS, MAC
   │
   ▼
Scan networks for RSSI
   │
   ▼
Return info dictionary
   │
END


display_wifi_info(info)

START
   │
   ▼
Is info available?
   │
  No ─────► Display "No WiFi Info Available" → END
   │
  Yes
   │
   ▼
Display SSID & IP on LCD → wait 3 sec
   │
   ▼
Display Signal % & RSSI → wait 3 sec
   │
   ▼
Display Gateway → wait 3 sec
   │
   ▼
Display MAC → wait 3 sec
   │
END




main
START
   │
   ▼
Clear LCD & Display "ESP32 WiFi Lab Starting..."
   │
   ▼
Scan WiFi Networks
   │
   ▼
Display "Found X Networks" on LCD
   │
   ▼
Connect to WiFi (SSID & Password)
   │
   ▼
Connected?
   │
  No ─────► Display "WiFi Connection Failed" → END
   │
  Yes
   │
   ▼
WHILE True
   │
   ▼
Get WiFi Info
   │
   ▼
Info available?
   │
  No ─────► Display "Connection Lost, Reconnecting..." → Reconnect
   │
  Yes
   │
Display WiFi Info
   │
   ▼
Wait 1 sec → Loop





