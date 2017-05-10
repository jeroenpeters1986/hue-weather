HUE_BRIDGE_IP = '192.168.2.4'
HUE_BRIDGE_USER = 'newdeveloper'
HUE_BRIDGE_PORT = '80'
HUE_LIGHT_ID = 9

TOTAL_DURATION_MINUTES = 30

BUIENRADAR_WEATHER_STATION = '6278'
BUIENRADAR_MEASUREMENT = 'temperatuur10cm'  # Should only be 'temperatuurGC' or 'temperatuur10cm'

# Color which is picked is always the one 'above' the offset.
# If it's 12.5 degrees, it will be an orange color
TEMPERATURE_COLORS = {
    -100: (255,255,255),    # Hell freezing over    White
    0: (15, 255, 255),      # Freezing              Cool Mint Blue
    6: (0, 172, 230),       # Freezing              Blue
    10: (230, 187, 0),      # Pretty cold           Yellow
    15: (50, 230, 0),       # Chilly                Green
    20: (230, 130, 0),      # Convenient            Orange
    99: (214, 0, 0)         # YH cool               Superhot Red
}