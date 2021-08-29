"""
Home Assistant Sensor sucht bei Duden.de das 'Wort des Tage'.
"""
import logging
from datetime import datetime, timedelta

import voluptuous as vol

from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.util import Throttle

from .const import (
    CONF_NAME,
    CONF_DATE,
    DOMAIN,
    DEFAULT_NAME,
    ISSUE_URL,
    ATTR_WDT_WORD_FREQUENCY,
    ATTR_WDT_CURRENT_TIME,
    ATTR_WDT_LAST_UPDATED,
    ATTR_WDT_SPELLING,
    ATTR_WDT_MEANING,
    ATTR_WDT_ORIGIN,
    ATTR_WDT_WORD,
)

_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_UPDATES = timedelta(hours=1)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the sensor platform."""
    wdt = WDTSensor(hass, config)
    wdt.update()
    add_entities([wdt], True)


class WDTSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, hass, config):
        """Initialize the sensor and variables."""
        self._name = config[CONF_NAME]
        self._word_frequency = None
        self._current_time = None
        self._last_updated = None
        self._spelling = None
        self._meaning = None
        self._origin = None
        self._state = None
        self._word = None
        self._update =  Throttle(MIN_TIME_BETWEEN_UPDATES)(self.update)

    @staticmethod
    def create_frequency(full, empty):
        word_frequency = ''
        for _ in range(full):
            word_frequency += '▮'
        for _ in range(empty):
            word_frequency += '▯'
        return word_frequency

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    def update(self):
        if self._last_updated == datetime.now().date():
            logging.debug("no update %s".format(DOMAIN))
            return
        last_updated = datetime.now().date()
        self._last_updated = '{:%Y-%m-%d}'.format(last_updated)
        now = datetime.now()
        self._current_time = now.strftime("%H:%M:%S")

        import requests
        from bs4 import BeautifulSoup

        baseurl = 'https://www.duden.de'
        word_of_the_day_url = '/wort-des-tages'

        response = requests.get(baseurl + word_of_the_day_url)

        soup = BeautifulSoup(response.text, "html.parser")

        block = soup.find(id='block-wordoftheday').find('a').attrs['href']
        word_url = baseurl + block

        response = requests.get(word_url, "html.parser")
        soup = BeautifulSoup(response.text, "html.parser")

        word = soup.find("span", {"class": "lemma__main"}).text
        self._word = word.replace('\u00AD', '')

        try:
            full = len(soup.find("span", {"class": "shaft__full"}).text)
            empty = len(soup.find("span", {"class": "shaft__empty"}).text)
            self._word_frequency = self.create_frequency(full, empty)
        except AttributeError:
            self._word_frequency = 'nicht verfügbar'

        try:
            self._spelling = soup.find(id='rechtschreibung').find('dd').text
        except AttributeError:
            self._spelling = 'nicht verfügbar'

        try:
            self._meaning = soup.find(id='bedeutung').find('p').text
        except AttributeError:
            self._meaning = 'nicht verfügbar'

        try:
            self._origin = soup.find(id='herkunft').find('p').text
        except AttributeError:
            self._origin = 'nicht verfügbar'

        self._state = self._word

    @property
    def word(self):
        """Return the word of the sensor."""
        return f"{self._word}"

    @property
    def spelling(self):
        """Return the spelling of the sensor."""
        return self._spelling

    @property
    def origin(self):
        """Return the origin of the sensor."""
        return self._origin

    @property
    def meaning(self):
        """Return the meaning of the sensor."""
        return self._meaning

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{self._name}"

    @property
    def last_updated(self):
        """Return the last_updated of the sensor."""
        return f"{self._last_updated}"

    @property
    def current_time(self):
        """Return the last_updated of the sensor."""
        return f"{self._current_time}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def device_state_attributes(self):
        """Return the state attributes"""
        return {
            ATTR_WDT_WORD_FREQUENCY: self._word_frequency,
            ATTR_WDT_CURRENT_TIME: self._current_time,
            ATTR_WDT_LAST_UPDATED: self._last_updated,
            ATTR_WDT_SPELLING: self._spelling,
            ATTR_WDT_MEANING: self._meaning,
            ATTR_WDT_ORIGIN: self._origin,
            ATTR_WDT_WORD: self._word,
        }
