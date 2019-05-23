# General Reference
This is an accumulation of things I have found useful in my use of different
linux tools. 
Hopefully it ends up being a reference that prevents me from googling the same thing multiple times.


## Matlab
* To open matlab without the GUI. This will still open GUIs for figures too.
	* `matlab -nodesktop`


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

## Vim
