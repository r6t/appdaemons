import appdaemon.plugins.hass.hassapi as hass

class BackRightSunLight(hass.Hass):

  def initialize(self):
    self.run_at_sunrise(self.sunrise_cb)
    self.run_at_sunset(self.before_sunset_cb, offset=-60)

  def sunrise_cb(self, kwargs):
    self.turn_on("scene.brsl_red")

  def before_sunset_cb(self, kwargs):
    self.turn_on("scene.brsl_blue")