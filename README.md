# Scrapyng propoerties to buy in sorocaba

This project aims to scan through multiple listing websites and collect info about properties that are available to buy in Sorocaba - SP. 
The goal is to understand average square prices per region of the cities and understand which prices are outliers.  

## Set up

### Python
	* If you haven't installed xcode tools on Mac
		"xcode-select --install"
	* Make sure that [python3](https://www.python.org/downloads/) is installed
	* Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments) for the project
		python3 -m venv properties-listings
	* If you haven't touched Python for a while, checkout [this tutorial](https://docs.python.org/3/tutorial/)

### Scrapy
	* Access the created environment 
		cd properties-listings
		source bin/activate
	* Make sure pip3 is updated
		python3 -m pip install --upgrade pip
	* Install [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html)
		pip3 install Scrapy

## Running
	cd props
	scrapy crawl vidal -O vidal.json
