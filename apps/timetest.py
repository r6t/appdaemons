import appdaemon.plugins.hass.hassapi as hass
import datetime

class TimeTest(hass.Hass):

    def initialize(self):
        runtime = datetime.time(16, 38, 0)
        self.run_daily(self.speakup, runtime)

    def speakup(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.sonos_time_test")