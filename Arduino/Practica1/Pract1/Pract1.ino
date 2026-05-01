
/* Use File->Load Prog to
   load a different Program
*/

int a;

void setup() {
	Serial.begin(115200);
	a = 2; // 
	randomSeed(analogRead(0));
	Serial.println("a b  result");
}

void loop() {
	float result;
	int b;
	String s;
	
	b = random(2,6); s += String(a) + " " + String(a+b) + " ";
	result = ecuacion(a,a+b); s += String(result);
	Serial.println(s);
	a++;
	
	delay(2000);
}

float ecuacion(int a, int b) {
	float r;
	int i;
	
	r = 0;
	for(i=a;i<=b;i++) {
		r += pow(i,2)*(i/(i-1));
	}
	return r;
}

