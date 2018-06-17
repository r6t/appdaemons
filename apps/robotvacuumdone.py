import appdaemon.plugins.hass.hassapi as hass

class RobotVacuumDone(hass.Hass):

    def initialize(self):
        self.listen_state(self.robot_done, "sensor.roomba_activity", new="Charging")

    def robot_done(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.vacuum_done")