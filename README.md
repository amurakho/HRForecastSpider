# HRForecastSpider
HRForecastSpider 

В каталоге лежит полный проект. Т.е. виртуальное окружение со всеми нужными библиотеками уже "в коробке"

Скачать проэкт

Зайти в дирректорию с проэктом (cd hrforecastspider)

Активировать виртуальное окружение (source venv/bin/activate)

Зайти в нужный каталог для запуска проэкта (cd hrforecastspider/hrforecastspider)

Запустить паука, с сохранением в base.csv (scrapy crawl hrforecastspider -o base.csv)

Запустить конвектер из .csv в .xlsx (python read_csv.py)

В файле data.xlsx хранится база

!!! Переменые с названиями файлов баз, вшиты в код !!!"
