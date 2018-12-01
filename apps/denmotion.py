import appdaemon.plugins.hass.hassapi as hass

class DenMotion(hass.Hass):

    def initialize(self):
        self.listen_state(self.denmotionscript, "binary_sensor.motion_sensor_158d0002244f18", new = "on")

    def denmotionscript(self, entity, attribute, old, new, kwargs):
        alarm = self.get_state("input_boolean.alarm_security")
        if alarm == "on":
            self.turn_on("script.alarm_den")
