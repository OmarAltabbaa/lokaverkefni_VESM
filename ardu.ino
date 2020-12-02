


#include <Wire.h>
#include <LiquidCrystal.h>
#include "Adafruit_MCP9808.h"


//setup for the LCD keypad shield
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
Adafruit_MCP9808 tempsensor = Adafruit_MCP9808();


void setup()
{
  //init serial for some debug
  Serial.begin(9600);
  //init MCP9808
  if (!tempsensor.begin())
  {
  Serial.println("Couldn't find MCP9808!");
  while (1);
  }
  //init LCD
  lcd.begin(16,2);
  //line 1 - temperature
  lcd.setCursor(0,0);
  lcd.print("Temp = ");
  
}

void loop()
{
 
  //read temperature in
  float c = tempsensor.readTempC();
  //convert to fahrenheit - not used in this example
  float f = c * 9.0 / 5.0 + 32;
  //display temperature and altitude on lcd
  Serial.println(c); //debug
  lcd.setCursor(0,0);
  lcd.print("Temp = ");
  lcd.print(c);

  delay(1000);
}
