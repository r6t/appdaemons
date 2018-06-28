import appdaemon.plugins.hass.hassapi as hass

class BackToSleep(hass.Hass):

    def initialize(self):
        self.listen_state(self.you_are_feeling_sleepy, "binary_sensor.motion_sensor_158d0002119c02", new="off")

    def you_are_feeling_sleepy(self, entity, attribute, old, new, kwargs):
        sleeping = self.get_state("input_boolean.sleep_mode")
        if sleeping == "on":
            self.turn_on("script.all_lights_out")