#include <LiquidCrystal.h>

 

// initialize the library with the numbers of the interface pins
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
char* nafn = "hallo world\0";
int stadsetnig=0;


 

void setup() {
  // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  //lcd.print("hello, world!");
  pinMode(9, OUTPUT);
}

 

void loop() {
    // set the cursor to column 0, line 1
    // (note: line 1 is the second row, since counting begins with 0):
    analogWrite(9, 31);
    lcd.setCursor(stadsetnig, 0 );
    lcd.write(nafn[stadsetnig]);
    delay(150);
    stadsetnig++;
  if(stadsetnig> 15){
    stadsetnig=0;
    lcd.clear();  
  }
    
    // print the number of seconds since reset:
   // lcd.print(millis() / 1000);
}
