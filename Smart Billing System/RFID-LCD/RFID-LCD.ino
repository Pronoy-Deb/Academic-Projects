// Including Libraries
#include <SPI.h>
#include <MFRC522.h>
#include <LCD_I2C.h>
// Defining Pins
LCD_I2C lcd(0x27, 16, 2);
#define RST_PIN 9
#define SS_PIN 10
// Defining Tags
byte readCard[4];
String MasterTag = "13EB26";
String MasterTag1 = "973DF5E3";
String tagID = "";
MFRC522 mfrc522(SS_PIN, RST_PIN);
int totalPrice = 0, item = 0;  // initial price and item is 0
const unsigned long MESSAGE_INTERVAL = 3000; // message switch interval in milliseconds
unsigned long lastMessageTime = 0; // time of last message switch
bool showMessageScan = true; // flag indicating which message to display
void setup() {
  lcd.begin();
  lcd.backlight();
  SPI.begin(); // SPI bus
  mfrc522.PCD_Init(); // MFRC522
  lcd.clear();
  lcd.setCursor(2, 0);
  lcd.print("Scan Product"); // initial message on display
}

void loop() {
  Serial.begin(9600);
  // switch messages every MESSAGE_INTERVAL milliseconds
  unsigned long currentTime = millis();
  if (currentTime - lastMessageTime >= MESSAGE_INTERVAL) {
    lastMessageTime = currentTime;
    showMessageScan = !showMessageScan;
    // update display with new message
    lcd.clear();
    if (showMessageScan) { // showing the message
      lcd.setCursor(2, 0);
      lcd.print("Scan Product");
    } else {
      lcd.print("Total Item: ");
      lcd.print(item);
      lcd.setCursor(0, 1);
      lcd.print("Total Bill: ");
      lcd.print(totalPrice);
    }
  }
  // checking for new RFID tag
  while (getID()) {
    if (tagID == MasterTag) {
      totalPrice += 50;
      ++item;
      // updating display with new item and total price
      lcd.clear();
      lcd.print("Total Item: ");
      lcd.print(item);
      lcd.setCursor(0, 1);
      lcd.print("Total Bill: ");
      lcd.print(totalPrice);
    }
    else if (tagID == MasterTag1) {
      totalPrice += 100;
      ++item;
      // updating display with new item and total price
      lcd.clear();
      lcd.print("Total Item: ");
      lcd.print(item);
      lcd.setCursor(0, 1);
      lcd.print("Total Bill: ");
      lcd.print(totalPrice);
    }
    else {
      // display final totals and reset counters
      lcd.clear();
      lcd.setCursor(2, 0);
      lcd.print(item);
      if (item <= 1) lcd.print(" Item Sold");
      else lcd.print(" Items Sold");
      lcd.setCursor(3, 1);
      lcd.print("at TK. ");
      lcd.print(totalPrice);
      delay(5000);
      totalPrice = item = 0;
    }
  }
}
boolean getID() {
  if (!mfrc522.PICC_IsNewCardPresent()) { // If a new PICC placed to RFID reader continue
    return false;
  }
  if (!mfrc522.PICC_ReadCardSerial()) { // Since a PICC placed get Serial and continue
    return false;
  }
  tagID = "";
  for (uint8_t i = 0; i < 4; ++i) { // The MIFARE PICCs that we use have 4 byte UID
    tagID.concat(String(mfrc522.uid.uidByte[i], HEX)); // Adds the 4 bytes in a single String variable
  }
  tagID.toUpperCase();
  mfrc522.PICC_HaltA(); // Stop reading
  return true;
}
