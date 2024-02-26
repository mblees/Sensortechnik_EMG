// Grove - EMG Sensor demo code
// This demo will need a Grove - Led Bar to show the motion 
// Grove - EMG Sensor connect to A0
// Grove - LED Bar connect to D8, D9
// note: it'll take about serval seconds to detect static analog value
// when you should hold your muscle static. You will see led bar from level 10 turn to 
// level 0, it means static analog value get ok

int max_analog_dta      = 300;              // max analog data
int min_analog_dta      = 100;              // min analog data
int static_analog_dta   = 0;                // static analog data


// get analog value
int getAnalog(int pin)
{
    long sum = 0;
    
    for(int i=0; i<32; i++)
    {
        sum += analogRead(pin);
    }
    
    int dta = sum>>5;
    


    max_analog_dta = dta>max_analog_dta ? dta : max_analog_dta;         // if max data
    Serial.print(max_analog_dta);
    Serial.print(",");

    min_analog_dta = min_analog_dta>dta ? dta : min_analog_dta;         // if min data
    Serial.print(min_analog_dta);
    Serial.print(",");
    return sum>>5;
}

void setup()
{
    Serial.begin(9600);
}


void loop()
{
    int val = getAnalog(A0);                    // get Analog value
    
    Serial.print(0);
    Serial.print(",");
    Serial.print(1200);
    Serial.print(",");
    Serial.println(val);
    
    delay(10);
}