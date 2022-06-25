# jugamosotra

Web Scraping Project using Scrapy with Selenium to get dynamic content written in Javascript from html pages.

I applied this on web scraping the board gaming store website called [Jugamosotra](https://jugamosotra.com/es/) to get information details about the board games, like:

- minimum number of players

- maximum number of players

- best number of players

- game duration (min)

- weight (difficulty)

- minimum age recommended

## Prerequisites
To execute the project you need to install the following Python libraries:
- scrapy
- [scrapy-selenium](https://github.com/clemfromspace/scrapy-selenium)
- [chromedriver](https://chromedriver.chromium.org/) -> Check what is the correct version for your Chrome browser

## Execute
To execute the code you need to run the following command:
`scrapy crawl jugamos -O games.csv`
