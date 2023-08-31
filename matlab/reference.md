# MATLAB

## Subdirectory as module
If you prepend a directory name with "+", matlab will treat it as something akin to a module, accessible with dot notation.

`+foo/bar.m:`
```
fprintf("You're in bar.m\n");
```

`+foo/baz.m`
```
fprintf("This is baz.m\n");
```

`./testfoo.m:`
```
foo.bar;
foo.baz;
```

`Output:`
```
>> testfoo
You're in bar.m
This is baz.m
```