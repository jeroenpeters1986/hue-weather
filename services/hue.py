#!/usr/bin/env python


def get_light_by_id(bridge, light_id):

    for light in bridge.lights:
        if light_id == int(light.id):
            return light

    raise Exception("Nee")
