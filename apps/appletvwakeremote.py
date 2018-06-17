import appdaemon.plugins.hass.hassapi as hass

class AppleTVWakeRemote(hass.Hass):

    def initialize(self):
        self.listen_state(self.wakeremote, "media_player.samsung_tv", new="on")

    def wakeremote(self, entity, attribute, old, new, kwargs):
        atv_remote_status = self.get_state("remote.apple_tv")
        if atv_remote_status == "off":
            self.turn_on("remote.apple_tv")