import appdaemon.plugins.hass.hassapi as hass

class EmptyPlace(hass.Hass):

    def initialize(self):
        self.listen_state(self.action, "binary_sensor.bayesian_sensor_emily_is_home", new="off")
        self.listen_state(self.action, "binary_sensor.bayesian_sensor_ryan_is_home", new="off")

    def action(self, entity, attribute, old, new, kwargs):
        home1 = self.get_state("binary_sensor.bayesian_sensor_emily_is_home")
        home2 = self.get_state("binary_sensor.bayesian_sensor_ryan_is_home")
        if home1 == "off" and home2 == "off":
            self.turn_on("script.empty_place")
