import appdaemon.plugins.hass.hassapi as hass

class EmptyPlace(hass.Hass):

    def initialize(self):
        self.listen_state(self.action, "binary_sensor.via_6_away", new="on")

    def action(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.empty_place")
