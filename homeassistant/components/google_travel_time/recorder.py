"""Integration platform for recorder."""
from __future__ import annotations

from homeassistant.core import HomeAssistant, callback

from .const import ATTR_DEPARTURES, ATTR_LAST_POLL


@callback
def exclude_attributes(hass: HomeAssistant) -> set[str]:
    """Exclude the frequently updated departure board and poll timestamp from recording."""
    return {ATTR_DEPARTURES, ATTR_LAST_POLL}
