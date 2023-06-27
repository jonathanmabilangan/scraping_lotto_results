# Disclaimer: This application does not predict what will be the winning number combination of the future lotto results.

# Setting up in local
  Fill out environment variables in local.env file
    * If database is not yet created. Kindly create one using MySQL

  Create virtual environment through terminal:
  ```python3 -m venv venv```

  Install required libraries
  ```pip3 install -r /path/to/requirements.txt```


# To run the spider type in command line
  ``` scrapy crawl lottos ```

  # To run the spider and export data afterwards
  ``` scrapy crawl lottos -O lotto_result.csv


