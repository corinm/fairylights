# fairylights

## States

### Flickering fairy lights

Inspired by this [Youtube video](https://www.youtube.com/watch?v=zeOw5MZWq24)

- Flickering pretty much there
- Colours pretty much there
- **Could**: Allow choice of colour

### Random twinkling

- Now generates a gradient where hue doesn't change
- Fixed bug where shuffle combined with large number of steps led to bulbs starting a new twinkle before they'd finished a previous one
- Now accepts a list of colours instead of just one
- Now supports updating the list of colours after instantiation
- **Should**: Factor in "gamma" / weight changes in luminosity to change based on perceived brightness
- **Could**: Combine gamma with bell curve to create nice fade in and out effect

#### Retro fairy lights

Inspired by vintage fairy lights e.g. Noma Pickwick

- Colours: Pink, red, orange, green, blue

#### Random colours

- Iterates through pairs of colours over time

### Fireflies

Inspired by:
- https://www.youtube.com/watch?v=k72jGJTC_3o&t=43s
- https://www.youtube.com/watch?v=Z7VZlaHWR1s

Features:

- Initial type - static glow
- Implemented a static flickering one
- Fireflies light up in waves
- Fireflies are randomly assigned one of two shades of green
- **Should** implement a moving glow one


### Rainbow

Based on:
- https://www.instructables.com/How-to-Make-Proper-Rainbow-and-Random-Colors-With-/

- TODO

### Other ideas

- Static version of retro colours
- Pale twinkling stars / ice effect - much more subtle twinkle that existing kind
- ^ Should have similar interface to twinkling so that it accepts same colour generator functions
- Define states in an e.g. yaml file and load them dynamically - currently the states.py file is very boilerplatey
