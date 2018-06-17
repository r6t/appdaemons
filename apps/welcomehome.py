import appdaemon.plugins.hass.hassapi as hass

class WelcomeHome(hass.Hass):

    def initialize(self):
        self.listen_state(self.welcome, "binary_sensor.door_window_sensor_158d0001b714ad", old="off", new="on")

    def welcome(self, entity, attribute, old, new, kwargs):
        ryan_greeted = self.get_state("input_boolean.ryan_greeted")
        if ryan_greeted == "off":
            self.turn_on("script.welcome_home_ryan")
    