from __future__ import annotations

from custom_components.wort_des_tages.const import (
    ATTR_WDT_CURRENT_TIME,
    ATTR_WDT_LAST_UPDATED,
    ATTR_WDT_MEANING,
    ATTR_WDT_ORIGIN,
    ATTR_WDT_SPELLING,
    ATTR_WDT_WORD,
    ATTR_WDT_WORD_FREQUENCY,
)


SENSOR_TYPES = {
    ATTR_WDT_WORD: [  # state
        "Wort des Tages",
        "mdi:book-open-variant",
        None,
    ],
    ATTR_WDT_ORIGIN: [  # origin
        "Herkunft",
        "mdi:map-marker-star-outline",
        None,
    ],
    ATTR_WDT_MEANING: [  # meaning
        "Bedeutung",
        "mdi:script-text-play-outline",
        None,
    ],
    ATTR_WDT_SPELLING: [  # spelling
        "Worttrennung",
        "mdi:format-text-wrapping-clip",
        None,
    ],
    ATTR_WDT_WORD_FREQUENCY: [  # word_frequency
        "Häufigkeit",
        "hass:eye",
        None,
    ],
    ATTR_WDT_LAST_UPDATED: [  # last_updated
        "Update Datum",
        "mdi:update",
        None,
    ],
    ATTR_WDT_CURRENT_TIME: [  # current_time
        "Update Zeit",
        "mdi:update",
        None,
    ],
}
