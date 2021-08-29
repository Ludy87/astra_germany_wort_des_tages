# Astra-Germany - Wort des Tages
 Home Assistant - Wort des Tages

Ein Home Assistant Sensor, der das aktuelle "Wort des Tages" auf Duden.de findet und anzeigt.

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Ludy87/astra_germany_wort_des_tages)](https://github.com/Ludy87/astra_germany_wort_des_tages/releases)
![GitHub Release Date](https://img.shields.io/github/release-date/Ludy87/astra_germany_wort_des_tages)
[![GitHub](https://img.shields.io/github/license/Ludy87/astra_germany_wort_des_tages)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ludy87/astra_germany_wort_des_tages)](https://github.com/Ludy87/astra_germany_wort_des_tages/issues)

## Features
  - Häufigkeit
  - Worttrennung
  - Bedeutung
  - Herkunft

## Options

| Name | Type | Default | Required | Description
| ---- | ---- | ------- | -------- | -----------
| name | string | `WDT` | no | Name des Sensors

## Installation

---

### MANUAL INSTALLATION

1. In deinem `config/custom_components` Ordner, einen Ordner mit dem Namen `wort_des_tages` erstellen
2. Downloade [last Releae](https://github.com/Ludy87/astra_germany_wort_des_tages/releases) oder die [\_\_init\_\_.py](https://raw.githubusercontent.com/Ludy87/astra_germany_wort_des_tages/main/custom_components/astra_germany_wort_des_tages/__init__.py), [manifest.json](https://raw.githubusercontent.com/Ludy87/astra_germany_wort_des_tages/main/custom_components/astra_germany_wort_des_tages/manifest.json) und [sensor.py](https://raw.githubusercontent.com/Ludy87/astra_germany_wort_des_tages/main/custom_components/astra_germany_wort_des_tages/sensor.py) und speichere sie in `config/custom_components/wort_des_tages` ab
3. Füge den Sensor in die `configuration.yaml` ein
```yaml
sensor:
  - platform: wort_des_tages
```
oder mit custom `name` für den Sensor
```yaml
sensor:
  - platform: wort_des_tages
    name: "my custom name"
```
4. Restart Home Assistant
5. Check `Home Assistant » Developer Tools » States`

## Template Erweiterung `configuration.yaml`

```yaml
template:
  - sensors:
    wort_des_tages:
      friendly_name: "Wort des Tages"
      value_template: "{{ state_attr('sensor.wdt', 'word') }}"
      icon_template: "mdi:book-open-variant"
    wort_des_tages_freq:
      friendly_name: "Häufigkeit"
      value_template: "{{ state_attr('sensor.wdt', 'wordfrequency') }}"
    wort_des_tages_spelling:
      friendly_name: "Worttrennung"
      value_template: "{{ state_attr('sensor.wdt', 'spelling') }}"
      icon_template: "mdi:format-text-wrapping-clip"
    wort_des_tages_meaning:
      friendly_name: "Bedeutung"
      value_template: "{{ state_attr('sensor.wdt', 'meaning') }}"
      icon_template: "mdi:script-text-play-outline"
    wort_des_tages_origin:
      friendly_name: "Herkunft"
      value_template: "{{ state_attr('sensor.wdt', 'origin') }}"
      icon_template: "mdi:map-marker-star-outline"
    wort_des_tages_last_updated:
      friendly_name: "Update Datum"
      value_template: "{{ state_attr('sensor.wdt', 'last_updated') }}"
      icon_template: "mdi:update"
    wort_des_tages_current_time:
      friendly_name: "Update Zeit"
      value_template: "{{ state_attr('sensor.wdt', 'current_time') }}"
      icon_template: "mdi:update"
```