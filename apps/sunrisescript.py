import appdaemon.plugins.hass.hassapi as hass

class SunriseScript(hass.Hass):

    def initialize(self):
        self.run_at_sunrise(self.sunrise_cb)

    def sunrise_cb(self, kwargs):
        self.turn_on("script.suns_out")