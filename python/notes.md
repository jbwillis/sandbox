## Python
This is a compilation of random notes on python things I have found interesting, or want to keep recorded.
* To re-load a module that you have changed
  ```
  from importlib import reload
  import foo
  # time passes and foo gets changed
  foo = reload(foo)
