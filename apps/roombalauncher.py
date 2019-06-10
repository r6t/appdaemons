import appdaemon.plugins.hass.hassapi as hass

class RoombaLauncher(hass.Hass):

    def initialize(self):
        self.listen_state(self.preflight, "binary_sensor.via_6_away", new = "on")

    def preflight(self, entity, attribute, old, new, kwargs):
        door = self.get_state("binary_sensor.door_window_sensor_158d0001b714ad")
        if door == "off":
            self.turn_on("vacuum.roomba")
