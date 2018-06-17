import appdaemon.plugins.hass.hassapi as hass

class BathroomMotion(hass.Hass):

    def initialize(self):
        self.listen_state(self.motion, "sensor.bathroom_motion_sensors", new = "on")

    def motion(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.fire_in_the_hole")