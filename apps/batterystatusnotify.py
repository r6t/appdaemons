import appdaemon.plugins.hass.hassapi as hass

class BatteryStatusNotify(hass.Hass):

    def initialize(self):
        self.listen_state(self.battstatusnotify, "sensor.xiaomi_air_filter_life")

    def battstatusnotify(self, entity, attribute, old, new, kwargs):
        life = self.get_state("sensor.xiaomi_air_filter_life")
        if (int(life) / 10) == 0:
            self.turn_on("script.battery_status_notify")