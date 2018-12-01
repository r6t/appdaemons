import appdaemon.plugins.hass.hassapi as hass

class DoorMotion(hass.Hass):

    def initialize(self):
        self.listen_state(self.doormotionscript, "binary_sensor.door_window_sensor_158d0001b714ad", new = "on")

    def doormotionscript(self, entity, attribute, old, new, kwargs):
        alarm = self.get_state("input_boolean.alarm_security")
        if alarm == "on":
            self.turn_on("script.alarm_front_door_empty_place")
