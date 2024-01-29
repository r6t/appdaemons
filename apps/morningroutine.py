import appdaemon.plugins.hass.hassapi as hass
import datetime

class MorningRoutine(hass.Hass):

    def initialize(self):
        # Schedule the time for morning routine to start
        time = datetime.time(18, 0, 4)
        self.run_daily(self.start_morning_routine, time)

    def start_morning_routine(self, kwargs):
        # Set climate.thermostat to 72F heat
        self.set_thermostat(72)
        self.set_lights

    def set_thermostat(self, temperature):
        # Set the thermostat
        self.call_service("climate/set_temperature", 
                          entity_id="climate.thermostat", 
                          temperature=temperature, 
                          hvac_mode="heat")

    def set_lights(self):
        # Turn on the Nanoleaf with specific settings
        self.call_service("light/turn_on", 
                          entity_id="light.light_panels_57_90_23", 
                          brightness_pct=100, 
                          effect="Mint")