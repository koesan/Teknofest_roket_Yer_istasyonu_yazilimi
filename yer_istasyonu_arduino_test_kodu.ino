#include <SoftwareSerial.h>
float data_irtifa[] = {1.85,1.80,1.75,1.70,1.90,1.82,1.80,1.78,2.05,1.80,1.80,1.85,1.85,1.85,1.85,1.85,1.85,1.85,1.87,1.78,1.77};
float data_gps_irtifa = 34.5;
float data_enlem = 40.98566884447199;
float data_boylam = 29.05306375869976;
float data_aci = 29.0;
float faydaliyuk_gps_irtifa = 1.35;
float faydaliyuk_gps_enlem = 1.35;
float faydaliyuk_gps_boylam = 1.35;
float data_ivme_x[] = {1.85,1.80,1.75,1.70,1.90,1.82,1.80,1.78,2.05,1.80,1.80,1.85,1.85,1.85,1.85,1.85,1.85,1.85,1.87,1.78,1.77};
float data_ivme_y[] = {1.85,1.80,1.75,1.70,1.90,1.82,1.80,1.78,2.05,1.80,1.80,1.85,1.85,1.85,1.85,1.85,1.85,1.85,1.87,1.78,1.77};
float data_ivme_z[] = {1.85,1.80,1.75,1.70,1.90,1.82,1.80,1.78,2.05,1.80,1.80,1.85,1.85,1.85,1.85,1.85,1.85,1.85,1.87,1.78,1.77};
float data_gyro_x[]= {0.03,0.04,0.09,1.70,1.90,0.82,0.80,0.78,2.05,1.80,1.80,0.85,0.05,0.55,0.75,0.45,0.15,0.25,0.22,0.03,0.07};
float data_gyro_y[]= {-0.02,-1.80,-1.75,-1.70,-1.90,-1.82,-1.80,-1.78,-2.05,-0.80,-1.08,-0.45,-0.05,-0.15,-0.35,-0.25,-1.85,-1.25,-2.87,-2.78,-1.77};
float data_gyro_z[] = {1.85,0.30,0.30,1.70,1.90,0.82,0.80,0.78,2.05,0.02,0.07,0.85,0.45,0.15,0.35,0.81,0.84,0.35,0.07,0.07,0.77};
int parasut_1 = 1;
int parasut_2 = 0;
int takim_id = 001;
int i =0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.print(data_irtifa[i]);
  Serial.print(",");
  Serial.print(data_gps_irtifa);
  Serial.print(",");
  Serial.print(data_enlem);
  Serial.print(",");
  Serial.print(data_boylam);
  Serial.print(",");
  Serial.print(data_ivme_x[i]);
  Serial.print(",");
  Serial.print(data_ivme_y[i]);
  Serial.print(",");
  Serial.print(data_ivme_z[i]);
  Serial.print(",");
  Serial.print(data_gyro_x[i]);
  Serial.print(",");
  Serial.print(data_gyro_y[i]);
  Serial.print(",");
  Serial.print(data_gyro_z[i]);
  Serial.print(",");
  Serial.print(data_aci);
  Serial.print(",");
  Serial.print(parasut_1);
  Serial.print(",");
  Serial.print(parasut_2);
  Serial.print(",");
  Serial.print(faydaliyuk_gps_irtifa);
  Serial.print(",");
  Serial.print(faydaliyuk_gps_enlem);
  Serial.print(",");
  Serial.print(faydaliyuk_gps_boylam);
  Serial.print(",");
  Serial.println(takim_id);
  i++;
  if(i == 20){
    i=0;
  }
  delay(200);

}
