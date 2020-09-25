# Scrapping Framar and BGMedic

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

This project contains the code for scrapping the diseases described in the bulgarian medical websites - medpedia.framar.bg and bgmedic.com.
The purpose of this project is to scrape the description of each disease in bulgarian language so that we can expand our existing dataset.
The data will help for training a model in NLP Machine Learning tasks.

Pages that were scrapped are:

* Diseases section - https://medpedia.framar.bg/%D0%B7%D0%B0%D0%B1%D0%BE%D0%BB%D1%8F%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F
* Diseases in BGMedic - https://www.bgmedic.com/systoyaniya-i-zabolyavaniya

## To run the code:

1. Trigger the Framar scrapper:
    ```
    >>> cd src/crawlers/framar
    >>> scrapy crawl diseases -o diseases.json
    ```

2. Trigger the BGMedic scrapper:
    ```
    >>> cd src/crawlers/bgmedic
    >>> scrapy crawl diseases -o diseases.json
    ```
