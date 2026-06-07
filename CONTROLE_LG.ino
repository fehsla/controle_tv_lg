#include <IRremote.h>

#define IR_LED_PIN 2

void setup() {
  Serial.begin(9600);
  IrSender.begin(IR_LED_PIN);

  Serial.println("=== Controle LG via Serial ===");
  Serial.println("p = Power");
  Serial.println("+ = Volume +");
  Serial.println("- = Volume -");
  Serial.println("c = Canal +");
  Serial.println("x = Canal -");
  Serial.println("m = Menu");
  Serial.println("u = Seta Cima");
  Serial.println("d = Seta Baixo");
  Serial.println("l = Seta Esquerda");
  Serial.println("r = Seta Direita");
  Serial.println("o = OK");
}

void loop() {
  if (Serial.available()) {

    char comando = Serial.read();

    switch (comando) {

      case 'p':
        Serial.println("Power");
        IrSender.sendNEC(0x20DF10EF, 32);
        break;

      case '+':
        Serial.println("Volume +");
        IrSender.sendNEC(0x20DF40BF, 32);
        break;

      case '-':
        Serial.println("Volume -");
        IrSender.sendNEC(0x20DFC03F, 32);
        break;

      case 'c':
        Serial.println("Canal +");
        IrSender.sendNEC(0x20DF00FF, 32);
        break;

      case 'x':
        Serial.println("Canal -");
        IrSender.sendNEC(0x20DF807F, 32);
        break;

      case 'm':
        Serial.println("Menu");
        IrSender.sendNEC(0x20DFC23D, 32);
        break;

      case 'u':
        Serial.println("Seta Cima");
        IrSender.sendNEC(0x20DF02FD, 32);
        break;

      case 'd':
        Serial.println("Seta Baixo");
        IrSender.sendNEC(0x20DF827D, 32);
        break;

      case 'l':
        Serial.println("Seta Esquerda");
        IrSender.sendNEC(0x20DFE01F, 32);
        break;

      case 'r':
        Serial.println("Seta Direita");
        IrSender.sendNEC(0x20DF609F, 32);
        break;

      case 'o':
        Serial.println("OK");
        IrSender.sendNEC(0x20DF22DD, 32);
        break;
    }
  }
}