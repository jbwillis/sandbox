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
## LaTeX
* To recompile live, use `latexmk`
  * `latexmk -pvc -pdf main.tex`
  * There needs to be a ~/.latexmkrc file containing the following:
```
$pdflatex = 'pdflatex -interaction=nonstopmode';
$pdf_previewer = '/usr/bin/evince';
```
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
* To rename a window
	* Ctrl-A then `:`
	* `:rename-window <name>`

## Vim
* To diff two buffers in vim:
	* Navigate to the buffer and then `:diffthis`
* Useful diff commands (from https://unix.stackexchange.com/questions/52754/whats-the-recommended-way-of-copying-changes-with-vimdiff)
```
]c               - advance to the next block with differences
[c               - reverse search for the previous block with differences
do (diff obtain) - bring changes from the other file to the current file
dp (diff put)    - send changes from the current file to the other file
zo               - unfold/unhide text
zc               - refold/rehide text
zr               - unfold both files completely
zm               - fold both files completely
```
* EasyAlign
	* (github.com/junegunn/vim-easy-align`)
	* To align to an '='
		* Select the text in visual mode
		* `ga=`
