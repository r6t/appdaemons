import appdaemon.plugins.hass.hassapi as hass
import time

class BathroomMotion(hass.Hass):

    def initialize(self):
        self.listen_state(self.motionOn, "sensor.bathroom_motion_sensors", new = "on")
        self.listen_state(self.motionOff, "sensor.bathroom_motion_sensors", new = "off")

    def motionOn(self, entity, attribute, old, new, kwargs):
        sun = self.entities.sun.sun.state
        if sun == "above_horizon":
            self.turn_on("light.bathroom", brightness = 255)
        else:
            currenttime = time.localtime()
            if 5 < currenttime.tm_hour < 22:
                self.turn_on("light.bathroom", brightness = 155)
                self.turn_on("light.shower_light", brightness = 155)
            else:
                self.turn_on("light.bathroom_light_4", brightness = 55)
        self.run_in(motionOff, 500)

    def motionOff(self, entity, attribute, old, new, kwargs):
        occupied = self.get_state("sensor.bathroom_motion_sensors")
        if occupied == "on":
            self.run_in(motionOff, 30)
        else:
            self.turn_off("light.bathroom")
