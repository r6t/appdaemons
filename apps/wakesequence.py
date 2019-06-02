import appdaemon.plugins.hass.hassapi as hass

class WakeSequence(hass.Hass):

    def initialize(self):
        self.listen_state(self.wakeup, "sensor.bedside_motion_sensors", new = "on")

    def wakeup(self, entity, attribute, old, new, kwargs):
        soundcheck = self.get_state("media_player.sonos_bedroom")
        if soundcheck == "playing":
            self.turn_on("light.bedroom")
    #        self.half_hour_warm("light.hallway", "light.kitchen")

    #def half_hour_warm(self, **kwargs):
    #    for x in kwargs.items():
    #        self.turn_on(x, transition = 1800)
    #    self.log("devices powered on for half hour warm up")
