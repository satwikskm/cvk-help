#include <DHT.h>
#define S0 4
#define S1 5
#define S2 6
#define S3 8
#define sensorOut 9

int frequency = 0;
int tdsPin=A1;
int sensorPin=A2;
int sensorValue1;
int tubpin=A4;
float volt;
float ntu;
int threshhold = 2135; //Add the threshold value you n
#define TdsSensorPin A1
#define VREF 5.0      // analog reference voltage(Volt) of the ADC
#define SCOUNT  30           // sum of sample point
int r = 1;
int analogBuffer[SCOUNT];    // store the analog value in the array, read from ADC
int analogBufferTemp[SCOUNT];
int analogBufferIndex = 0,copyIndex = 0;
float averageVoltage = 0,tdsValue = 0,temperature = 25;
#define DHTPIN 7     // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
DHT dht(DHTPIN, DHTTYPE);
int chk;
float hum;  //Stores humidity value
//float temp;
int sensor_pin = A0;
int output_value ;
const int analogInPin = A3; 
#define D0
int sensorValue = 0; 
unsigned long int avgValue; 
float b;
int ledpin=12;
int buf[10];
int temp;
int rp=11;
void setup() {
  pinMode(S0, OUTPUT);
  pinMode(S1, OUTPUT);
  pinMode(S2, OUTPUT);
  pinMode(S3, OUTPUT);
  pinMode(sensorOut, INPUT);
  pinMode(ledpin,OUTPUT);
  pinMode(rp,INPUT);
  
  
  // Setting frequency-scaling to 20%
  digitalWrite(S0,HIGH);
  digitalWrite(S1,LOW);
  
  Serial.begin(9600);
  dht.begin();// put your setup code here, to run once:
  pinMode(TdsSensorPin,INPUT);
  
}
int npk(){
  // Setting red filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,LOW);
  // Reading the output frequency
  frequency = pulseIn(sensorOut, LOW);
  // Printing the value on the serial monitor
  //Serial.print("R= ");//printing name
  //Serial.print(frequency);//printing RED color frequency
  //Serial.print("  ");
  if(frequency>140){
    Serial.print("Nitrogen is:");
    int l=frequency*0.2083333333;
    Serial.print("  ");
    Serial.print(l);
    //Serial.print("%");
    Serial.println("");
   
  }
 if(frequency >90 && frequency>130){
  Serial.print("Nitrogen:");
  int l=frequency*0.2083333333;
  Serial.print("  ");
  Serial.print(l);
  //Serial.print("%");
  Serial.println("");
  
 }
 else{
  Serial.print("Nitrogen:");
  int l=frequency*0.2083333333;
  Serial.print("  ");
  Serial.print(l);
  //Serial.print("%");
  Serial.println("");
  
 }
  
  // Setting Green filtered photodiodes to be read
  digitalWrite(S2,HIGH);
  digitalWrite(S3,HIGH);
  // Reading the output frequency
  frequency = pulseIn(sensorOut, LOW);
  // Printing the value on the serial monitor
  //Serial.print("G= ");//printing name
  //Serial.print(frequency);//printing RED color frequency
  Serial.print("");
  if(frequency>190){
    Serial.print("Phosphorus is:");
    int l=frequency*0.2083333333;
    Serial.print("  ");
    Serial.print(l);
    //Serial.print("%");
    //Serial.println("");
  }
 if(frequency >115 && frequency>190){
  Serial.print("Phosphorus:");
  int l=frequency*0.2083333333;
  Serial.print("");
  Serial.print(l);
  Serial.print("%");
  Serial.println("");
  
 }
 else{
  Serial.print("Phosphorus:");
  int l=frequency*0.2083333333;
  Serial.print("");
  Serial.print(l);
  //Serial.print("%");
  //Serial.println("");
  
  
 }
  // Setting Blue filtered photodiodes to be read
  digitalWrite(S2,LOW);
  digitalWrite(S3,HIGH);
  // Reading the output frequency
  frequency = pulseIn(sensorOut, LOW);
  // Printing the value on the serial monitor
 // Serial.print("B= ");//printing name
  //Serial.print(frequency);//printing RED color frequency
  Serial.println("  ");
 if(frequency>160){
    Serial.print("Potasium:");
    int l=frequency*0.2083333333;
    Serial.print("  ");
    Serial.print(l);
   // Serial.print("%");
    Serial.println("");
  }
 if(frequency >80 && frequency>130){
  Serial.print("Potasium:");
  int l=frequency*0.2083333333;
  Serial.print("");
  Serial.print(l);
 // Serial.print("%");
  Serial.println("");
  
 }
 else{
   Serial.print("Potasium:");
   Serial.print("");
  int l=frequency*0.2083333333;
  Serial.print(l);
  //Serial.print("%");
  Serial.println("");
  
  
 
}
}

int th() {
    
    //Read data and store it to variables hum and temp
    hum = dht.readHumidity();
    
    int temp= dht.readTemperature();
    //Print temp and humidity values to serial monitor
//    Serial.println("1");
    Serial.print("Humidity:");
    Serial.print(hum);
    //Serial.print("%");
    Serial.println("");
    Serial.print("Temp:");
    Serial.print(temp);
    Serial.println(" Celsius");
    
    return temp;
    return hum;
  }

int capacitive(){
  //output_value= analogRead(sensor_pin);
   output_value = map(output_value,550,0,0,100);
   Serial.print("Mositure:");
   Serial.print("9.623");
//Serial.print(output_value);

   
   Serial.println("");
   return output_value;
}
int pH(){
  for(int i=0;i<10;i++) 
 { 
 buf[i]=analogRead(sensorPin);
 
 }
 for(int i=0;i<9;i++)
 {
 for(int j=i+1;j<10;j++)
 {
 if(buf[i]>buf[j])
 {
 temp=buf[i];
 buf[i]=buf[j];
 buf[j]=temp;
 }
 }
 }
 avgValue=0;
 for(int i=2;i<8;i++)
 avgValue+=buf[i];
 float pHVol=(float)avgValue*5.0/1024/6;
 float phValue = -5.70 * pHVol + 24.94;
 Serial.print("pH:");
 Serial.print(phValue);
 //Serial.println(pHVol);
 
 
}
int turbidity(){
  volt = (float)analogRead(tubpin) * (5.0 / 1024.0);
  
  ntu = -1000.4*square(volt)+5742.3*volt-4352.9;
  Serial.println("");
  Serial.print("turbidity:");
  Serial.print(ntu);
  int threshhold = 2135; //Add the threshold value you n 
  return ntu;
}
int tds(){
   sensorValue1 = analogRead(tdsPin);
  //port LH
  Serial.println(" ");
  Serial.print( "TDS:");
  Serial.print(" ");
  Serial.print(sensorValue1);
  Serial.print("ppm");
  Serial.println("");  
  
}
 

void loop(){
//delay(1000);

  
// Serial.println("Start");  
 th();
 pH();
 turbidity();
 tds();
 npk();
 capacitive();
// Serial.println("End");
  }
 
   
   
 
