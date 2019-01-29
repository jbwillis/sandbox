/* program for converting a 32 bit float to a 32 bit hex value
 */

#include <stdio.h>

int main() {
	float f = 100.0/3.0;
	int i = (int)*((int*) &f);
	printf("%f, 0x%X\n", f, i);
}
