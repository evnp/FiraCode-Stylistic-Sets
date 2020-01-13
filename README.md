# An Ode to FiraCode
All FiraCode stylistic set permutations as generated `*.ttf` fonts, for systems where stylistic sets are not supported (e.g. OSX).

**Contents** - [Intro](https://github.com/evnp/FiraCode-Stylistic-Sets#a-font-for-cutting-through-the-noise) | [Stylistic Sets](https://github.com/evnp/FiraCode-Stylistic-Sets#stylistic-sets) | [Install](https://github.com/evnp/FiraCode-Stylistic-Sets#install) | [Credits](https://github.com/evnp/FiraCode-Stylistic-Sets#credits)

![Example](https://raw.githubusercontent.com/evnp/FiraCode-Stylistic-Sets/master/example.png)

### A font to cut through the noise
FiraCode is a wonderful coding font, not just in form but function. Usage of ligatures for common symbols engenders a reading and writing experience that is delightful; but further, nurtures focus by allowing the mind to more easily parse meaning with each glance. The effect is subtle (though in my experience, profound)—in code where tension between brevity and clarity is resolved by effective symbolism, increasing the fidelity of the symbols is a windfall. Code that is too verbose or too obtuse fails when put to the test of reading, re-reading, and understanding over time; a balance is essential, and building that balance little-by-little leads to successful software collaboration. [@tonsky](https://github.com/tonsky)'s work has given us an elegant tool to promote this harmony at zero cost.

### Stylistic sets
With V2, FiraCode incorporated a variety of "stylistic sets"—special glyph features—that range from details that enchant, to improvements that directly bolster legibility. In particular, I find the old-style numerals add texture to documents that contain many numbers, giving my eyes differences to digest as they scan (they also just look amazing, if you can get on board with the antiquated style).

I have a theory—over decades of reading code, FiraCode and its seemingly subjective qualities will impart an objective benefit to understanding. Possible, though optimistic, and at the end of the day a choice of font is a personal one—like a woodworker choosing the perfect grain. With that in mind, I humbly submit every permutation of stylistic sets in the form of `*.ttf` font files immediately installable on OSX or Linux without any extra tooling or setup. Simply follow these steps:

### Install
- from this repository homepage, press `t` to activate the file finder
- search the repository for stylistic-set combination of your choice
  - e.g. start typing `onum-ss01-sso2` and results will automatically update include all fonts with sets `onum`, `ss01`, `ss02`
  - list of stylistic set names is here: http://github.com/tonsky/FiraCode/wiki/How-to-enable-stylistic-sets
- click on the matching font file in the style you want (e.g. `FiraCode-Light-onum-ss01-ss02.ttf`)
- click `Download` or `View raw` to download the font file
- repeat for any other desired styles (e.g. `Bold`, `Medium`, `Retina`, etc.)
- select all downloaded `*.ttf` font files in your system's file manager (e.g. `Finder`, in folder `Downloads`)
- double-click to "open" font files
- follow the instructions in your system's font manager to install the fonts
- in your application (e.g. iterm, VSCode, etc.) preferences pane, select the new font-family (e.g. `FiraCode-onum-ss03-ss04-zero`) and text should now be rendered with your chosen stylistic sets
  - you may need to enable a "ligatures" setting in order for ligature symbols to render (i.e. symbols made up of multiple base characters)
  - e.g. for iterm, this setting is located under "Profiles" tab -> "Text" tab -> "Use ligatures"
- Enjoy!

### Further reading
https://github.com/tonsky/FiraCode/wiki/How-to-enable-stylistic-sets

### Credits
Huge thanks to these developers for their hard work making the craft of software development better for all of us:
- [@tonsky](https://github.com/tonsky) - [FiraCode](https://github.com/tonsky/FiraCode/)
- [@twardoch](https://github.com/twardoch) - [pyftfeatfreeze](https://github.com/twardoch/fonttools-utils/tree/master/pyftfeatfreeze) (generator used to bake stylistic set modifications directly into `*.ttf` font files)



