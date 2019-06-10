import appdaemon.plugins.hass.hassapi as hass

class BathroomMotion(hass.Hass):

    def initialize(self):
        self.listen_state(self.motionOn, "sensor.bathroom_motion_sensors", new = "on")
        self.listen_state(self.motionOff, "sensor.bathroom_motion_sensors", new = "off")
        #self.listen_state(self.motion, "sensor.bathroom_motion_sensors")

    def motionOn(self, entity, attribute, old, new, kwargs):
        sun = self.get_state("sun.sun")
        if sun == "above_horizon":
            self.turn_on("light.bathroom", brightness = 255)
        else:
            self.turn_on("light.bathroom", brightness = 10)
        self.run_in(motionOff, 60)

    def motionOff(self, entity, attribute, old, new, kwargs):
        occupied = self.get_state("sensor.bathroom_motion_sensors")
        if occupied == "on":
            self.run_in(motionOn, 60)
        else:
            self.turn_off("light.bathroom")
