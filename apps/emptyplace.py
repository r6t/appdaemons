import appdaemon.plugins.hass.hassapi as hass

class EmptyPlace(hass.Hass):

    def initialize(self):
        self.listen_state(self.action, "!secret ryan_device_tracker", old="home")

    def action(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.alarm_arm")