# fairylights

## States

### Flickering fairy lights

Inspired by this [Youtube video](https://www.youtube.com/watch?v=zeOw5MZWq24)

- Flickering pretty much there
- Colours pretty much there
- **Could**: Allow choice of colour
- **Should**: Check that tests still pass

### Random twinkling

- Need a function that can generate colours from COLOUR to BLACK without changing hue
- Shuffling approach causes bug where a bulb mid-twinkle can be reset to start a new twinkle. Simplest solution may be to just block this

### Fireflies

Sources of inspiration:
- https://www.youtube.com/watch?v=k72jGJTC_3o&t=43s
- https://www.youtube.com/watch?v=Z7VZlaHWR1s

### Rainbow

Based on:
- https://www.instructables.com/How-to-Make-Proper-Rainbow-and-Random-Colors-With-/

### TODO

* Create own function to generate range of colours between a colour and black (off). Need to factor in gamma https://gist.github.com/hexagon5un/3df734ad08d8dc8d9ace0491ef97cc58
* Implement this for rahdom_twinkling and check it generates sensible gradients
* Example random_twinkling to accept a list of colours
* Add rainbow to FSM
