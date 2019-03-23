import appdaemon.plugins.hass.hassapi as hass

class BathroomMotion(hass.Hass):

    def initialize(self):
        self.listen_state(self.motion, "binary_sensor.motion_sensor_158d0002239c8d", new = "on")

    def motion(self, entity, attribute, old, new, kwargs):
        self.turn_on("light.bathroom")
