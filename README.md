# Scrapping Framar

This project contains the code for scrapping the diseases described in the bulgarian medical website - medpedia.framar.bg.
The purpose of this project is to scrape the description of each disease in bulgarian language so that we can expand our existing dataset.
The data will help for training a model in NLP Machine Learning tasks.

Pages that were scrapped are:

* Diseases section - https://medpedia.framar.bg/%D0%B7%D0%B0%D0%B1%D0%BE%D0%BB%D1%8F%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F

## To run the code:

1. Trigger the scrapper:
    ```
    >>> scrapy crawl diseases -o diseases.json
    ```
