/* simple program to list a directory
 * From: http://www.gnu.org/savannah-checkouts/gnu/libc/manual/html_node/Simple-Directory-Lister.html
 */

#include <stdio.h>
#include <sys/types.h>
#include <dirent.h>


int
main (void)
{
  DIR *dp;
  struct dirent *ep;

  dp = opendir ("./testdir/");
  if (dp != NULL)
    {
      while (ep = readdir (dp))
        puts (ep->d_name);
      (void) closedir (dp);
    }
  else
    perror ("Couldn't open the directory");

  return 0;
}
