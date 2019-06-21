# General Reference
This is an accumulation of things I have found useful in my use of different
linux tools. 
Hopefully it ends up being a reference that prevents me from googling the same thing multiple times.

## Git
* To have git "forget" about a file that is tracked but is now in gitignore
	* `git rm --cached <file>`
	* This will delete the file when others pull the commit, but works fine for files that are generated on a build.

## Matlab
* To open matlab without the GUI. This will still open GUIs for figures too.
	* `matlab -nodesktop`
* Debugging
	| Command | Action |
	|---------|--------|
	|`dbstop in myfile at ##` |Set a breakpoint in myfile on line ## | 
	| `dbstop in myprogram at 6 if n>=4` | Conditional breakpoint in myfile on line ## |
	| `dbstatus` | List breakpoints |
	| `dbcont` | Continue debugging |
	| `dbclear all` | Clear all breakpoints |
	| `dbclear in file at location` | removes the breakpoint set at the location in file |
	| `dbquit` | Terminates debug mode |


## Linux
* Spell check
	* `aspell` will spell check a text file. 

## Python
* To re-load a module that you have changed
  ```
  from importlib import reload
  import foo
  # time passes and foo gets changed
  foo = reload(foo)
  ```
* Shebang
	`#!/usr/bin/env python3`

## Tmux
* To re-load the configuration file
	* Ctrl-A then `:`
	* `:source ~/.tmux.conf`

## Vim
