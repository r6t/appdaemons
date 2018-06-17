import appdaemon.plugins.hass.hassapi as hass
import datetime

# Declare Class
class NightLight(hass.Hass):
  #initialize() function which will be called at startup and reload
  def initialize(self):
    # Create a time object for 7pm
    time = datetime.time(19, 31, 0)
    # Schedule a daily callback that will call run_daily() at 7pm every night
    self.run_daily(self.run_daily_callback, time)

   # Our callback function will be called by the scheduler every day at 7pm
  def run_daily_callback(self, kwargs):
    # Call to Home Assistant to turn the porch light on
    self.turn_on("light.front_right")