import appdaemon.plugins.hass.hassapi as hass

class RobotVacuumDied(hass.Hass):

    def initialize(self):
        self.listen_state(self.robot_died, "sensor.roomba_battery", new="0")

    def robot_died(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.roomba_died")