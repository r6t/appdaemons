import appdaemon.plugins.hass.hassapi as hass
import datetime

class UpdateVolume(hass.Hass):

    def initialize(self):
        runtime = datetime.time(22, 0, 0)
        self.run_daily(self.setvol, runtime)

    def setvol(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.sonos_night_volume")