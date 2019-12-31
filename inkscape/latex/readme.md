# Rendering LaTeX in inkscape
Rather than the tedious and ugly pixelated mess created by using latex2png, the best solution I have found for creating nice vector graphics with latex rendering is the [LaTeXText plugin](https://github.com/seebk/LaTeXText).

The git repo readme has a good example that the other files in this directory are based off of. The basic use is to put all text that you want rendered in one layer, then run `Extensions -> Render -> Text with Latex (GTK3)`. This puts rendered vector text in a new layer.

Some nice features I have found:
* The position of the rendered text is independent of the position of the latex code. Re-running the plugin won't move custom placements of rendered latex.

