/* Overprint.c 
 * Write over the same printed text repeatedly
 */

#include <stdio.h>
#include <unistd.h>

int main() {
	for(int i = 0; i < 100; i++){
		printf("\r%2d", i);
		fflush(stdout);
		sleep(1);
	}
}
