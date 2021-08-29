from datetime import datetime

""" Constants """
# Base component constants
__version__ = '0.0.9'
VERSION = __version__
NAME = "Wort des Tages"
DOMAIN = 'wort_des_tages'
ISSUE_URL = "https://github.com/Ludy87/astra_germany_wort_des_tages/issues"

CONF_DATE = 'date'
CONF_NAME = 'name'

ATTR_WDT_WORD_FREQUENCY = 'wordfrequency'
ATTR_WDT_SPELLING = 'spelling'
ATTR_WDT_MEANING = 'meaning'
ATTR_WDT_ORIGIN = 'origin'
ATTR_WDT_WORD = 'word'

# Platforms
SENSOR = "sensor"
PLATFORMS = [SENSOR]

# Defaults
DEFAULT_NAME = DOMAIN

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
