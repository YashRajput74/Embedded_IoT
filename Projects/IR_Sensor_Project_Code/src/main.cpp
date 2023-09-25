/*Author Name: Yash Rajput
Arduino script fot esp32s3
Project Name: Tresspass detection*/

#include <Arduino.h>

// pins
static const uint8_t led_pin_first = 1;
static const uint8_t sensor_pin = 42;
static const uint8_t buzzer_pin = 40;
static const uint8_t led_pin_second = 38;

// global variables
static long last_tresspass = 0;
static long last_display = 0;
static int trespass_count = 0;

void setup()
{
  Serial.begin(115200);
  while (!Serial)
    ;
  pinMode(led_pin_first, OUTPUT);
  pinMode(led_pin_second, OUTPUT);
  pinMode(buzzer_pin, OUTPUT);
  pinMode(sensor_pin, INPUT);
}

void loop()
{
  uint8_t sensor_value = digitalRead(sensor_pin);
  long current_time = millis();

  if (sensor_value == 1)
  {
    if (current_time - last_tresspass > 1000)
    {
      last_tresspass = current_time;
      digitalWrite(led_pin_first, HIGH);
      digitalWrite(led_pin_second, LOW);
      trespass_count = 1;
      Serial.println("Alert!! Trespasser detected");
    }
    else
    {
      trespass_count++;
      digitalWrite(led_pin_second, HIGH);
      digitalWrite(buzzer_pin, HIGH);
      Serial.println("Trespasser detected again");
    }
  }
  else
  {
    digitalWrite(buzzer_pin, LOW);
    if (current_time - last_display > 10000)
    {
      Serial.print("Last trespass was: ");
      Serial.print((current_time - last_tresspass) / 1000);
      Serial.println(" seconds ago");
      Serial.print("Trespass count: ");
      Serial.println(trespass_count);
      last_display = current_time;
    }
  }
}