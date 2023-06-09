# YaParser
![Python](https://img.shields.io/badge/dynamic/xml?color=white&label=Python&query=3.9&url=https%3A%2F%2Fpython.org%2F) ![Twisted](https://img.shields.io/pypi/v/Twisted?color=blue&label=Twisted) ![Scrapy](https://img.shields.io/pypi/v/Scrapy?color=red&label=Scrapy)
____
YaParser - инструмент, предназначенный для сбора и анализа информации о различных версиях языка Python и сопровождающих его документах PEP. Он позволяет автоматизировать процесс извлечения исходных данных, сортировки, обработки и классификации информации о версиях Python и PEP, что делает его полезным инструментом для разработчиков и аналитиков, которые интересуются историей и развитием данного программного языка. Кроме того, этот парсер может быть использован для создания различных отчетов и аналитических данных, которые могут быть полезны для принятия решений в области разработки программного обеспечения на языке Python.
## Как пользоваться проектом. На windows:
1) Склонируйте репозиторий на свой компьютер или сервер:
```
git clone https://github.com/QBC1/scrapy_parser_pep.git
```
2) Создайте и активируйте виртуальное акружение:
```
python -m venv venv
```
```
source venv/Scripts/activate
```
3) Обновите менеджер пакетов pip и установите зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
4) Запустите работу парсера командой:
```
scrapy crawl pep
```
[Автор](https://github.com/QBC1) [шедевра](https://github.com/QBC1/scrapy_parser_pep)
