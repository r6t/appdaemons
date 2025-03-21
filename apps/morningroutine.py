import appdaemon.plugins.hass.hassapi as hass
import datetime

class MorningRoutine(hass.Hass):

    def initialize(self):
        try:
            hour = float(self.get_state("input_number.alarm_clock_hour"))
            minute = float(self.get_state("input_number.alarm_clock_minute"))
            self.log(f"Morning routine will run at Hour: {hour}, Minute: {minute}")
        except ValueError as e:
            self.log(f"Error fetching input numbers: {e}")
            return
        
        scheduled_time = datetime.time(int(hour), int(minute), 0)
        self.run_daily(self.start_morning_routine, scheduled_time)

    def start_morning_routine(self, kwargs):
        self.log("running morning routine")
        mode = self.get_state("input_select.alarm_clock_thermostat_mode", default="off")
        temperature = float(self.get_state("input_number.alarm_clock_temperature"))
        
        if mode == "off":
            self.set_thermostat(None)
        else:
            self.set_thermostat(mode, temperature)
        self.set_lights()

    def set_thermostat(self, mode, temperature=None):
        if mode is None:
            # Turn off the thermostat
            self.call_service("climate/turn_off", entity_id="climate.thermostat")
            self.log("Thermostat turned off")
        else:
            # Set the thermostat to the specified mode and temperature
            if temperature is not None:
                self.call_service("climate/set_temperature", 
                                  entity_id="climate.thermostat", 
                                  temperature=temperature)
            self.log(f"Thermostat set to {mode} mode")

    def set_lights(self):
        # Turn on the Nanoleaf with specific settings
        self.call_service("light/turn_on", 
                          entity_id="light.light_panels_57_90_23", 
                          brightness_pct=100, 
                          effect="Mint")
        self.log("set_lights complete")
