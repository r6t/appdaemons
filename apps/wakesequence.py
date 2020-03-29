import appdaemon.plugins.hass.hassapi as hass

class WakeSequence(hass.Hass):

    def initialize(self):
        self.listen_state(self.wakeup, self.args["trigger"], new = "on")

    def wakeup(self, entity, attribute, old, new, kwargs):
        soundcheck = self.get_state(self.args["alarm_speaker"])
        print("soundcheck value is: ", soundcheck)
        if soundcheck == "playing":
            for x in self.args["lights_ensure_off"]:
                self.turn_off(x)
            for x in self.args["lights"]:
                self.turn_on(x, brightness = 220, rgb_color = [255,207,120], transition = 15)
            self.turn_on(self.args["thermostat"])
            self.call_service("climate/set_hvac_mode", entity_id = self.args["thermostat"], hvac_mode = self.args["thermostat_mode"])
            self.call_service("climate/set_temperature", entity_id = self.args["thermostat"], temperature = self.args["thermostat_temp"])
