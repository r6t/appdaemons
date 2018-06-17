import appdaemon.plugins.hass.hassapi as hass

class BedroomMotionNightLight(hass.Hass):

    def initialize(self):
        self.listen_state(self.low_nightlight, "binary_sensor.motion_sensor_158d00022399ea", new="on")

    def low_nightlight(self, entity, attribute, old, new, kwargs):
        sleeping = self.get_state("input_boolean.sleep_mode")
        if sleeping == "off":
            if self.sun_down():
                self.turn_on("script.low_nightlight")