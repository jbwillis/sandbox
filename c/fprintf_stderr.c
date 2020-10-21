/**
 * Print to standard error
 */

#include<stdio.h>


int main()
{

	char* str = "Hello";
	fprintf(stdout, "Printed to stdout\n");
	fprintf(stderr, "Printed to stderr\n");
	fprintf(stderr, "Concatenate" "Strings\n");
}
