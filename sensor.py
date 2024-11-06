from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

class VodarenskaSensor(SensorEntity):
    """Vodarenska sensor entity."""

    def __init__(self, coordinator: DataUpdateCoordinator):
        """Initialize the sensor."""
        self.coordinator = coordinator
        self._name = "Vodarenska Sensor"
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    async def async_update(self):
        """Update the sensor state."""
        self._state = await self.coordinator.async_update()
