import appdaemon.plugins.hass.hassapi as hass

class WakeSequence(hass.Hass):

    def initialize(self):
        self.listen_state(self.wakeup, "sensor.bedside_motion_sensors", new = "on")

    def wakeup(self, entity, attribute, old, new, kwargs):
        soundcheck = self.get_state("media_player.sonos_den")
        print("soundcheck value is: ", soundcheck)
        if soundcheck == "playing":
            self.turn_off("light.hallway")
            for x in self.args["lights"]:
                self.turn_on(x, brightness = 220, rgb_color = [255,207,120], transition = 15)
