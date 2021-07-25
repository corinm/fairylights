# fairylights

## Quick start

Install dependencies manually then:

        sudo python3 src/main.py

## Setup

1. Set up a service for the lights and http api

        sudo systemctl --force --full edit fairylights.service

2. Edit the configuration

        [Unit]
        Description=Fairylights
        After=multi-user.target

        [Service]
        ExecStart=/usr/bin/python3 /home/pi/fairylights/src/main.py

        [Install]
        WantedBy=multi-user.target

3. Start the service

        sudo systemctl start fairylights.service
        sudo systemctl stop fairylights.service

4. Set up a service for the web page

        sudo systemctl --force --full edit fairylights-page.service

2. Edit the configuration

        [Unit]
        Description=Fairylights webpage
        After=multi-user.target

        [Service]
        ExecStart=/usr/bin/python3 /home/pi/fairylights/src/main2.py

        [Install]
        WantedBy=multi-user.target

3. Start the service

        sudo systemctl start fairylights-page.service
        sudo systemctl stop fairylights-page.service

## States

See 

### Twinkle - various colour effects

This is a traditional twinkling effect where bulbs fade in and out at random
Can be combined with different algorithms for generating different colours/palettes - see `src/utils/randomColours.py` for examples

Features/todo:

- Now generates a gradient where hue doesn't change
- Fixed bug where shuffle combined with large number of steps led to bulbs starting a new twinkle before they'd finished a previous one
- Now accepts a list of colours instead of just one
- Now supports updating the list of colours after instantiation, every certain number of seconds
- Now supports regenerating the whole palette every certain number of seconds
- Is stoppable and on stopping fades out naturally as each bulb iterates to its off state
- **Could**: Factor in "gamma" / weight changes in luminosity to change based on perceived brightness
- **Could**: Combine gamma with bell curve to create nice fade in and out effect

#### Retro fairy lights

Inspired by vintage fairy lights e.g. Noma Pickwick. Uses the existing twinkling effect but with hand-picked colours: Pink, red, orange, green, blue

#### Analagous colours

Creates a palette made up of 3 colours that are next to each other on the colour wheel. These colours change over time, as does the palette.

#### Analagous weighted colours

As above, but colours are arranged to be more pleasing

#### Complementary colours

- Iterates through pairs of colours over time

### Fireflies

Inspired by:
- https://www.youtube.com/watch?v=k72jGJTC_3o&t=43s
- https://www.reddit.com/r/NatureIsFuckingLit/comments/o2dyj5/fireflies_flying/
- https://www.youtube.com/watch?v=Z7VZlaHWR1s

Features:

- Initial type - static glow
- Implemented a static flickering one
- Fireflies light up in waves
- Fireflies are randomly assigned one of two shades of green
- **Should** implement a moving glow one


### Flickering fairy lights

Inspired by this [Youtube video](https://www.youtube.com/watch?v=zeOw5MZWq24)

- Flickering pretty much there
- Colours pretty much there
- **Could**: Allow choice of colour


### Other ideas

- Static version of retro colours
- Pale twinkling stars / ice effect - much more subtle twinkle that existing kind
- ^ Should have similar interface to twinkling so that it accepts same colour generator functions
- Define states in an e.g. yaml file and load them dynamically - currently the states.py file is very boilerplatey
