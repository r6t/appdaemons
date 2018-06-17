#currently throwing warnings (that should be errors?) because updater.updater is not present until it has a state change
import appdaemon.plugins.hass.hassapi as hass

class UpdateAvailable(hass.Hass):

    def initialize(self):
        self.listen_state(self.patch_your_shit, "updater.updater", new="on")

    def patch_your_shit(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.update_hass")