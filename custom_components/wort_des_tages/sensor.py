"""
Home Assistant Sensor sucht bei Duden.de das 'Wort des Tages'.
"""
import logging
from datetime import datetime, timedelta

from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle

from .sensor_const import *

_LOGGER = logging.getLogger(__name__)

MIN_TIME_BETWEEN_UPDATES = timedelta(hours=1)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Setup the sensor platform."""

    wdt_object = WDT()
    entity_list = []
    for sensor_type in SENSOR_TYPES:
        entity_list.append(WDTSensor(sensor_type, wdt_object))

    add_entities(entity_list, True)


class WDT:
    def __init__(self):
        self.data = {
            ATTR_WDT_WORD: '',
            ATTR_WDT_WORD_FREQUENCY: '',
            ATTR_WDT_ORIGIN: '',
            ATTR_WDT_MEANING: '',
            ATTR_WDT_SPELLING: '',
            ATTR_WDT_LAST_UPDATED: '',
            ATTR_WDT_CURRENT_TIME: '',
        }

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
        _current_time = datetime.now().date()
        current_time = '{:%Y-%m-%d}'.format(_current_time)
        if self.data[ATTR_WDT_LAST_UPDATED] == current_time:
            return
        last_updated = datetime.now().date()
        self.data[ATTR_WDT_LAST_UPDATED] = last_updated.strftime("%Y-%m-%d")
        now = datetime.now()
        self.data[ATTR_WDT_CURRENT_TIME] = now.strftime("%H:%M:%S")

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
        self.data[ATTR_WDT_WORD] = word.replace('\u00AD', '')

        try:
            full = len(soup.find("span", {"class": "shaft__full"}).text)
            empty = len(soup.find("span", {"class": "shaft__empty"}).text)
            self.data[ATTR_WDT_WORD_FREQUENCY] = self.create_frequency(full, empty)
        except AttributeError:
            self.data[ATTR_WDT_WORD_FREQUENCY] = 'nicht verfügbar'

        try:
            self.data[ATTR_WDT_SPELLING] = soup.find(id='rechtschreibung').find('dd').text
        except AttributeError:
            self.data[ATTR_WDT_SPELLING] = 'nicht verfügbar'

        try:
            self.data[ATTR_WDT_MEANING] = soup.find(id='bedeutung').find('p').text
        except AttributeError:
            self.data[ATTR_WDT_MEANING] = 'nicht verfügbar'

        try:
            self.data[ATTR_WDT_ORIGIN] = soup.find(id='herkunft').find('p').text
        except AttributeError:
            self.data[ATTR_WDT_ORIGIN] = 'nicht verfügbar'


class WDTSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, sensor_type, wdt_object):
        self._sensor = sensor_type
        self._name = f"{SENSOR_TYPES[self._sensor][0]}"
        self._icon = SENSOR_TYPES[self._sensor][1]
        self._state = None
        self.wdt_object = wdt_object

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    @property
    def icon(self):
        """Icon to use in the frontend."""
        return self._icon

    def update(self):
        """Fetch new state data for the sensor.
        This is the only method that should fetch new data for Home Assistant.
        """
        self.wdt_object.update()
        self._state = self.wdt_object.data[self._sensor]
