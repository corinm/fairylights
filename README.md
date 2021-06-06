# fairylights

## States

### Flickering fairy lights

Inspired by this [Youtube video](https://www.youtube.com/watch?v=zeOw5MZWq24)

- Flickering pretty much there
- Colours pretty much there
- **Could**: Allow choice of colour
- **Should**: Check that tests still pass

### Random twinkling

- Now generates a gradient where hue doesn't change
- Fixed bug where shuffle combined with large number of steps led to bulbs starting a new twinkle before they'd finished a previous one
- Now accepts a list of colours instead of just one
- **Should**: Factor in "gamma" / weight changes in luminosity to change based on perceived brightness
- **Could**: Combine gamma with bell curve to create nice fade in and out effect

#### Retro fairy lights

Inspired by:
- Vintage fairy lights e.g. Noma Pickwick

- Colours: Pink, red and orange are good
- **Should**: Improve green (slightly more blue?) and blue (slightly more greenish?)

### Fireflies

Sources of inspiration:
- https://www.youtube.com/watch?v=k72jGJTC_3o&t=43s
- https://www.youtube.com/watch?v=Z7VZlaHWR1s

- Initial type - static glow
- Fireflies light up in waves
- Fireflies are randomly assigned one of two shades of green
- **Should** implement a static flickering one
- **Should** implement a moving glow one

### Rainbow

Based on:
- https://www.instructables.com/How-to-Make-Proper-Rainbow-and-Random-Colors-With-/

- TODO

