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

    bridge = pyhue.Bridge(settings.HUE_BRIDGE_IP, settings.HUE_BRIDGE_USER,
                          settings.HUE_BRIDGE_PORT)
    light = services.hue.get_light_by_id(bridge, settings.HUE_LIGHT_ID)

    # If Hue Light is off, you cannot set/get any attributes except for 'on'
    if not light.on:
        light.on = True
        light.bri = 1

    # Store this, so we can restore it after we are done
    original_color_setting = light.xy

    # Retrieve the colorset
    current_temperature = services.buienradar.get_station_temperature(
        settings.BUIENRADAR_WEATHER_STATION, settings.BUIENRADAR_MEASUREMENT)
    for max_temperature in settings.TEMPERATURE_COLORS:
        if current_temperature < max_temperature:
            color_set = settings.TEMPERATURE_COLORS[max_temperature]

    # Set the correct color to the light
    light.xy = pyhue.rgb2xy(color_set[0], color_set[1], color_set[2])

    for i in range(4, 254, 50):
        light.bri = i
        time.sleep(60)

    # Since it took 5 minutes to start up, we only want to wait if the total duration exceeds 5 minutes
    if settings.TOTAL_DURATION_MINUTES > 5:
        time.sleep((settings.TOTAL_DURATION_MINUTES-5)*60)

    light.xy = original_color_setting
    light.on = False

if __name__ == "__main__":
    main()
