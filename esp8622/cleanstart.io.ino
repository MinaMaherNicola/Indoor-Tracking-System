#include <ArduinoJson.h>

#include <ESP8266HTTPClient.h>

#include <ArduinoWiFiServer.h>
#include <BearSSLHelpers.h>
#include <CertStoreBearSSL.h>
#include <ESP8266WiFi.h>
#include <ESP8266WiFiAP.h>
#include <ESP8266WiFiGeneric.h>
#include <ESP8266WiFiGratuitous.h>
#include <ESP8266WiFiMulti.h>
#include <ESP8266WiFiScan.h>
#include <ESP8266WiFiSTA.h>
#include <ESP8266WiFiType.h>
#include <WiFiClient.h>
#include <WiFiClientSecure.h>
#include <WiFiClientSecureBearSSL.h>
#include <WiFiServer.h>
#include <WiFiServerSecure.h>
#include <WiFiServerSecureBearSSL.h>
#include <WiFiUdp.h>

#include <dummy.h>

ESP8266WiFiMulti WiFiMulti;
WiFiClientSecure client;
const char *host = "https://ips-grad-project.herokuapp.com";

const size_t CAPACITY = JSON_OBJECT_SIZE(9);
StaticJsonDocument<CAPACITY> doc;
JsonObject object = doc.to<JsonObject>();

void setup()
{
  Serial.begin(115200);
  client.setInsecure();
  client.connect(host, 443);
  WiFiMulti.addAP("ssid", "password");
  WiFiMulti.run();

  while (WiFi.status() != WL_CONNECTED)
  {
    //    Serial.println("Awaiting connection...");
    delay(200);
  }
}

void loop()
{

  int n = WiFi.scanNetworks();
  if (n == 0)
  {
    //    Serial.println("no networks found");
  }
  else
  {
    for (int i = 0; i < n; ++i)
    {
      if (WiFi.SSID(i) == "AP-00" || WiFi.SSID(i) == "AP-01" || WiFi.SSID(i) == "AP-02" || WiFi.SSID(i) == "AP-03" || WiFi.SSID(i) == "AP-04" || WiFi.SSID(i) == "AP-05" || WiFi.SSID(i) == "AP-06" || WiFi.SSID(i) == "AP-07")
      {
        if (WiFi.SSID(i) == "AP-00")
        {
          // AP-00
          delay(200);
          object["AP-00"] = WiFi.RSSI(i);

          Serial.println(WiFi.SSID(i) + " IM IN 00");
          // ------------------
        }
        else if (WiFi.SSID(i) == "AP-01")
        {
          // AP-01
          delay(200);
          object["AP-01"] = WiFi.RSSI(i);

          Serial.println(WiFi.SSID(i) + " IM IN 01");
          // ------------------
        }
        else if (WiFi.SSID(i) == "AP-02")
        {
          // AP-02
          delay(200);
          object["AP-02"] = WiFi.RSSI(i);

          Serial.println(WiFi.SSID(i) + " IM IN 02");
          // ------------------
        }
        else if (WiFi.SSID(i) == "AP-03")
        {
          // AP-03
          delay(200);
          object["AP-03"] = WiFi.RSSI(i);

          Serial.println(WiFi.SSID(i) + " IM IN 03");
          // ------------------
        }
        else if (WiFi.SSID(i) == "AP-04")
        {
          // AP-04
          delay(200);
          object["AP-04"] = WiFi.RSSI(i);

          Serial.println(WiFi.SSID(i) + " IM IN 04");
          // ------------------
        }
        else if (WiFi.SSID(i) == "AP-05")
        {
          // AP-05
          delay(200);
          object["AP-05"] = WiFi.RSSI(i);

          Serial.println(WiFi.SSID(i) + " IM IN 05");
          // ------------------
        }
        else if (WiFi.SSID(i) == "AP-06")
        {
          // AP-06
          delay(200);
          object["AP-06"] = WiFi.RSSI(i);

          Serial.println(WiFi.SSID(i) + " IM IN 06");
          // ------------------
        }
        else if (WiFi.SSID(i) == "AP-07")
        {
          // AP-07
          delay(200);
          object["AP-07"] = WiFi.RSSI(i);

          Serial.println(WiFi.SSID(i) + " IM IN 07");
          // ------------------
        }
      }
    }
  }
  //  Serial.println("-----------------------");
  //  Serial.println("THIS IS THE JSON OBJECT");
  //  serializeJson(doc, Serial);
  //  Serial.println("-----------------------");
  WiFi.scanDelete();
  if (WiFi.status() == WL_CONNECTED)
  {
    HTTPClient http;

    //    Serial.println("[HTTP] begin...\n");

    http.begin(client, "https://ips-grad-project.herokuapp.com/watch");
    http.addHeader("Content-Type", "Application/JSON");

    String json;
    serializeJson(doc, json);

    //    Serial.println("[HTTP] POST...\n");
    int httpCode = http.POST(json);

    //    Serial.println(httpCode);
    //    Serial.println(http.getString());

    http.end();
  }
  delay(3000);
}
