# General Reference
This is an accumulation of things I have found useful in my use of different
linux tools. 
Hopefully it ends up being a reference that prevents me from googling the same thing multiple times.

## Git
* To have git "forget" about a file that is tracked but is now in gitignore
	* `git rm --cached <file>`
	* This will delete the file when others pull the commit, but works fine for files that are generated on a build.

## Jupyter
It seems that the modern Jupyter Notebook system is jupyterlab. This can be installed simply by running `pip3 install jupyterlab`.
I looked into using a Docker image to encapsulate the jupyterlab installation, but since I didn't use anaconda to set up my notebooks, it seems that it isn't actually that messy to just intall jupyterlab.

One feature that I really want in my jupyter notebooks is for them to be as similar to latex documents as possible. The following extension seems to acheive that [jupyter_latex_envs](https://github.com/jfbercher/jupyter_latex_envs). 

To install extensions it is necessary to install Node.js and npm (the nodejs package manager).
To do this I did the following (see https://github.com/nodesource/distributions#debinstall):
```
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs
```

### Interesting Features
* C++ jupyter notebooks using xeus-cling (a nice description on Medium https://blog.jupyter.org/interactive-workflows-for-c-with-jupyter-fe9b54227d92)
* Vim keybinding
* nbviewer and binder for my git repos
* nbdime (diff tool for notebooks)
* Printing variables from code in markdown (https://data-dive.com/jupyterlab-markdown-cells-include-variables)
* Using either mkdocs-material or jupyterbooks to produce a nice webpage/blog interface for my notebooks

### Jupyter Notebooks vs Jupyter lab
It seems that while jupyterlab is the most modern system in the jupyter ecosystem, it doesn't have the number of extensions that jupyter notebooks do and is not compatible with jupyter notebook extensions. Frustrating, since this could mean that notebooks which take advantage of one type of extension won't work in the other environment. I have found, however that some of the most useful extensions (for me) aren't available in jupyterlab, so I am going to use jupyter notebooks instead.

#### Interesting Extensions
* jupyter_latex_envs (linked above)
* python-markdown/main
  * allows python variables to be printed in markdown

#### Installing Jupyter Notebook Extensions
* `pip3 install jupyter_contrib_nbextensions`
* `jupyter nbextensions_configurator enable`
* ` pip3 install jupyter_latex_envs`
* `jupyter nbextension install --py latex_envs --user`
* `jupyter nbextension enable latex_envs --user --py`

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
