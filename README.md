# fairylights

Tired of off-the-shelf red, green, blue, yellow Christmas lights, I designed this program to create much more pleasing Christmas tree light effects.

## Requirements
- A raspberry pi
- Some WS2811 individually-addressable LED lights and power supply
- Jumper wires to connect raspberry pi to lights

[See this video for further details on how to get started with RPi and WS2811](https://www.youtube.com/watch?v=KJupt2LIjp4&t=87s)

## Quick start

⚠️ Will only work on RaspberryPi

    sudo pipenv install
    sudo python3 src/main.py

`sudo` is required so that `rpi-ws281x` can use GPIO pin 18 (PWM)

## Setup to run on start-up

1. Set up a service for the lights and http api

    1. Create service

        ```
        sudo systemctl --force --full edit fairylights.service
        ```

    2. Paste and save the config from [here](docs/fairylights.service.txt)

2. Set up a service for the web page

    1. Create service

        ```
        sudo systemctl --force --full edit fairylights-page.service
        ```

    2. Paste and save the config from [here](docs/fairylights-page.service.txt)

3. Start the services

    ```
    sudo systemctl start fairylights.service fairylights-page.service
    ```

## Modes

This is an FSM that controls how the lights move between patterns - whether the lights stay on one pattern or cycle throught them

### Cycle

Cycles through all available patterns

### Static

Stay on a specific pattern indefinitely

### Off

Lights are off

## Patterns

This is another FSM where each state represents a specfic pattern. This is primarily a combination of an effect (twinkling, glittering etc.) and a colour scheme (retro colours, random complimentary colours etc.). This FSM is controlled by the outer Modes FSM.

### Effects

#### Twinkle

This is a twinkling effect where bulbs fade in and out at random. This effect ensures a nice spread across the whole chain by splitting it up into 'buckets' and not selecting multiple bulbs in a row from the same bucket.

#### Glitter

A glittering effect, created by reusing the Twinkle effect, speeding it up and dimming the lights.

#### Fireflies

This effects chooses bulbs at random to glow a yellow-green colour. Active bulbs are added in waves, but individual bulbs have a random delay so they don't all start at once, giving the effect a more organic feel.

Inspired by:
- https://www.youtube.com/watch?v=k72jGJTC_3o&t=43s
- https://www.reddit.com/r/NatureIsFuckingLit/comments/o2dyj5/fireflies_flying/
- https://www.youtube.com/watch?v=Z7VZlaHWR1s

#### Cycle

Creates a gradient across the entire strand and cycles it along over time.

Based on [jgarff/rpi_ws281x strandtest.py example](https://github.com/jgarff/rpi_ws281x/blob/master/python/examples/strandtest.py)

### Flickering fairy lights (DISABLED)

Inspired by this [Youtube video](https://www.youtube.com/watch?v=zeOw5MZWq24)

Needs some work / doesn't look great right now

### Colours

These are either: lists of hard-coded colours, a list of palettes (a list of lists of colours) or an algorithm that generates colours on the fly

#### Retro fairy lights

Inspired by vintage fairy lights e.g. [Noma Pickwick](https://www.youtube.com/watch?v=2HGbVXWyC3M&t=508s). Made up of hand-picked colours: Pink, red, orange, green, blue

![Noma Pickwick vintage lights](https://i.pinimg.com/originals/56%2F8a%2F9c%2F568a9c84ee486b4341ad2a6889984f40.jpg)

> Source: Pinterest

#### Analagous colours

Creates a palette made up of 3 colours that are next to each other on the colour wheel.

![Analogous colours](https://user-images.githubusercontent.com/13546503/135750632-421bf7b6-8b53-4a01-9e52-95c7daeffcc6.png)

> Source: https://decoart.com/blog/article/318/color_theory_basics_the_color_wheel

#### Analagous weighted colours

As above, but colours are chosen such that 5 colours are selected from 3x 1/12 arcs of the colours wheel, and saturation and luminance are varied. This is designed to replicate how colour theory is used in artwork and should create a more visually interesting selection of colours.

#### Complementary colours

Iterates through pairs of colours that are opposite each other on the colour wheel (e.g. green and red or violet and yellow).

![Complementary colours](https://decoart.com/blog/uploads/Color-Theory-Graphics-COMP.jpg)

> Source: https://decoart.com/blog/article/318/color_theory_basics_the_color_wheel

#### Split complementary

Rather than choosing colours opposite on the colour wheel it chooses one colour, then two colours either side of the colour opposite on the wheel (e.g. blue-violet and shades and multiple tints of yellow and orange).

![Split complementary](https://decoart.com/blog/uploads/split-complementary-colors.jpg)

> Source: https://uxplanet.org/how-to-use-a-split-complementary-color-scheme-in-design-a6c3f1e22644

#### Golden angle / every 137 Degrees

This algorithm uses an approximation of the golden angle (137.5°) to select colours that don't repeat very often.

![Golden angle](https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Goldener_Schnitt_Blattstand.png/220px-Goldener_Schnitt_Blattstand.png)

> Source: https://simple.wikipedia.org/wiki/Golden_ratio

#### Colour wheel

This algorithm generates colours that gradually rotate around the colour wheel starting at a random starting position (e.g. red -> red-violet -> violet -> violet-purple etc.).

#### Coolor palettes

These palettes were chosen from some of the highest rates palettes from [coolors.co](https://coolors.co/palettes/trending)
