import pyhue
import settings

bridge = pyhue.Bridge(settings.HUE_BRIDGE_IP, settings.HUE_BRIDGE_USER)


light = None
for available_light in bridge.lights:
    if settings.HUE_LIGHT_ID == int(available_light.id):
        print "Found the correct light, name: {}".format(available_light.name)
        light = available_light
        break

light.on = False
print light.state


#'bridge', 'id', 'manufacturername', 'modelid', 'name', 'set', 'state', 'swversion', 'type', 'uniqueid', 'update']

#  {u'on': False, u'hue': 55251, u'colormode': u'xy', u'effect': u'none', u'alert': u'select', u'xy': [0.4161, 0.2562], u'reachable': True, u'bri': 95, u'sat': 165}
