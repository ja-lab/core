"""Sensor implementation for the RPi Sensors integration."""
import logging

from homeassistant.components.sensor import DEVICE_CLASS_TEMPERATURE, SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

# import psutil


# from vcgencmd import Vcgencmd


_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, config_entry: ConfigEntry, async_add_entities
):
    """Set up rpi_sensors sensor."""
    # vcgm = False  # await hass.async_add_executor_job(Vcgencmd())
    async_add_entities([RaspberryTemperature("")], True)
    async_add_entities([RaspberryTemperature("2")], True)


class RaspberryTemperature(SensorEntity):
    """Sensor representing the rpi temperature status."""

    def __init__(self, vcgm):
        """Initialize the sensor."""
        self._vcgm = vcgm
        # self._is_on = None
        # self._last_is_on = False
        self._attr_native_unit_of_measurement = "°C"

    def update(self):
        """Update the state."""
        # vcgm.measure_temp()
        temp = 5  # psutil.sensors_temperatures()["cpu_thermal"][0]
        self._attr_native_value = temp  # .current  # = self._vcgm.measure_temp()
        # self._is_on = self._under_voltage.get()
        # if self._is_on != self._last_is_on:
        #    if self._is_on:
        #        _LOGGER.warning(DESCRIPTION_UNDER_VOLTAGE)
        #    else:
        #        _LOGGER.info(DESCRIPTION_NORMALIZED)
        #    self._last_is_on = self._is_on

    @property
    def unique_id(self):
        """Return the unique id of the sensor."""
        id = "rpi_sensors" + self._vcgm
        return id  # "rpi_sensors"  # only one sensor possible

    @property
    def name(self):
        """Return the name of the sensor."""
        return "RPi Temperature" + self._vcgm

    # @property
    # def is_on(self):
    #    """Return if there is a problem detected."""
    #    return self._is_on

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return "mdi:thermometer"

    @property
    def device_class(self):
        """Return the class of this device."""
        return DEVICE_CLASS_TEMPERATURE
