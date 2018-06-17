import appdaemon.plugins.hass.hassapi as hass

class AppleTVFromPlaying(hass.Hass):

    def initialize(self):
        self.listen_state(self.motion, "media_player.apple_tv", old = "playing")

    def motion(self, entity, attribute, old, new, kwargs):
        self.turn_on("scene.tv_night_paused")