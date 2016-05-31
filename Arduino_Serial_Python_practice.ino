int redLed = 2;
int blueLed = 4;
int greenLed = 3;
int buttA = 5;
int buttB = 6;

char readCh;
int redState, blueState, greenState = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(redLed, OUTPUT);
  pinMode(blueLed, OUTPUT);
  pinMode(greenLed, OUTPUT);

  pinMode(buttA, INPUT);
  pinMode(buttB, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0)
  {
    readCh = Serial.read();

    switch (readCh) 
    {
      case 'r':
        {
          redState = changeState(redLed, redState);
          break;
        }
      case 'g':
        {
          greenState = changeState(greenLed, greenState);
          break;
        }
      case 'b':
        {
          blueState = changeState(blueLed, blueState);
          break;
        }
      case '1':
        {
          // turn on all lights
          redState = blueState = greenState = 1;
          digitalWrite(redLed, redState);
          digitalWrite(blueLed, blueState);
          digitalWrite(greenLed, greenState);
          break;
        }
      case '0':
        {
          // turn off all lights
          redState = blueState = greenState = 0;
          digitalWrite(redLed, redState);
          digitalWrite(blueLed, blueState);
          digitalWrite(greenLed, greenState);
          break;
        }
      default:
        break;
    }
    
    printf("Red State: %d\nGreen State: %d\n"
           "Blue State: %d\n\n", redState,
           greenState, blueState);

  }
}

int changeState(int led, int state)
{
  state = digitalRead(led);
  state ^= 1;
  digitalWrite(led, state);
  return state;
}

