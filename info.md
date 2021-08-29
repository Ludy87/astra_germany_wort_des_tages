# Wort des Tages

Ein Home Assistant Sensor, der das aktuelle "Wort des Tages" auf Duden.de findet und anzeigt.

## Features
  - Häufigkeit
  - Worttrennung
  - Bedeutung
  - Herkunft

## Options

| Name | Type | Default | Description
| ---- | ---- | ------- | -----------
| name | string | Optional | Name of the Sensor (default: `WDT`)

## Instructions
1. In deinem `config/custom_components` Ordner, einen Ordner mit dem Namen `astra_germany_wort_des_tages` erstellen
2. Downloade die [\_\_init\_\_.py](https://raw.githubusercontent.com/Ludy87/astra_germany_wort_des_tages/main/custom_components/astra_germany_wort_des_tages/__init__.py), [manifest.json](https://raw.githubusercontent.com/Ludy87/astra_germany_wort_des_tages/main/custom_components/astra_germany_wort_des_tages/manifest.json) und [sensor.py](https://raw.githubusercontent.com/Ludy87/astra_germany_wort_des_tages/main/custom_components/astra_germany_wort_des_tages/sensor.py) und speichere sie in `config/custom_components/astra_germany_wort_des_tages` ab
5. Füge den Sensor in die `configuration.yaml` ein
```yaml
- platform: wort_des_tages
```
oder mit custom `name` für den Sensor
```yaml
- platform: wort_des_tages
  name: "my custom name"
```

6. Restart Home Assistant
7. Check `Home Assistant » Developer Tools » States`
