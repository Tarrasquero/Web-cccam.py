# Scraper Python para actualizar lineas en Oscam r11391

## Dependencias:
- from `requests.auth` import HTTPDigestAuth

- import `requests`

- from `lxml` import html

- import `time`

- Reacuerda `cambiar ip del deco y los user passwd`.

- Es necesario que `CCcam.cfg` esté en el mismo directorio que este script.

- Ejecutar Readers.py

## Este Scraper comprueba el estado en las lineas de dos cards previamente creadas(vacias) si el estado es CONNECTED sale sin hacer nada, si alguna de las dos está desconectada la actualiza con lineas generadas por: 
[Reloadcam.py](https://github.com/gavazquez/ReloadCam "Gracias a gavazquez por este gran trabajo")

Ante la imposivilidad de usar el recurso que propone gavazquez en su proyecto para actualizar las lineas cccam en mi deco,
me veo obligado a crear este scraper para darle solució a mi problema.
