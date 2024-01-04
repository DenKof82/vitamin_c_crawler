import crawl_vitamin_c_products

if __name__ == "__main__":
    # Crawling all the articles from 2021-01-01 related to 'vakcinacija'
    # and saving to csv file. It takes a while to finish, be patient.
    # In total should have ~220k articles.
    crawl_vitamin_c_products(
        time_limit=config.TIME_LIMIT,
        source=config.SOURCE_URL,
        download_images=config.DOWNLOAD_IMAGES
    ).to_csv(
        "vitamin_c_products.csv"
    )