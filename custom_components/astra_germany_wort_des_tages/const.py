from datetime import datetime

""" Constants """
# Base component constants
__version__ = '0.0.5'
DOMAIN = 'wort_des_tages'
ISSUE_URL = "https://github.com/Ludy87/astra_germany_wort_des_tages/issues"

CONF_DATE = datetime.now().date()
CONF_NAME = 'name'

ATTR_WDT_WORD_FREQUENCY = 'wordfrequency'
ATTR_WDT_SPELLING = 'spelling'
ATTR_WDT_MEANING = 'meaning'
ATTR_WDT_ORIGIN = 'origin'
ATTR_WDT_WORD = 'word'
