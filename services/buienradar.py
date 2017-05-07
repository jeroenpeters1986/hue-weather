#!/usr/bin/env python
import urllib
import xml.etree.cElementTree as etree


def get_xml_base_location():
    """ Return HTTP XML Location for Buienradar """
    return "http://xml.buienradar.nl"


def get_weather_from_station(station_id):
    """ Gather weather information based on a weather station ID """
    initial_xml = urllib.urlopen(get_xml_base_location()).read()
    xml_rootelement = etree.fromstring(initial_xml)

    weather_info = {}
    for weather_station in xml_rootelement[0][7][0]:
        if weather_station.attrib['id'] == station_id:
            for item in weather_station:
                if item.tag == 'icoonactueel':
                    weather_info['zin'] = item.get('zin')
                    weather_info['iconid'] = item.get('ID')
                weather_info[item.tag] = item.text

    # Split up larger descriptions, @duikboot: do you have suggestions for this?
    if len(weather_info['zin']) > 13 and ' ' in weather_info['zin']:
        desc_words = weather_info['zin'].split(' ', 1)
        weather_info['zin'] = '\n'.join(desc_words)

    return weather_info


def get_station_temperature(station_id, measure_element):
    """ Gather weather information based on a weather station ID """
    initial_xml = urllib.urlopen(get_xml_base_location()).read()
    xml_rootelement = etree.fromstring(initial_xml)

    for weather_station in xml_rootelement[0][7][0]:
        if weather_station.attrib['id'] == station_id:
            for item in weather_station:
                if item.tag == measure_element:
                    return float(item.text)

    return 1000
