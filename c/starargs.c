/* 
 * Read in all arguments and print them
 * Intended for testing the use of * in the arguments
 */

#include <stdio.h>

int main(int argc, char** argv)
{
	for(int i = 0; i < argc; i++)
	{
		printf("File %d:\t%s\n", i, argv[i]);
	}
	return 0;
}


