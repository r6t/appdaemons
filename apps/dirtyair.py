import appdaemon.plugins.hass.hassapi as hass

class DirtyAir150(hass.Hass):

    def initialize(self):
        self.listen_state(self.aqi150, "sensor.xiaomi_air_quality_monitor")

    def aqi150(self, entity, attribute, old, new, kwargs):
        spam = self.get_state("input_boolean.aqi_notified_today")
        if spam == "off":
          aqi = int(self.get_state("sensor.xiaomi_air_quality_monitor"))
          if aqi > 149:
            self.turn_on("script.dirty_air_notify_150")