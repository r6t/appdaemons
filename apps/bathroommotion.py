import appdaemon.plugins.hass.hassapi as hass

class BathroomMotion(hass.Hass):

    def initialize(self):
        self.listen_state(self.motionOn, "sensor.bathroom_motion_sensors", new = "on")
        self.listen_state(self.motionOff, "sensor.bathroom_motion_sensors", new = "off")
        #self.listen_state(self.motion, "sensor.bathroom_motion_sensors")

    def motionOn(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.fire_in_the_hole")
#        if entity.get_state() == "on":
#            self.turn_on("script.fire_in_the_hole")
#        elif entity.get_state() == "off":
#            self.turn_on("script.shitters_quiet")
#        else:
#            self.log("ERROR: unexpected state in motion")

    def motionOff(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.shitters_quiet")
