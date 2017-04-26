#!/usr/bin/env python
import pyhue
import time

import services.buienradar
import services.hue
import services.timing

from config import settings


def main():
    """
    Executes this one-time 'program' that shows the home-owner a hint about the
    outside-temperature with a predefined color on a predefined offset. 
    Want to influence this? Create your own settings.py, based on settings_base
    """

    bridge = pyhue.Bridge(settings.HUE_BRIDGE_IP, settings.HUE_BRIDGE_USER)
    light = services.hue.get_light_by_id(bridge, settings.HUE_LIGHT_ID)

    #light.xy = [0.4161, 0.2562]

    # If the Hue Light is not on, you cannot set any attributes except for 'on'
    if not light.on:
        light.on = True
        light.bri = 1

    original_color_setting = light.xy
    original_color_setting = [0.4161, 0.2562]
    print original_color_setting

    COLOR_BLUE = pyhue.rgb2xy(138, 192, 58)
    print COLOR_BLUE
    light.xy = COLOR_BLUE

    for i in range(1, 254, 50):
        light.bri = i
        print i
        time.sleep(3)

    #'bridge', 'id', 'manufacturername', 'modelid', 'name', 'set', 'state', 'swversion', 'type', 'uniqueid', 'update']

    #  {u'on': False, u'hue': 55251, u'colormode': u'xy', u'effect': u'none', u'alert': u'select', u'xy': [0.4161, 0.2562], u'reachable': True, u'bri': 95, u'sat': 165}


    light.xy = original_color_setting
    light.on = False



if __name__ == "__main__":
    main()
