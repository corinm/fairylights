# fairylights

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

    2. Paste and save this config

        ```
        [Unit]
        Description=Fairylights
        After=multi-user.target

        [Service]
        ExecStart=/usr/bin/python3 /home/pi/fairylights/src/main.py

        [Install]
        WantedBy=multi-user.target
        ```

2. Set up a service for the web page

    1. Create service

        ```
        sudo systemctl --force --full edit fairylights-page.service
        ```

    2. Paste and save this config

        ```
        [Unit]
        Description=Fairylights webpage
        After=multi-user.target

        [Service]
        ExecStart=/usr/bin/python3 /home/pi/fairylights/src/main2.py

        [Install]
        WantedBy=multi-user.target
        ```

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

This is a traditional twinkling effect where bulbs fade in and out at random
Can be combined with different algorithms for generating different colours/palettes - see `src/utils/randomColours.py` for examples

#### Glitter

Pleasing glitter effect. Effectively a speeded-up and more subtle version of twinkle

#### Fireflies

Inspired by:
- https://www.youtube.com/watch?v=k72jGJTC_3o&t=43s
- https://www.reddit.com/r/NatureIsFuckingLit/comments/o2dyj5/fireflies_flying/
- https://www.youtube.com/watch?v=Z7VZlaHWR1s

### Flickering fairy lights

Inspired by this [Youtube video](https://www.youtube.com/watch?v=zeOw5MZWq24)

Currently disabled. Needs some work / doesn't look great right now

### Colours

These are either: lists of hard-coded colours, a list of palettes (a list of lists of colours) or an algorithm that generates colours on the fly

#### Retro fairy lights

Inspired by vintage fairy lights e.g. Noma Pickwick. Uses the existing twinkling effect but with hand-picked colours: Pink, red, orange, green, blue

#### Analagous colours

Creates a palette made up of 3 colours that are next to each other on the colour wheel. These colours change over time, as does the palette.

#### Analagous weighted colours

As above, but colours are arranged to be more pleasing

#### Complementary colours

- Iterates through pairs of colours over time
