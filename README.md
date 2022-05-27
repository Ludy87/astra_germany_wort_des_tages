# Astra-Germany - Wort des Tages
 Home Assistant - Wort des Tages

Ein Home Assistant Sensor, der das aktuelle "Wort des Tages" auf Duden.de findet und anzeigt.

[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge&logo=appveyor)](https://github.com/hacs/integration)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Ludy87/astra_germany_wort_des_tages?style=for-the-badge&logo=appveyor)](https://github.com/Ludy87/astra_germany_wort_des_tages/releases)
![GitHub Release Date](https://img.shields.io/github/release-date/Ludy87/astra_germany_wort_des_tages?style=for-the-badge&logo=appveyor)
[![GitHub](https://img.shields.io/github/license/Ludy87/astra_germany_wort_des_tages?style=for-the-badge&logo=appveyor)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/Ludy87/astra_germany_wort_des_tages?style=for-the-badge&logo=appveyor)](https://github.com/Ludy87/astra_germany_wort_des_tages/issues)

## Features
  - Häufigkeit
  - Worttrennung
  - Bedeutung
  - Herkunft

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
4. Restart Home Assistant
5. Check `Home Assistant » Developer Tools » States`
