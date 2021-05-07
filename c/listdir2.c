/* Slightly more involved directory listing program
 * From: http://www.gnu.org/savannah-checkouts/gnu/libc/manual/html_node/Simple-Directory-Lister-Mark-II.html#Simple-Directory-Lister-Mark-II
 *
 * Modified to not print hidden directories
 */

#include <stdio.h>
#include <dirent.h>


static int
one (const struct dirent *d)
{
	if (d->d_name[0] == '.')
	{
		// don't include hidden directories or . or ..
		return 0;
	}
	return 1;
}

int
main (void)
{
  struct dirent **eps;
  int n;

  n = scandir ("./", &eps, one, alphasort);
  if (n >= 0)
    {
      int cnt;
      for (cnt = 0; cnt < n; ++cnt)
        puts (eps[cnt]->d_name);
    }
  else
    perror ("Couldn't open the directory");

  return 0;
}
