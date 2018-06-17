import appdaemon.plugins.hass.hassapi as hass

class InBed(hass.Hass):

    def initialize(self):
        self.listen_state(self.hit_the_hay, "binary_sensor.eight_left_bed_presence", new="on")
    
    def hit_the_hay(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.sleep_sequence")