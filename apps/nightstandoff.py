import appdaemon.plugins.hass.hassapi as hass

class NightstandOff(hass.Hass):

    def initialize(self):
        self.listen_state(self.kill_the_light, "binary_sensor.motion_sensor_158d00022399ea", new="off")

    def kill_the_light(self, entity, attribute, old, new, kwargs):
        sleeping = self.get_state("input_boolean.sleep_mode")
        if sleeping == "off":
            self.turn_on("script.nightlight_off")