
# Vitamin_C_crawler

`Vitamin_C_crawler` is an advanced data crawling system developed in Python, designed for efficient web scraping and data analysis. This tool specializes in collecting and analyzing web page data, with a particular focus on product names, prices, and image URLs. It offers flexibility for various data crawling scenarios, utilizing libraries like `lxml`, `requests`, and `pandas`.

## Key Features
    - Dynamic web page content scraping.
    - Precise extraction of product information (names, prices, image URLs).
    - Capability to export data in multiple formats, including CSV and JSON.
    - Modular architecture, easily adaptable to specific requirements.

## Quick Start Guide
### Prerequisites
- Ensure you are using Python 3.10 or newer.
- Have `poetry` installed for dependency management.

## Installation

### Using a package manager

You can install the crawler as a package: Using `pip`:

```sh
pip install vitamin_c_crawler
```

Or using `poetry`:

```sh
poetry add vitamin_c_crawler
```
### Cloning the repository

You can also clone the repository and install the dependencies. Using `poetry`:

```sh
git clone https://github.com/DenKof82/vitamin_c_crawler
cd vitamin_c_crawler
poetry install
```

## Usage

### As a module

```python
from vitamin_c_crawler import crawl_vitamin_c_products

print(crawl_vitamin_c_products(
    time_limit=config.TIME_LIMIT,
    source=config.SOURCE_URL,
    download_images=config.DOWNLOAD_IMAGES
))
# 
SOURCE_URL = "https://www.gintarine.lt/search?q=vitaminas+c"
RETURN_FORMAT = 'csv'
DOWNLOAD_IMAGES = True
IMAGE_FOLDER = 'downloaded_images'
CSV_FILE_PATH = 'vitamin_c_products.csv'
```

For more examples look in the [examples](./examples) directory.

## Structure

The project is structured as follows:

- `example_data_crawler/`: Main package directory.
  - `__init__.py`: Package initialization file.
  - `crawlers/`: Directory containing individual crawler scripts.
    - `__init__.py`: Initialization file for crawlers module.
    - `lrytas.py`: Crawler for the Lrytas website.
    - `mersedes_crawler.py`: Crawler for the Mercedes website.
  - `definitions.py`: Definitions and utility functions.
  - `dl_image.py`: Script for downloading images.
  - `main.py`: Main script for the crawler package.
- `examples/`: Directory containing example scripts.
  - `lrytas/`: Examples for the Lrytas crawlers.
    - `all.py`: Example script for crawling all data.
    - `by_topic.py`: Example script for crawling by topic.
- `tests/`: Test scripts for the package.
  - `__init__.py`: Initialization file for tests.

## License

This project is licensed under the MIT license.