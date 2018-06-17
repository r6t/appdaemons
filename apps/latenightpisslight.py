import appdaemon.plugins.hass.hassapi as hass

class LateNightPissLight(hass.Hass):

    def initialize(self):
        self.listen_state(self.light_the_way, "binary_sensor.motion_sensor_158d00022399ea", new="on")

    def light_the_way(self, entity, attribute, old, new, kwargs):
        sleeping = self.get_state("input_boolean.sleep_mode")
        if sleeping == "on":
            self.turn_on("scene.night_light_phase_one")