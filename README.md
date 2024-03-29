
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
import vitamin_c_crawler as vc_crawler
import config  # Ensure this script also has access to config

if __name__ == '__main__':
    vc_crawler.crawl_vitamin_c_products(
        time_limit=config.TIME_LIMIT,
        source=config.SOURCE_URL,
        download_images=config.DOWNLOAD_IMAGES
    )
```

For more examples look in the [examples](Vitamin_C_crawler/examples) directory.


## License

This project is licensed under the MIT license.