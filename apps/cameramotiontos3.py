import appdaemon.plugins.hass.hassapi as hass

class CameraMotionToS3(hass.Hass):

    def initialize(self):
        self.listen_state(self.tothecloud, "binary_sensor.door_window_sensor_158d0001b714ad", old="off", new="on")

    def tothecloud(self, entity, attribute, old, new, kwargs):
        self.turn_on("script.camera_motion_to_s3")
